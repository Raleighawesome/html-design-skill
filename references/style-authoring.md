# Style authoring contract

Read this reference only when adding or materially changing a style.

## Required files

```text
styles/<id>/
  design-language.md
  starter.html
  snippets/           Optional; add only useful, reusable patterns
```

`design-language.md` frontmatter is the source of truth:

```yaml
---
schema_version: 1
id: example
name: Example
description: A short description used for routing.
best_for: ["reports", "explainers"]
avoid_for: ["dense dashboards"]
external_assets: none
---
```

Use lowercase kebab-case IDs. `external_assets` is `none`, `optional`, or `required`; required assets make the style ineligible unless the user approves them. Keep routing metadata concise.

## Design language

Document only rules that materially affect decisions: recognizable traits, palette roles, typography, layout rhythm, components, interaction character, responsive behavior, print behavior, and a completion checklist. Treat the starter's CSS custom properties as the canonical token implementation; do not duplicate the complete token block in prose.

## Starter

Provide a minimal, working, offline-first page that demonstrates hierarchy, layout, focus, responsive behavior, reduced motion, print behavior, and one content-specific SVG. Do not turn the starter into a component catalog.

Put optional patterns in focused snippet files. Each snippet should contain the minimum CSS and HTML needed to adapt it without loading unrelated examples.

## Completion

Run:

```bash
python3 scripts/build_index.py
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

Then render desktop and mobile reference images and review them for visual regressions.

```bash
python3 scripts/render_references.py --style <id>
```
