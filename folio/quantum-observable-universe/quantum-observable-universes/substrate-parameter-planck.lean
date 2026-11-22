import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

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

/-- When `q ≠ 1`, the quantum Planck constant `ℏ_q = 1 - q⁻¹` is nonzero.

    `hbar_q` is a structure field carrying the default value `1 - q⁻¹`;
    the hypothesis `hdef` records that the constant takes this canonical
    value (it holds for any instance built without overriding the field).
    This is the definitional content of `\hbar_q = 1 - q^{-1}` in the
    narrative. -/
-- Ref: [leitner2026] Chapter 8, §1
theorem hbar_q_ne_zero (p : SubstrateParameterPlanck)
    (hdef : p.hbar_q = 1 - p.q⁻¹) (hq1 : p.q ≠ 1) :
    p.hbar_q ≠ 0 := by
  rw [hdef]
  intro h
  apply hq1
  -- h : 1 - p.q⁻¹ = 0, so p.q⁻¹ = 1, so p.q = 1
  have hinv : p.q⁻¹ = 1 := (sub_eq_zero.mp h).symm
  rwa [inv_eq_one] at hinv

end QOU.AlgebraicSubstrate
