---
# qou-h4fe
title: 'qou-x631: g(t) is sublinear -- first-order genus expansion cannot give -0.164; use the integrated covariance'
status: completed
type: task
priority: normal
created_at: 2026-09-07T07:03:02Z
updated_at: 2026-09-26T11:03:19Z
---


Follows `qou-ml0m`, which reduced the conjecture to `ρ(k) = E_Q[Σ₃]/sd_P(Σ₃) ≤ 0`
with ρ ≈ −0.164. This asks what route `qou-t5m1` actually has to compute, and the
answer changes the shape of the work.

Embed `P ∝ (f^λ)²` and `Q ∝ (f^λ)³` in one family, `Q_t ∝ (f^λ)^{2+t}`, and set
`g(t) = E_{Q_t}[Σ₃]/sd_P(Σ₃)`. Then `g(0) = 0` **exactly** (`qou-cze8`) and `g(1)`
is the conjecture's quantity.

## g is monotone decreasing and markedly sublinear

Measured 16 ≤ k ≤ 40:

| | |
|---|---|
| `g'(0)` — linear response | **−0.245 ± 0.008** |
| `g(1)` — the conjecture | **−0.164 ± 0.015** |

A first-order expansion in the tilt predicts `g(1) = g'(0) = −0.245`; the truth is
−0.164. **Linear response overshoots by ~50 %, and about a third of the answer is
nonlinear.** It degrades further out — at k = 40, linear predicts `g(3) = −0.74`
against an actual −0.374.

So: **a first-order Śniady genus expansion in the tilt cannot produce −0.164.** It
would produce roughly −0.245. That is worth knowing before starting rather than
after.

## The reformulation that restores first order

Since `d/dt E_{Q_t}[X] = Cov_{Q_t}(log f^λ, X)`,

    E_Q[Σ₃]  =  ∫₀¹ Cov_{Q_t}(log f^λ, Σ₃) dt

so the conjecture **follows from** the pointwise condition

    Cov_{Q_t}(log f^λ, Σ₃) ≤ 0   for all t ∈ [0,1]

verified here for every k and t tested (−0.245 at t = 0 rising to about −0.12 at
t = 1, monotone in magnitude — which is exactly what makes g sublinear).

This is the useful shape. Each instance is a **covariance** — first order — so a
genus expansion applies at each t, and the nonlinearity that defeats the direct
expansion is absorbed into the t-integration instead of having to be expanded.

**Sufficient, not equivalent.** An integral can be negative without its integrand
being so, and the pointwise claim is checked numerically only.

## Consistency with the earlier discrepancy

`qou-ml0m` measured `Cov_P(log f, Σ₃)/E_Q[Σ₃] = 1.44 ± 0.19` and recorded the
linearisation as "quantitatively wrong" without explaining why. That ratio is
exactly `g'(0)/g(1)`, and 0.245/0.164 = 1.49 — the same number from the other
side, now with a mechanism (the integrand decays along the path) rather than as a
bare discrepancy.

## Two targets for a derivation

- `g'(0) ≈ −0.245` — the Plancherel linear-response coefficient, a pure CLT-scale
  covariance and the easier of the two.
- `g(1) ≈ −0.164` — the conjecture's constant.

Hitting the first would be strong evidence a method is working before it is asked
for the second.
