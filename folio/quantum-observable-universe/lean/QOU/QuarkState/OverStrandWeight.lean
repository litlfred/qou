/-
# Which weight passes over: convention D and the over/under rule fix `u = T³ = +½`

Bean `qou-q1a4` / `qou-0whz` (epic `qou-qs0e`). Owner decision 2026-11-15:
"Probe C4 + Lean, one PR".

Level 2: `H_2(q)` acting on `C² ⊗ C²` through the Jimbo matrix `Ř`, basis
`(e₁e₁, e₁e₂, e₂e₁, e₂e₂)` = indices `0, 1, 2, 3`. The first tensor factor is the
strand at the lower position `i`. The corpus fixes that for `σ_i` (positive) the
strand at the lower position `i` passes OVER (`QOU.Knot.BraidClosure`, `stepOver_lo`;
introduction: "σ_i crosses strand i over strand i+1"). For `σ_i⁻¹` the strand at
position `i + 1` passes over.

## What this file proves (all over any field, no ordering)

1. `Rch_hecke`: `Ř² = h Ř + 1`, `h = q − q⁻¹`.
2. **Convention D forces the weight `K`.** `ptr_markov`: with `K = diag(q, q⁻¹)` the partial
   quantum trace of `Ř` is `q² · 1`, i.e. Markov with `z = q²/(q + q⁻¹) = q³/(q² + 1)`.
   `ptr_other_not_scalar`: with `K = diag(q⁻¹, q)` it is not a scalar when `q⁴ ≠ 1`, so
   that orientation is not a Markov trace at all. `ptr_markov_inv`: the same `K` works for
   the negative crossing (`q⁻² · 1`), so crossing sign cannot move it.
3. **Over/under.** For the positive crossing (`Rch_e12`, `Rch_e21`) and the negative one
   (`Rinv_e21`, `Rinv_e12`): the crossing is a pure transposition of the two strands exactly
   when the OVER strand carries `e₁` (the `K = q` vector). When the over strand carries `e₂`,
   the image has an extra `± h` component on the input vector itself: the two strands
   exchange labels.

## Reading (a definition plus these lemmas, not a new assumption)

`def:down-quark` defines: at every crossing `u` passes over and `d` passes under, and each
strand keeps its flavour. By 3, at `h ≠ 0` that is consistent with `Ř` only if `u = e₁`;
by 2, `e₁` is the `K = q` vector forced by convention D, i.e. `T³ = +½` under
`K = q^{2T³}`. The identification of the corpus flavour with the `gl₂` weight space is the
standard Schur–Weyl reading at level 2; it is stated here, not derived.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

namespace QOU.QuarkState.OverStrandWeight

open Matrix

variable {K : Type*} [Field K]

/-- The Jimbo matrix `Ř` on `C² ⊗ C²` (basis `e₁e₁, e₁e₂, e₂e₁, e₂e₂`), `h` on `e₂e₁`. -/
def Rch (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, q - q⁻¹, 0;
     0, 0, 0, q]

/-- The negative crossing `Ř⁻¹ = Ř − h`. -/
def Rinv (q : K) : Matrix (Fin 4) (Fin 4) K := Rch q - (q - q⁻¹) • (1 : Matrix (Fin 4) (Fin 4) K)

/-- Basis vector `b i`. -/
def b (i : Fin 4) : Fin 4 → K := Pi.single i 1

theorem Rch_hecke (q : K) (hq : q ≠ 0) :
    Rch q * Rch q = (q - q⁻¹) • Rch q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Rch, Matrix.mul_apply, Fin.sum_univ_four] <;>
    field_simp <;> ring

theorem Rch_mul_Rinv (q : K) (hq : q ≠ 0) : Rch q * Rinv q = 1 := by
  rw [Rinv, Matrix.mul_sub, Rch_hecke q hq, Matrix.mul_smul, Matrix.mul_one]
  abel

/-- Partial quantum trace over the second factor with weight `K = diag(d₁, d₂)`. -/
def ptr (d₁ d₂ : K) (M : Matrix (Fin 4) (Fin 4) K) : Matrix (Fin 2) (Fin 2) K :=
  !![d₁ * M 0 0 + d₂ * M 1 1, d₁ * M 0 2 + d₂ * M 1 3;
     d₁ * M 2 0 + d₂ * M 3 1, d₁ * M 2 2 + d₂ * M 3 3]

