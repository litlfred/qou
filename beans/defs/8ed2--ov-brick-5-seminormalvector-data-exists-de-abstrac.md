---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-10-04T15:13:26Z
parent: qou-1oif
---

OV brick-5 syt_all_connect_to_some — CLOSED sorry-free (PR #3935).
FULL CHAIN MERGED: #3843 base tableau+bridge+swapCellsSYT+swap-symm; #3893 content_ne_of_succ (d!=0); #3904 d^2!=1 admissibility; #3910 REALIZATION adjacentSwapStep_swapCells; #3922 PermInversion measure kernel (invCount_mul_swap_lt + WF helpers).
CLOSURE #3935 (open): JucysMurphy.lean permOf + permOf_swapCells + descent_ne_row/col + WF induction on invCount(permOf T) => syt_all_connect_to_some sorry-free. Reorg moved private tableauCellEquiv lemmas + realization above L889. lean-direct EXIT 0.
Only remaining sorry in JucysMurphy: seminormalVector_base_exists (ceded to g_rho/chi_lambda thread, separate). Parent epic 08a2.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-18 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
