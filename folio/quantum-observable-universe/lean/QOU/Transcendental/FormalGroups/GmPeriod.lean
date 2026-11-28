import Mathlib.MeasureTheory.Integral.CircleIntegral

/-!
# The period of `G_m`: the only transcendental the multiplicative group carries

The invariant differential of `G_m` is `ω = dq/q`. Its residue at `q = 0` is the algebraic
number `1`, and its pullback along the endomorphism `q ↦ qᵏ` is `k · ω`
(`QOU.MassTheory.EnergyReadingTower.energyTower_T` is the formal-neighbourhood form of this, on
main). Integrating over the unit circle turns residues into periods:

* `gm_period`: `∮_{|q|=1} dq/q = 2πi`.
* `gm_period_pullback_zpow`: `∮_{|q|=1} (qᵏ)′/qᵏ dq = 2πi · k` for every `k ∈ ℤ`. With
  `Aut(G_m) = {±1}` (`QOU.FormalGroups.GmAut`, on main) this says the **sign of the period is
  the orientation of `G_m`**: the inversion `q ↦ q⁻¹` sends `2πi` to `−2πi`.
* `inv_eight_pi_eq`: `1/(8π) = (1/4) · |2πi|⁻¹`. This is only arithmetic. It records the proposed
  split of `μ₁ = 1/(8π)` into a rational part (`1/4`) and the `G_m` period. Deriving the `1/4`
  (from the heat-kernel `a₀` and the period map `Φ`) is open and is not claimed here.

This file is analytic, so it lives in `QOU/Transcendental/`. No measured values.
-/

namespace QOU.Transcendental.FormalGroups.GmPeriod

open Complex Real

/-- **The `G_m` period:** `∮_{|q|=1} dq/q = 2πi`. -/
theorem gm_period : (∮ z in C(0, 1), z⁻¹) = 2 * π * I := by
  have h := circleIntegral.integral_sub_inv_of_mem_ball (c := 0) (w := 0) (R := 1)
    (by simp)
  simpa using h

/-- **Pullback along `q ↦ qᵏ` multiplies the period by `k`.** -/
theorem gm_period_pullback_zpow (k : ℤ) :
    (∮ z in C(0, 1), ((k : ℂ) * z ^ (k - 1)) / z ^ k) = 2 * π * I * k := by
  have hcongr : (∮ z in C(0, 1), ((k : ℂ) * z ^ (k - 1)) / z ^ k) =
      ∮ z in C(0, 1), (k : ℂ) * z⁻¹ := by
    apply circleIntegral.integral_congr zero_le_one
    intro z hz
    have hz0 : z ≠ 0 := by
      rintro rfl
      simp at hz
    simp only
    rw [zpow_sub₀ hz0, zpow_one]
    field_simp
  rw [hcongr, circleIntegral.integral_const_mul, gm_period]
  ring

/-- **The inversion flips the sign of the period** (`k = −1`). -/
theorem gm_period_inversion :
    (∮ z in C(0, 1), (((-1 : ℤ) : ℂ) * z ^ ((-1 : ℤ) - 1)) / z ^ (-1 : ℤ)) = -(2 * π * I) := by
  rw [gm_period_pullback_zpow]
  push_cast
  ring

/-- `1/(8π) = (1/4) · |2πi|⁻¹` (arithmetic only). -/
theorem inv_eight_pi_eq : (1 : ℝ) / (8 * Real.pi) = (1 / 4) * ‖2 * (π : ℂ) * I‖⁻¹ := by
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  rw [norm_mul, norm_mul, Complex.norm_I, mul_one, Complex.norm_real, Complex.norm_two,
    Real.norm_eq_abs, abs_of_pos hpi]
  field_simp
  ring

end QOU.Transcendental.FormalGroups.GmPeriod
