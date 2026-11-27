import BraidKnotOctonion.F3_eps6_leading_eq_neg_2b_cubed
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# `F₃` leading `ε⁶` coefficient with `Real.sqrt 3` (Transcendental companion)

Split from `BraidKnotOctonion.F3_eps6_leading_eq_neg_2b_cubed` (bean `qou-dk7p`), which
proves `-2 b³ = -(3/2) b` for any symbol `b` with `b² = 3/4`. This file evaluates at
`b = √3/2` under the original names.
-/

namespace QOU.BraidKnot

/-- Hoefsmit `b` evaluated at q = 1: `b(1) = √3/2`. -/
noncomputable def b_at_one : ℝ := Real.sqrt 3 / 2

/-- `b(1)² = 3/4`. -/
theorem b_at_one_sq : b_at_one^2 = 3 / 4 := by
  unfold b_at_one
  -- (√3 / 2)² = 3 / 4
  rw [div_pow]
  rw [show (Real.sqrt 3)^2 = 3 by
    rw [sq, Real.mul_self_sqrt]; norm_num]
  norm_num

/-- `b(1)³ = (3 · √3) / 8`. -/
theorem b_at_one_cubed : b_at_one^3 = 3 * Real.sqrt 3 / 8 := by
  unfold b_at_one
  rw [show (Real.sqrt 3 / 2)^3 = (Real.sqrt 3)^3 / 8 from by ring]
  -- (√3)³ = √3 · 3 = 3·√3
  have h_sqrt3_sq : (Real.sqrt 3)^2 = 3 := by
    rw [sq, Real.mul_self_sqrt]; norm_num
  rw [show (Real.sqrt 3)^3 = (Real.sqrt 3)^2 * Real.sqrt 3 from by ring]
  rw [h_sqrt3_sq]

/-- **The exact symbolic-match lemma.**
    `-2 · b(1)³ = -2 · (3·√3 / 8) = -(3·√3) / 4`. -/
-- Ref: [leitner2026] prop:q-beta-categorical-precision-ladder §"Story B c_3"
-- Ref: [leitner2026] probe_q_beta_cat_per_factor_decomposition.py (sympy symbolic match)
theorem F3_eps6_leading_eq_neg_2b_cubed :
    -2 * b_at_one^3 = -(3 * Real.sqrt 3) / 4 := by
  rw [b_at_one_cubed]
  ring

/-- **Alternative form**: with `-3√3/4` written as `-3/4 · √3`. -/
theorem F3_eps6_leading_eq_neg_2b_cubed' :
    -2 * b_at_one^3 = -3 / 4 * Real.sqrt 3 := by
  rw [F3_eps6_leading_eq_neg_2b_cubed]
  ring

/-! ## Numerical evaluation

For sanity checking: `-3·√3/4 ≈ -1.29904`.

This matches the empirical ε^6 coefficient of F_3 - 1 computed via
sympy in `probe_q_beta_cat_per_factor_decomposition.py`:

  Predicted: `-2 · b³(q=1) = -3·√3/4 ≈ -1.299038`
  Empirical: `-3·√3/4` (sympy-exact, no numerical rounding)
  Match:     DIFFERENCE EXACTLY 0 (algebraic match)

This DISCHARGES the leading-order content of the
`ThreeFoldMarkovHopfExtraction` class for the c_3 = -2 identification
in `prop:q-beta-c3-hopf-three-fold-markov`. -/

end QOU.BraidKnot
