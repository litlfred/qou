---
# qou-fbrp
title: 'Wire weak-isospin T3 into hypercharge Y=2(Q-I3) and the sin^2theta_W normalization. Consumes #4597 Milnor mu-bar_123=Y + #4561 writhe->I3. Closes the electroweak-mixing leg of the convergence.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-08-02T19:10:32Z
updated_at: 2026-10-10T18:10:00Z
parent: qou-20sx
---

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress Note (2026-11-16)
- Formalized weak-isospin `T_3` into hypercharge `Y = 2(Q - I_3)` across all 7 chiral SM multiplets `(u_L, d_L, u_R, d_R, nu_L, e_L, e_R)` and unrenormalized electroweak mixing ratio `Tr(I_3^2)/(Tr(I_3^2) + Tr((Y/2)^2)) = 2/(2 + 10/3) = 3/8` in `QOU/Eightfold/AtomicitySp2ElectroweakAndPartitionUnification.lean` (`weak_isospin_hypercharge_and_weinberg_3_8_certificate`) + 50-dps probe `atomicity_sp2_electroweak_and_partition_unification_probe.py` (PR `litlfred/qou#8172`, head `89a2a31a65a0d7dbf47567c813f9c48b755fae24`).
