# HTML Effectiveness Design Language

Source studied: `https://thariqs.github.io/html-effectiveness/` and its 20 linked example pages.

## What makes it recognizable

This design language feels like a small independent editorial site mixed with a practical engineering artifact. It is quiet, structured, and highly legible. It avoids decoration for decoration's sake. Most visual interest comes from spacing, type contrast, numbered sections, restrained color, compact diagrams, and small inline SVG illustrations.

## Palette

Use these tokens as the default base:

```css
:root {
  --ivory: #FAF9F5;
  --paper: #FFFFFF;
  --slate: #141413;
  --clay: #D97757;
  --clay-dark: #B85C3E;
  --oat: #E3DACC;
  --olive: #788C5D;
  --gray-50: #F0EEE6;
  --gray-100: #E6E3DA;
  --gray-200: #D1CFC5;
  --gray-500: #87867F;
  --gray-700: #3D3D3A;
}
```

Usage:

- `--ivory`: page background.
- `--paper`: cards, panels, tables.
- `--slate`: primary text and active borders.
- `--clay`: links, section numbers, highlights, key accents.
- `--olive`: secondary positive or system accent.
- `--oat`: soft filled blocks, diagram fills, inactive accents.
- Grays: borders, metadata, muted copy, code backdrops.

Keep saturation low. Use clay as punctuation, not paint.

## Typography

Default type system:

```css
:root {
  --serif: ui-serif, Georgia, "Times New Roman", Times, serif;
  --sans: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --mono: ui-monospace, "SF Mono", Menlo, Monaco, Consolas, monospace;
}
```

Pattern:

- Large headings use serif, weight 500, tight tracking.
- Body uses system sans for neutral readability.
- Labels, file names, numbers, counters, code, status chips use monospace.
- Italic serif emphasis is often colored clay.

Typical sizes:

- H1: `clamp(38px, 5.4vw, 62px)`, line height around `1.06`.
- H2: 24px to 32px serif.
- Body intro: 16px to 17px.
- Dense card copy: 13.5px to 14.5px.
- Mono labels: 10px to 12.5px, uppercase, tracked.

## Layout rhythm

Use a restrained document grid:

- Outer wrapper: max width near 1120px, 32px side padding, generous bottom padding.
- Masthead: 72px to 88px top padding, bottom border, short intro, optional visual figure.
- Section spacing: about 72px between sections.
- Section head: left numeric index, serif title, mono count pill.
- Section intro: offset left to align under title text on desktop, flush on mobile.
- Card grids: `repeat(auto-fill, minmax(316px, 1fr))`, 20px gap.

The page should feel like a browsable document, not a homepage template.

## Borders, radii, shadows

- Border width is usually `1.5px`.
- Main cards: 12px to 14px radius.
- Tiny labels and chips: 6px to 999px radius depending shape.
- Shadows are rare and subtle. Use on hover or the primary hero figure only.
- Prefer border contrast over shadow depth.

Common hover behavior:

```css
.card {
  transition: transform 150ms ease, box-shadow 150ms ease, border-color 150ms ease;
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(20, 20, 19, 0.10);
  border-color: var(--slate);
}
```

## Components

### Eyebrow

Monospace, uppercase, gray, with a short clay rule before it.

```css
.eyebrow {
  font-family: var(--mono);
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gray-500);
  display: flex;
  align-items: center;
  gap: 12px;
}
.eyebrow::before {
  content: "";
  width: 24px;
  height: 1.5px;
  background: var(--clay);
}
```

### Pills

Use for navigation, counts, tags, and filters. They should feel tactile but quiet.

```css
.pill {
  font-size: 12.5px;
  padding: 7px 14px;
  border: 1.5px solid var(--gray-200);
  border-radius: 999px;
  background: var(--paper);
  color: var(--gray-700);
}
```

### Cards

Cards are paper rectangles, not floating glass. Each card usually has:

- Thumbnail or diagram region.
- Serif title.
- Compact description.
- Mono footer with file name, status, or next action.

### Thumbnails and diagrams

The examples rely heavily on inline SVG.

Use:

- Thin strokes, usually gray or clay.
- Simple geometric metaphors.
- Filled rectangles and circles in oat, clay, olive, slate, white.
- `overflow: visible` for SVG thumbnails.
- Reusable classes: `.st`, `.fl`, `.cl`, `.ol`, `.oa`, `.sl`, `.wh`, `.ln`, `.lc`, `.da`.

Avoid stock icons. Build tiny diagrams that reflect the content.

### Code and diff views

Patterns seen across examples:

- Monospace file paths.
- Small colored line markers.
- Additions and deletions as muted green or red rows.
- Inline annotations in clay or olive.
- Tables or CSS grid rows instead of screenshots.

### Reports and plans

Use a document-first structure:

- Header with title, status, and date.
- Summary cards with restrained metrics.
- Timeline rows with mono dates.
- Risk or decision blocks with colored left borders.
- Action lists with owners and next steps.

### Custom editors

Use compact controls, obvious state, and an export affordance. The point is to tighten the human-agent loop, so the UI should make editing easier and produce text or JSON that can be copied back.

## Interaction style

Use no JS by default. Add JS only for:

- Slide navigation.
- Tabs.
- Expand/collapse.
- Small custom editor state.
- Copy or export buttons.

Keep interactions local, transparent, and dependency-free.

## Responsive behavior

- Collapse hero grids to one column below 880px.
- Collapse section intro left offsets below 640px.
- Card grids should naturally become one column.
- Preserve readable line length.
- Avoid hiding essential content on mobile.

## Print behavior

For durable artifacts, add:

```css
@media print {
  body { background: white; }
  .card, .panel { box-shadow: none; break-inside: avoid; }
  nav, button { display: none; }
}
```

## Design checklist

Before finishing, verify:

- Does the page have a clear document-like structure?
- Is there one strong serif headline, not a generic centered hero?
- Are metadata and numbers in monospace?
- Are accents mostly clay, with olive and oat as secondary support?
- Are borders doing more work than shadows?
- Is there at least one content-specific inline SVG or visual figure?
- Would this be more readable than the same content in markdown?
