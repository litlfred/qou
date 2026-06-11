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
