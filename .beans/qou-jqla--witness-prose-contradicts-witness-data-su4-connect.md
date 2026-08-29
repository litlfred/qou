---
# qou-jqla
title: 'Witness prose contradicts witness data: su4-connected-1111-magnitude and b4-framework-connected-cumulant-deficit carry hardcoded convention-C-era verdict strings'
status: todo
type: task
priority: normal
created_at: 2026-08-29T07:05:04Z
updated_at: 2026-08-29T07:05:40Z
---

Measured 2026-08-29 on branch claude/he4-magnitude-fork-2026-08-29 (PR #5966).

Two committed witnesses on main carry hardcoded verdict prose from the
convention-C era while their data blocks hold current convention-D values:

1. computations/probes/su4-connected-1111-magnitude.witness.json
   data: delivered x1.398, |b4c|=1.17395, ungated A=6 cluster 10.17
   verdict_note: 'x1.54 delivered vs x2.09 needed, 74%' and 'overshoots to 22.2'
   The producer also PRINTS a stale caveat line: 'the direct |b4c|=1.96 vs
   2.093 (6%)' — the live D-frame figure is 1.174 vs 2.097, i.e. 44% off,
   not 6%. That printed 6% is the near-match trap the same line warns about.

2. computations/probes/b4-framework-connected-cumulant-deficit.witness.json
   data: b4 = -0.3035 MeV = -3.28% of the 9.243 target; b3 = -1.3878
   verdict: 'b4 = 0.583 MeV = 6.3% of the 9.243 target ... -2.52 vs +1.43 ...
   must supply ~94% of the 4-body'
   Its assertion framework_b4_far_below_target (expected 0.063 +/- 0.02,
   computed -0.03284) is LIVE FAILING on main, and allPassed is false.

Both verdict strings are hardcoded in the producer, so re-running regenerates
the numbers and preserves the stale prose. Fix at the producer: derive the
verdict text from the computed values.

Not fixed on PR #5966 to avoid touching producers a sibling may hold.
