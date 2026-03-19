# Claude Code — Quantum Observable Universe

This repository is a LaTeX manuscript for a formal mathematics paper.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json`

### When to use skills

See **§12 Using Skills for Content Changes** in
`.github/copilot-instructions.md` for the authoritative task-to-skill mapping
and rules. That section is the single source of truth — do not duplicate its
guidance here.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, notation, and skill
usage for content changes.

## Project structure

| Path | Purpose |
|------|---------|
| `main.tex` | Preamble and document structure |
| `chapters/*.tex` | One file per chapter |
| `references.bib` | BibTeX database |
| `lean/` | Lean 4 formalization (lakefile.lean, QOU/) |
| `blueprint/src/` | LeanBlueprint source (content.tex, preamble.tex, web.tex, print.tex) |
| `home_page/` | Jekyll landing page for GitHub Pages |
| `.github/workflows/` | CI/CD pipelines |
| `.github/scripts/` | Python orchestration (ontologist, extraction, stub generation) |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `skills-config.json` | Skill package subscriptions |

## Build output (gh-pages)

Three workflows deploy to the `gh-pages` branch. GitHub Pages must be
configured to **deploy from the `gh-pages` branch** (not "GitHub Actions").

### Workflow → artifact mapping

| Workflow | Artifacts deployed to gh-pages |
|----------|-------------------------------|
| `blueprint.yml` | `blueprint/` (interactive dependency graph), `blueprint.pdf`, `docs/` (doc-gen4 API), `axiom-report.txt`, manifests |
| `lean_ci.yml` | `lean/` (source browser), `lean/docs/`, `axiom-report.txt`, `dependency-graph.svg`, manifests |
| `publish.yml` | `quantum-observable-universe.pdf`, `.md`, `index.html`, `paper.html`, `style.css`, `drafts/` (feature branches) |

### Expected gh-pages contents

| Path | Source | Description |
|------|--------|-------------|
| `index.html` | publish.yml | Landing page with paper/visualizer toggle |
| `quantum-observable-universe.pdf` | publish.yml | Compiled paper |
| `quantum-observable-universe.md` | publish.yml | Pandoc Markdown |
| `blueprint/` | blueprint.yml | Interactive dependency graph (plasTeX HTML) |
| `blueprint.pdf` | blueprint.yml | Print blueprint |
| `docs/` | blueprint.yml | doc-gen4 API documentation with hover definitions |
| `lean/` | lean_ci.yml | Raw Lean source files |
| `lean/docs/` | lean_ci.yml | doc-gen4 or fallback source browser |
| `axiom-report.txt` | blueprint.yml / lean_ci.yml | sorry audit, axiom dependencies |
| `dependency-graph.svg` | lean_ci.yml / publish.yml | Visual proof dependency graph |
| `proof-objects.json` | all | Formalization status manifest |
| `glossary.json` | all | Semantic glossary |
| `mapping.json` | all | Narrative-to-Lean identifier map |
| `drafts/<branch>/` | publish.yml | Feature branch preview builds |

### Error resilience

All workflows use `continue-on-error: true` at critical points so partial
output is still deployed even when the Lean build fails:

- **Lean build fails** → proof status updates, axiom report generates, source
  browser deploys.  `proof-objects.json` records which declarations errored.
- **doc-gen4 fails** → `lean_ci.yml` generates a fallback HTML source browser.
- **Blueprint compilation fails** → other artifacts (manifests, axiom report)
  still deploy.
- **latexdiff fails** → main PDF still publishes; diff PDF is skipped.
