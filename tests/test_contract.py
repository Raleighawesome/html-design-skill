from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from stylelib import load_styles, render_index
from validate import audit_html


class StyleContractTests(unittest.TestCase):
    def test_registry_is_deterministic(self) -> None:
        expected = render_index(load_styles())
        self.assertEqual(expected, (ROOT / "styles" / "index.yaml").read_text(encoding="utf-8"))

    def test_starters_pass_html_contract(self) -> None:
        for style in load_styles():
            with self.subTest(style=style.id):
                self.assertEqual([], audit_html(style.directory / "starter.html"))

    def test_missing_anchor_is_detected(self) -> None:
        source = (ROOT / "styles" / "editorial" / "starter.html").read_text(encoding="utf-8")
        broken = source.replace('href="#overview"', 'href="#missing"', 1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.html"
            path.write_text(broken, encoding="utf-8")
            errors = audit_html(path)
        self.assertTrue(any("missing internal anchor" in error for error in errors))

    def test_generated_files_are_current(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_index.py"), "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_remote_assets_require_an_explicit_override(self) -> None:
        source = (ROOT / "styles" / "redhat" / "starter.html").read_text(encoding="utf-8")
        remote = source.replace("</head>", '<link rel="stylesheet" href="https://example.com/font.css">\n</head>')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "remote.html"
            path.write_text(remote, encoding="utf-8")
            blocked = audit_html(path)
            allowed = audit_html(path, allow_remote=True)
        self.assertTrue(any("remote assets" in error for error in blocked))
        self.assertFalse(any("remote assets" in error for error in allowed))

    def test_duplicate_ids_and_placeholder_links_are_detected(self) -> None:
        source = (ROOT / "styles" / "editorial" / "starter.html").read_text(encoding="utf-8")
        broken = source.replace('<a href="#overview">Overview</a>', '<a href="#">Overview</a>')
        broken = broken.replace('<section id="evidence"', '<section id="overview"', 1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.html"
            path.write_text(broken, encoding="utf-8")
            errors = audit_html(path)
        self.assertTrue(any("duplicate element ids" in error for error in errors))
        self.assertTrue(any("placeholder links" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
