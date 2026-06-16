# Coordination ledger — tooling extraction + skills/MCP consolidation

Master workplan: [`docs/workplans/2026-06-11-tooling-extraction-skills-migration.md`](../workplans/2026-06-11-tooling-extraction-skills-migration.md)

## Entries

### 2026-06-11 — plan opened (session claude/modest-einstein-oytxmq)

- Workplan committed; census appendix pending (background inventory agent).
- Confirmed: pyhecke `gram.py`/`wedderburn.py` bind substrate q₀ at import
  time → Phase 2a is an API change (parametrize q), not find-replace.
- Clarabel: feature-flag `clarabel-sdp` in hecke-engine Cargo.toml;
  fork-vs-crates status to be recorded here once censused.
- Sibling overlaps to coordinate: #2104 (compute-pipeline generalization —
  scope reconciliation needed before either side restructures), #2103
  (per-isotope stack — pyhecke consumer, API-stability notice).
- Owner decisions pending: new repo name/org; license (MIT/Apache-2.0 dual
  recommended); witness-schema split; provenance wording.

### 2026-06-11 — census appendix landed (same session)

- Verdicts: pyhecke / pyhecke-native / witness-schema **mechanical**;
  **hecke-engine needs-refactor** (83 physics-coupled files; hardcoded
  `Q_0`, `_proton_g0`/`_neutron_g0` in `src/gram.rs`); bindings trivial;
  qou-substrate **stays** (census's "generic-q-solver" alternative recorded
  as an owner option).
- Clarabel confirmed: fork `litlfred/Clarabel.rs` rev `9673209`
  (bigrational/MpfrFloat backend, BlockDiagPSDConeT), `[patch.crates-io]`
  in hecke-engine + pyhecke-native; 71/71 tests green with `clarabel-sdp`.
- Consumer set: 221/778 compute scripts, choked through
  `computations/hecke_core.py` → Phase 4 repoints the shim.
- Skills/MCP: 80 .md + 24 .ts in `.claude/skills/local/`; design doc is the
  ARCHIVED `docs/_archive/orphan-top-level/FOLIO_MIGRATION_PLAN.md`
  (~5 generic skills move; domain skills stay) — Phase 5 revives it.

### 2026-06-11 — Phase 0 started (session claude/modest-einstein-oytxmq)

- Wall gate live: `scripts/extraction_wall_gate.py` (warn-only ratchet;
  `--strict` flips hard after Phase 2) + committed baseline
  `tools/extraction-wall-baseline.json` (94 qou-referencing source files
  across the nine extraction-bound packages; hecke-engine 49 — the
  earlier 186 census count included build artifacts, now skipped).
- Intent comments posted: #2104 (scope reconciliation before tools/
  restructure), #2103 (pyhecke API-stability notice).
- Still pending from owner: new repo name/org, license, witness-schema
  split, provenance wording.
