import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic


/-!
# QOU.Braiding.crossing_energy_decomposition — cosh/sinh decomposition

The crossing weights +q and -q⁻¹ decompose into symmetric (cosh)
and antisymmetric (sinh) channels under the mirror operation.

LaTeX label: `prop:crossing-energy-decomposition`

## References
- [manuscript] Ch. 7, §crossing-energy-decomposition

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Braiding

/-- The symmetric (strong) channel weight: cosh(ln q). -/
noncomputable def symmetricWeight (q : ℝ) : ℝ := (q + q⁻¹) / 2

/-- The antisymmetric (Coulomb) channel weight: sinh(ln q). -/
noncomputable def antisymmetricWeight (q : ℝ) : ℝ := (q - q⁻¹) / 2

/-- q decomposes as cosh + sinh. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem q_decomposition (q : ℝ) (hq : 0 < q) :
    q = symmetricWeight q + antisymmetricWeight q := by
  unfold symmetricWeight antisymmetricWeight
  ring

/-- q⁻¹ decomposes as cosh - sinh. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem q_inv_decomposition (q : ℝ) (hq : 0 < q) :
    q⁻¹ = symmetricWeight q - antisymmetricWeight q := by
  unfold symmetricWeight antisymmetricWeight
  ring

/-- The symmetric weight (q + q⁻¹)/2 equals cosh(ln q), for q > 0.
    This is what makes the "cosh channel" name a derived identity, not a
    definition: the symmetric crossing weight IS the hyperbolic cosine of
    the crossing rapidity λ = ln q. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem symmetricWeight_eq_cosh (q : ℝ) (hq : 0 < q) :
    symmetricWeight q = Real.cosh (Real.log q) := by
  unfold symmetricWeight Real.cosh
  rw [Real.exp_log hq, Real.exp_neg, Real.exp_log hq]

/-- The antisymmetric weight (q - q⁻¹)/2 equals sinh(ln q), for q > 0.
    The "Coulomb / sinh channel" is therefore a derived identity — the
    antisymmetric crossing weight IS the hyperbolic sine of λ = ln q,
    not a fitted parameter. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem antisymmetricWeight_eq_sinh (q : ℝ) (hq : 0 < q) :
    antisymmetricWeight q = Real.sinh (Real.log q) := by
  unfold antisymmetricWeight Real.sinh
  rw [Real.exp_log hq, Real.exp_neg, Real.exp_log hq]

/-- General identity: q = cosh(ln q) + sinh(ln q), for any q > 0.
    This is `eˣ = cosh x + sinh x` at x = ln q (so the RHS is e^{ln q} = q).
    It holds for every q > 0 — it is NOT specific to the substrate value. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem q_eq_cosh_add_sinh (q : ℝ) (hq : 0 < q) :
    q = Real.cosh (Real.log q) + Real.sinh (Real.log q) := by
  rw [← symmetricWeight_eq_cosh q hq, ← antisymmetricWeight_eq_sinh q hq]
  unfold symmetricWeight antisymmetricWeight
  ring

/-- General identity: q⁻¹ = cosh(ln q) - sinh(ln q), for any q > 0. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem q_inv_eq_cosh_sub_sinh (q : ℝ) (hq : 0 < q) :
    q⁻¹ = Real.cosh (Real.log q) - Real.sinh (Real.log q) := by
  rw [← symmetricWeight_eq_cosh q hq, ← antisymmetricWeight_eq_sinh q hq]
  unfold symmetricWeight antisymmetricWeight
  ring

/-- The EM/strong ratio is (q - q⁻¹)/(q + q⁻¹). -/
noncomputable def emStrongRatio (q : ℝ) : ℝ :=
  antisymmetricWeight q / symmetricWeight q

/-- EM/strong ratio equals tanh(ln q) for q > 1.
    Proof: tanh(ln q) = (e^{ln q} - e^{-ln q})/(e^{ln q} + e^{-ln q})
           = (q - q⁻¹)/(q + q⁻¹) = emStrongRatio q. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem em_strong_ratio_tanh (q : ℝ) (hq : 1 < q) :
    emStrongRatio q = Real.tanh (Real.log q) := by
  have hq0 : 0 < q := by linarith
  unfold emStrongRatio antisymmetricWeight symmetricWeight Real.tanh Real.sinh Real.cosh
  rw [Real.exp_log hq0, Real.exp_neg, Real.exp_log hq0]

/-- Symmetric weight is positive for q > 0. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem symmetric_pos (q : ℝ) (hq : 0 < q) :
    0 < symmetricWeight q := by
  unfold symmetricWeight
  have hqi : 0 < q⁻¹ := inv_pos.mpr hq
  linarith

/-- Antisymmetric weight is positive for q > 1. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem antisymmetric_pos (q : ℝ) (hq : 1 < q) :
    0 < antisymmetricWeight q := by
  unfold antisymmetricWeight
  have : q⁻¹ < 1 := by rw [inv_lt_one_iff_of_pos (by linarith)]; exact hq
  linarith

end QOU.Braiding
