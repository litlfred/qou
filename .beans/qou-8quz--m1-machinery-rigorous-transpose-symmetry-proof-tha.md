---
# qou-8quz
title: 'M1 machinery: rigorous transpose-symmetry proof that c_{1/2}=0 (half-power vanishes)'
status: scrapped
type: task
priority: normal
created_at: 2026-08-29T01:34:20Z
updated_at: 2026-08-29T02:26:58Z
---

REFUTED as posed (2026-08-29, PR #5939). Transpose-symmetry does NOT prove c_{1/2}=0: reflection
k->-1-k sends g_A->-g_A, J^2->J^2, so V_A is AUTOMATICALLY invariant (a relabelling of the sum; does
not isolate the half-power). 'Even statistic => half-power cancels' is a distributional heuristic, not
a variance-expansion fact. Numerics also indeterminate (theta^{-1/2}/-2/3/-5/6/-1 all fit; best single
power ~0.94) => a theta^{-5/6} Airy-edge term cannot be excluded. Question folds into qou-tvok.
