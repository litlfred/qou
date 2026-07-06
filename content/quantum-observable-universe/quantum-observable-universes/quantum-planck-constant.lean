import QOU.QuantumObservableUniverse.SubstrateParameter
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith


/-!
# QOU.quantumPlanckConstant

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/SubstrateParameter.lean

The quantum Planck constant `ℏ_q(p) = 1 − q(p)⁻¹` of a substrate parameter
`q : M → ℝ` with `q(p) ≥ 1`.  At classicality (`q → 1`) we get `ℏ_q → 0`;
in the deep-quantum regime (`q → ∞`) we get `ℏ_q → 1`.
-/

namespace QOU

/-- **Quantum Planck constant**: `ℏ_q(p) = 1 − q(p)⁻¹`.

    A field `M → [0, 1)`.  At classicality `q → 1` we get `ℏ_q → 0`;
    in the deep-quantum regime `q → ∞` we get `ℏ_q → 1`.

    LaTeX: `\label{def:quantum-planck-constant}` -/
noncomputable def quantumPlanckConstantSibling {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  1 - (sp.field p)⁻¹

/-- The quantum Planck constant is non-negative (`0 ≤ ℏ_q`), since `q(p) ≥ 1`. -/
theorem quantumPlanckConstantSibling_nonneg {M : Type*} (sp : SubstrateParameter M)
    (p : M) : 0 ≤ quantumPlanckConstantSibling sp p := by
  unfold quantumPlanckConstantSibling
  have hq := sp.field_ge_one p
  have hpos := sp.field_pos p
  have hne : sp.field p ≠ 0 := hpos.ne'
  nlinarith [mul_le_mul_of_nonneg_right hq (le_of_lt (inv_pos.mpr hpos)),
             mul_inv_cancel₀ hne]

/-- The quantum Planck constant is strictly less than one (`ℏ_q < 1`). -/
theorem quantumPlanckConstantSibling_lt_one {M : Type*} (sp : SubstrateParameter M)
    (p : M) : quantumPlanckConstantSibling sp p < 1 := by
  unfold quantumPlanckConstantSibling
  have hpos := sp.field_pos p
  have hinv : 0 < (sp.field p)⁻¹ := inv_pos.mpr hpos
  linarith

/-- At classicality (`q = 1`), the quantum Planck constant vanishes. -/
theorem planck_classical_limit {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p = 1) :
    quantumPlanckConstantSibling sp p = 0 := by
  unfold quantumPlanckConstantSibling
  rw [hq, inv_one, sub_self]

end QOU
