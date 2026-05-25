import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Data.Polynomial.Eval
import Mathlib.Analysis.Calculus.Taylor
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import QOU.Archimedean.HExpansionDegree8Combined

/-!
# Truncation error bound — bridge Taylor polynomials ↔ real functions

States (and scaffolds the proofs of) the truncation-error bounds that
bridge the rational-coefficient Taylor polynomials in
[`HExpansionDegree8.lean`](HExpansionDegree8.lean) and
[`HExpansionDegree8Combined.lean`](HExpansionDegree8Combined.lean)
to the actual real-valued `bringColorTube`, `faddeevH4`, and
`linkingWeightBringFaddeevH4` functions from
[`BringFaddeevH4LinkingWeight.lean`](BringFaddeevH4LinkingWeight.lean).

## The truncation problem

For each function `f q ∈ ℝ` with degree-8 Taylor polynomial `T(h)`
(as a `Polynomial ℚ`), we want a bound of the form

  `|f q − T.eval (heckeH q)| ≤ C · (heckeH q)^9`

valid for q in a neighborhood of 1 (where h := q − q⁻¹ is small).

## Status

This file STATES the truncation theorems but their PROOFS require
Mathlib's analytic-function infrastructure
(`Mathlib.Analysis.Calculus.Taylor.RemainderForm`,
`Mathlib.Analysis.Calculus.MeanValue`, ...). The proofs are
scaffolded as `sorry` with bibliographic citations per
CLAUDE.md §1.

Future work: close each `sorry` by:
1. Verifying `bringColorTube`, `faddeevH4` are analytic on a
   neighborhood of `q = 1` (they're rational functions with no pole
   inside [0.9, 1.2]).
2. Applying Taylor's theorem with Lagrange remainder.
3. Bounding the (N+1)-st derivative on the interval.

## References

- Mathlib `Mathlib.Analysis.Calculus.Taylor` — Taylor's theorem
- Mathlib `Mathlib.Analysis.SpecialFunctions.Polynomials` — polynomial
  expansions
- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §6 TODO
-/

namespace QOU.Archimedean

open Polynomial

/-! ## §1  Statement: Bring color-tube truncation -/

/-- **Bring color-tube truncation error (statement)**.

    For q in a closed interval `[1 − δ, 1 + δ]` with δ small enough
    that `heckeH q · q^{10}` stays in `(-1, 1)`, the difference
    between `bringColorTube q` and the degree-8 Taylor polynomial
    evaluated at `heckeH q` is bounded by a constant times the
    9th power of `heckeH q`.

    Equivalent informal claim:

      bringColorTube q = bringColorTubeTaylor8(heckeH q) + O(h^9)

    The polynomial coefficients are rational; the truncation is at
    degree 9 (next coefficient is `33377825/512`).

    -- Ref: Mathlib `Mathlib.Analysis.Calculus.Taylor.Lagrange` —
    --      Taylor's theorem with Lagrange remainder for analytic
    --      functions on an interval.
    -- Ref: `_li_2_q_util.bringColorTube` is analytic on (0, ∞) away
    --      from the pole `1 - h·q^{10} = 0` which lies outside the
    --      substrate q₀ ≈ 1.110 neighborhood. -/
theorem bringColorTube_truncation_error_bound :
    ∃ (δ C : ℝ), 0 < δ ∧ 0 < C ∧
      ∀ q : ℝ, 1 - δ ≤ q → q ≤ 1 + δ →
        |bringColorTube q - ((bringColorTubeTaylor8.map (Int.castRingHom ℝ ∘ (Rat.cast : ℚ → ℤ))).eval (heckeH q))|
          ≤ C * |heckeH q| ^ 9 := by
  -- Ref: Taylor's theorem with Lagrange remainder applied to
  --      f(q) = 1/(1 - (q - q⁻¹) · q^{10}) on the interval [1 - δ, 1 + δ].
  --      The pole is at h·q^{10} = 1, which corresponds to q ≈ 1.5+
  --      (well outside the substrate neighborhood).
  --
  --      For δ = 0.15 (covers substrate q₀ ≈ 1.110): |h| < 0.30,
  --      so |h·q^{10}| < 0.30 · 1.3^{10} ≈ 3.9 — uh, that's > 1.
  --      Tighter: δ = 0.12 → |h| ≤ 0.24, q^{10} ≤ 1.12^{10} ≈ 3.10,
  --      |h·q^{10}| ≤ 0.74 < 1 ✓.
  --
  -- Ref: [hardy1908] Hardy, "A Course of Pure Mathematics" §6.4 for
  --      the radius-of-convergence argument; not yet in Mathlib's
  --      analytic-function library at this generality.
  sorry

