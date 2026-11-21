import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# The proton and neutron weight spaces carry isomorphic braid actions

Level-2 Jimbo braiding on `(C²)^{⊗3}`, `h = q - q⁻¹`. The weight space of weight `(2,1)`
(two `e₁`, one `e₂`; basis `e₁e₁e₂, e₁e₂e₁, e₂e₁e₁`) and the weight space of weight `(1,2)`
(basis `e₁e₂e₂, e₂e₁e₂, e₂e₂e₁`) are preserved by `σ₁ = Ř ⊗ 1` and `σ₂ = 1 ⊗ Ř`.
On them the generators act by the 3×3 matrices `A₁, A₂` and `B₁, B₂` below.

This file gives an explicit invertible `P` with `P Aᵢ = Bᵢ P`. So the plain trace of every
braid word is the same on the two weight spaces. Consequence: the quantum trace restricted to
the two weight spaces differs only by the scalar by which `K^{⊗3}` acts. This is the
permutation-module half of the level-2 weight-space result (np-splitting audit §13–§15).
No numerical value enters.
-/

namespace QOU.BraidsAndKnots.NucleonWeightSpaceTraces

open Matrix

variable {R : Type*} [Field R]

/-- `σ₁` on the `(2,1)` weight space. -/
def A₁ (q : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]
/-- `σ₂` on the `(2,1)` weight space. -/
def A₂ (q : R) : Matrix (Fin 3) (Fin 3) R := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]
/-- `σ₁` on the `(1,2)` weight space. -/
def B₁ (q : R) : Matrix (Fin 3) (Fin 3) R := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]
/-- `σ₂` on the `(1,2)` weight space. -/
def B₂ (q : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]

/-- The intertwiner. -/
def P (q : R) : Matrix (Fin 3) (Fin 3) R := !![q⁻¹ ^ 2, q⁻¹, 0; q⁻¹, 0, q⁻¹; 0, q⁻¹, 1]

theorem intertwine₁ (q : R) (hq : q ≠ 0) : P q * A₁ q = B₁ q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, A₁, B₁, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem intertwine₂ (q : R) (hq : q ≠ 0) : P q * A₂ q = B₂ q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, A₂, B₂, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem det_P (q : R) (hq : q ≠ 0) : (P q).det = -(q ^ 2 + 1) / q ^ 4 := by
  simp [P, Matrix.det_fin_three]; field_simp; ring

/-- A braid word in `σ₁, σ₂` (`true` = `σ₁`), evaluated on a pair of matrices. -/
def word (X Y : Matrix (Fin 3) (Fin 3) R) : List Bool → Matrix (Fin 3) (Fin 3) R
  | [] => 1
  | b :: w => (if b then X else Y) * word X Y w

theorem intertwine_word (q : R) (hq : q ≠ 0) (w : List Bool) :
    P q * word (A₁ q) (A₂ q) w = word (B₁ q) (B₂ q) w * P q := by
  induction w with
  | nil => simp [word]
  | cons b w ih =>
    cases b
    · simp only [word, Bool.false_eq_true, if_false]
      rw [← mul_assoc, intertwine₂ q hq, mul_assoc, ih, mul_assoc]
    · simp only [word, if_true]
      rw [← mul_assoc, intertwine₁ q hq, mul_assoc, ih, mul_assoc]

/-- **Equal plain traces.** For `q ≠ 0` and `q² + 1 ≠ 0`, every braid word has the same
trace on the proton-type `(2,1)` and the neutron-type `(1,2)` weight spaces. -/
theorem trace_word_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace (word (A₁ q) (A₂ q) w) = trace (word (B₁ q) (B₂ q) w) := by
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  have key : word (B₁ q) (B₂ q) w = P q * word (A₁ q) (A₂ q) w * (P q)⁻¹ := by
    rw [intertwine_word q hq w, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]
  rw [key, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hdet, one_mul]

end QOU.BraidsAndKnots.NucleonWeightSpaceTraces
