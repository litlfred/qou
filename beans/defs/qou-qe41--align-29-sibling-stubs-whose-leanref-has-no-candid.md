---
# qou-qe41
title: Align 29 sibling stubs whose lean.ref has no candidate-2 resolution (MISMATCH/NEEDED)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:12:11Z
updated_at: 2026-10-04T15:16:18Z
parent: qou-6qbv
---


## Scope

29 sibling-resolution stubs whose `lean.ref` decl path has **no
candidate-2 resolution** (`<lakeRoot>/<Decl/Path>.lean` does not exist).
These are the `MISMATCH` (decl sits in a mis-named library file) and
`NEEDED` (genuinely unformalised) classes of the
[`2026-06-14-lean-vacuous-proof-audit.md`](../docs/audits/2026-06-14-lean-vacuous-proof-audit.md)
manifest.

## Why this is NOT a delete sweep

AGENTS.md §0a prescribes **align** for MISMATCH, not delete: rename the
library file (or move the decl) so the decl path resolves. Deleting a
stub whose ref has no candidate-2 leaves the block relying on the
resolver's grep fallback, or resolving to nothing at all.

Renames touch imports, so each is a real change, not a sweep.

## Method that works (from the 7 + 4 already drained)

1. Confirm the sibling is genuinely vacuous — **reading it, not matching
   its name.** `mass-theory/reidemeister-mass-invariance.lean` matched a
   library decl by name and carries a real proof; a name-match
   classifier would have deleted working Lean.
2. Confirm the library decl exists and is substantive — check under the
   **ref's leaf name**, not the class name (that error inflated the
   orphan count by 4).
3. Apply the change, then `bun run scripts/run-validate.ts
   folio/quantum-observable-universe` and **diff the warning set**
   against the pre-change run. A broken `lean.ref` surfaces as a new
   *"no Lean declaration yet"* warning on the affected block; an
   identical warning set is the pass condition.

## Round 86 Formalization (`litlfred/qou#8463`)
- Formalized in `QOU.Foundations.CemeteryBoundaryExclusionCandidateResolutionAlignmentVacuityGateCompletenessDetectorSeededDisjointnessSiblingFieldDriftMasking` (`folio/quantum-observable-universe/lean/QOU/Foundations/CemeteryBoundaryExclusionCandidateResolutionAlignmentVacuityGateCompletenessDetectorSeededDisjointnessSiblingFieldDriftMasking.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`8c2d0febf29bb89e22f415f36e99b433db4a6e8c` -> `7db0f2c21353c4c150810bb9822c963b3c0ed80d`, `scriptHash = scriptSha256 = c68b728f98350112bedd3f85302ce46d7d3318d556c2797c1bfab1197342b290`).
- PR: https://github.com/litlfred/qou/pull/8463
