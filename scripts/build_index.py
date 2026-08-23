#!/usr/bin/env python3
"""Generate or verify the compact style registry and README table."""

from __future__ import annotations

import argparse

from stylelib import INDEX_PATH, README_PATH, load_styles, render_index, render_readme_table, replace_readme_table


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()

    styles = load_styles()
    expected_index = render_index(styles)
    expected_readme = replace_readme_table(README_PATH.read_text(encoding="utf-8"), render_readme_table(styles))

    stale = []
    if not INDEX_PATH.exists() or INDEX_PATH.read_text(encoding="utf-8") != expected_index:
        stale.append("styles/index.yaml")
    if README_PATH.read_text(encoding="utf-8") != expected_readme:
        stale.append("README.md")

    if args.check:
        if stale:
            print("Generated files are stale: " + ", ".join(stale))
            return 1
        print(f"Style index is current ({len(styles)} styles)")
        return 0

    INDEX_PATH.write_text(expected_index, encoding="utf-8")
    README_PATH.write_text(expected_readme, encoding="utf-8")
    print(f"Generated style index and README table ({len(styles)} styles)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
