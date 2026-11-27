/-
# The ring mass reading is a true derivative

Analytic half of `QOU.Observations.ElectronRingMassReading`: the explicit `dMassE` is the
derivative of the ring mass `[4]/q³` on `q ≠ 0`, so `uE` is `−q ∂_q log m_e`.
-/
import QOU.Observations.ElectronRingMassReading
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Tactic

namespace QOU.Transcendental.MassTheory.ElectronRingMassReading

open QOU.Observations.ElectronRingMassReading

theorem hasDerivAt_qInt4 (q : ℝ) (hq : q ≠ 0) :
    HasDerivAt (fun x : ℝ => qInt4 x) (3 * q ^ 2 + 1 - (q ^ 2)⁻¹ - 3 * (q ^ 4)⁻¹) q := by
  have h1 : HasDerivAt (fun x : ℝ => x ^ 3) (3 * q ^ 2) q := by simpa using hasDerivAt_pow 3 q
  have h2 : HasDerivAt (fun x : ℝ => x) 1 q := hasDerivAt_id q
  have h3 : HasDerivAt (fun x : ℝ => x⁻¹) (-(q ^ 2)⁻¹) q := hasDerivAt_inv hq
  have h4 : HasDerivAt (fun x : ℝ => x⁻¹ ^ 3) (3 * q⁻¹ ^ 2 * (-(q ^ 2)⁻¹)) q := by
    exact (h3.pow 3).congr_deriv (by norm_num)
  have := ((h1.add h2).add h3).add h4
  unfold qInt4
  convert this using 1
  field_simp
  ring

/-- **`dMassE` is the derivative of the ring mass `[4]/q³`.** -/
theorem hasDerivAt_massE (q : ℝ) (hq : q ≠ 0) :
    HasDerivAt (fun x : ℝ => qInt4 x / x ^ 3) (dMassE q) q := by
  have hn := hasDerivAt_qInt4 q hq
  have hd : HasDerivAt (fun x : ℝ => x ^ 3) (3 * q ^ 2) q := by simpa using hasDerivAt_pow 3 q
  have := hn.div hd (pow_ne_zero 3 hq)
  unfold dMassE
  exact this

/-- **`U_e = −q ∂_q log m_e`** on `q > 0`. -/
theorem uE_eq_neg_log_deriv (q : ℝ) (hq : 0 < q) :
    -(q * deriv (fun x : ℝ => qInt4 x / x ^ 3) q / (qInt4 q / q ^ 3)) = uE q := by
  have h4 : qInt4 q ≠ 0 := by unfold qInt4; positivity
  rw [(hasDerivAt_massE q hq.ne').deriv, q_mul_dMassE q hq.ne' h4]
  unfold uE
  have : qInt4 q / q ^ 3 ≠ 0 := by positivity
  field_simp
  ring

end QOU.Transcendental.MassTheory.ElectronRingMassReading
