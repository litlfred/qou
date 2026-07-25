---
# qou-4wl1
title: 'A3 (leg 2): bound remainder |R|<|g''(0)| via mixed-cumulant (Sniady genus) scaling'
status: in-progress
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T03:45:42Z
parent: qou-v8t7
---

## A3 — leg 2: remainder |R|<|g'(0)| — REFINED to complete monotonicity (2026-07-25)
BREAKTHROUGH FRAMING. The Taylor coeffs a_m=g^{(m)}(0)/m! of g(θ)=E_{2+θ}[ω₃] follow sign(a_m)=(−1)^m
EXACTLY for n=8..17 (verified to order 10, 60dps) ⇒ the COMPLETE-MONOTONICITY signature of −g'(θ).
Plus Σ_{m≥2}|a_m|<|a_1| all n (absolute domination).

UNIFIED TARGET (subsumes A2). Prove −g'(θ)=−d/dβ E_β[ω₃] is COMPLETELY MONOTONE on [2,∞) for n≥n₀.
Bernstein ⇒ −g'(θ)=∫e^{−θs}dμ(s), μ≥0 ⇒ g'≤0 ∀θ≥0 ⇒ g(1)=∫_0^1 g'≤0 (KERNEL) AND E_β[ω₃]≤0 ∀β≥2
(whole family), in one stroke. A2 (Cov(ln f,ω₃)≤0) is the θ=0 endpoint of this.

PROOF ROUTE. Exhibit the positive Bernstein measure μ, OR derive alternating θ-derivatives from an
MLR/association property of the tilted family Q_θ∝e^{θ ln f}·P applied to ω₃. Read Ivanov-Olshanski
(0304010) for the covariance structure; the mixed cumulants κ_{m+1}(ln f;…;ω₃) are the −g' moments.

CAVEAT. Verified via SIGNS to order 10, n=8..17 — not an all-orders proof; property is asymptotic in n
(n≤7 deviate at high order, covered by exact k≤40). Audit: 2026-07-25-covariance-kernel-complete-monotonicity-target.md. Probe: wlambda_covariance_epic_phase8_complete_monotonicity.py.
