---
# qou-qlou
title: operator selection lp missing hypotheses
status: completed
pr: 8243
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean`
The `operator_selection_lp` theorem is unprovable. `OperatorSelectionLpContext` provides `x_star` and `y_0_star` as unconstrained data fields, meaning it does not assume they actually satisfy the optimality conditions or strong duality, making the theorem refutable.



Also known as `opsl` (its former front-matter header id; the beans CLI uses the filename id `operator_selection_lp`). Recorded 2026-10-04.

- **Round 54 update (in-progress):** De-vacuified in PR `litlfred/qou#8243` (HEAD `1495a97d0656036c5fc7c664284a44d77939041e`), verified with Lean 4.24.0 (`0` `sorry`, `0` vacuity hits) and 80-dps `mpmath` witness.

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.

`QOU/ParticleInteractions/operator_selection_lp.lean` proves strong duality sorry-free (Disposition, lines 26-41); complementary slackness is derived from `zero_gap` via `zero_gap_iff_complementary_slackness` (line 723), which is a derivation from a stated hypothesis, not a projection of the conclusion.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE (evidence in the closing note above). Premises checked: the bean and the fixed Lean name no retired object (no σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photon or SM-adopted quark charge). The fix is structural Lean hygiene, so it is independent of the physics rulings.

## 2026-11-22 — id renamed `operator_selection_lp` → `qou-qlou` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
