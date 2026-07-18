---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-18T10:07:29Z
---

OV brick-5 syt_all_connect_to_some closure. MERGED: #3843 (base tableau, bridge, swapCellsSYT, swap-symm), #3893 (content_ne_of_succ d!=0 + entry-mono), #3904 (d^2!=1: sameRow/sameCol/sq_content_gap_ne_one + entryLtRow/Col). OPEN #3910: swapCellsSYT_entry_{mem,at_p,at_q,other} + swapSucc_self/succ helpers (sorry-free).
NEXT (fully-worked proof recorded in docs/coordination/yt-seminormal-infra.md):
1. Realization adjacentSwapStep_swapCells in JucysMurphy.lean (import SytAdjacentSwap+SytEntryMono): AdjacentSwapStep T (swapCellsSYT T (cell a)(cell b)). Refine <a,b,hab,...>; 3 cell-identities via cellLabel T' c = l (Fin.ext + swapCellsSYT_entry_* + entry_tableauCellEquiv, invert w/ tableauCellEquiv_cellLabel); gap conds from content_ne_of_succ + sq_content_gap_ne_one. Coercion caution: Prod.mk.eta for cell<->pair.
2. Measure inv(pi_T), pi_T=cellLabel(T0).tableauCellEquiv T (Equiv, =id at T0); step=right-mult by Equiv.swap a b; inv drops 1 on descent; every descent admissible (same-row/col=>ascent via T0 strictness). WF-recurse to T0=rowSuperstandardBraidKnot. Requires moving JucysMurphy private tableauCellEquiv lemmas L1120-1144 before L887. Parent epic 08a2.
