---
schema_version: 1
id: editorial
name: Editorial
description: Calm, document-shaped layouts with warm ivory surfaces, serif hierarchy, restrained accents, and content-specific diagrams.
best_for: ["galleries", "explainers", "reports", "code reviews", "design references", "plans", "research explainers"]
avoid_for: ["dense operational dashboards", "brand-specific corporate presentations"]
external_assets: none
---

# Editorial design language

Source studied: `https://thariqs.github.io/html-effectiveness/` and its linked examples.

## Recognizable traits

This style feels like an independent editorial publication shaped into a practical engineering artifact. It is quiet, structured, and highly legible. Visual interest comes from spacing, type contrast, numbered sections, restrained color, and small content-specific diagrams—not decoration for its own sake.

Use the CSS custom properties in `starter.html` as the canonical token implementation.

## Color and type

- Warm ivory is the page field; white paper surfaces hold cards and dense content.
- Slate is the primary ink. Clay is punctuation for links, indexes, and decisive emphasis.
- Olive and oat provide limited secondary support. Keep saturation low.
- Use a sturdy system serif for large headings, system sans for body copy, and monospace for metadata, code, counters, dates, and file paths.
- Headings are moderately weighted and tightly spaced. Avoid generic centered hero copy.

## Layout rhythm

- Center content in a document wrapper near 1120px with generous side and bottom padding.
- Give the masthead 72–88px of top space and a quiet bottom rule.
- Separate major sections by roughly 64–72px.
- Pair section titles with a clay numeric index and optional count pill.
- On desktop, offset supporting copy and grids beneath the title text; remove the offset on narrow screens.
- Prefer a readable prose measure over filling the entire canvas.

## Components

- **Cards:** white paper rectangles, 1–1.5px borders, 12–14px radii, rare shadows, and restrained hover lift.
- **Pills:** quiet outlined controls for navigation, filters, counts, or status—not decoration.
- **Diagrams:** inline SVG using thin strokes and a small palette. Build a metaphor for the actual content rather than using stock icons.
- **Code and diffs:** monospace paths, compact rows, muted additions/deletions, and clear annotations.
- **Reports:** document header, decisions, timeline, risks, owners, and next actions.
- **Editors:** compact native controls, obvious state, keyboard operation, live preview, and a clear export action.

Load only the relevant file from `snippets/` when the starter does not demonstrate the needed pattern.

## Interaction and accessibility

- Use no JavaScript by default. Add it for disclosure, tabs, copying, exporting, or small editor state.
- Keep motion quiet and remove nonessential transitions for reduced-motion users.
- Use visible clay focus rings, native controls, logical headings, and meaningful SVG labels.
- Check clay and muted gray text against their actual backgrounds; do not rely on color alone.

For complex interactions or data displays, also read `../../references/accessibility.md`.

## Responsive and print behavior

- Collapse split mastheads below roughly 880px.
- Remove section offsets and use a single-column card flow below roughly 640px.
- Preserve readable line length and never hide essential content.
- In print, remove navigation and controls, use white backgrounds, flatten shadows, and avoid splitting cards or panels.

## Completion checklist

- Does the page read like a structured document rather than a dashboard?
- Is there one strong serif headline and a clear reading order?
- Are metadata and numbers set in monospace?
- Are clay, olive, and oat used with restraint?
- Are borders doing more work than shadows?
- Is every visual specific to the content?
- Does keyboard, mobile, reduced-motion, and print behavior hold together?
