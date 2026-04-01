/-!
# QOU.AlgebraicSubstrate.SubstrateParameterPlanck

Substrate parameter and quantum Planck constant.

LaTeX label: `def:substrate-parameter-planck`
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- **SubstrateParameterPlanck**: the deformation parameter `q ∈ ℂ*`
    and the derived quantum Planck constant `ℏ_q = 1 - q⁻¹`.

    LaTeX: `\label{def:substrate-parameter-planck}` -/
structure SubstrateParameterPlanck where
  /-- The substrate parameter `q ∈ ℂ`, nonzero. -/
  q : ℂ
  /-- `q ≠ 0`, ensuring the Hopf algebra is well-defined. -/
  hq_ne_zero : q ≠ 0
  /-- The quantum Planck constant `ℏ_q = 1 - q⁻¹`. -/
  hbar_q : ℂ := 1 - q⁻¹

/-- When `q ≠ 1`, the quantum Planck constant is nonzero. -/
-- Ref: [manuscript] Chapter 8, §1
theorem hbar_q_ne_zero (p : SubstrateParameterPlanck) (hq1 : p.q ≠ 1) :
    p.hbar_q ≠ 0 := by
  simp only [SubstrateParameterPlanck.hbar_q]
  intro h
  apply hq1
  have : q⁻¹ = 1 - (1 - q⁻¹) := by ring
  rw [show (1 : ℂ) - p.q⁻¹ = p.hbar_q from rfl] at h ⊢
  simp [h, inv_eq_one] at *
  exact (mul_right_cancel₀ p.hq_ne_zero (by rwa [mul_inv_cancel₀ p.hq_ne_zero, mul_one])).symm

end QOU.AlgebraicSubstrate
