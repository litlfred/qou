# Census appendix — tooling extraction + skills/MCP consolidation

Companion to
[`2026-06-11-tooling-extraction-skills-migration.md`](2026-06-11-tooling-extraction-skills-migration.md).
Produced by repo-wide inventory, 2026-06-11.

## Per-package extraction verdicts

| Package | QOU refs | Physics-term files | Verdict |
|---|---|---|---|
| `tools/pyhecke` | 13 | 14 | **Mechanical** — soft try/except substrate import (no pyproject dep); the import-time q₀ constants in `gram.py` are the one API change (Phase 2a) |
| `tools/pyhecke-native` | 3 | 1 | **Mechanical** — thin wrapper; Cargo path-dep on hecke-engine (extract together) |
| `tools/hecke-engine` | 27 | **83** | **Needs refactor** — ~15.9k LOC Rust; hardcoded `Q_0: f64 = 1.10997…`, `_proton_g0()` / `_neutron_g0()` in `src/gram.rs`; parametrize q + rename physics-flavored items |
| `tools/hecke-engine-{wasm,node,r,jvm,c}` | 0 | 0 | **Trivial** — move as-is, Tier-3 banner for r/jvm/c |
| `tools/witness-schema` | 6 | 1 | **Mechanical** — naming only |
| `tools/qou-substrate` | 8 | 6 | **Stays** (per wall principle). Census alternative noted: generalize to an abstract q-solver + optional physics calibration — owner decision, not default scope |

Test fixtures: only 4 physics-named test files (`test_gram_values.py`,
`test_native.py`, `test_undo.py`, `test_markov_combo.py` + one Rust
`test_proton_borromean_in_h3`), all with generic assertions (q pinned as a
constant, no MeV values) → rename + parametrize, math unchanged. Low cost.

## Dependency directions

- pyhecke → substrate: conditional (`q_parameter` shim → `qou_substrate`
  fallback); already anticipates standalone use (Sage/PyPI/Pyodide chain).
- pyhecke-native → hecke-engine: Cargo `path = "../hecke-engine"`.
- **Clarabel: confirmed git fork** — `[patch.crates-io] clarabel = { git =
  "https://github.com/litlfred/Clarabel.rs", rev = "9673209" }` in BOTH
  `hecke-engine/Cargo.toml` and `pyhecke-native/Cargo.toml`. Fork delta:
  trait decoupling (Copy→Clone) for exact-rational diagnostics, `rug`
  interop (MpfrFloat backend), BlockDiagPSDConeT + `tighten_to_rational`
  (Round 4). 71/71 hecke-engine tests pass under `--features clarabel-sdp`.
  Disposition: sibling repo (or workspace member) of the new home; assess
  what is upstreamable to oxfordcontrol/Clarabel.rs.
- folio-assistant/src: **zero** imports from tools/ (clean).
- computations: **221 of 778 scripts** consume
  pyhecke/qou_substrate — but routed through the `hecke_core.py` sys.path
  bootstrap, which is the single choke point for the Phase 4 repoint.

## Package metadata / release infra

pyhecke 0.1.1, pyhecke-native 0.9.0, hecke-engine 0.8.0 (crates.io),
witness-schema 0.1.1, qou-substrate 0.1.1. Repository URLs in metadata
point into the monorepo tree (`github.com/litlfred/qou/tree/main/tools/…`)
→ Phase 3 repoint. Workflows: `pyhecke.yml`, `pyhecke-pypi-publish.yml`
(manual), `pyhecke-native-wheels.yml` (4-target maturin matrix),
`hecke-engine-wasm.yml` (npm), `wrapper-tests.yml` (R/Julia/GAP/Octave),
`release-please.yml` (version automation) — the new repo needs equivalents.

## Skills/MCP migration state ("started not finished")

- Inventory: **80 skill .md + 24 .ts** under `.claude/skills/local/`.
- Design doc exists but is ARCHIVED:
  [`docs/_archive/orphan-top-level/FOLIO_MIGRATION_PLAN.md`](../_archive/orphan-top-level/FOLIO_MIGRATION_PLAN.md)
  (550 lines; Phases 1–4). Its §Skills Audit prescribes: move the
  adapter-generic skills (`deployment-auth`, `editor` core, `todo-review`,
  `readability-editing`); domain skills (formalizer, lean-*, proof-*,
  compute-*, ontologist, …) stay with the paper repo.
- Implemented so far: folio-assistant core + auth stub;
  `folio-assistant/src/tools/skill-fetch.ts` exists as a skeleton; **no
  skills directory in folio-assistant yet** (estimate: 40% design, 0%
  execution).
- Phase 5 of the master workplan = revive the archived plan's Phase 4:
  skill registry + routing layer in folio-assistant, move the ~5 generic
  skills, leave `.claude/skills/local/` shims.

## Critical paths (extraction references)

- `tools/qou-substrate/python/qou_substrate/constants.py` — physics anchor
  (q₀, m_p/m_e CODATA, proton substrate identity)
- `tools/hecke-engine/src/gram.rs` — hardcoded Q_0 + nucleon-named fns
- `tools/pyhecke/python/pyhecke/{constants,gram}.py` — conditional
  substrate import + import-time q₀ constants
- `computations/hecke_core.py` — consumer choke point
- `.github/workflows/{pyhecke,pyhecke-native-wheels,hecke-engine-wasm,release-please}.yml`
