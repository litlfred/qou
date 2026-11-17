---
# qou-otbb
title: Wenzl semisimplicity criterion for H_n(q) in Lean — residue-semisimplicity bridge for conj:qou-p-neq-np
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T01:32:15Z
updated_at: 2026-11-17T07:06:58Z
parent: qou-rtxm
---


Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: Wenzl semisimplicity criterion for H_n(q) in Lean — residue-semisimplicity bridge for conj:qou-p-neq-np


## Round 56 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8241 (`f5d60a0cc755a36459696dc679eebd3728acc344`)
- **Module:** `QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity` (`folio/quantum-observable-universe/lean/QOU/Foundations/SymplecticAtomicityWenzlSemisimplicity.lean`), wired into `QOU.lean`.
- **Theorems:** `wenzlBranch_step_id`, `wenzlBranch_eq_mul_pred`, `wenzlBranch_ratio`, `chebyshevU_rec`, `wenzlIdempotentCoeff_cleared_identity`, `wenzl_trace_recurrence_cleared` — proving Wenzl / Jones-Wenzl projector trace branching recurrence and Chebyshev quantum dimension `[n+1]_q = U_n(d/2)` recurrence over any `CommRing R`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
