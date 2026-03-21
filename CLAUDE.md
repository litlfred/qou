# Claude Code — Quantum Observable Universe

This repository is a LaTeX manuscript for a formal mathematics paper.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json`

### Skill routing (quick reference)

When a user request arrives, route to the right skill(s):

| User request pattern | Primary skill(s) |
|---------------------|------------------|
| "fill in / prove / remove sorry" | `local/formalizer` + `local/category-theory` |
| "define / formalize / add structure" | `local/formalizer` + `local/lean-generation` |
| "diagram / naturality / monoidal" | `local/category-theory` |
| "extract / stub / from LaTeX" | `local/lean-generation` |
| "review / check / audit Lean" | `local/lean-proof-review` |
| "status / tracking / manifest" | `local/proof-status-tracking` |
| "what next / priority / triage" | `local/proof-triage` |
| "write / edit chapter text" | `local/scientific-accuracy` + `local/readability-editing` |
| "simplify / streamline proofs" | `local/proof-simplifier` |
| "validate LaTeX" | `local/latex-validation` |

**Decision tree**: (1) Does it touch `.tex`? → LaTeX skills.
(2) Does it touch `.lean`? → Lean skills above. (3) Both? → also
`local/lean-generation` for cross-refs. (4) Ambiguous? → read the skill
`.md` files, then ask the user.

See **§12 Using Skills for Content Changes** in
`.github/copilot-instructions.md` for the full authoritative mapping,
including the detailed decision tree and Lean-specific routing table.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, notation, and skill
usage for content changes.

## Lean MCP server (lean-lsp-mcp)

The [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) server is
configured via `.mcp.json`. It provides Claude Code with:

- Diagnostics, goal states, hover docs, completions
- LeanSearch, Loogle, Lean Finder, Lean Hammer search tools
- Code actions ("Try This"), profiling, axiom verification
- Local project search (requires ripgrep)

### Setup (ChromeOS / Crostini)

Prerequisites: `git`, `curl`.

```bash
./scripts/setup-lean-mcp.sh
```

This installs: uv (Python package manager), elan, the Lean toolchain
pinned in `lean/lean-toolchain`, Mathlib cache, ripgrep, and verifies
`lean-lsp-mcp` via uvx.

**Important**: Run `lake build` in `lean/` before first MCP session to avoid
timeouts.

### Session-start hook

A `SessionStart` hook in `.claude/settings.json` runs `scripts/check-lean.sh`
at the beginning of every session. If Lean or uv is not available and the
user's request requires Lean, the editor skill will prompt the author with
setup instructions rather than silently failing.

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
| `scripts/` | Setup and health-check scripts (Lean MCP, etc.) |
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
