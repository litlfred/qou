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
updated_at: 2026-11-23T21:39:57Z
parent: qou-20sx
---

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress Note (2026-11-16)
- Formalized weak-isospin `T_3` into hypercharge `Y = 2(Q - I_3)` across all 7 chiral SM multiplets `(u_L, d_L, u_R, d_R, nu_L, e_L, e_R)` and unrenormalized electroweak mixing ratio `Tr(I_3^2)/(Tr(I_3^2) + Tr((Y/2)^2)) = 2/(2 + 10/3) = 3/8` in `QOU/Eightfold/AtomicitySp2ElectroweakAndPartitionUnification.lean` (`weak_isospin_hypercharge_and_weinberg_3_8_certificate`) + 50-dps probe `atomicity_sp2_electroweak_and_partition_unification_probe.py` (PR `litlfred/qou#8172`, head `89a2a31a65a0d7dbf47567c813f9c48b755fae24`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8172, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.



## Session Intent (2026-11-23)
Claimed by `claude/w2-h7-h8-hypercharge-zremoval-20261123` (W2: H7/H8 two-row Wedderburn pair identities, coideal Killing-norm hypercharge slope 1/2, and Z-channel Yukawa removal).


Claimed by claude/w2-h7-h8-hypercharge-zremoval-20261123 (Worker 15)



## Session Results (2026-11-23 — PR litlfred/qou#9216, Issue #9215)
- **Branch:** `claude/w2-h7-h8-hypercharge-zremoval-20261123` (`b4948fad7d2` pre-registration -> `a9bdf696a8d` Lean + probe -> `e857686ddb1` witness).
- **Lean (`QOU/QBeta/CrossNucleonPairWedderburnZRemoval.lean`):** 35 theorems, `0 sorry`, `0` custom axioms (`[propext, Classical.choice, Quot.sound]` only, `§7c` generic, zero empirical constants in `.lean`). Proves Convention-D two-row Wedderburn collapse on `H_7(q)` (`C_7 = 429`, corank `4,611`) and `H_8(q)` (`C_8 = 1,430`, corank `38,890`), quantum Schur–Weyl character decompositions, right-spectator `z_D`/`z_D_bar` factorization (`L7e`, `L8e`), inductive left-spectator weight-counting operator `L_{m+1}(q)` with `L_2(q) = (q^2+1) L_1(q) - q^2 I_2` (`L8s` vs `L7s`), all-`q` pinned pair identity `alpha_6(q) + beta_6(q) = 1` excluding pure Coulomb on Hecke insertions, split-bundle `F = V_2 (+) W_3^*` Killing norms (`Tr_F((2 T_3)^2) = 2`, `Tr_F((Y/2)^2) = 5/6`, `Tr_G(T_3^2) = 2`, `Tr_G((Y/2)^2) = 10/3`, `sin^2 theta_W^0 = 3/8`) fixing GMN slope `1/2` (`(q_u, q_d) = (2/3, -1/3)`, chiral anomaly cancellation), and separated-hadron `Z`-channel Yukawa suppression `< 10^-280` for `x >= 653`.
- **80-dps Probe & Witness (`computations/probes/w2_h7_h8_wedderburn_zremoval/w2-h7-h8-wedderburn-zremoval.witness.json`):** `19/19` assertions passed (`< 10^-78` agreement on `H_7(q_0)` and `H_8(q_0)` Hoefsmit character traces across `pp`, `pn`, `nn` dressings; `x(r_{pi+-}) = 653.34488... => lambda(r_{pi+-}) = 1.8027e-284 < 10^-280`).
- **Status:** Kept `in-progress` per Rule 13a / reviewer-separated closure discipline.
