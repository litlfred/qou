---
# qou-atsd
title: Atomicity from self-duality — derive TensorGenerationFree (rank-one) from the volume-form axiom + dim V=2
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T20:32:48Z
updated_at: 2026-11-17T07:06:58Z
parent: qou-rtxm
---

Replace the bare TensorGenerationFree premise (#4285) with a derivation: symplectic self-duality of V + dim V=2 => G <= Sp(V)=Sp2=SL2 => rank G <= dim V/2 = 1 => Subsingleton S. Plan: docs/workplans/2026-07-25-atomicity-from-self-duality-attack-plan.md. Children T0-T4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: atomicity from self-duality — derive TensorGenerationFree (rank-one) from the volume-form axiom + dim V=2


## Round 56 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8241 (`f5d60a0cc755a36459696dc679eebd3728acc344`)
- **Module:** `QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity` (`folio/quantum-observable-universe/lean/QOU/Foundations/SymplecticAtomicityWenzlSemisimplicity.lean`), wired into `QOU.lean`.
- **Theorems:** `symplecticForm2_bilinear`, `symplecticForm2_eq_det2_mul`, `sp2_iff_sl2`, `sp2_preserves_symplecticForm2` — proving non-vacuously over any `CommRing R` that `M^T J_2 M = det(M) J_2` and `Sp(2, R) = SL(2, R)` via genuine 2x2 matrix multiplication.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
