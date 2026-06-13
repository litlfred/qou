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

## Detangler scope (deferred to a focused editorial pass)

All 54 detangler findings are **structural/editorial restructures**, not mechanical
fixes — so they are scoped here and deferred to a `chapter-complexity-review` +
`content-validation` editorial tranche with author judgment on chapter ordering.
They are NOT drained in this compute-focused PR.

| Class | Count | Severity | Nature |
|---|---|---|---|
| forward-ref | 3 | major | logical def→def cross-chapter forward refs |
| cross-chapter-forward | 12 | minor | chapter-pair forward-edge aggregates (baseline coupling) |
| isolated-block | 18 | minor | orphan blocks needing `uses[]` wiring |
| sparse-section | 20 | minor | sections below the 3-block band |
| dense-section | 1 | minor | one section above the 18-block band |

**The 3 majors (logical forward-refs)** each need a reorder/rewire decision:
- `def:skein-resolution-obstruction` (braids-and-knots) → `def:computational-horizon` (information-theory)
- `def:embeddable-knot-operator` (molecular-construction) → `def:covalent-bond-types` (organic-chemistry)
- `def:quark-antiquark-production` (particle-interactions) → `def:breit-wheeler-pair-production` (predicted-spectra)

Each is a definition referencing one defined in a LATER chapter; resolving requires
moving the referenced definition earlier or breaking the dependency — a chapter-ordering
call for the author. **Recommended:** a dedicated `chapter-complexity-review` editorial
tranche; do not auto-restructure chapters here.
