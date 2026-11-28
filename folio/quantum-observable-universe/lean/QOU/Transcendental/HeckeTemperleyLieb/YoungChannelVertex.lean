/-
Young-channel vertex energy (prereg Addendum 17, audit §28).

The quark strand and the lepton strand at the β vertex form a pair in `H₂(q)`. On the
weight-zero space of `V ⊗ V`, basis `(ud, du)`, the Jimbo R-matrix acts by
`ud ↦ du`, `du ↦ ud + h·du` with `h = q - q⁻¹`. We split each basis state by the Hecke
idempotents `P_sym = (Ř + q⁻¹)/[2]`, `P_anti = (q - Ř)/[2]`, weight each channel by the
absolute value of its eigenvalue (`q`, `q⁻¹`), and compare the two states.

Result: the split is real but its energy `E₀·ln((q² + q⁻²)/2)` is strictly smaller than the
cell `2E₀·ln q`, its sign flips with the tensor order, and it is bounded by
`E₀·(q - q⁻¹)²/2`. No empirical number enters any statement.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.QBeta.YoungChannelVertex

open Matrix

section Generic

variable {R : Type*} [Field R]

/-- Jimbo `Ř` on the weight-zero space, basis `(ud, du)`; `h = q - q⁻¹`. -/
def rCheck (h : R) : Matrix (Fin 2) (Fin 2) R := !![0, 1; 1, h]

/-- `Ř` satisfies the Hecke relation `Ř² = h·Ř + 1`. -/
theorem rCheck_hecke (h : R) : rCheck h * rCheck h = h • rCheck h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [rCheck, Matrix.mul_apply, Fin.sum_univ_two, add_comm]

/-- Symmetric idempotent `(Ř + q⁻¹)/[2]`. -/
noncomputable def pSym (q : R) : Matrix (Fin 2) (Fin 2) R :=
  (q + q⁻¹)⁻¹ • (rCheck (q - q⁻¹) + q⁻¹ • 1)

/-- Antisymmetric idempotent `(q - Ř)/[2]`. -/
noncomputable def pAnti (q : R) : Matrix (Fin 2) (Fin 2) R :=
  (q + q⁻¹)⁻¹ • (q • 1 - rCheck (q - q⁻¹))

theorem pSym_add_pAnti (q : R) (h2 : q + q⁻¹ ≠ 0) : pSym q + pAnti q = 1 := by
  have key : (q + q⁻¹)⁻¹ * (q + q⁻¹) = 1 := inv_mul_cancel₀ h2
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [pSym, pAnti, rCheck] <;> linear_combination key

/-- Diagonal channel entries of `ud` (index 0): `(q⁻¹/[2], q/[2])`. -/
theorem diag_ud (q : R) :
    pSym q 0 0 = q⁻¹ / (q + q⁻¹) ∧ pAnti q 0 0 = q / (q + q⁻¹) := by
  constructor <;> simp [pSym, pAnti, rCheck] <;> ring

/-- Diagonal channel entries of `du` (index 1): `(q/[2], q⁻¹/[2])`. -/
theorem diag_du (q : R) :
    pSym q 1 1 = q / (q + q⁻¹) ∧ pAnti q 1 1 = q⁻¹ / (q + q⁻¹) := by
  constructor <;> simp [pSym, pAnti, rCheck] <;> ring

/-- Channel Gibbs weight of a basis state: `q·P_sym(s,s) + q⁻¹·P_anti(s,s)`. -/
noncomputable def stateWeight (q : R) (s : Fin 2) : R :=
  q * pSym q s s + q⁻¹ * pAnti q s s

theorem weight_ud (q : R) : stateWeight q 0 = 2 / (q + q⁻¹) := by
  obtain ⟨h1, h2⟩ := diag_ud q
  by_cases hq : q = 0
  · subst hq; simp [stateWeight, h1, h2]
  · rw [stateWeight, h1, h2]; field_simp; ring

theorem weight_du (q : R) : stateWeight q 1 = (q ^ 2 + q⁻¹ ^ 2) / (q + q⁻¹) := by
  obtain ⟨h1, h2⟩ := diag_du q
  rw [stateWeight, h1, h2]; ring

end Generic

section Real

/-- Vertex energy for a transition from a state of weight `Wi` to one of weight `Wf`. -/
noncomputable def vertexEnergy (E₀ Wi Wf : ℝ) : ℝ := E₀ * Real.log (Wi / Wf)

