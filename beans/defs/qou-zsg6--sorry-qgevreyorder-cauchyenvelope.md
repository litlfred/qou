---
# qou-zsg6
title: 'Sorry: QGevreyOrder cauchyEnvelope'
status: completed
type: task
priority: normal
created_at: 2026-08-04T01:39:44Z
updated_at: 2026-08-22T16:14:31Z
---

QGevreyOrder.lean: 1 sorry in q-Gevrey order of Cauchy envelope of Cauchy product. Needs analytic continuation / q-Borel summation infrastructure.

── Partial progress 2026-08-19 (session qou-a6rd, PR #5348, branch n24484) ──
The ENDPOINT half is now discharged sorry-free: cauchyMul_leadingCoeff_ge_endpoint (QGevreyOrder.lean, lean-direct EXIT=0). It closes the θ*=1 pick the cauchyMul_order sorry cites — the ≥ (lower) direction when a dominates (t ≤ s, envelope = max s t = s), given NoCancellation + b 0 ≠ 0 + a eventually nonzero. Uses hnc at k=n to transfer the a_n·b_0 summand's q^{s n²/2} growth to the whole convolution.
RESIDUAL cauchyMul_order sorry (line 463) is now specifically the INTERIOR-OPTIMUM case: both orders ≤ 0, envelope = s·t/(s+t), needing a near-optimal k ≈ θ*·n (θ* = t/(s+t)) attainment argument + zero-coefficient handling. Not the endpoint. This is genuinely harder (RSZ slope=order machinery).

── CLOSED 2026-08-22 (branch n24484, commit f7338802ee) ──
The residual cauchyMul_order sorry was proof-no-false-cited-sorry, NOT the
interior-saddle gap the old note described (that was already proved sorry-free
for positive coeffs in cauchyMul_order_of_pos). The general normed-field
statement is FALSE as written: the hnc:NoCancellation hypothesis (added
2026-08-08) is insufficient — b≡0 satisfies it vacuously (a⋆b=0) yet breaks the
conclusion (order 0 ≠ max s 0). Fix per lean-proof-vacuity-audit §9 recipe 5:
(a) cauchyMul_order_noCancellation_insufficient — machine-proved ¬∀ with hnc
    satisfied (b≡0, a=2^{n²} order 2, E=max 2 0=2 vs product order 0);
(b) restated cauchyMul_order with ∀n,a n≠0 / ∀n,b n≠0;
(e) PROVED sorry-free by reducing to cauchyMul_order_of_pos on ‖a‖,‖b‖ via a
    factor-(n+1) squeeze. lean-direct EXIT=0; axioms [propext,Classical.choice,
    Quot.sound], no sorryAx. Last sorry in QGevreyOrder.lean is gone.
