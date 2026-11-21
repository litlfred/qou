import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# The gl_N Jimbo R-matrix satisfies the Hecke relation blockwise (issue #8833)

The U_q(gl_N) Jimbo R on `C^N ⊗ C^N` is block diagonal in the basis `e_i ⊗ e_j`:
`R (e_i ⊗ e_i) = q (e_i ⊗ e_i)`, and for `i < j` the pair `{e_i ⊗ e_j, e_j ⊗ e_i}` spans a
block `[[0, 1], [1, h]]`, `h = q - q⁻¹`. This file proves, over a generic field, that every
block satisfies `X² = h X + 1` and has inverse `X - h`. Used by
`computations/probes/qbeta_colour_gl6`, where isospin and colour share one gl₆ R-matrix.
-/

namespace QOU.QBeta.GlNJimboHecke

open Matrix

variable {R : Type*} [Field R]

/-- The off-diagonal block of the Jimbo R on `{e_i ⊗ e_j, e_j ⊗ e_i}`, `i < j`. -/
def offBlock (h : R) : Matrix (Fin 2) (Fin 2) R := !![0, 1; 1, h]

/-- The diagonal entry satisfies the Hecke relation. -/
theorem diag_hecke (q : R) (hq : q ≠ 0) : q * q = (q - q⁻¹) * q + 1 := by
  field_simp; ring

/-- The off-diagonal block satisfies the Hecke relation `X² = h X + 1`. -/
theorem offBlock_hecke (h : R) : offBlock h * offBlock h = h • offBlock h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [offBlock, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- The inverse of the off-diagonal block is `X - h`. -/
theorem offBlock_inv (h : R) : offBlock h * (offBlock h - h • 1) = 1 := by
  rw [Matrix.mul_sub, offBlock_hecke, Matrix.mul_smul, Matrix.mul_one, add_sub_cancel_left]

/-- The inverse of the diagonal entry is `q - h = q⁻¹`. -/
theorem diag_inv (q : R) (hq : q ≠ 0) : q * (q - (q - q⁻¹)) = 1 := by
  field_simp; ring

end QOU.QBeta.GlNJimboHecke
