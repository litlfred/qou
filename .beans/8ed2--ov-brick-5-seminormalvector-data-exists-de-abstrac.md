---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-17T23:17:11Z
---

OV brick-5 seminormal existence, JucysMurphy.lean. DELIVERED tranche 1 (#3255, merged): all-T existence assembled from 2 cores. DELIVERED tranche 2 (#3843): (a) syt_adjacentSwap_connected proved sorry-free via AdjacentSwapStep symmetry (adjacentSwapStep_symm + reflTransGen_adjacentSwap_symm) -> reduced to one-directional syt_all_connect_to_some; (b) SytRowSuperstandard.lean: row-superstandard SSYT sorry-free (rowPrefix + rowSuperstandardSsyt). REMAINING for syt_all_connect_to_some: (i) card=Sum rowLen via cells=disjoint-union-of-rows (biUnion + card_biUnion) ~40-60 lines; (ii) BijOn wrap -> Nonempty(StandardYoungTableau) [MapsTo/InjOn easy from rowPrefix_mono; SurjOn via Finset.surjOn_of_injOn_of_card_le] ~60-80 lines; (iii) inversion measure + exchange step -> the walk to base. Parent epic 08a2.
