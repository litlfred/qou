---
# confinement_frobenius_reciprocity
title: confinement frobenius reciprocity missing hypotheses
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-16T20:28:25Z
parent: qou-uot9
pr: 8189
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean`
The `confinement_frobenius_reciprocity` theorem is unprovable. The class `ConfinementFrobeniusReciprocityContext` only provides data fields (Gram matrix, shadow prices, active set) without the KKT/complementary slackness axioms needed to prove the reciprocity master formula.



Also known as `cfre` (its former front-matter header id; the beans CLI uses the filename id `confinement_frobenius_reciprocity`). Recorded 2026-10-04.

## Progress (PR #8189, 2026-11-16T20:28:25Z)

- [x] Replaced the 6-tuple self-assuming projection in `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean` with the 2-step KKT active-subspace derivation (`reciprocity_of_kkt` via `Finset.sum_mul` and `Finset.sum_comm`), derived all 5 LP supporting facts (`primal_nontrivial_of_net`, `y_0_star_pos_of_duality`, `A_star_nonempty_of_witness`, `active_iff_pos_shadow_of_bounds`, `strong_duality_of_zero_gap`), and exhibited the inhabited instance `unitConfinementFrobeniusContext`.
- [x] Verified with Lean v4.24.0 (`lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`) and all 6 static vacuity audits (0 findings).
- [x] Verified with 80-dps `mpmath` probe (`computations/probes/round50_devacuify_6qbv_probe.py`) and 2-commit stamped witness (`computations/probes/round50-devacuify-6qbv.witness.json`, `scriptCommitSha: 357a63280dd6b77b067855dfd2ebaeb6340b2c28`, `scriptHash: 3ff73a87c2af`).
- [ ] Awaiting review and merge of PR https://github.com/litlfred/qou/pull/8189 (`status: in-progress` maintained per repo rule).
