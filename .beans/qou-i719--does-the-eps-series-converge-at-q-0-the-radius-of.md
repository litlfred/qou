---
# qou-i719
title: Does the eps-series converge at q_0? The radius of convergence of the insertion expansion
status: completed
type: task
priority: high
created_at: 2026-09-03T20:35:02Z
updated_at: 2026-09-03T21:01:41Z
---

Successor to qou-qqm4. The diagonal-insertion expansion gives every eps-order of tr_M as a fixed-point count costing 2^n C(L,<=k) -- vastly cheaper than the direct trace (15! at A=5). But an order-k truncation is only useful at q_0 = 1.1099785828 (eps = 0.10997858) if the series CONVERGES there. Measured coefficients of Dtr for the deuteron: 1/8, 19/8, 357/32 -- ratios 19 then 4.70. If the ratio settles below 1/eps = 9.09 the series converges at q_0 and the expansion is a COMPUTE ROUTE to A=5,6 that no current method reaches; if it settles above, the expansion is a structural tool only and that must be said plainly. Decisive, cheap at n=6 (high-order exact series), and it also bounds the truncation error of any c_k-based claim.



ANSWERED 2026-09-03, PR #6541. Radius is EXACTLY 1 (Dtr is rational; poles only q=0 order 23 and q=+-i order 6; Laurent numerator degrees -23..33, interpolated and validated on held-out points). Converges at eps_0: 1 ppb by order 16-18, 1 ppQ by order 26.

BUT the compute route is CLOSED: 2^n C(L,<=k) at A=5 (n=15, L=59) is 4.1e21 subset-state pairs at order 26 vs 15! = 1.3e12 for the direct trace. Convergence necessary, not sufficient. The insertion expansion is a STRUCTURAL tool (it derived c0, c1, c2) and does not lift the A>=5 barrier. Scope (a).

TRAP recorded (probe assertion + compute-precision-auditor memory): the ratio and root tests give 0.40-0.60 at order 26 and are wrong by 2.5x; reading the first three coefficients suggests divergence at eps_0. The order-23 pole makes C(k+22,22) growth look exponential. I drew both wrong conclusions before computing the exact rational function.
