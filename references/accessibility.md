# Accessibility details

Read this reference for interactive, data-dense, or unusually visual artifacts.

- Maintain logical heading order and landmark structure.
- Keep text contrast at WCAG AA: 4.5:1 for normal text and 3:1 for large text and meaningful graphics.
- Never rely on color alone for state or meaning.
- Provide visible `:focus-visible` treatment for links, buttons, inputs, and custom controls.
- Use native controls before ARIA. Give informative SVGs a role and accessible name; hide decorative SVGs.
- Ensure every interaction is keyboard operable and does not trap focus.
- Respect `prefers-reduced-motion: reduce` and avoid essential information conveyed only through animation.
- Reflow without horizontal page scrolling at narrow widths; place unavoidable wide tables in labeled scrolling regions.
- Preserve readable output when printed or saved as PDF.
