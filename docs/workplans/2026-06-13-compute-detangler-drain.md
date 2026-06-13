# D-drain follow-up — compute + detangler (post-#2246)

Follow-up tranche to PR #2246 (`/integration-watch all`). Drains the tractable
remaining compute backlog and scopes the detangler restructures. Full context:
[`docs/audits/2026-06-13-integration-watch-all-handover.md`](../audits/2026-06-13-integration-watch-all-handover.md).

## Scope
- **compute I6 ×2** — fix the list-shaped witness producers
  (`per_pair_wedderburn_enumeration`, `topic2_mirror_pair_phi8_boundary_scan`) to
  emit dict-shaped `data` so `witness_dependency_drift.py` stops crashing.
  Coordinate with PR #1878.
- **compute I9 ×21** — route un-exempt CODATA literals through the registry; mark
  Class-B/C/D exempt with reasons.
- **compute I1 ×9** — add probe + production consumer where trivial; flag the rest
  (mostly real open work).
- **detangler ×54** — scope only (semantic section restructures → focused editorial pass).

## Verification
Restored lake-cache + `lean`-direct over `LEAN_PATH` (never `lake`, which wipes the
cache), `bun run validate`, witness re-runs per the compute-audit long-compute discipline.
