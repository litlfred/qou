---
# qou-tcl2
title: 'G2: block-dependent braid coefficient at level 3A (T(T+1) term)'
status: todo
type: task
priority: high
tags:
    - compute-accuracy
    - term-completeness
created_at: 2026-11-27T20:25:00Z
updated_at: 2026-11-28T11:36:00Z
parent: qou-tcl0
---

Closed form tr_M = τ_p^Z τ_n^N ∏ f_i and the Q-CLT proxy are log-linear in Z, N, interface counts: no dependence on the level-3A isospin block, so no T(T+1) term, no isobaric parabola (Q_β 0/1009 exothermic). Under convention D level 3A has 3A/2+1 nonzero blocks (19 at A=12), correcting the p(36) caveat in mass_table_comprehensive.py; evaluate block by block (character dims are ballot numbers).

2026-11-27: A-scaling follow-up in qou-o8lo / PR #9747 (T(T+1) coefficient = writhe/(N(N-1))).

2026-11-28 (merge-steward): Division-free `IsobaricBetaWritheCoulombStep.lean` + 80-dps composite beta^- benchmark probe landed on `origin/main` in PR #10000; open symmetry-energy scale items remain.
