# HTML Artifact Design

A reusable agent skill for producing polished, self-contained HTML artifacts without defaulting to generic dashboard UI. It combines a small routing entrypoint with independently maintained visual styles, minimal starter templates, and selectively loaded component snippets.

## How it works

1. An explicitly requested style routes directly to its folder.
2. Otherwise the agent reads the generated `styles/index.yaml` registry and selects a style.
3. Only the selected design language, starter, and relevant snippets enter context.
4. The resulting artifact is validated for structure, links, dependencies, responsive behavior, reduced motion, and print support.

HTML is offline-first: inline CSS and optional inline SVG or JavaScript, with no network requests by default. Styles may declare optional external assets, but using them requires explicit approval.

## Available styles

<!-- BEGIN GENERATED STYLE INDEX -->
| Style | Best for | Description |
|---|---|---|
| [Editorial](styles/editorial/) | galleries, explainers, reports, code reviews, design references, plans, research explainers | Calm, document-shaped layouts with warm ivory surfaces, serif hierarchy, restrained accents, and content-specific diagrams. |
| [Red Hat](styles/redhat/) | presentations, team updates, project reports, strategy decks, technical overviews, architecture explainers | An open, confident enterprise presentation system with Red Hat typography, restrained red accents, compact radii, and generous whitespace. |
<!-- END GENERATED STYLE INDEX -->

## Repository structure

```text
SKILL.md                         Runtime routing and shared contract
styles/index.yaml               Generated compact style registry
styles/<id>/design-language.md  Style metadata and distinctive rules
styles/<id>/starter.html        Minimal offline-first starter
styles/<id>/snippets/           Optional components loaded on demand
references/                     Conditional guidance
scripts/                        Scaffolding, registry generation, validation
tests/                          Deterministic contract and routing fixtures
```

## Add a style

```bash
python3 scripts/new_style.py <style-id> --name "Style Name" \
  --description "Short routing description" --best-for "reports,explainers"
python3 scripts/build_index.py
python3 scripts/validate.py
```

The style folder is the source of truth. `styles/index.yaml` and this README table are generated from its frontmatter. See [`references/style-authoring.md`](references/style-authoring.md) for the contract.

## Validate

```bash
python3 scripts/build_index.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

Regenerate the reviewed starter baselines with `python3 scripts/render_references.py`.

## Reference renders

| Style | Desktop | Narrow/mobile |
|---|---|---|
| Editorial | [1440×1000](references/screenshots/editorial-desktop.png) | [500×900](references/screenshots/editorial-mobile.png) |
| Red Hat | [1440×1000](references/screenshots/redhat-desktop.png) | [500×900](references/screenshots/redhat-mobile.png) |
