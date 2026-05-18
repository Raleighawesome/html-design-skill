# HTML Design Skill

A Claude Code skill for generating self-contained HTML pages with high design quality. Instead of producing generic dashboard UI, this skill uses curated visual styles to create pages that feel intentional and hand-crafted.

## How it works

The skill supports multiple design styles, each stored as a self-contained folder under `styles/`. When invoked, the skill:

1. Discovers available styles by scanning the `styles/` directory
2. Reads each style's frontmatter to understand what it's best suited for
3. Recommends a style based on the user's request
4. Confirms the choice with the user
5. Reads the full design language and uses the starter template to build the page

All output is self-contained HTML — inline CSS, optional inline SVG, no external dependencies.

## Available styles

| Style | Description |
|-------|-------------|
| [Editorial](styles/editorial/) | Calm, editorial aesthetic inspired by independent publishing. Warm ivory palette, serif headings, restrained accents, document-shaped layouts. |
| [Red Hat](styles/redhat/) | Faithful reproduction of the Red Hat brand design system. Clean, open, and confident with Red Hat Display headings, a red-black-white core palette, 3px border radius, and generous whitespace. |

## Adding a new style

Create a new directory under `styles/` with two files:

```
styles/<style-name>/
  design-language.md
  starter.html
```

### design-language.md

The design language file defines the visual system. It must start with frontmatter:

```yaml
---
name: Human-readable style name
description: One-sentence description of the visual feel.
best-for: comma-separated list of content types this style suits
---
```

The body should cover palette, typography, layout rhythm, component patterns, interaction style, and a design checklist. See [`styles/editorial/design-language.md`](styles/editorial/design-language.md) for a complete example.

### starter.html

A working, self-contained HTML page that demonstrates the style. This is the copy-and-adapt base for new artifacts. It should include:

- CSS custom properties for all design tokens
- Representative layout structure (masthead, sections, cards, footer)
- Responsive breakpoints
- Print styles

See [`styles/editorial/starter.html`](styles/editorial/starter.html) for a complete example.

## Installation

Add this repo as a Claude Code skill, or clone it into a location where your Claude Code configuration can reference it.
