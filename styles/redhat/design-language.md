---
schema_version: 1
id: redhat
name: Red Hat
description: An open, confident enterprise presentation system with Red Hat typography, restrained red accents, compact radii, and generous whitespace.
best_for: ["presentations", "team updates", "project reports", "strategy decks", "technical overviews", "architecture explainers"]
avoid_for: ["informal editorial stories", "ornamental portfolios", "consumer lifestyle content"]
external_assets: optional
---

# Red Hat design language

Sources studied: Red Hat Brand Standards v6.5, the Red Hat Digital Design System, and `@rhds/tokens`. These source claims are documentation context; verify current brand requirements when exact compliance matters.

## Recognizable traits

The style is clean, open, and confident: generous whitespace, direct hierarchy, compact corners, and deliberate red punctuation against black, gray, and white. It should feel enterprise-grade without becoming sterile.

The brand personality is open, authentic, helpful, and brave. Translate that into uncluttered layouts, useful content, confident typography, and little ornamentation.

Use the CSS custom properties in `starter.html` as the canonical token implementation.

## External fonts

The offline-first starter requests no remote assets. It uses locally installed Red Hat fonts when available and falls back to Helvetica, Arial, and Courier.

When the user explicitly approves network-loaded fonts, read `snippets/google-fonts.html` and add its head links. Never enable them silently.

## Typography

- **Red Hat Display:** headings, titles, pull quotes, navigation, and calls to action. Use weight 800 for major headings.
- **Red Hat Text:** paragraphs, descriptions, and extended reading.
- **Red Hat Mono:** code, technical labels, dates, versions, and measured values.
- Use sentence case for content. A compact uppercase eyebrow is the sole permitted display exception.
- Do not alter tracking except for that eyebrow treatment.
- Use bold or color for emphasis, not both. Keep body copy neutral rather than red.
- Keep body lines below roughly 100 characters and align text left by default.

## Color

- Red `#ee0000` must appear, but as punctuation rather than a large default field.
- White and gray surfaces carry most of the composition; `#151515` is primary text.
- Blue is for links. Add at most two other semantic accent families.
- Never use brand red as the sole indication of failure or danger.
- Maintain 4.5:1 contrast for normal text and 3:1 for large text and meaningful graphics.
- Never rely on color alone to communicate state.

## Spacing and layout

- Use a 4px spacing base, with 16, 24, 32, 48, 64, and 80px as the main rhythm.
- Center presentation artifacts in a wrapper near 1136px.
- Use broad sections with clear separation and generous whitespace.
- Keep prose to roughly seven desktop grid columns rather than spanning the full wrapper.
- Collapse multi-column layouts below 768px and reduce gutters from 32px to 16px.

## Components

- **Cards:** white surfaces, 1px gray borders, 3px radii, and optional subtle shadow on hover.
- **Pills:** compact status or metadata labels with text; never communicate status through color alone.
- **Tables:** strong header rule, quiet row dividers, left-aligned labels, and horizontal containment on mobile.
- **Metrics:** measured values in Red Hat Mono. Do not invent metrics to decorate the page.
- **Takeaways:** one decisive statement with a red directional accent or a single red emphasis panel.
- **Diagrams:** simple geometric inline SVG, 2px strokes, rounded ends, and red/black/white as the default palette.

Load optional components from `snippets/` rather than copying the entire catalog into every artifact.

## Interaction and accessibility

- Use no JavaScript by default. Add only local, transparent interactions.
- Use visible blue focus rings and native controls.
- Keep transitions near 300ms with the starter easing; disable them for reduced-motion users.
- Give informative SVGs accessible names and hide decorative shapes.

For complex interactions or data displays, also read `../../references/accessibility.md`.

## Print behavior

- Use white backgrounds and black text.
- Remove navigation and controls.
- Flatten shadows and avoid splitting cards, tables, metrics, or takeaways.
- Print link destinations only when the resulting page remains readable.

## Completion checklist

- Are headings bold, confident, and sentence case?
- Is red visible but restrained?
- Are default corners 3px rather than broadly rounded?
- Are measured values and technical labels in Red Hat Mono?
- Is the layout open, accessible, responsive, and print-ready?
- Does the page work offline unless the user approved optional fonts?
