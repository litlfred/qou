---
# qou-pzwk
title: confinement frobenius reciprocity missing hypotheses
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
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

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.

`QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean:72` is derived sorry-free; the active-set nonemptiness is proved, conditional on the stationarity hypothesis stated in the signature (docstring lines 27, 69). PR #8189 is superseded.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE (evidence in the closing note above). Premises checked: the bean and the fixed Lean name no retired object (no σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photon or SM-adopted quark charge). The fix is structural Lean hygiene, so it is independent of the physics rulings.

## 2026-11-22 — id renamed `confinement_frobenius_reciprocity` → `qou-pzwk` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
