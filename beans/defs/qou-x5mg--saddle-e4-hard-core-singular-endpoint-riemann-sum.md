---
# qou-x5mg
title: 'saddle E4 (hard core): singular-endpoint Riemann sum (π/N)Σⱼ≤ₖ log(2sin(πj/N)) → ∫₀^{πx}log(2sin) = −clausen(2πx)/2, uniform in k/N→x (split [0,δ]+[δ,πx]; monotone tail comparison at the log singularity)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - close-candidate
created_at: 2026-07-19T13:12:36Z
updated_at: 2026-10-04T15:13:54Z
parent: qou-n4nr
---

E4 singular-endpoint Riemann sum (π/N)Σⱼ≤ₖ log(2sin(πj/N)) → ∫₀^{πx}log(2sin) = −clausen(2πx)/2, uniform in k/N→x. DECOMPOSITION (2026-07-19, calibrated vs Mathlib — Analysis/SumIntegralComparisons.lean has the FULL toolbox incl. sum_mul_Ico_le_integral_of_monotone_antitone, the exact unimodal form): E4a change-of-var identity ∫₀^a log(2sin u)du = −clausen(2a)/2 (integral_comp_div, same machinery as clausen_pi); E4b unimodality of log(2sin) — MonotoneOn Ioc(0,π/2], AntitoneOn [π/2,π) (strictMonoOn_sin + log_le_log); E4c Riemann-vs-integral bounds per monotone piece (MonotoneOn.sum_le_integral / AntitoneOn.integral_le_sum — LIBRARY, was feared hand-rolled); E4d singular first cell ∫₀^{π/N}|log(2sin)| → 0 (continuity of the primitive = clausen continuity at 0); E4e uniform-in-k sandwich assembly. E4a+E4b this tranche.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-19 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
