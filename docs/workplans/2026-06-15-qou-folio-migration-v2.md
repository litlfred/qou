# Requirements V2 — `litlfred/qou` = content/math only, `folio-assistant` = the platform

**Date:** 2026-06-15
**Status:** revised requirements spec
**Owner direction:** *"qou only has content that is math/physics specific and uses folio-assistant as infrastructure."*

## Why V2?
The previous plan (V1) incorrectly grouped some math/physics libraries (like `qou-mass` and Hecke engines in `tools/`) into the "move to folio-assistant" bucket, treating them as generic infrastructure. We must carefully distinguish between **platform infrastructure** (LaTeX build scripts, variable substitution, CI/CD, sidecar validation) and **math/physics content** (computations, predictors, theorem provers).

## Target architecture

| Repo | Role |
|------|------|
| **`litlfred/qou`** | **Content & Math/Physics** — The paper content (`content/<paper>/*.{ts,md,lean}` triples), mathematical computations (`computations/`, `qou-mass/`), domain-specific tools (Hecke engines), bibliography source, and planning/audit docs. No generic pipeline, CI machinery, or platform code. |
| **`folio-assistant`** | **The platform** — generic content pipeline, schemas, LaTeX rendering infra, CI workflows, Docker images, MCP server, documentation generation infra, and build orchestration scripts. |

## Inventory — moves vs stays

### STAYS in qou (Math / Physics / Content)
- `content/<paper>/` — the `.ts` / `.md` / `.lean` triples (the paper itself), including macros.
- `content/schema/references.ts` — bibliography source.
- `docs/` (audits, coordination, workplans), `todos/`.
- `computations/` — Math-specific Python/Lean compute scripts.
- `qou-mass/` — The mass-prediction library (computes Borromean-tower and Markov traces).
- `tools/hecke-engine-*` and other purely mathematical tools.
- `scripts/` (Math/Physics subset) — Specifically, scripts like `derive-stable-n.py`, `first-20-elements.py`, `generate-knot-plots.py`, `knot-particle-generation.py`. (These will be moved to `computations/` to completely clear out `scripts/`).

### MOVES to folio-assistant (Platform / Infra)
- `content/pipeline/` — validate, render-latex, build, `generate-main-tex.ts`, latex-preflight, qa-sweep, migrate-lean-refs, script-sidecars, etc.
- `content/schema/` types/builders/constraints (consolidate with `folio-assistant/schemas/`).
- `latex/` — `preamble.tex` + rendering-target infra.
- `.github/workflows/` (done) + `.github/docker/` + `.github/scripts/` + `.github/actions/`.
- `scripts/` (Infra subset) — `install-tex.sh`, `feature-build.sh`, lake/lean-env build helpers, `render-*.sh`, `audit-*.ts`, etc.
- `blueprint/` and `home_page/` — Web presentation and rendering.
- `tools/` (Infra subset) — Things like `block-qa-schema`, `witness-schema` (should move to `folio-assistant/schemas/`).

## Implementation Steps

1. **Python / Script Audit & Move**:
   - Audit `scripts/` and `tools/`. Move all infra Python/TS/Bash scripts to `folio-assistant`.
   - Move the remaining math/physics scripts into `qou/computations/` or `qou/qou-mass/`.
   - Move `tools/witness-schema` and `tools/block-qa-schema` to `folio-assistant/schemas/`.
2. **Platform Core Migration**:
   - Move `content/pipeline/` to `folio-assistant/pipeline/`.
   - Move `latex/` to `folio-assistant/latex/`.
   - Move `blueprint/` and `home_page/` to `folio-assistant/`.
3. **CI Restoration**:
   - Ensure `folio-assistant` has reusable workflows.
   - Create a thin `.github/workflows/build.yml` in `qou` that calls `folio-assistant/.github/workflows/publish.yml`.
4. **Inherit LaTeX Build Work (#2310)**:
   - Fix paths in `.github/workflows/paper-builder-image.yml` and `build-latex-image.yml` (prefix `folio-assistant/`).
   - Implement fast preview tooling (`generate-main-tex.ts`, `install-tex.sh`, `feature-build.sh`) in `folio-assistant`.