/-- **Markov at convention D**: `K = diag(q, q⁻¹)` gives `q² · 1`. -/
theorem ptr_markov (q : K) (hq : q ≠ 0) : ptr q q⁻¹ (Rch q) = (q ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [ptr, Rch] <;> field_simp <;> ring

/-- The resulting Markov parameter is `z_D = q³/(q² + 1)`. -/
theorem markov_z_eq_zD (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q ^ 2 / (q + q⁻¹) = q ^ 3 / (q ^ 2 + 1) := by
  have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp; try ring
  rw [this]; field_simp; try ring

/-- The same `K` is Markov for the negative crossing too (`q⁻² · 1`). -/
theorem ptr_markov_inv (q : K) (hq : q ≠ 0) :
    ptr q q⁻¹ (Rinv q) = (q⁻¹ ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [ptr, Rinv, Rch, Matrix.one_apply] <;> field_simp <;> ring

/-- **The other orientation is not a Markov trace**: `K = diag(q⁻¹, q)` gives a non-scalar. -/
theorem ptr_other_not_scalar (q : K) (hq : q ≠ 0) (h4 : q ^ 4 ≠ 1) :
    ¬ ∃ c : K, ptr q⁻¹ q (Rch q) = c • (1 : Matrix (Fin 2) (Fin 2) K) := by
  rintro ⟨c, hc⟩
  have h00 := congrFun (congrFun hc 0) 0
  have h11 := congrFun (congrFun hc 1) 1
  simp [ptr, Rch] at h00 h11
  apply h4
  have e : q⁻¹ * (q - q⁻¹) + q * q = q⁻¹ * q := by rw [h11, ← h00]
  field_simp at e
  linear_combination e

/-- Positive crossing, over strand (position `i`) carries `e₁`: pure transposition. -/
theorem Rch_e12 (q : K) : Rch q *ᵥ b 1 = b 2 := by
  ext k; fin_cases k <;> simp [Rch, b, Matrix.mulVec, dotProduct, Fin.sum_univ_four]

/-- Positive crossing, over strand carries `e₂`: an extra `h` on the input (label exchange). -/
theorem Rch_e21 (q : K) : Rch q *ᵥ b 2 = b 1 + (q - q⁻¹) • b 2 := by
  ext k; fin_cases k <;> simp [Rch, b, Matrix.mulVec, dotProduct, Fin.sum_univ_four]

/-- Negative crossing, over strand (position `i + 1`) carries `e₁`: pure transposition. -/
theorem Rinv_e21 (q : K) : Rinv q *ᵥ b 2 = b 1 := by
  ext k; fin_cases k <;> simp [Rinv, Rch, b, Matrix.sub_mulVec, Matrix.mulVec, dotProduct,
    Fin.sum_univ_four, Matrix.one_apply]

/-- Negative crossing, over strand carries `e₂`: an extra `−h` on the input (label exchange). -/
theorem Rinv_e12 (q : K) : Rinv q *ᵥ b 1 = b 2 - (q - q⁻¹) • b 1 := by
  ext k; fin_cases k <;> simp [Rinv, Rch, b, Matrix.sub_mulVec, Matrix.mulVec, dotProduct,
    Fin.sum_univ_four, Matrix.one_apply]

/-- **Over/under rule, both signs.** At `h ≠ 0`, a crossing keeps each strand's label
(pure transposition) iff its over strand carries `e₁`. -/
theorem over_e1_iff_pure (q : K) (hh : q - q⁻¹ ≠ 0) :
    (Rch q *ᵥ b 1 = b 2) ∧ (Rch q *ᵥ b 2 ≠ b 1) ∧
    (Rinv q *ᵥ b 2 = b 1) ∧ (Rinv q *ᵥ b 1 ≠ b 2) := by
  refine ⟨Rch_e12 q, ?_, Rinv_e21 q, ?_⟩
  · rw [Rch_e21]; intro h
    have := congrFun h 2; simp [b] at this
    first | exact hh this | exact hh (by linear_combination -this)
  · rw [Rinv_e12]; intro h
    have := congrFun h 1; simp [b] at this
    first | exact hh this | exact hh (by linear_combination -this)

end QOU.QuarkState.OverStrandWeight
