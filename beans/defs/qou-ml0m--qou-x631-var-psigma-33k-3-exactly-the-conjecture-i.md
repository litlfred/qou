---
# qou-ml0m
title: 'qou-x631: Var_P(Sigma_3)=3(k)_3 exactly; the conjecture is a correlation coefficient near -0.164'
status: completed
type: task
priority: normal
created_at: 2026-09-07T06:16:44Z
updated_at: 2026-09-26T11:03:20Z
---


Follows `qou-rh0m` (the quadratic twist) and `qou-ujil` (the CLT scale). Sharpens
both, and corrects one of my own attributions.

## `Var_P(Σ₃) = 3k(k−1)(k−2)`, exactly — not just asymptotically

`qou-ujil` cited Kerov's CLT for `sd_P(Σ₃) ≈ √3·k^{3/2}`. That constant is exact
at every k, and elementary. Since `Σ_p(λ) = (k)_p χ^λ(p)/f^λ`,

    (f^λ)² Σ_p Σ_q  =  (k)_p (k)_q χ^λ(p) χ^λ(q)

— **the `f^λ` cancel completely** — and summing over λ is character **column
orthogonality**. Hence `Var_P(Σ_p) = (k)_p²/|C_p|`, so

    Var_P(Σ₃) = (k)₃² / |C₃| = 3·k(k−1)(k−2).

Verified against direct computation, 4 ≤ k ≤ 12.

## The Σ_p are *exactly* uncorrelated under Plancherel

`E_P[Σ_p Σ_q] = 0` for every `p ≠ q` and every k, by the same orthogonality —
stronger than the CLT's asymptotic independence.

## Self-correction: this is orthogonality, not the twist

I first attributed that vanishing to the quadratic twist —
`Σ_p(λ') = (−1)^{p−1}Σ_p(λ)`, so the product is ω-odd when exactly one of p, q is
even. The reasoning is correct but **subsumed**: orthogonality kills the mixed
moment for *all* p ≠ q, including the pairs parity leaves free. Measured, `(3,5)`
and `(2,4)` also vanish, and the parity argument predicts nothing about them.

The twist is genuinely needed only for `S_μ = 0` on odd classes — a **triple**
product `Σ_λ χ(e)χ(e)χ(μ)`, which is not an orthogonality relation. Worth keeping
straight: `qou-rh0m` claimed the twist as the explanation for a family of
vanishings, and for the mixed moments that credit belongs elsewhere.

## The conjecture is a correlation coefficient near −0.164

With an exact denominator,

    ρ(k) := E_Q[Σ₃] / sd_P(Σ₃)  =  −0.164 ± 0.015,   10 ≤ k ≤ 42

and the conjecture is exactly `ρ(k) ≤ 0`. So route `qou-t5m1` now has a **single
dimensionless number** to hit — a derivation can be checked against −0.164 rather
than merely against a sign. Both the numerator's scale (`k^{3/2}`, `qou-ujil`) and
the denominator (`√(3(k)₃)`, here) are now pinned.

## And one simplification that does not work

`Q ∝ (f^λ)³` is `P` tilted by `f^λ = exp(log f^λ)`, so one hopes
`E_Q[Σ₃] ≈ Cov_P(log f^λ, Σ₃)`. Measured, the ratio is **1.44 ± 0.19** over
6 ≤ k ≤ 30 with no trend: the linearisation gets the **sign and the scale right
and the constant wrong**, so it cannot transfer the inequality. The exact
statement remains `E_Q[Σ₃] = Cov_P(f^λ, Σ₃)/E_P[f^λ]`. Recorded so the
linearisation is not assumed asymptotically exact by the next attempt.
