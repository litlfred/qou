---
# 8ed2
title: 'OV brick-5: seminormalVector_data_exists de-abstraction (piece 3)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-03T00:33:16Z
updated_at: 2026-07-17T20:49:46Z
---

Young seminormal existence de-abstraction (JucysMurphy.lean). TRANCHE 1 (PR #3255, merged): all-T existence from 2 cores. TRANCHE 2 (PR #3843): syt_adjacentSwap_connected now sorry-free via proved adjacentSwapStep_symm + reflTransGen_adjacentSwap_symm; reduced to strictly-smaller one-directional core syt_all_connect_to_some (every SYT walks to one base tableau). REMAINING 2 cores: seminormalVector_base_exists (base seminormal vector) + syt_all_connect_to_some (exchange argument: construct row-superstandard base + inversion measure + admissible-swap-decreases-measure step + WF induction). Parent epic 08a2.
