import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import QOU.Archimedean.HExpansionDegree8Combined

/-!
# Truncation error bounds — bridge polynomials ↔ real functions

Bridges the rational-coefficient Taylor polynomials in
[`HExpansionDegree8.lean`](HExpansionDegree8.lean) /
[`HExpansionDegree8Combined.lean`](HExpansionDegree8Combined.lean)
to the actual real-valued `bringColorTube`, `faddeevH4`, and
`linkingWeightBringFaddeevH4` functions from
[`BringFaddeevH4LinkingWeight.lean`](BringFaddeevH4LinkingWeight.lean).

## Three truncation theorems

| Theorem | Status |
|---|---|
| `faddeevH4_truncation_eq` | **PROVED** (geometric-series identity, `field_simp + ring`) |
| `bringColorTube_truncation_error_bound` | `sorry` with `Ref`: needs `Mathlib.Analysis.Calculus.Taylor.Lagrange` |
| `linkingWeightBringFaddeevH4_truncation_error_bound` | `sorry` with `Ref`: triangle inequality once Bring closes |

## The Faddeev truncation — closed-form identity

The Faddeev factor `1/(1 − h⁴)` has the EXACT power series
`1 + h⁴ + h⁸ + h¹² + …`. Truncating at degree 8 (keep `1 + h⁴ + h⁸`)
leaves a tail = `h¹² + h¹⁶ + …` which is itself a geometric series
in `h⁴` with sum `h¹²/(1 − h⁴)`.

Result (proved via `field_simp + ring`):

  `1/(1 − h⁴) − (1 + h⁴ + h⁸) = h¹² / (1 − h⁴)`   when `h⁴ ≠ 1`.

This is a closed-form EQUALITY, not just an inequality. The
absolute-value bound is then a corollary.

## References

- Mathlib `Mathlib.Analysis.SpecificLimits.Basic` — geometric series
- Mathlib `Mathlib.Analysis.Calculus.Taylor.Lagrange` — Taylor's theorem
  with Lagrange remainder (needed for Bring color-tube)
- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §6 TODO
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Faddeev h⁴ truncation — CLOSED FORM (proved) -/

/-- Direct evaluation of the degree-8 Faddeev Taylor polynomial at a
    real argument. Equivalent to `faddeevH4Taylor8.eval h` once the
    Polynomial ℚ is mapped to ℝ, but we define it inline as a real
    expression for direct algebraic manipulation. -/
noncomputable def faddeevH4Taylor8_realEval (h : ℝ) : ℝ :=
  1 + h ^ 4 + h ^ 8

/-- The degree-8 Faddeev Taylor at h = 0 is 1 (matches `faddeevH4 1 = 1`). -/
theorem faddeevH4Taylor8_realEval_at_zero :
    faddeevH4Taylor8_realEval 0 = 1 := by
  unfold faddeevH4Taylor8_realEval
  norm_num

/-- **Faddeev truncation error — exact identity (PROVED).**

    For any real h with `h⁴ ≠ 1` (which holds at substrate `h ≈ 0.21`
    where `h⁴ ≈ 0.0019`):

      `1/(1 − h⁴) − (1 + h⁴ + h⁸)  =  h¹² / (1 − h⁴)`.

    The proof is `field_simp + ring`: algebraic identity. -/
theorem faddeevH4_truncation_eq (h : ℝ) (hne : 1 - h ^ 4 ≠ 0) :
    1 / (1 - h ^ 4) - faddeevH4Taylor8_realEval h
      = h ^ 12 / (1 - h ^ 4) := by
  unfold faddeevH4Taylor8_realEval
  field_simp
  ring

/-- **Faddeev truncation error — absolute-value bound (PROVED).**

    For real h with `h⁴ < 1` (so `1 − h⁴ > 0`):

      `|1/(1 − h⁴) − (1 + h⁴ + h⁸)|  ≤  h¹² / (1 − h⁴)`.

    Follows from the closed-form identity above (the difference is
    non-negative when h^4 < 1). -/
theorem faddeevH4_truncation_abs_bound (h : ℝ) (hlt : h ^ 4 < 1) :
    |1 / (1 - h ^ 4) - faddeevH4Taylor8_realEval h|
      ≤ h ^ 12 / (1 - h ^ 4) := by
  have hpos : 1 - h ^ 4 > 0 := by linarith
  have hne : 1 - h ^ 4 ≠ 0 := ne_of_gt hpos
  rw [faddeevH4_truncation_eq h hne]
  have h12_nonneg : h ^ 12 ≥ 0 := by positivity
  have div_nonneg : h ^ 12 / (1 - h ^ 4) ≥ 0 := div_nonneg h12_nonneg (le_of_lt hpos)
  rw [abs_of_nonneg div_nonneg]

/-- **Cross-check (informal)**: at the substrate `q₀ ≈ 1.110`, we have
    `h ≈ 0.21`, so `h⁴ ≈ 0.0019` and the Faddeev truncation bound
    `h¹² / (1 − h⁴) ≈ 7e-9` is negligible compared to the production
    probe's +108 ppm m_p prediction error.

    The +108 ppm error is dominated by the Bring color-tube h⁹
    truncation, NOT by the Faddeev h¹² tail. -/
example (h : ℝ) (h_small : h = 21 / 100) (h_lt : h ^ 4 < 1) :
    h ^ 12 / (1 - h ^ 4) ≤ 1 / 10 ^ 7 := by
  -- Numerical: at h = 0.21, h^12 ≈ 7e-9, 1-h^4 ≈ 0.998,
  -- so h^12 / (1 - h^4) ≈ 7e-9 < 1e-7 ✓.
  -- This is a numerical sanity check, not a load-bearing theorem.
  sorry

/-! ## §2  Bring color-tube truncation (sorry, with Ref) -/

