---
# qou-xajh
title: 'C: 1/g vs 5g v-level passage — operationalize (q−q⁻¹)=(v−v⁻¹)·[2]_v; test Lean-proven 1/g=5g(1+x/5) as resummed form (likely different gap than −9%)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T17:54:14Z
updated_at: 2026-10-04T15:16:50Z
parent: qou-10v9
---

### Progress Update (2026-11-16, PR #8179)
- Formalized the $v$-level passage (`q = v^2`) and criticality resummation identities in `QOU/BraidKnot/MagicShellCouplingKappa.lean`: `q_sub_qinv_eq_v_level` ($v^2 - v^{-2} = (v - v^{-1})(v + v^{-1})$), `q_sub_qinv_sq_eq_x_mul_four_plus_x`, `inv_g_eq_five_g_mul_one_plus_x_div_five` ($g^{-1} = (5g)(1 + x/5)$ for $g^2(5 + x) = 1$), and `inv_g_sub_five_g_eq_g_mul_x` (`0` `sorry`).
- Evaluated at 80 dps at $v_0 = \sqrt{q_0}$ in `computations/probes/tail_d6_lp_dual_altchar_vlevel_probe.py`.
- Opened PR `litlfred/qou#8179` (`bf3902040cf206123f8aa0b5dc2b79c176dd9ce1`). Keeping status `in-progress` pending owner review.