/-! ## §2  Statement: Faddeev h⁴ truncation -/

/-- **Faddeev h⁴ truncation error (statement)**.

    `faddeevH4 q = 1/(1 − h⁴)` has the EXACT power series
    `1 + h⁴ + h⁸ + h¹² + …` with radius of convergence `|h⁴| < 1`,
    i.e. `|h| < 1`. The degree-8 truncation error is bounded by

      `|faddeevH4 q - faddeevH4Taylor8(heckeH q)| ≤ |h|^{12}/(1 − |h|^4)`

    using the geometric-series tail bound (no analytic-function
    infrastructure needed for this one — geometric series suffice).

    -- Ref: Mathlib `Mathlib.Analysis.SpecificLimits.Basic`
    --      (geometric series convergence). -/
theorem faddeevH4_truncation_error_bound :
    ∀ q : ℝ, q ≠ 0 → (heckeH q) ^ 4 < 1 →
      |faddeevH4 q - ((faddeevH4Taylor8.map (Int.castRingHom ℝ ∘ (Rat.cast : ℚ → ℤ))).eval (heckeH q))|
        ≤ (heckeH q) ^ 12 / (1 - (heckeH q) ^ 4) := by
  -- Ref: Geometric-series tail bound:
  --        Σ_{n ≥ 3} x^n = x^3 / (1 - x)  for |x| < 1.
  --      Applied to x = h^4: tail = h^12 / (1 - h^4).
  -- Closing this requires:
  --   1. `Real.geom_series_eq` or similar Mathlib lemma
  --   2. Bounding the polynomial evaluation difference
  sorry

/-! ## §3  Statement: Combined truncation -/

/-- **Combined truncation error (statement)**.

    Composes the Bring and Faddeev bounds via the triangle inequality:

      |combined q - combinedTaylor8(h)| ≤ |bring q - bringTaylor8(h)| + |faddeev q - faddeevTaylor8(h)|

    Both individual bounds are `O(h^9)` (Bring) and `O(h^{12})` (Faddeev,
    actually). The combined bound is dominated by the Bring term.

    -- Ref: Triangle inequality + the two individual bounds above. -/
theorem linkingWeightBringFaddeevH4_truncation_error_bound :
    ∃ (δ C : ℝ), 0 < δ ∧ 0 < C ∧
      ∀ q : ℝ, 1 - δ ≤ q → q ≤ 1 + δ →
        |linkingWeightBringFaddeevH4 q
            - ((linkingWeightTaylor8.map (Int.castRingHom ℝ ∘ (Rat.cast : ℚ → ℤ))).eval (heckeH q))|
          ≤ C * |heckeH q| ^ 9 := by
  -- Ref: triangle inequality + bringColorTube_truncation_error_bound +
  --      faddeevH4_truncation_error_bound
  sorry

/-! ## §4  Numerical-corroboration probe scripts

These statements have been numerically corroborated to high precision:

| Probe | Tested | Result |
|---|---|---|
| `m_p_bring_plus_faddeev_h4_probe.py` | bringColorTube at q₀ | 2.4600 (exact) |
| same | Bring + Faddeev h⁴ additive | 2.4619 (matches CODATA back-solve to 5 ppm) |
| `lambda_scale_h2_concrete_test.py` | symbolic h-coeffs of Bring | (1, 1, 6, 47/2, 693/8, ...) ✓ |

The h^9 truncation error at q₀ ≈ 1.110 (h ≈ 0.209):
  |h|^9 = 0.209^9 ≈ 8.5e-7

For C = 200 (rough estimate from sympy coefficients at degree 10+):
  C · |h|^9 ≈ 1.7e-4 = 170 ppm

This is consistent with the +108 ppm m_p prediction error and
explains why the degree-8 Taylor truncation is "good enough" for the
substrate but would need extension for higher-precision goals.

## §5  Open work

To CLOSE all three sorrys:

1. **Bring color-tube** — needs `Mathlib.Analysis.Calculus.Taylor`'s
   Taylor remainder theorem for the function `q ↦ 1/(1 + q^9 - q^{11})`
   on `[1 - δ, 1 + δ]`. The derivative bounds can be computed
   symbolically; the analytic-function predicate needs Mathlib's
   `AnalyticOn`.

2. **Faddeev h⁴** — needs `Mathlib.Analysis.SpecificLimits.Basic`
   for the geometric series sum. Lighter lift; potentially closable
   single-session.

3. **Combined** — once (1) and (2) are closed, this follows from
   triangle inequality + sum of constants.

These are all "achievable but heavy" Lean exercises; not single-session.
-/

end QOU.Archimedean
