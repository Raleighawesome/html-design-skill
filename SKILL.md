---
name: html-artifact-design
description: Create or refine polished, self-contained HTML artifacts such as reports, explainers, reviews, presentations, diagrams, and compact interactive tools. Use for artifact-like single-page deliverables; do not use for full web applications or ordinary prose that does not benefit from visual structure.
---

# HTML Artifact Design

Create readable, intentional HTML artifacts with a curated visual style. Optimize the information hierarchy before decorating it.

## Route the style

- If the user names an existing style, open `styles/<style-id>/design-language.md` directly. If that path is absent, read the registry rather than inventing a style.
- Otherwise read `styles/index.yaml`, select the strongest match from `best_for` and `avoid_for`, and state the choice briefly.
- Ask the user only when multiple styles are genuinely plausible or the choice would require optional external assets.
- Read only the chosen style's design language, its starter, and the snippets needed for the requested page.

If the content structure is unclear, read `references/page-patterns.md`. When adding or changing a style, read `references/style-authoring.md` and run the repository validator.

## Build the artifact

1. Inventory the source content, required facts, and intended audience.
2. Choose one primary page pattern and establish a clear reading order.
3. Adapt the chosen `starter.html`; load component snippets only as needed.
4. Replace all example copy, links, labels, and diagrams with content-specific material.
5. Add minimal inline JavaScript only when interaction materially improves comprehension.

## Shared contract

- Produce one semantic HTML file with inline CSS and optional inline SVG or JavaScript.
- Default to zero network requests: no remote fonts, scripts, images, analytics, or trackers.
- A style may declare optional external assets, but use them only after explicit user approval.
- Preserve source meaning. Never invent facts to fill a layout.
- Include a useful title, language, landmarks, logical headings, keyboard-visible focus, mobile behavior, reduced-motion behavior, and print styles.
- Avoid generic dashboards, decorative metrics, stock imagery, excessive motion, and placeholder content.

## Verify

Before handoff:

1. Open the final page and inspect it at desktop and mobile widths.
2. Confirm navigation, keyboard focus, overflow, print behavior, and intentional external requests.
3. Confirm there are no secrets, private tokens, sensitive raw data, or placeholder links.
4. When this repository is available, run `python3 scripts/validate.py --artifact <path>`. Add `--allow-external-assets` only when the user approved them.