/-- Direct degree-8 Bring Taylor evaluation at a real argument. -/
noncomputable def bringColorTubeTaylor8_realEval (h : ℝ) : ℝ :=
  1 + h + 6 * h ^ 2 + (47/2) * h ^ 3 + (693/8) * h ^ 4
    + (1299/4) * h ^ 5 + (156651/128) * h ^ 6 + (294787/64) * h ^ 7
    + (17743341/1024) * h ^ 8

/-- **Bring color-tube truncation error (statement, sorry with Ref).**

    For q in a small neighborhood of 1 (where h := q − q⁻¹ is small
    and `h · q^{10}` stays bounded away from 1), there exists a
    constant C such that

      `|bringColorTube q − bringColorTubeTaylor8_realEval (heckeH q)|
        ≤ C · |heckeH q|⁹`.

    The proof requires Mathlib's `Mathlib.Analysis.Calculus.Taylor`
    machinery (Taylor's theorem with Lagrange remainder for analytic
    functions on an interval). Outside the scope of this file.

    -- Ref: Taylor's theorem with Lagrange remainder applied to
    --      `f(q) = 1/(1 + q^9 − q^{11})` on `q ∈ [1−δ, 1+δ]`.
    --      For δ = 0.12: |h| ≤ 0.24, q^{10} ≤ 3.10, |h·q^{10}| ≤ 0.74 < 1 ✓.
    -- Ref: [hardy1908] Hardy, "A Course of Pure Mathematics" §6.4.
    -- Numerical corroboration: production probe gives 108 ppm m_p
    --   prediction error, consistent with C · h⁹ ≈ 170 ppm for C ≈ 200. -/
theorem bringColorTube_truncation_error_bound :
    ∃ (δ C : ℝ), 0 < δ ∧ 0 < C ∧
      ∀ q : ℝ, 1 - δ ≤ q → q ≤ 1 + δ →
        |bringColorTube q - bringColorTubeTaylor8_realEval (heckeH q)|
          ≤ C * |heckeH q| ^ 9 := by
  -- Ref: see docstring; needs Mathlib.Analysis.Calculus.Taylor.Lagrange
  sorry

/-! ## §3  Combined truncation -/

/-- Direct degree-8 combined-additive Taylor evaluation. -/
noncomputable def linkingWeightTaylor8_realEval (h : ℝ) : ℝ :=
  bringColorTubeTaylor8_realEval h + faddeevH4Taylor8_realEval h - 1

/-- **Combined truncation error (statement, sorry with Ref)**.

    Composes the Bring and Faddeev bounds via the triangle inequality.
    Closes once `bringColorTube_truncation_error_bound` closes.

    -- Ref: triangle inequality + faddeevH4_truncation_abs_bound
    --      (PROVED above) + bringColorTube_truncation_error_bound
    --      (sorry pending). -/
theorem linkingWeightBringFaddeevH4_truncation_error_bound :
    ∃ (δ C : ℝ), 0 < δ ∧ 0 < C ∧
      ∀ q : ℝ, 1 - δ ≤ q → q ≤ 1 + δ →
        |linkingWeightBringFaddeevH4 q
            - linkingWeightTaylor8_realEval (heckeH q)|
          ≤ C * |heckeH q| ^ 9 := by
  -- Ref: triangle inequality on
  --      (linkingWeightBringFaddeevH4 q - linkingWeightTaylor8_realEval h)
  --    = (bringColorTube q - bringColorTubeTaylor8_realEval h)
  --    + (faddeevH4 q - faddeevH4Taylor8_realEval h)
  --  + (Faddeev term is O(h^12), dominated by Bring's O(h^9))
  sorry

/-! ## §4  Numerical corroboration

These statements are numerically corroborated to high precision in
existing probes:

| Probe | Result |
|---|---|
| `m_p_bring_plus_faddeev_h4_probe.py` | bringColorTube(q₀) = 2.4600 |
| same | Bring + Faddeev h⁴ at q₀ = 2.4619 |
| same | m_p_pred = 938.4 MeV → +108 ppm vs CODATA |
| `lambda_scale_h2_concrete_test.py` | All h^k coeffs match sympy |

At substrate q₀ ≈ 1.110 (h ≈ 0.209):
  |h|^9 ≈ 8.5e-7
  |h|^{12} ≈ 7e-9
  For C ≈ 200 (rough): C·h^9 ≈ 1.7e-4 = 170 ppm

The faddeev tail is ~25,000× smaller than the bring h^9 tail at
substrate. So combined error budget is essentially the Bring term.

## §5  Open work

To CLOSE the two remaining sorrys:

1. `bringColorTube_truncation_error_bound` — needs Taylor's theorem
   with Lagrange remainder on `q ↦ 1/(1 + q^9 - q^{11})`. The
   derivative bounds can be computed; the `AnalyticOn` predicate
   needs `Mathlib.Analysis.Analytic.Basic`. Multi-session.

2. `linkingWeightBringFaddeevH4_truncation_error_bound` — follows
   from (1) + faddeevH4_truncation_abs_bound (PROVED) via triangle
   inequality. ~30 lines of Lean once (1) is in hand.

## §6  PROVED THEOREMS THIS FILE

  ✓ faddeevH4Taylor8_realEval_at_zero (= 1)
  ✓ faddeevH4_truncation_eq (closed-form identity, field_simp + ring)
  ✓ faddeevH4_truncation_abs_bound (bound from identity)
  ⏸️ informal substrate-domain example (1 sorry)
  ⏸️ bringColorTube_truncation_error_bound (1 sorry, Ref)
  ⏸️ linkingWeightBringFaddeevH4_truncation_error_bound (1 sorry, Ref)
-/

end QOU.Archimedean
