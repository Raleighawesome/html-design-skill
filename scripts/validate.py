#!/usr/bin/env python3
"""Validate style contracts or a generated HTML artifact with no dependencies."""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path

from stylelib import INDEX_PATH, README_PATH, ROOT, load_styles, parse_frontmatter, render_index, render_readme_table, replace_readme_table


class HTMLAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: dict[str, int] = {}
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.anchors: list[str] = []
        self.placeholder_links: list[str] = []
        self.remote_assets: list[str] = []
        self.lang = ""
        self.has_viewport = False
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags[tag] = self.tags.get(tag, 0) + 1
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang") or ""
        if tag == "meta" and values.get("name") == "viewport":
            self.has_viewport = True
        if tag == "title":
            self.has_title = True
        if values.get("id"):
            element_id = values["id"] or ""
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if tag == "a":
            href = values.get("href")
            if href in {"", "#"} or (href and href.lower().startswith("javascript:")):
                self.placeholder_links.append(href or "<empty>")
            elif href and href.startswith("#"):
                self.anchors.append(href[1:])
        asset = None
        if tag in {"script", "img", "iframe", "source", "video", "audio", "embed", "track", "image"}:
            asset = values.get("src") or values.get("srcset") or values.get("href") or values.get("poster")
        elif tag == "object":
            asset = values.get("data")
        elif tag == "link":
            asset = values.get("href")
        if asset and re.match(r"https?://", asset):
            self.remote_assets.append(asset)


def audit_html(path: Path, *, require_contract: bool = True, allow_remote: bool = False) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    parser = HTMLAudit()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:
        return [f"{path}: HTML parsing failed: {exc}"]

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(f"{path}: {message}")

    require(text.lstrip().lower().startswith("<!doctype html>"), "missing HTML doctype")
    require(bool(parser.lang), "html element needs a language")
    require(parser.has_viewport, "missing viewport meta tag")
    require(parser.has_title, "missing title")
    require(parser.tags.get("main", 0) == 1, "expected exactly one main element")

    missing_anchors = sorted(anchor for anchor in parser.anchors if anchor and anchor not in parser.ids)
    if missing_anchors:
        errors.append(f"{path}: missing internal anchor targets: {', '.join(missing_anchors)}")
    if parser.duplicate_ids:
        errors.append(f"{path}: duplicate element ids: {', '.join(sorted(parser.duplicate_ids))}")
    if parser.placeholder_links:
        errors.append(f"{path}: placeholder links are not allowed: {', '.join(parser.placeholder_links)}")
    if parser.remote_assets and not allow_remote:
        errors.append(f"{path}: remote assets are not allowed by default: {', '.join(parser.remote_assets)}")
    if not allow_remote and re.search(r"url\(\s*['\"]?https?://", text, re.IGNORECASE):
        errors.append(f"{path}: remote CSS URLs are not allowed by default")
    if not allow_remote and re.search(r"@import\s+(?:url\()?\s*['\"]?https?://", text, re.IGNORECASE):
        errors.append(f"{path}: remote CSS imports are not allowed by default")

    declarations = set(re.findall(r"(--[\w-]+)\s*:", text))
    references = set(re.findall(r"var\((--[\w-]+)", text))
    undefined = sorted(references - declarations)
    if undefined:
        errors.append(f"{path}: undefined CSS variables: {', '.join(undefined)}")

    if require_contract:
        require(bool(re.search(r":focus-visible", text)), "missing keyboard-visible focus styles")
        require(bool(re.search(r"@media\s*\([^)]*max-width", text)), "missing mobile media query")
        require("prefers-reduced-motion" in text, "missing reduced-motion behavior")
        require(bool(re.search(r"@media\s+print", text)), "missing print styles")
    return errors


def validate_eval_cases(styles_by_id: dict[str, object]) -> list[str]:
    path = ROOT / "tests" / "eval-cases.json"
    if not path.exists():
        return [f"{path}: missing evaluation cases"]
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]
    errors: list[str] = []
    if not isinstance(cases, list) or not cases:
        return [f"{path}: expected a non-empty list"]
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict) or not case.get("request"):
            errors.append(f"{path}: case {index} needs a request")
            continue
        style_id = case.get("expected_style")
        if style_id not in styles_by_id:
            errors.append(f"{path}: case {index} references unknown style {style_id!r}")
        snippets = case.get("snippets", [])
        if not isinstance(snippets, list):
            errors.append(f"{path}: case {index} snippets must be a list")
            continue
        for snippet in snippets:
            snippet_path = ROOT / "styles" / str(style_id) / "snippets" / str(snippet)
            if not snippet_path.exists():
                errors.append(f"{path}: case {index} references missing snippet {snippet_path.relative_to(ROOT)}")
    return errors


def validate_reference_images(style_ids: set[str]) -> list[str]:
    errors: list[str] = []
    expected = {"desktop": (1440, 1000), "mobile": (500, 900)}
    for style_id in sorted(style_ids):
        for label, dimensions in expected.items():
            path = ROOT / "references" / "screenshots" / f"{style_id}-{label}.png"
            if not path.exists():
                errors.append(f"{path}: missing reference render")
                continue
            data = path.read_bytes()[:24]
            if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
                errors.append(f"{path}: expected a PNG image")
                continue
            actual = struct.unpack(">II", data[16:24])
            if actual != dimensions:
                errors.append(f"{path}: expected {dimensions[0]}x{dimensions[1]}, found {actual[0]}x{actual[1]}")
    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []
    try:
        skill = parse_frontmatter(ROOT / "SKILL.md")
        if skill.get("name") != "html-artifact-design":
            errors.append("SKILL.md: canonical skill name must be html-artifact-design")
        styles = load_styles()
    except ValueError as exc:
        return [str(exc)]

    expected_index = render_index(styles)
    if not INDEX_PATH.exists() or INDEX_PATH.read_text(encoding="utf-8") != expected_index:
        errors.append("styles/index.yaml: generated registry is stale; run scripts/build_index.py")
    readme = README_PATH.read_text(encoding="utf-8")
    expected_readme = replace_readme_table(readme, render_readme_table(styles))
    if readme != expected_readme:
        errors.append("README.md: generated style table is stale; run scripts/build_index.py")

    styles_by_id = {style.id: style for style in styles}
    for style in styles:
        starter = style.directory / "starter.html"
        if not starter.exists():
            errors.append(f"{starter}: missing starter")
        else:
            errors.extend(audit_html(starter))
        snippets = style.directory / "snippets"
        if snippets.exists():
            for snippet in sorted(snippets.glob("*.html")):
                if not snippet.read_text(encoding="utf-8").strip():
                    errors.append(f"{snippet}: empty snippet")
    errors.extend(validate_eval_cases(styles_by_id))
    errors.extend(validate_reference_images(set(styles_by_id)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, help="validate one generated HTML artifact")
    parser.add_argument("--allow-external-assets", action="store_true", help="allow approved remote assets for artifact validation")
    args = parser.parse_args()

    if args.artifact:
        errors = audit_html(args.artifact.resolve(), allow_remote=args.allow_external_assets)
        subject = str(args.artifact)
    else:
        errors = validate_repository()
        subject = "repository"

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validation passed: {subject}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
