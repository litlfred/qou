---
# qou-ahss
title: 'RETAINED: eigenvalue_norm_sq_axiom — needs complex analysis plumbing (Complex.abs_div etc)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-03T19:25:39Z
updated_at: 2026-11-22T21:31:33Z
parent: qou-6qbv
---


## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.
Done on main: there is no `eigenvalue_norm_sq_axiom` declaration any more. `lean/QOU/AlgebraicSubstrate/WeilZeta.lean:107` proves `theorem eigenvalue_norm_sq`, and `eigenvalue_norm_sq_of_isWeilZeta` (line 126) consumes it. Nothing left to do.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE (evidence in the closing note above). Premises checked: the bean and the fixed Lean name no retired object (no σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photon or SM-adopted quark charge). The fix is structural Lean hygiene, so it is independent of the physics rulings.
