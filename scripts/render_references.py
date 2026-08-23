#!/usr/bin/env python3
"""Render deterministic desktop and narrow reference images for each starter."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from stylelib import ROOT, load_styles

VIEWPORTS = {"desktop": (1440, 1000), "mobile": (500, 900)}


def find_chrome() -> str:
    candidates = [
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise SystemExit("Chrome or Chromium is required to render reference images")


def render(chrome: str, source: Path, target: Path, width: int, height: int) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="html-artifact-render-") as profile:
        temporary = target.with_suffix(".new.png")
        command = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--disable-background-networking",
            "--disable-component-update",
            "--disable-sync",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            f"--window-size={width},{height}",
            f"--screenshot={temporary}",
            source.resolve().as_uri(),
        ]
        process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            for _ in range(100):
                if temporary.exists() and temporary.stat().st_size:
                    temporary.replace(target)
                    return
                time.sleep(0.1)
            raise RuntimeError(f"Chrome did not create {target}")
        finally:
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=3)
            temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--style", action="append", help="render only this style id; repeatable")
    args = parser.parse_args()
    requested = set(args.style or [])
    chrome = find_chrome()
    styles = [style for style in load_styles() if not requested or style.id in requested]
    if requested - {style.id for style in styles}:
        raise SystemExit("Unknown style ids: " + ", ".join(sorted(requested - {style.id for style in styles})))

    for style in styles:
        for label, (width, height) in VIEWPORTS.items():
            target = ROOT / "references" / "screenshots" / f"{style.id}-{label}.png"
            render(chrome, style.directory / "starter.html", target, width, height)
            print(f"Rendered {target.relative_to(ROOT)} ({width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
