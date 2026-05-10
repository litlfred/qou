import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# §3  Substrate Parameter, Gauge Group, Planck Constant

The substrate parameter `q : M → ℝ`, the quantum gauge group family
`{SU_{q(p)}(2)}`, and the quantum Planck constant `ℏ_q = 1 − q⁻¹`.
-/


namespace QOU

/-! ## §3  Substrate Parameter, Gauge Group, Planck Constant -/

/-- **Substrate parameter** (abstract): a ring homomorphism
    `ι : ℤ[q, q⁻¹] → k` specialising the Lusztig integral form.

    LaTeX: `\label{def:substrate-parameter}` -/
structure SubstrateParameter (M : Type*) where
  /-- The substrate field `q : M → ℝ` with `q(p) ≥ 1`. -/
  field : M → ℝ
  /-- Invertibility: `q(p) > 0` for all `p`. -/
  field_pos : ∀ (p : M), 0 < field p
  /-- Lower bound: `q(p) ≥ 1` (classicality bound). -/
  field_ge_one : ∀ (p : M), 1 ≤ field p
  /-- `q₀(p)` is never a root of unity. -/
  not_root_of_unity : ∀ (p : M) (k : ℕ), k ≥ 1 → field p ^ k ≠ 1

/-- **Quantum gauge group**: the family `{SU_{q(p)}(2)}_{p ∈ M}`.
    LaTeX: `\label{def:quantum-gauge-group}` -/
structure QuantumGaugeGroup (M : Type*) extends SubstrateParameter M where
  /-- The quantum group at each point. -/
  groupAt : M → Type*

/-- **Quantum Planck constant**: `ℏ_q(p) = 1 − q(p)⁻¹`.
    LaTeX: `\label{def:quantum-planck-constant}` -/
noncomputable def quantumPlanckConstant {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  1 - (sp.field p)⁻¹

/-- The quantum Planck constant takes values in `[0, 1)`. -/
theorem quantumPlanckConstant_nonneg {M : Type*} (sp : SubstrateParameter M)
    (p : M) : 0 ≤ quantumPlanckConstant sp p := by
  unfold quantumPlanckConstant
  have hq := sp.field_ge_one p
  have hpos := sp.field_pos p
  have hne : sp.field p ≠ 0 := hpos.ne'
  -- (sp.field p)⁻¹ ≤ 1 follows from 1 ≤ sp.field p via multiplication
  nlinarith [mul_le_mul_of_nonneg_right hq (le_of_lt (inv_pos.mpr hpos)),
             mul_inv_cancel₀ hne]

theorem quantumPlanckConstant_lt_one {M : Type*} (sp : SubstrateParameter M)
    (p : M) : quantumPlanckConstant sp p < 1 := by
  unfold quantumPlanckConstant
  have hpos := sp.field_pos p
  have hinv : 0 < (sp.field p)⁻¹ := inv_pos.mpr hpos
  linarith

end QOU
