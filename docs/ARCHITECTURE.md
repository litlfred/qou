# QOU Architecture

This document describes the **architecture of the QOU repository** — how the layers fit together, where canonical compute lives, and how downstream consumers access it. For contributor onboarding, see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## Layered architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│ LAYER 4 — Witness JSON (universal interchange format)                │
│ folio-assistant/computations/*.witness.json — every script emits     │
│ ~860 files; schema = tools/witness-schema/schema/witness.schema.json │
└──────────────────────────────────────────────────────────────────────┘
                                  ▲
                                  │ emits
                                  │
┌──────────────────────────────────────────────────────────────────────┐
│ LAYER 3 — Two consumer paths emit Layer-4 witnesses                  │
│                                                                      │
│ (A) In-repo compute scripts (Python, folio-assistant/computations/)  │
│     ~539 scripts. Each runs the canonical pipeline directly. ~67%    │
│     depend on the substrate trio; ~60% depend on pyhecke; ~2% depend │
│     on pyhecke-native (Rust acceleration).                           │
│                                                                      │
│ (B) qou-mass high-level facade (qou-mass/, PyPI `qou-mass`)          │
│     `predict("4He")` / `compute_tr_M(Z, N)` / `canonical_braid(...)` │
│     for external researchers — no paper-repo checkout needed.        │
│     Vendors per-Z shards + on-demand `markov_peel` recomputation.    │
│     Status: alpha (`v0.1.0a1`); not yet adopted by the in-repo       │
│     scripts (path-A and path-B are parallel today, see Coherence     │
│     status below).                                                   │
└──────────────────────────────────────────────────────────────────────┘
                  ▲                                ▲
                  │ uses                           │ uses
                  │                                │
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│ LAYER 2a — qou-substrate (Py)   │   │ LAYER 2b — pyhecke (Py)          │
│ tools/qou-substrate/            │   │ tools/pyhecke/                   │
│ • WitnessBuilder                │   │ • gram (NF, Markov-trace)        │
│ • _precision (mpmath dps)       │   │ • wedderburn (q-combinatorics)   │
│ • q_parameter (Q, HA, q_int)    │   │ • molecular (binding)            │
│                                 │   │ • atom (NF + per-gen volumes)    │
│ Published as `qou-substrate`    │   │ • constants (α-EM, E_MOL, FIG8)  │
│ on PyPI. Pyodide-ready.         │   │                                  │
│                                 │   │ Published as `pyhecke` on PyPI.  │
└─────────────────────────────────┘   └─────────────────────────────────┘
                                                   ▲
                                                   │ wraps via PyO3
                                                   │
                          ┌─────────────────────────────────────────┐
                          │ LAYER 1 — hecke-engine (Rust core)       │
                          │ tools/hecke-engine/                       │
                          │ • Gröbner-Shirshov reducer (gb_nf_reducer)│
                          │ • Gram matrix (gram)                      │
                          │ • Hoefsmit seminormal (seminormal{,_mn,   │
                          │   _mpfr})                                 │
                          │ • Markov-trace (tr_m_word_lq,             │
                          │   tr_m_atomic_mpfr)                       │
                          │ • Wenzl LR (wenzl_lr)                     │
                          │ • Clarabel SDP backends (opt-in feature)  │
                          │                                           │
                          │ Consumers:                                │
                          │ • pyhecke-native (PyO3, on PyPI)          │
                          │ • hecke-engine-node (napi-rs, npm)        │
                          │ • hecke-engine-wasm (wasm-bindgen, npm)   │
                          └─────────────────────────────────────────┘
```

## Cross-language consumer matrix

| Runtime | Witness reader | Hecke compute |
|---|---|---|
| **Python (CPython, Pyodide)** | `qou-substrate` + `witness-schema` (PyPI) | `pyhecke` + `pyhecke-native` (PyPI); `qou-mass` (high-level facade, PyPI, alpha) |
| **TypeScript / Node / Deno / Bun** | `@litlfred/witness-schema` (npm — Zod + JSON Schema) | `@litlfred/hecke-engine-node` (npm — napi-rs native) |
| **Browser / WASM** | Same npm package as above | `@litlfred/hecke-engine-wasm` (npm — wasm-bindgen, rug-free surface) |
| **R / Kotlin / Java / Swift / C** | JSON Schema (from npm or PyPI download) | Tier-3; not yet shipped (UniFFI / extendr / cbindgen templates ready) |

The **witness JSON** is the universal data-interchange format. Any language with a JSON parser + JSON-Schema validator can read every witness file the repo produces.

## Library coherence status

The package ecosystem is layered but **mid-migration**. Today's import counts (from `folio-assistant/computations/*.py`, the 901-file compute layer; refresh with [`scripts/audit-library-coherence.sh`](../scripts/audit-library-coherence.sh)):

| Package | Importers in compute layer | Status |
|---|---:|---|
| [`qou-substrate`](../tools/qou-substrate/) | 25 | wired — substrate trio, the foundation |
| [`pyhecke`](../tools/pyhecke/) | 41 | wired — primary Hecke / Gram surface |
| [`pyhecke-native`](../tools/pyhecke-native/) | 20 | wired — Rust-accelerated Markov trace |
| [`qou-mass`](../qou-mass/) | **0** | alpha, not yet adopted |
| [`witness-schema`](../tools/witness-schema/) | **0** | alpha, not yet adopted |
| `mpmath` (transitive via `qou_substrate.precision`) | 593 | direct imports — pre-substrate carve-out |
| `sympy` | 206 | direct imports — `Rational`, `Symbol`, partition combinatorics |
| `numpy` | 127 | direct imports — Gram-matrix linear algebra |
| `scipy` | 20 | direct imports — LP/SDP fallbacks |

The two zero-import packages (`qou-mass`, `witness-schema`) ship clean public APIs (`predict()`, `compute_tr_M()`, `ComputationWitness.model_validate_json()`); they're not yet adopted because the in-repo compute scripts predate them. They are the **external-researcher interface** — `pip install qou-mass` gets you the canonical predictions without cloning this repo. The migration of in-repo scripts onto these packages is tracked by [`docs/workplans/2026-05-24-library-reuse-production-readiness.md`](workplans/2026-05-24-library-reuse-production-readiness.md).

A pre-commit / CI audit ([`scripts/audit-library-coherence.sh`](../scripts/audit-library-coherence.sh)) re-counts these numbers and flags any new zero-import library packages.

## Content-object architecture

Each definition / theorem / lemma / proposition / corollary / remark / conjecture is a file triple:

```
<chapter-dir>/<block>.ts     ← typed manifest (kind, label, dependencies)
<chapter-dir>/<block>.md     ← narrative content (markdown + TeX snippets)
<chapter-dir>/<block>.lean   ← Lean formalization (required for `definition`)
```

Validation is three layers (run via `bun run validate` from `content/`):

1. **Zod schema** — shape + types
2. **Constraint rules** — file existence, cross-references, lean requirements
3. **AST validation** — `unified-latex` parse of rendered LaTeX

See `content/schema/types.ts` for the typed manifest definitions and [`CLAUDE.md`](../CLAUDE.md) §"Content-object architecture" for the full rules.

## Lean workspace

The repo uses a **single root Lake workspace** ([`/lakefile.toml`](../lakefile.toml), [`/lean-toolchain`](../lean-toolchain)) that aggregates every paper package as a `[[require]]`:

| Package | Paper directory | Library module |
|---|---|---|
| `qou` | `content/quantum-observable-universe/lean/` | `QOU` |
| `ugb` | `content/unital-groebner-bases/lean/` | `UGB` |
| `fred2005` | `content/fred2005-formal-groups/lean/` | `Fred2005` |

**Preferred build commands** (from repo root):

```bash
lake build           # build every paper package
lake build QOU       # single paper library
lake exe cache get   # fetch Mathlib cache for the workspace
```

Per-paper `cd content/<paper>/lean && lake build` still works, but root-workspace commands are the standardized entry point used by CI.

The CI [`lean_ci.yml`](../.github/workflows/lean_ci.yml) uses the [`lake-cache-restore` composite action](../.github/actions/lake-cache-restore/action.yml) — a 3-tier fallback (actions/cache → orphan-branch `lake-cache/<pkg>-<toolchain>` → Mathlib upstream Reservoir). See [`docs/workplans/2026-05-24-lean-cache-strategy.md`](workplans/2026-05-24-lean-cache-strategy.md).

## CI architecture

| Workflow | Triggers | What | Wall time |
|---|---|---|---:|
| [`witness-pipeline.yml`](../.github/workflows/witness-pipeline.yml) | push / PR | 9 substrate-precision smoke scripts | ~2 min |
| [`lean_ci.yml`](../.github/workflows/lean_ci.yml) | push / PR | `lake build` workspace (with 3-tier cache) | ~30 s warm, ~10 min cold |
| [`publish.yml`](../.github/workflows/publish.yml) | push / PR | Content → LaTeX → PDF → gh-pages preview (uses `paper-builder` Docker container — Phase C of parallelization) | ~22-28 min |
| [`blueprint.yml`](../.github/workflows/blueprint.yml) | push to main | LeanBlueprint dependency graph + axiom report | ~5-10 min |
| [`paper-builder-image.yml`](../.github/workflows/paper-builder-image.yml) | Dockerfile change | Builds `ghcr.io/litlfred/qou-paper-builder` (TeX Live + bun + py-sci) | ~15-20 min |
| [`lake-cache-refresh.yml`](../.github/workflows/lake-cache-refresh.yml) | lakefile / lean-toolchain change on main | Refreshes `lake-cache/*` orphan branches | ~5-15 min/pkg |
| [`pyhecke-pypi-publish.yml`](../.github/workflows/pyhecke-pypi-publish.yml) | `workflow_dispatch` only | Publish `pyhecke` to PyPI (Trusted Publishers OIDC) | ~3 min |
| [`pyhecke-native-wheels.yml`](../.github/workflows/pyhecke-native-wheels.yml) | push / `workflow_dispatch` | Build + publish `pyhecke-native` wheels (cibuildwheel on Linux + macOS-arm64) | ~15-20 min |
| [`snappea_wasm.yml`](../.github/workflows/snappea_wasm.yml) | `workflow_dispatch` only | Build + publish `@snappea/kernel` WASM kernel to npm | ~20 min |
| [`hecke-engine-wasm.yml`](../.github/workflows/hecke-engine-wasm.yml) | push / PR | Build `@litlfred/hecke-engine-wasm` WASM artifact (Phase B publish-on-demand) | ~5 min |

## Deployment

`gh-pages` branch hosts:

| Path | Source | What |
|---|---|---|
| `index.html` | `publish.yml` | Folio landing page |
| `papers/<dir>/` | `publish.yml` | Per-paper viewer + PDF |
| `blueprint/` | `blueprint.yml` | LeanBlueprint interactive graph |
| `docs/` | `blueprint.yml` | doc-gen4 API documentation |
| `content/quantum-observable-universe/lean/` | `lean_ci.yml` | Raw Lean source browser |
| `schema-docs/` | `publish.yml` | TypeDoc content-object reference |
| `drafts/<branch>/` | `publish.yml` | Feature-branch previews |

The **folio deployment** (`deploy/`) is a separate Docker-based hosting for the MCP server + folio-assistant viewer; see [`deploy/setup-remote.sh`](../deploy/setup-remote.sh) and [`lean-mcp.config.json`](../lean-mcp.config.json).

## Workplan + design-doc index

| Document | Purpose |
|---|---|
| [`docs/workplans/2026-05-24-library-reuse-production-readiness.md`](workplans/2026-05-24-library-reuse-production-readiness.md) | Master tier-1/2/3 plan for the package ecosystem |
| [`docs/workplans/2026-05-24-downstream-consumer-libraries-status.md`](workplans/2026-05-24-downstream-consumer-libraries-status.md) | What's done vs. pending across the consumer matrix |
| [`docs/workplans/2026-05-24-lean-cache-strategy.md`](workplans/2026-05-24-lean-cache-strategy.md) | Hybrid Tier-1 actions/cache + Tier-2 orphan-branch family |
| [`docs/workplans/2026-05-24-publish-yml-parallelization-plan.md`](workplans/2026-05-24-publish-yml-parallelization-plan.md) | 5-stage / 8-job DAG for publish.yml (Phase A→D) |
| [`docs/canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md) | The 11-step canonical chain (substrate → MeV) |
| [`docs/precision-goals.md`](precision-goals.md) | L1 (compute) + L2 (per-observable) precision targets |
| [`docs/audits/2026-05-24-hecke-core-canonical-audit.md`](audits/2026-05-24-hecke-core-canonical-audit.md) | Canonical vs exploratory classification of `hecke_core.py` |

## Glossary

| Term | Meaning |
|---|---|
| **Substrate** | The fundamental parameter `q_0 ≈ 1.1097` from which all observables derive |
| **Canonical surface** | The 11-step derivation chain (cheat sheet) — pyhecke owns 100% of this |
| **Exploratory surface** | Phase-5 LP-dual + Plancherel-trace cluster — lives in `_deprecated/hecke_core_legacy.py` |
| **L1 / L2 precision** | L1 = compute-stable to 1 ppb; L2 = per-observable σ_pred ≤ σ_exp / 100 |
| **CAL-2 floor** | The CODATA-2022 experimental precision floor (~780 ppb on m_p) |
| **NF** | Normal Form (in the H₃(q) Gröbner-Shirshov reduction) |
| **Markov trace** | The Jones-polynomial-yielding trace on H_n(q) |
| **Hoefsmit** | The seminormal-form construction of irreducible representations |
| **Wedderburn-Artin weights** | `w_λ = d_q(λ)² / [n]_q!` — LP shadow prices from Frobenius positivity |
| **AME** | Atomic Mass Evaluation (the experimental nuclear-mass database) |
