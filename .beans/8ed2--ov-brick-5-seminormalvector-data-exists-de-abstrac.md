---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-18T13:47:51Z
---

OV brick-5 syt_all_connect_to_some. ALL HARD LEMMAS PROVEN.
MERGED: #3843 base+bridge+swapCellsSYT+swap-symm; #3893 content_ne_of_succ (d!=0); #3904 d^2!=1 admissibility; #3910 swap-entry helpers + REALIZATION adjacentSwapStep_swapCells (sorry-free).
OPEN #3922: PermInversion.lean measure KERNEL sorry-free (invCount, invCount_mul_swap_lt [adjacent descent swap lowers inv], eq_one_of_invCount_eq_zero, exists_adjacent_descent_of_ne_one, eq_one_of_strictMono, strictMono_of_adjacent).
FINAL ASSEMBLY (only step left, all inputs proven; in JucysMurphy.lean importing PermInversion+SytMathlibBridge; needs reorg moving private tableauCellEquiv lemmas L1120-1144 before L887):
1. permOf T = tableauCellEquiv T . cellLabel T0 (T0=rowSuperstandardBraidKnot); permOf T0 = 1.
2. export tableauCellEquiv-of-swapCells identities => permOf(T')=permOf T * swap a b.
3. descent => diff row/col (same-row/col => ascent via T0 strictness) => realization edge; invCount_mul_swap_lt => measure drops.
4. WF Nat.strong_induction on invCount(permOf T): =0 => permOf=1 => T=T0 => refl; else descent+step+recurse. Closes L887 sorry. Parent 08a2.
