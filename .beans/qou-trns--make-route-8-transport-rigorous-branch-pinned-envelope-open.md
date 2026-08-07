---
# qou-trns
title: 'Route 8 transport: branch integer now PINNED by the base point; envelope theorem still open'
status: in-progress
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - analysis
created_at: 2026-08-07T21:15:00Z
updated_at: 2026-08-07T21:15:00Z
parent: 0yqu
---


## Why this bean

After Route 11 (`qou-fivt`) **derived** the three numerators from the five-term
relation, the 5₂ sum rule's only remaining mathematical gap moved to **Route 8's
analytic transport** — and it is analytic, not arithmetic. This bean tracks
closing it.

Two sub-gaps were listed in `qou-8v3k`:

1. the branch integer `k = 0` on `|x| = 1` — **now closed, see below**;
2. the envelope theorem itself — **still open**.

## ✅ Sub-gap 1 CLOSED: `k = 0` is pinned by the base point, not assumed

Previously `k = 0` was argued from *integrality + local constancy on a
collision-free arc*. That shows `k` is **constant**; it does not say **which**
constant. The stronger argument determines it:

Let `g(x) := Σⱼ Log[(1 − yⱼ/x)/(1 − x·yⱼ)]`, continued **continuously** from
`x = 1` along the arc.

1. `exp(g(x)) = ∏ⱼ[(1 − yⱼ/x)/(1 − x·yⱼ)] = (1/x)/x = 1/x²` — exact Vieta, and
   **already Lean-proved** (`prod_one_sub_x_mul`, `prod_x_sub` in
   `QOU/QBeta/FiveTwoCyclotomicBloch.lean`).
2. The three branches `yⱼ(x)` are continuous and never collide on the arc
   (`min |disc| = 0.348`), so `g` is continuous.
3. Hence `g(x) + 2·log x` is continuous and valued in `2πiℤ`, therefore
   **constant**.
4. **At `x = 1` every factor is exactly `(1 − yⱼ)/(1 − yⱼ) = 1`**, so `g(1) = 0`,
   and `log 1 = 0`. The constant is **0**.
5. Therefore `g(x) = −2·log x` on the continuous branch — `k = 0` is *forced*.

**Verified:** 2000 points on `φ ∈ [0, π]` with continuous root tracking and
unwrapped per-root logs; worst `|g(x) + 2iφ| = 1.6e-30`.

Consequence, with `x = e^{iφ}`:

    S(e^{iφ}) − S(1) = Re ∫₀^φ (g/x)·(i·x) dt = ∫₀^φ 2t dt = φ²

so **`S(−1) = S(1) + π²`** — the transport step, now branch-pinned.

## ⚠ Two errors made getting here — recorded so they are not repeated

1. **A probe whose printed conclusion contradicted its own data.** The first
   branch-tracking script hard-coded "no jump" while its own output showed
   `|diff| = 6.2832 = 2π` at `φ = π`. Cause: it summed **principal** `Log`s,
   which wrap, instead of unwrapping them. **Never hard-code a verdict string
   that the run cannot falsify.**
2. **Comparing against the wrong branch.** The corrected run still showed
   `|diff| = 4π`, because it compared continuous `g` against mpmath's
   **principal** `log x`, which jumps at `φ = π` (`exp(1j*π)` lands just below
   the cut, so `arg = −π`). The mathematics was fine; the comparison was not.
   Compare against `log x = iφ`.

## ❌ Sub-gap 2 STILL OPEN: the envelope theorem

`d/dx V(x, yⱼ(x)) = ∂V/∂x` needs:

* `V` differentiable in both arguments along the path — for the complex `Li₂`
  terms this touches `qou-clx8`/`qou-ph1k`;
* `yⱼ(x)` differentiable, which follows from the implicit function theorem given
  non-vanishing discriminant (**have it**: `min |disc| = 0.348` on the arc), but
  is not written down;
* `∂V/∂y = 0` at `yⱼ`, which is the curve — **already Lean-proved algebraically**.

So the residual analytic content is differentiation of the complex dilogarithm
along a path, plus the implicit function theorem. **That is ordinary analysis,
not a research problem** — but it is not done, and it is the last mathematical
gap in the whole chain.

## Status of the full chain

    sum rule
      --Route 8--> cyclotomic identity at Q(zeta_7)+   [transport: branch PINNED,
                                                        envelope OPEN]
      --Route 9--> Re[2L(w_k)+L(-w_k)] = m_k pi^2/42   [algebra Lean-proved]
      --Route 11-> m = (17,5,-1)                       [DERIVED from five-term]

**Sum rule: verified to 80 dps. Numerators derived. Transport branch-pinned.
Envelope theorem open. Still not proved.**

## Refs

* `qou-8v3k` (Route 8), `qou-fivt` (Routes 10–11), `qou-b7cy` (Route 9)
* `QOU/QBeta/FiveTwoCyclotomicBloch.lean` — the Vieta products this argument uses
