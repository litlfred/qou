---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-18T01:43:55Z
---

OV brick-5, JucysMurphy.lean. #3255 (merged): all-T existence from 2 cores. #3843 (open): (a) syt_adjacentSwap_connected sorry-free via swap-symmetry -> one-directional syt_all_connect_to_some; (b) SytRowSuperstandard.lean base-tableau brick NOW COMPLETE sorry-free: rowPrefix + rowSuperstandardSsyt + card_eq_sum_rowLen + BijOn(MapsTo/InjOn/SurjOn) + rowSuperstandardStd + instNonemptyStandardYoungTableau (explicit T_0 witness; axioms [propext,Classical.choice,Quot.sound]). REMAINING for syt_all_connect_to_some: inversion measure m:SYT->N (on reading word / content) + exchange step (T != rowSuperstandard => exists admissible adjacent swap decreasing m; discharge |d|>=2 gap from standardness) + WF induction walking any SYT to the base. Then wire T_0:=rowSuperstandardStd into syt_all_connect_to_some. Parent epic 08a2.
