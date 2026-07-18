---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-18T09:05:48Z
---

OV brick-5, JucysMurphy.lean. #3255 (merged): all-T existence from 2 cores. #3843 (open) progress:
(a) syt_adjacentSwap_connected sorry-free via swap-symmetry -> one-directional syt_all_connect_to_some.
(b) SytRowSuperstandard.lean base-tableau brick COMPLETE sorry-free (rowSuperstandardStd + Nonempty, Mathlib.SYT type).
(c) SytMathlibBridge.lean COMPLETE sorry-free: Mathlib.SYT -> BraidKnot.SYT (entry-1); rowSuperstandardBraidKnot + Nonempty(BraidKnot.SYT) = T_0 in the type syt_all_connect_to_some consumes.
(d) SytAdjacentSwap.lean COMPLETE sorry-free: swapCellsSYT (consecutive-label cell-swap constructor) via swapSucc involution; the admissible edge object.
REMAINING for syt_all_connect_to_some (all in JucysMurphy.lean, which would import SytAdjacentSwap; needs private cellLabel/tableauCellEquiv lemmas):
1. Realization AdjacentSwapStep T (swapCellsSYT T (cell a)(cell b)); incl. proving consecutive labels |gap|>=2 <=> diff row&col.
2. Measure inv(pi_T), pi_T = cellLabel(T_0) . tableauCellEquiv T; step = right-mult by (a,a+1), inv +-1.
3. Exchange lemma (CRUX): T != T_0 => some adjacent descent is a valid (diff row/col) swap decreasing inv; rule out row/col-adjacent descent via Yamanouchi order.
4. WF induction on inv closes it with T_0 := rowSuperstandardBraidKnot.
Decomposition recorded in docs/coordination/yt-seminormal-infra.md. Parent epic 08a2.
