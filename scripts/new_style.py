#!/usr/bin/env python3
"""Scaffold a new independent style and refresh the generated registry."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

from stylelib import ROOT


def csv_items(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("style_id")
    parser.add_argument("--name", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--best-for", required=True, type=csv_items)
    parser.add_argument("--avoid-for", default="", type=csv_items)
    parser.add_argument("--external-assets", choices=("none", "optional", "required"), default="none")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.style_id):
        parser.error("style_id must be lowercase kebab-case")

    directory = ROOT / "styles" / args.style_id
    if directory.exists():
        parser.error(f"style already exists: {directory}")
    directory.mkdir(parents=True)

    guide = f'''---
schema_version: 1
id: {args.style_id}
name: {json.dumps(args.name)}
description: {json.dumps(args.description)}
best_for: {json.dumps(args.best_for)}
avoid_for: {json.dumps(args.avoid_for)}
external_assets: {args.external_assets}
---

# {args.name} design language

## Recognizable traits

Document only the visual decisions that distinguish this style.

## Tokens and typography

Treat `starter.html` as the canonical token implementation.

## Layout and components

Describe the recurring layout rhythm and component character.

## Responsive, accessibility, and print behavior

Record style-specific behavior beyond the shared skill contract.

## Completion checklist

- Does the artifact clearly express this style without sacrificing readability?
'''
    starter = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Artifact title</title>
<style>
  :root { --background: #fff; --text: #181818; --focus: #0066cc; }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--background); color: var(--text); font-family: system-ui, sans-serif; }
  a:focus-visible, button:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
  main { width: min(70rem, calc(100% - 2rem)); margin: 0 auto; }
  @media (max-width: 48rem) { main { width: min(100% - 1.25rem, 70rem); } }
  @media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; transition: none !important; } }
  @media print { body { background: #fff; color: #000; } }
</style>
</head>
<body>
<main>
  <header><h1>Artifact title</h1><p>Replace this example with source-grounded content.</p></header>
  <section aria-labelledby="section-title"><h2 id="section-title">Section title</h2></section>
</main>
</body>
</html>
'''
    (directory / "design-language.md").write_text(guide, encoding="utf-8")
    (directory / "starter.html").write_text(starter, encoding="utf-8")

    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_index.py")], cwd=ROOT)
    if result.returncode:
        return result.returncode
    print(f"Scaffolded {directory.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