/-- Claim 3: swapping the tensor order swaps the two weights, which negates the energy.
So the sign of the Young-channel vertex energy is a convention. -/
theorem vertexEnergy_swap (E₀ Wi Wf : ℝ) (hi : 0 < Wi) (hf : 0 < Wf) :
    vertexEnergy E₀ Wf Wi = - vertexEnergy E₀ Wi Wf := by
  unfold vertexEnergy
  rw [Real.log_div hf.ne' hi.ne', Real.log_div hi.ne' hf.ne']; ring

/-- The ratio `W(du)/W(ud)` is `(q² + q⁻²)/2`. -/
theorem ratio_du_ud (q : ℝ) (hq : 0 < q) :
    stateWeight q 1 / stateWeight q 0 = (q ^ 2 + q⁻¹ ^ 2) / 2 := by
  rw [weight_du, weight_ud]
  have : q + q⁻¹ ≠ 0 := by positivity
  field_simp

/-- Claim 4 (lower): the split is real, `0 < ln((q² + q⁻²)/2)` for `q > 1`. -/
theorem log_ratio_pos (q : ℝ) (hq : 1 < q) : 0 < Real.log ((q ^ 2 + q⁻¹ ^ 2) / 2) := by
  apply Real.log_pos
  have hq0 : 0 < q := by linarith
  have hqi : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hqi0 : 0 < q⁻¹ := inv_pos.mpr hq0
  have hm : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0.ne'
  nlinarith [sq_nonneg (q - q⁻¹), mul_pos (sub_pos.mpr hq) (sub_pos.mpr hqi)]

/-- Claim 4 (upper): the split is strictly smaller than the cell, `ln((q²+q⁻²)/2) < 2 ln q`. -/
theorem log_ratio_lt_cell (q : ℝ) (hq : 1 < q) :
    Real.log ((q ^ 2 + q⁻¹ ^ 2) / 2) < 2 * Real.log q := by
  have hq0 : 0 < q := by linarith
  rw [show 2 * Real.log q = Real.log (q ^ 2) by rw [Real.log_pow]; norm_num]
  apply Real.log_lt_log (by positivity)
  have hqi : q⁻¹ < q := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  have hqi0 : 0 < q⁻¹ := inv_pos.mpr hq0
  nlinarith [mul_lt_mul hqi hqi.le hqi0 hq0.le]

/-- Bound: `ln((q² + q⁻²)/2) ≤ (q - q⁻¹)²/2`, so the vertex energy is at most
`E₀·(q - q⁻¹)²/2`. -/
theorem log_ratio_le (q : ℝ) (hq : 0 < q) :
    Real.log ((q ^ 2 + q⁻¹ ^ 2) / 2) ≤ (q - q⁻¹) ^ 2 / 2 := by
  have hm : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  have heq : (q ^ 2 + q⁻¹ ^ 2) / 2 = (q - q⁻¹) ^ 2 / 2 + 1 := by
    have : (q - q⁻¹) ^ 2 = q ^ 2 + q⁻¹ ^ 2 - 2 * (q * q⁻¹) := by ring
    rw [this, hm]; ring
  rw [heq]
  have := Real.log_le_sub_one_of_pos (show 0 < (q - q⁻¹) ^ 2 / 2 + 1 by positivity)
  linarith

/-- Combined: for `E₀ > 0` and `q > 1`, the du → ud vertex energy is positive, below the
cell `2E₀ ln q`, and at most `E₀(q - q⁻¹)²/2`. -/
theorem vertex_lt_cell (E₀ q : ℝ) (hE : 0 < E₀) (hq : 1 < q) :
    0 < vertexEnergy E₀ (stateWeight q 1) (stateWeight q 0) ∧
    vertexEnergy E₀ (stateWeight q 1) (stateWeight q 0) < 2 * E₀ * Real.log q ∧
    vertexEnergy E₀ (stateWeight q 1) (stateWeight q 0) ≤ E₀ * ((q - q⁻¹) ^ 2 / 2) := by
  have hq0 : 0 < q := by linarith
  unfold vertexEnergy
  rw [ratio_du_ud q hq0]
  refine ⟨mul_pos hE (log_ratio_pos q hq), ?_, ?_⟩
  · have := log_ratio_lt_cell q hq; nlinarith
  · exact mul_le_mul_of_nonneg_left (log_ratio_le q hq0) hE.le

end Real

end QOU.QBeta.YoungChannelVertex
