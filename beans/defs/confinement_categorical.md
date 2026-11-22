---
# confinement_categorical
title: confinement categorical missing hypotheses
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:31:33Z
parent: qou-uot9
pr: 8189
---

File: `folio/quantum-observable-universe/lean/QOU/WedderburnMass/confinement_categorical.lean`
The `confinement_categorical` theorem is unprovable. The `ConfinementCategoricalContext` carries only the structural data (algebra, projectors) but lacks the Hochschild vanishing and Whitehead lemma inputs needed to prove the three categorical confinement properties.



Also known as `cnca` (its former front-matter header id; the beans CLI uses the filename id `confinement_categorical`). Recorded 2026-10-04.

## Progress (PR #8189, 2026-11-16T20:28:25Z)

- [x] Replaced the conjunctive self-assuming field `confinement_ident` in `folio/quantum-observable-universe/lean/QOU/WedderburnMass/confinement_categorical.lean` with upstream Hochschild collapse (`hh_collapse_to_centre`), Wedderburn block sum (`wedderburn_centre_sum`), `Z(A) ⊕ [A, A]` splitting (`centre_commutator_decomp`), and commutator vanishing hypotheses, deriving all 3 clauses of `confinement_categorical` (`survival_e_infinity_eq_wedderburn_sum`, `integral_factors_through_centre`, `observable_fixed_by_centre`).
- [x] Verified with Lean v4.24.0 (`lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`) and all 6 static vacuity audits (0 findings).
- [x] Verified with 80-dps `mpmath` probe (`computations/probes/round50_devacuify_6qbv_probe.py`) and 2-commit stamped witness (`computations/probes/round50-devacuify-6qbv.witness.json`, `scriptCommitSha: 357a63280dd6b77b067855dfd2ebaeb6340b2c28`, `scriptHash: 3ff73a87c2af`).
- [ ] Awaiting review and merge of PR https://github.com/litlfred/qou/pull/8189 (`status: in-progress` maintained per repo rule).

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.

`QOU/WedderburnMass/confinement_categorical.lean:177` `theorem confinement_categorical` is proved sorry-free from the Wedderburn isomorphism (docstring line 21); the old self-assuming class with unconstrained data and a `sorry` is deleted (line 33, bean qou-mtc9). The unmerged batch PR #8189 is superseded by this.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE (evidence in the closing note above). Premises checked: the bean and the fixed Lean name no retired object (no σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photon or SM-adopted quark charge). The fix is structural Lean hygiene, so it is independent of the physics rulings.
