/-
  The colour-ratio Möbius matrix at a branch point of the colour tube cubic.

  Ref: [manuscript] §Bring's surface / Bundle structures and smoothness,
  lem:colour-ratio-mobius-matrix

  For a nonzero `ϖ` in a field `R`, the matrix

      M = !![1, ϖ; -1, ϖ]

  acts on `t` by `t ↦ (t + ϖ)/(-t + ϖ)`. We prove, over a generic field
  (§7c: nothing here is archimedean):

  * `mobiusMatrix_eq_cayley_mul_diag` — the Cayley factorisation
    `M = C₀ · diag(1, ϖ)` with `C₀ = !![1, 1; -1, 1]`;
  * `det_mobiusMatrix` — `det M = 2ϖ`;
  * `transpose_mul_mobiusMatrix` — `Mᵀ M = diag(2, 2ϖ²)`, i.e. the columns
    are orthogonal for the standard bilinear form;
  * `trace_sq_sub_four_det` — `(tr M)² − 4 det M = ϖ² − 6ϖ + 1`, the
    discriminant of the characteristic polynomial, whose vanishing is the
    parabolic condition;
  * `mobius_apply_neg_zero_pos` — the map sends `-ϖ, 0` to `0, 1` (its pole
    is at `t = ϖ`).

  Sorry-free. Base ring: any field; `det_mobiusMatrix_ne_zero` carries
  `2 ≠ 0` as a hypothesis.
-/
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.BringsSurface

open Matrix

variable {R : Type*} [Field R]

/-- The colour-ratio Möbius matrix `!![1, ϖ; -1, ϖ]`. -/
def mobiusMatrix (ϖ : R) : Matrix (Fin 2) (Fin 2) R := !![1, ϖ; -1, ϖ]

/-- The Cayley matrix `!![1, 1; -1, 1]` (multiplication by `1 - i` on `ℝ²`). -/
def cayleyMatrix : Matrix (Fin 2) (Fin 2) R := !![1, 1; -1, 1]

/-- The Möbius map of `mobiusMatrix ϖ`: `t ↦ (t + ϖ)/(-t + ϖ)`. -/
def mobiusMap (ϖ t : R) : R := (t + ϖ) / (-t + ϖ)

/-- Cayley factorisation: `M = C₀ · diag(1, ϖ)`. -/
theorem mobiusMatrix_eq_cayley_mul_diag (ϖ : R) :
    mobiusMatrix ϖ = cayleyMatrix * !![1, 0; 0, ϖ] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [mobiusMatrix, cayleyMatrix, Matrix.mul_apply, Fin.sum_univ_two]

/-- `det M = 2ϖ`. -/
theorem det_mobiusMatrix (ϖ : R) : (mobiusMatrix ϖ).det = 2 * ϖ := by
  rw [mobiusMatrix, Matrix.det_fin_two_of]
  ring

/-- `M` is invertible exactly when `2ϖ ≠ 0`. -/
theorem det_mobiusMatrix_ne_zero {ϖ : R} (h2 : (2 : R) ≠ 0) (hϖ : ϖ ≠ 0) :
    (mobiusMatrix ϖ).det ≠ 0 := by
  rw [det_mobiusMatrix]
  exact mul_ne_zero h2 hϖ

/-- The columns of `M` are orthogonal: `Mᵀ M = diag(2, 2ϖ²)`. -/
theorem transpose_mul_mobiusMatrix (ϖ : R) :
    (mobiusMatrix ϖ)ᵀ * mobiusMatrix ϖ = !![2, 0; 0, 2 * ϖ ^ 2] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [mobiusMatrix, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- `(tr M)² − 4 det M = ϖ² − 6ϖ + 1`. -/
theorem trace_sq_sub_four_det (ϖ : R) :
    (mobiusMatrix ϖ).trace ^ 2 - 4 * (mobiusMatrix ϖ).det = ϖ ^ 2 - 6 * ϖ + 1 := by
  rw [det_mobiusMatrix]
  simp [mobiusMatrix, Matrix.trace, Fin.sum_univ_two]
  ring

/-- The marked points: `-ϖ ↦ 0` and `0 ↦ 1`. (The pole `t = ϖ` is where the
denominator `-t + ϖ` vanishes.) -/
theorem mobius_apply_neg_zero_pos {ϖ : R} (hϖ : ϖ ≠ 0) :
    mobiusMap ϖ (-ϖ) = 0 ∧ mobiusMap ϖ 0 = 1 := by
  refine ⟨?_, ?_⟩
  · simp [mobiusMap]
  · simp [mobiusMap, hϖ]

end QOU.BringsSurface
