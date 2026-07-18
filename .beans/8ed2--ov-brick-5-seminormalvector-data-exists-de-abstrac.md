---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-18T09:27:25Z
---

OV brick-5, JucysMurphy.lean. syt_all_connect_to_some closure.
MERGED (#3843): base tableau (rowSuperstandardStd/Nonempty), Mathlib.SYT->BraidKnot.SYT bridge (rowSuperstandardBraidKnot = T_0 in right type), swapCellsSYT (consecutive-label cell-swap constructor), swap-symmetry.
OPEN (#3893): SytEntryMono.lean sorry-free -- content_ne_of_succ (consecutive labels never share a diagonal, d!=0) + public entryLtDiagSucc/entryLtOfDiagRowLt.
KEY INSIGHT: every descent of inv(pi_T) [pi_T = cellLabel(T_0) . tableauCellEquiv T] is admissible for ANY T_0 (same-row/col pairs map to ascents via T_0 strictness); dissolves the Yamanouchi complication.
REMAINING on #3893: (2) d^2!=1 (same-row<=>gap+1 / same-col<=>gap-1); (3) realization AdjacentSwapStep T (swapCellsSYT ...); (4) inv measure + step=right-mult by (a,a+1); (5) descent=>admissible exchange lemma + WF induction -> close sorry with T_0:=rowSuperstandardBraidKnot. Best done in JucysMurphy.lean (private cellLabel/tableauCellEquiv lemmas); import SytAdjacentSwap+SytEntryMono. Decomposition in docs/coordination/yt-seminormal-infra.md. Parent epic 08a2.
