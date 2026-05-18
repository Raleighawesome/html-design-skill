---
name: Red Hat
description: Faithful reproduction of the Red Hat brand design system. Clean, open, and confident with Red Hat Display headings, a red-black-white core palette, 3px border radius, and generous whitespace. Enterprise-grade but approachable.
best-for: internal presentations, team updates, project reports, strategy decks, technical overviews, product summaries, architecture explainers, org announcements
---

# Red Hat Design Language

Source studied: Red Hat Brand Standards v6.5 (`redhat.com/en/about/brand/standards`), Red Hat Digital Design System (`ux.redhat.com`), and `@rhds/tokens` CSS package.

## What makes it recognizable

Clean, open layouts with generous whitespace. Red Hat Display for headings — geometric sans-serif with wide letters, tall x-height, open apertures, and a distinctive 12° angle on ascenders. Red used sparingly as punctuation against black and white. No ornamentation. Confidence without loudness. Every element earns its place.

The brand personality is **open, authentic, helpful, and brave**. Visually that means: uncluttered layouts, real content over decoration, clear hierarchy, and bold confident typography. The overall feel is enterprise-grade but approachable — professional without being sterile.

## Fonts

Red Hat fonts are open source and available on Google Fonts. Include this import in every artifact:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:ital,wght@0,300..900;1,300..900&family=Red+Hat+Mono:ital,wght@0,300..700;1,300..700&family=Red+Hat+Text:ital,wght@0,300..700;1,300..700&display=swap" rel="stylesheet">
```

Token definitions:

```css
:root {
  --rh-font-heading: 'Red Hat Display', Helvetica, Arial, sans-serif;
  --rh-font-body: 'Red Hat Text', Helvetica, Arial, sans-serif;
  --rh-font-code: 'Red Hat Mono', 'Courier New', Courier, monospace;
}
```

Usage rules:

| Font | When to use |
|------|-------------|
| **Red Hat Display** | Headlines, slide titles, section headers, pull quotes, navigation, CTAs. Default when unsure. Use at large sizes or in bold. |
| **Red Hat Text** | Body paragraphs, descriptions, small text, tooltips, extended reading. Optimized for demanding reading. |
| **Red Hat Mono** | Code snippets, data values, technical labels, timestamps, version numbers. |

## Typography scale

Base size: 16px. Headings use line-height 1.3. Body and code use line-height 1.5.

### Headings (Red Hat Display)

| Token | Desktop | Mobile (<768px) | Weight |
|-------|---------|-----------------|--------|
| heading-2xl | 48px / 3rem | 35px | 800 (ExtraBold) |
| heading-xl | 40px / 2.5rem | 29px | 800 (ExtraBold) |
| heading-lg | 36px / 2.25rem | 26px | 800 (ExtraBold) |
| heading-md | 28px / 1.75rem | 24px | 800 (ExtraBold) |
| heading-sm | 24px / 1.5rem | 20px | 800 (ExtraBold) |
| heading-xs | 20px / 1.25rem | 18px | 800 (ExtraBold) |

For expressive/hero headings:

| Token | Desktop | Mobile | Weight | Line-height |
|-------|---------|--------|--------|-------------|
| heading-5xl | 96px / 6rem | 48px | 800 | 1.1 |
| heading-4xl | 80px / 5rem | 48px | 800 | 1.1 |
| heading-3xl | 64px / 4rem | 48px | 800 | 1.1 |

### Body (Red Hat Text)

| Token | Size | Weight |
|-------|------|--------|
| body-2xl | 24px / 1.5rem | 400 |
| body-xl | 20px / 1.25rem | 400 |
| body-lg | 18px / 1.125rem | 400 |
| body-md | 16px / 1rem | 400 |
| body-sm | 14px / 0.875rem | 400 |
| body-xs | 12px / 0.75rem | 400 |

### Code (Red Hat Mono)

Same size scale as body text. Weight 400 (Regular).

### CTA text (Red Hat Display)

| Token | Size | Weight |
|-------|------|--------|
| cta-lg | 18px / 1.125rem | 700 (Bold) |
| cta-sm | 16px / 1rem | 700 (Bold) |

## Typography rules

- **Sentence case everywhere** — including titles and headlines. Never use all caps, even for small labels.
- **Never alter tracking** — the fonts are designed with optimal letter-spacing built in. Only exception: text below 6px may increase tracking to 10–20.
- **Emphasis** — use bold OR color, never both. Never use italics or underline for emphasis.
- **Body copy** — black or white only. Never red for long text.
- **Headlines** — Red Hat red (#ee0000) permitted for short headlines to draw attention.
- **Line length** — body text max 100 characters (roughly 7 grid columns, ~789px).
- **Alignment** — flush left by default. Centered only for short headers in narrow spaces. Never justified.

## Palette

### Core (use in every artifact)

```css
:root {
  --rh-color-red-50: #ee0000;     /* Brand red — THE red. Use as accent, not paint. */
  --rh-color-red-60: #a60000;     /* Dark red — hover states */
  --rh-color-red-40: #f56e6e;     /* Light red — decorative tint */
  --rh-color-red-30: #f9a8a8;     /* Lighter red */
  --rh-color-red-20: #fbc5c5;     /* Very light red */
  --rh-color-red-10: #fce3e3;     /* Faintest red tint */
  --rh-color-red-05: #fef0f0;     /* Near-white red */
  --rh-color-red-70: #5f0000;     /* Deep red */
  --rh-color-red-80: #3f0000;     /* Darkest red */

  --rh-color-white: #ffffff;
  --rh-color-black: #000000;

  --rh-color-gray-10: #f2f2f2;    /* Lightest surface */
  --rh-color-gray-20: #e0e0e0;    /* Light surface */
  --rh-color-gray-30: #c7c7c7;    /* Subtle borders (light theme) */
  --rh-color-gray-40: #a3a3a3;
  --rh-color-gray-50: #707070;    /* Subtle icon, muted text */
  --rh-color-gray-60: #4d4d4d;    /* Secondary text (light theme) */
  --rh-color-gray-70: #383838;    /* Dark surface */
  --rh-color-gray-80: #292929;    /* Darker surface */
  --rh-color-gray-90: #1f1f1f;    /* Even darker */
  --rh-color-gray-95: #151515;    /* Darkest surface / primary text */
}
```

### Semantic surface tokens

```css
:root {
  /* Light theme */
  --rh-surface-lightest: #ffffff;
  --rh-surface-lighter: #f2f2f2;
  --rh-surface-light: #e0e0e0;

  /* Dark theme */
  --rh-surface-dark: #383838;
  --rh-surface-darker: #1f1f1f;
  --rh-surface-darkest: #151515;
}
```

### Semantic text tokens

```css
:root {
  --rh-text-primary: #151515;     /* Light theme */
  --rh-text-secondary: #4d4d4d;   /* Light theme */
  --rh-text-brand: #ee0000;       /* Both themes */
  --rh-text-link: #0066cc;        /* Links (light theme) */
  --rh-text-link-hover: #004d99;  /* Link hover (light theme) */
}
```

### Secondary colors (limit 1–2 per composition, never alone)

```css
:root {
  --rh-color-blue-50: #0066cc;    /* Interaction / links */
  --rh-color-blue-30: #92c5f9;    /* Links on dark */
  --rh-color-purple-50: #5e40be;  /* Info / tips */
  --rh-color-teal-50: #37a3a3;    /* Neutral / general */
  --rh-color-orange-40: #f5921b;  /* Caution */
  --rh-color-yellow-30: #ffcc17;  /* Warning */
  --rh-color-green-50: #63993d;   /* Success */
}
```

### Color usage rules

1. **Keep it simple** — restrained, stylized color with generous whitespace.
2. **Use red with intention** — apply as "pops of red" to highlight key elements. Everything from Red Hat should include it, but never flood a composition with it.
3. **Create balance** — fill large areas with lightest tints, darkest shades, or white. Red is punctuation, not paint.
4. **Never** use red to represent something negative. Use danger-orange (#f0561d) for errors.
5. **Never** omit red entirely from a composition.
6. **Max 2 secondary/accent colors** per layout. Tints and shades of those 2 are fine.

### Color collections (themed palettes)

**Core Light** (default for most artifacts):
- Backgrounds: white, gray-10
- Text: gray-95 (primary), gray-60 (secondary), red-50 (brand accent)
- Borders: gray-30

**Core Dark**:
- Backgrounds: gray-95, gray-80
- Text: white (primary), gray-30 (secondary), red-50 (brand accent)
- Borders: gray-50

**Core Red** (for emphasis slides):
- Backgrounds: red-05, red-10, white
- Text: gray-95, red-50
- Accents: red tints/shades

### Accessibility

- Small text (≤17pt): minimum **4.5:1** contrast ratio (WCAG AA).
- Large text (≥18pt) and icons: minimum **3:1** contrast ratio.
- Never rely on color alone to convey meaning — supplement with text or icons.
- Don't place saturated hues of similar intensity together (causes vibration).

## Spacing

Base unit: 4px. All spacing values are multiples of 4 (one exception: 6px for form fields only).

```css
:root {
  --rh-space-xs: 4px;
  --rh-space-sm: 6px;
  --rh-space-md: 8px;
  --rh-space-lg: 16px;
  --rh-space-xl: 24px;
  --rh-space-2xl: 32px;
  --rh-space-3xl: 48px;
  --rh-space-4xl: 64px;
  --rh-space-5xl: 80px;
}
```

Vertical rhythm:

- Between heading and body text: `--rh-space-lg` (16px).
- Between sections within a layout: `--rh-space-4xl` (64px).
- Top/bottom of a layout: `--rh-space-4xl` (64px) default.
- Between stacked content blocks: `--rh-space-5xl` (80px).
- Headline to CTA: 24–32px depending on size.

## Layout

Use a 12-column grid on desktop/tablet, 2-column on mobile.

```css
:root {
  --rh-grid-max-width: 1136px;   /* xl breakpoint */
  --rh-grid-gutter: 30px;        /* desktop */
}
```

| Breakpoint | Width | Columns | Gutter |
|------------|-------|---------|--------|
| 2xl | ≥1440px | 12 | 32px |
| xl | ≥1200px | 12 | 32px |
| lg | ≥992px | 12 | 32px |
| md | ≥768px | 12 | 32px |
| sm | <768px | 2 | 16px |

For presentation artifacts, the grid is simpler — use a centered container with max-width and generous side padding. Body text should never exceed ~789px (7 grid columns).

## Borders, radii, shadows

```css
:root {
  --rh-border-width-sm: 1px;     /* Default for all borders */
  --rh-border-width-md: 2px;     /* Emphasis, hover/focus states */
  --rh-border-width-lg: 3px;     /* Strong directional emphasis (selected tab, active nav) */

  --rh-border-radius-default: 3px;   /* Cards, panels, buttons, dialogs */
  --rh-border-radius-pill: 64px;     /* Badges, pills, avatars, switches */

  --rh-shadow-sm: 0 2px 4px 0 rgba(21, 21, 21, 0.2);
  --rh-shadow-md: 0 4px 6px 1px rgba(21, 21, 21, 0.25);
  --rh-shadow-lg: 0 6px 8px 2px rgba(21, 21, 21, 0.3);
  --rh-shadow-xl: 0 8px 24px 3px rgba(21, 21, 21, 0.35);
}
```

- Default border radius is 3px — small, subtle rounding. Not the big 12–14px of editorial styles.
- Shadows are optional and should be soft and subtle. Direction must be consistent.
- Borders do more work than shadows. Prefer `border: 1px solid var(--rh-color-gray-30)` over box-shadow for separation.

## Components

### Section headers

Use Red Hat Display, extra-bold weight. No serif. Pair with a thin red accent line or red section number.

```css
.section-header {
  font-family: var(--rh-font-heading);
  font-size: 28px;
  font-weight: 800;
  line-height: 1.3;
  color: var(--rh-text-primary);
  margin: 0 0 var(--rh-space-lg);
}
```

### Eyebrow / overline

Small uppercase label in Red Hat Text or Display. Optional red-50 left bar accent.

```css
.eyebrow {
  font-family: var(--rh-font-body);
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--rh-color-gray-60);
}
```

### Cards

Paper rectangles with 3px radius, 1px border. Clean internal hierarchy.

```css
.card {
  background: var(--rh-color-white);
  border: 1px solid var(--rh-color-gray-30);
  border-radius: 3px;
  padding: var(--rh-space-xl);
  transition: box-shadow 200ms ease;
}
.card:hover {
  box-shadow: var(--rh-shadow-sm);
}
```

Card internal structure:
- Eyebrow or category label (optional)
- Heading (Red Hat Display, extra-bold)
- Body text (Red Hat Text)
- Footer with CTA or metadata

### Pills / badges

Small rounded labels for tags, counts, status.

```css
.pill {
  font-family: var(--rh-font-body);
  font-size: 12px;
  font-weight: 500;
  padding: 4px 12px;
  border-radius: var(--rh-border-radius-pill);
  background: var(--rh-color-gray-10);
  color: var(--rh-text-primary);
}
```

### CTAs / buttons

Red Hat Display bold. Primary uses red-50 background with white text. Secondary uses border only.

```css
.cta-primary {
  font-family: var(--rh-font-heading);
  font-size: 16px;
  font-weight: 700;
  padding: 16px 32px;
  background: var(--rh-color-red-50);
  color: var(--rh-color-white);
  border: none;
  border-radius: var(--rh-border-radius-default);
  cursor: pointer;
}
.cta-primary:hover {
  background: var(--rh-color-red-60);
}
.cta-secondary {
  font-family: var(--rh-font-heading);
  font-size: 16px;
  font-weight: 700;
  padding: 16px 32px;
  background: transparent;
  color: var(--rh-text-link);
  border: 1px solid var(--rh-text-link);
  border-radius: var(--rh-border-radius-default);
  cursor: pointer;
}
```

### Status indicators

Use semantic colors with text labels (never color alone):

| Status | Border/accent color | Background |
|--------|-------------------|------------|
| Success | #3d7317 | #e9f7df |
| Info | #5e40be | #ece6ff |
| Warning | #dca614 | #fff4cc |
| Danger | #b1380b | #ffe3d9 |
| Neutral | #4d4d4d | #f2f2f2 |

### Code blocks

```css
.code-block {
  font-family: var(--rh-font-code);
  font-size: 14px;
  line-height: 1.5;
  background: var(--rh-color-gray-10);
  border: 1px solid var(--rh-color-gray-30);
  border-radius: var(--rh-border-radius-default);
  padding: var(--rh-space-lg);
  overflow-x: auto;
}
```

### Tables

Clean, minimal. Borders between rows, header row distinguished by weight or background.

```css
table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--rh-font-body);
  font-size: 14px;
}
th {
  font-family: var(--rh-font-heading);
  font-weight: 500;
  text-align: left;
  padding: 12px 16px;
  border-bottom: 2px solid var(--rh-text-primary);
  color: var(--rh-text-primary);
}
td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--rh-color-gray-20);
  color: var(--rh-text-primary);
}
```

### Blockquotes

Red Hat Display, larger size. Optional red left border accent.

```css
blockquote {
  font-family: var(--rh-font-heading);
  font-size: 20px;
  font-weight: 400;
  line-height: 1.5;
  color: var(--rh-text-primary);
  border-left: 3px solid var(--rh-color-red-50);
  padding-left: var(--rh-space-xl);
  margin: var(--rh-space-2xl) 0;
}
```

## Icons and diagrams

When creating inline SVG diagrams:

- Use 1.25pt stroke weight (or 2px for screen).
- Rounded corners and rounded stroke ends.
- Angles restricted to 0°, 45°, 90° (or ±12° of those).
- Available in one color only: red, black, or white. No multicolor icons.
- Simple, geometric, flattened perspective.
- Icons work best at 32–100px. For larger visuals, use illustration-style SVGs.

Color for SVG elements:

```css
.icon-red { fill: var(--rh-color-red-50); stroke: none; }
.icon-dark { fill: var(--rh-text-primary); stroke: none; }
.icon-light { fill: var(--rh-color-white); stroke: none; }
.stroke-dark { fill: none; stroke: var(--rh-text-primary); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.stroke-red { fill: none; stroke: var(--rh-color-red-50); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
```

## Interaction style

Use no JS by default. Add JS only for:
- Slide/tab navigation.
- Expand/collapse sections.
- Copy buttons.
- Interactive demos.

Keep interactions local, transparent, and dependency-free. Transitions should be 0.3s with `cubic-bezier(0.465, 0.183, 0.153, 0.946)`.

## Presentation-specific patterns

Since this style is optimized for internal Red Hat presentations:

### Slide-style layout

Full-viewport sections that work as a scrollable deck. Each section is a "slide" with clear visual separation.

### Title slide

- Large heading (heading-2xl or heading-3xl) in Red Hat Display
- Subtitle in Red Hat Text at body-xl
- Optional red accent line
- Speaker/date info in body-sm, gray-60

### Content slide

- Section heading (heading-lg or heading-md)
- Body text, bullet lists, or card grids
- Maximum 3–4 key points per slide

### Data slide

- Section heading
- Table, chart placeholder, or metric cards
- Keep numbers in Red Hat Mono

### Key takeaway slide

- Large pull quote or single statement in heading-xl
- Red accent or red background variant

## Responsive behavior

- At <768px: switch from 12 to 2 columns.
- Heading sizes reduce per the mobile scale.
- Card grids collapse to single column.
- Maintain readable line length (no text spanning full mobile width without padding).
- Gutters reduce from 32px to 16px.

## Print behavior

```css
@media print {
  body { background: white; color: black; }
  .card, .panel { box-shadow: none; break-inside: avoid; }
  nav, button, .no-print { display: none; }
  a { color: inherit; text-decoration: underline; }
  a[href]::after { content: " (" attr(href) ")"; font-size: 0.85em; color: #4d4d4d; }
}
```

## Design checklist

Before finishing, verify:

- Does the page use Red Hat Display for headings and Red Hat Text for body?
- Is Red Hat red (#ee0000) present but used with restraint — as accent, not flood?
- Are all borders using 3px radius (not large rounded corners)?
- Is the type hierarchy clear? Big/bold headings, readable body, mono for data?
- Is all text in sentence case (no ALL CAPS)?
- Are there no more than 2 secondary accent colors?
- Do colors meet WCAG AA contrast requirements?
- Is whitespace generous — does the layout feel open and uncluttered?
- Are code/data elements in Red Hat Mono?
- Would this be immediately recognizable as "Red Hat" to a colleague?
