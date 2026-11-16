---
# qou-atsd-t2
title: 'T2: reduction skeleton — compose [G<=Sp(V)]+[rank Sp(2m)=m]+[dim V=2] => Subsingleton S; wire to rankOne_of_chain_of_bridge; rank-Sp = single named residual (no instance)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-atomicity
created_at: 2026-07-25T20:32:48Z
updated_at: 2026-10-10T07:16:13Z
parent: qou-8lxd
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Note (2026-11-16)
- Formalized T2 atomicity reduction skeleton (`dimV = 2*m`, `chooseTwo dimV = 1`, `rankG <= m`, `cardS <= rankG` => `dimV = 2, m = 1, rankG <= 1, cardS <= 1`) in `QOU/Eightfold/AtomicitySp2ElectroweakAndPartitionUnification.lean` (`atomicity_reduction_skeleton_certificate`) + 50-dps probe `atomicity_sp2_electroweak_and_partition_unification_probe.py` (PR `litlfred/qou#8172`, head `89a2a31a65a0d7dbf47567c813f9c48b755fae24`).
