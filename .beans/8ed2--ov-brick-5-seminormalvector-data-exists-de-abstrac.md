---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-18T10:21:30Z
---

OV brick-5 syt_all_connect_to_some closure. MERGED: #3843 (base tableau, bridge, swapCellsSYT, swap-symm), #3893 (content_ne_of_succ d!=0 + entry-mono), #3904 (d^2!=1 admissibility). OPEN #3910: swapCellsSYT_entry helpers + REALIZATION adjacentSwapStep_swapCells (SORRY-FREE, JucysMurphy.lean imports SytAdjacentSwap+SytEntryMono; computes tableauCellEquiv of swapped tableau via cellLabel; gap conds from content_ne_of_succ + sq_content_gap_ne_one). Only 2 pre-existing cited sorries remain (seminormalVector_base_exists L838, syt_all_connect_to_some L889).
FINAL piece: measure inv(pi_T), pi_T=cellLabel(rowSuperstandardBraidKnot).tableauCellEquiv T (Equiv, =id at T0); step=right-mult by Equiv.swap a b => inv drops 1 on descent; every descent admissible (same-row/col=>ascent via T0 strictness, realization supplies the edge). WF-recurse to T0. REQUIRES reorg: move JucysMurphy private tableauCellEquiv lemmas L1120-1144 + the realization before syt_all_connect_to_some L889 so the sorry can be closed in place. Parent epic 08a2.
