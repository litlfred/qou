/-
# QOU.Braiding.CoulombStrongRatioQRational
#
# Proves: for every real q > 0,
#   tanh(ln q) = (q - q⁻¹) / (q + q⁻¹) = (q² - 1) / (q² + 1).
#
# This is the formal version of the algebraic identity supporting
# `def:coulomb-charge`: the Coulomb/strong ratio stated in analytic
# form (tanh ∘ ln) coincides identically with the q-rational form
# at every real q > 0.
#
# Two parts:
#   1. `qDiffOverSum_eq_qSqDiff_over_qSqSum` — pure algebraic, generic Real
#   2. `Real.tanh_log_eq_qDiffOverSum`        — transcendental bridge via Real.exp_log
#
# LaTeX label: `prop:coulomb-strong-ratio-q-rational`
#
# CLAUDE.md §7c compliant: stated over ℝ for the archimedean realization;
# generic-ring version of the algebraic half stays over a CommRing.
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Hyperbolic

namespace QOU.Braiding

/-- **Algebraic half** — pure-ring identity (no transcendentals).

For any real q with `q ≠ 0` and `q² + 1 ≠ 0`,
  `(q - q⁻¹) / (q + q⁻¹) = (q² - 1) / (q² + 1)`. -/
theorem qDiffOverSum_eq_qSqDiff_over_qSqSum (q : ℝ) (hq : q ≠ 0) :
    (q - q⁻¹) / (q + q⁻¹) = (q^2 - 1) / (q^2 + 1) := by
  -- For q > 0 the LHS denominator is positive; we use q² + 1 > 0 generally.
  have h2 : (q^2 + 1 : ℝ) > 0 := by positivity
  have h2_ne : (q^2 + 1 : ℝ) ≠ 0 := ne_of_gt h2
  -- (q + q⁻¹) ≠ 0 follows because (q + q⁻¹) · q = q² + 1 ≠ 0 and q ≠ 0.
  have h_sum_ne : (q + q⁻¹) ≠ 0 := by
    intro h
    have : q * (q + q⁻¹) = q^2 + 1 := by
      field_simp
      ring
    rw [h, mul_zero] at this
    exact h2_ne this.symm
  field_simp
  ring

/-- **Transcendental bridge** — Real `tanh ∘ log` equals the q-rational.

For any real `q > 0`,
  `Real.tanh (Real.log q) = (q - q⁻¹) / (q + q⁻¹)`. -/
theorem tanh_log_eq_qDiffOverSum (q : ℝ) (hq : 0 < q) :
    Real.tanh (Real.log q) = (q - q⁻¹) / (q + q⁻¹) := by
  have hexp_log : Real.exp (Real.log q) = q := Real.exp_log hq
  have hexp_neg_log : Real.exp (-Real.log q) = q⁻¹ := by
    rw [Real.exp_neg, hexp_log]
  -- tanh = sinh/cosh; expand both via their `(exp x ± exp(-x))/2` forms.
  rw [Real.tanh_eq_sinh_div_cosh, Real.sinh_eq, Real.cosh_eq,
      hexp_log, hexp_neg_log]
  have hq_ne : q ≠ 0 := ne_of_gt hq
  -- (q - q⁻¹)/2 ÷ (q + q⁻¹)/2 = (q - q⁻¹)/(q + q⁻¹)
  have h2 : (2 : ℝ) ≠ 0 := two_ne_zero
  have h_sum_ne : q + q⁻¹ ≠ 0 := by
    have hsq : (q^2 + 1 : ℝ) > 0 := by positivity
    intro h
    have hmul : q * (q + q⁻¹) = q^2 + 1 := by field_simp; ring
    rw [h, mul_zero] at hmul
    linarith
  -- Close the algebraic goal after field_simp clears denominators (Copilot review PR #1765).
  field_simp
  ring

/-- **Composite proposition** (`prop:coulomb-strong-ratio-q-rational`).

The Coulomb/strong ratio `tanh(ln q)` from `def:coulomb-charge`
equals the q-rational `(q² − 1) / (q² + 1)` at every real `q > 0`. -/
theorem coulomb_strong_ratio_q_rational (q : ℝ) (hq : 0 < q) :
    Real.tanh (Real.log q) = (q^2 - 1) / (q^2 + 1) := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  rw [tanh_log_eq_qDiffOverSum q hq]
  exact qDiffOverSum_eq_qSqDiff_over_qSqSum q hq_ne

end QOU.Braiding
