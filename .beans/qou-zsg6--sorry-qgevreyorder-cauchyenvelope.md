---
# qou-zsg6
title: 'Sorry: QGevreyOrder cauchyEnvelope'
status: todo
type: task
priority: normal
created_at: 2026-08-04T01:39:44Z
updated_at: 2026-08-19T21:36:16Z
---

QGevreyOrder.lean: 1 sorry in q-Gevrey order of Cauchy envelope of Cauchy product. Needs analytic continuation / q-Borel summation infrastructure.

── Partial progress 2026-08-19 (session qou-a6rd, PR #5348, branch n24484) ──
The ENDPOINT half is now discharged sorry-free: cauchyMul_leadingCoeff_ge_endpoint (QGevreyOrder.lean, lean-direct EXIT=0). It closes the θ*=1 pick the cauchyMul_order sorry cites — the ≥ (lower) direction when a dominates (t ≤ s, envelope = max s t = s), given NoCancellation + b 0 ≠ 0 + a eventually nonzero. Uses hnc at k=n to transfer the a_n·b_0 summand's q^{s n²/2} growth to the whole convolution.
RESIDUAL cauchyMul_order sorry (line 463) is now specifically the INTERIOR-OPTIMUM case: both orders ≤ 0, envelope = s·t/(s+t), needing a near-optimal k ≈ θ*·n (θ* = t/(s+t)) attainment argument + zero-coefficient handling. Not the endpoint. This is genuinely harder (RSZ slope=order machinery).
