---
name: html-effectiveness-design
description: Create clean, modern, self-contained HTML artifacts in the style of Thariq Shihipar's "The unreasonable effectiveness of HTML" examples. Use when making artifact galleries, explainer pages, code review pages, implementation plans, design system references, reports, slide decks, research explainers, diagrams, or custom editors that should feel editorial, structured, readable, restrained, and hand-crafted rather than generic dashboard UI.
---

# HTML Effectiveness Design

Use this skill to make self-contained HTML pages with the design language observed at `https://thariqs.github.io/html-effectiveness/`.

The goal is not to copy content. The goal is to reproduce the visual grammar: editorial restraint, warm paper palette, thin borders, serif headlines, mono labels, compact cards, inline SVG thumbnails, and document-shaped layouts that make information easier to read than markdown.

## First steps

1. Read `references/design-language.md` before designing.
2. If starting from scratch, copy `assets/starter.html` and adapt it.
3. Keep the page self-contained: inline CSS, optional inline SVG, minimal inline JS only when interaction materially improves the artifact.
4. Build for reading first. Avoid generic app-dashboard aesthetics.

## Aesthetic stance

Use a calm editorial system:

- Warm ivory page background.
- White paper cards.
- Charcoal text.
- Clay accent.
- Oat and olive secondary colors.
- Thin 1.5px borders.
- Modest rounded corners.
- Serif headings, system sans body, monospace metadata.
- Layouts that feel like a designed document, not a SaaS admin panel.

## Core page patterns

Choose one primary structure:

- **Gallery index:** masthead, short intro, pill navigation, numbered sections, card grid with SVG thumbnails.
- **Explainer:** masthead, narrow prose column, side glossary, cards, callouts, collapsible details, diagrams.
- **Plan or report:** document header, status chips, timeline, table-like rows, risk blocks, next-step cards.
- **Code review:** PR summary, annotated diff rows, file path labels, call graph or module diagram.
- **Design reference:** token swatches, component contact sheets, variant matrix, usage notes.
- **Custom editor:** split panes, compact controls, export button, live preview, clear state.

## Non-negotiables

- Prefer semantic HTML: `header`, `nav`, `main`, `section`, `article`, `footer`.
- Use CSS custom properties for colors, fonts, spacing, border, and radius.
- Use inline SVG for diagrams and thumbnails when possible.
- Use hover states sparingly and precisely: border darkens, card lifts 2px to 3px, accent color appears.
- Use monospace labels for file names, section numbers, metadata, status, and code.
- Keep body copy compact and readable: 13.5px to 16.5px depending on density.
- Keep headings serif, medium weight, tight letter spacing.
- Include mobile breakpoints so grids collapse cleanly.
- Include print-friendly behavior for durable artifacts.

## Avoid

- Glassmorphism, neon gradients, huge shadows, purple AI palettes, oversized rounded cards.
- Centered hero everything.
- Generic metric dashboards unless the source content is truly a report.
- Heavy JS frameworks for static artifacts.
- External fonts, CDNs, analytics, remote images, or trackers unless explicitly approved.
- Over-animated interfaces. Motion should be quiet and purposeful.

## Verification

Before handing off:

1. Open or fetch the final HTML and confirm it loads.
2. Check responsive behavior at desktop and mobile widths when possible.
3. Confirm all links are valid or intentionally placeholder-free.
4. Confirm there are no secrets, private tokens, or raw sensitive data embedded.
5. If Erik will view it from TARS, save under `/Users/tars/clawd/public/artifacts/<slug>/index.html` and provide the Tailscale URL.
