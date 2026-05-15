---
name: html-effectiveness-design
description: Create clean, modern, self-contained HTML artifacts using curated design styles. Supports multiple visual languages — editorial, brutalist, technical, etc. Use when making artifact galleries, explainer pages, code review pages, implementation plans, design system references, reports, slide decks, research explainers, diagrams, or custom editors that should feel intentional and hand-crafted rather than generic dashboard UI.
---

# HTML Effectiveness Design

Use this skill to make self-contained HTML pages with high design quality. Multiple visual styles are available under `styles/`, each with its own design language and starter template.

## Style selection

1. List the directories under `styles/` to discover available styles.
2. Read the frontmatter of each style's `design-language.md` to see its `name`, `description`, and `best-for` list.
3. Based on the user's request, recommend the best-matching style and briefly explain why.
4. Confirm the choice with the user before proceeding.
5. Once confirmed, read the full `design-language.md` for that style and use its `starter.html` as the starting template.

If the user explicitly names a style, skip the recommendation step and use it directly.

## Building a page

1. Read the chosen style's `design-language.md` before designing anything.
2. If starting from scratch, copy the style's `starter.html` and adapt it.
3. Keep the page self-contained: inline CSS, optional inline SVG, minimal inline JS only when interaction materially improves the artifact.
4. Build for reading first. Avoid generic app-dashboard aesthetics.

## Core page patterns

Choose one primary structure based on the content:

- **Gallery index:** masthead, short intro, pill navigation, numbered sections, card grid with thumbnails.
- **Explainer:** masthead, narrow prose column, side glossary, cards, callouts, collapsible details, diagrams.
- **Plan or report:** document header, status chips, timeline, table-like rows, risk blocks, next-step cards.
- **Code review:** PR summary, annotated diff rows, file path labels, call graph or module diagram.
- **Design reference:** token swatches, component contact sheets, variant matrix, usage notes.
- **Custom editor:** split panes, compact controls, export button, live preview, clear state.

## Non-negotiables (all styles)

- Prefer semantic HTML: `header`, `nav`, `main`, `section`, `article`, `footer`.
- Use CSS custom properties for colors, fonts, spacing, border, and radius.
- Use inline SVG for diagrams and thumbnails when possible.
- Keep body copy compact and readable.
- Include mobile breakpoints so grids collapse cleanly.
- Include print-friendly behavior for durable artifacts.

## Avoid (all styles)

- Heavy JS frameworks for static artifacts.
- External fonts, CDNs, analytics, remote images, or trackers unless explicitly approved.
- Over-animated interfaces. Motion should be quiet and purposeful.
- Generic metric dashboards unless the source content is truly a report.

## Adding a new style

To add a style, create a new directory under `styles/` with two files:

```
styles/<style-name>/
  design-language.md    # Full design language with frontmatter (name, description, best-for)
  starter.html          # Self-contained HTML starter template implementing the style
```

The `design-language.md` frontmatter must include:

```yaml
---
name: Human-readable style name
description: One-sentence description of the visual feel and key characteristics.
best-for: comma-separated list of content types this style suits
---
```

The `starter.html` should be a working, self-contained HTML page that demonstrates the style's palette, typography, layout, and component patterns. It serves as the copy-and-adapt base for new artifacts.

## Verification

Before handing off:

1. Open or fetch the final HTML and confirm it loads.
2. Check responsive behavior at desktop and mobile widths when possible.
3. Confirm all links are valid or intentionally placeholder-free.
4. Confirm there are no secrets, private tokens, or raw sensitive data embedded.
5. If Erik will view it from TARS, save under `/Users/tars/clawd/public/artifacts/<slug>/index.html` and provide the Tailscale URL.
