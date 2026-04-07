/-!
# QOU.So3Generators

The images of the Dic₃ generators under the adjoint map to SO(3):
R_α (rotation by 2π/3 about e₃) and R_β (π-rotation about e₁).

LaTeX label: `def:so3-generators`

## References

- [manuscript] Chapter 4, §SU(2)–SO(3)
-/

import QOU.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fin.Basic

namespace QOU

/-- **SO(3) generator data**: rotation matrices from the adjoint map. -/
-- Ref: [manuscript] Chapter 4
structure So3Generators where
  /-- R_α: rotation by 2π/3 about e₃. -/
  R_alpha : Matrix (Fin 3) (Fin 3) ℝ
  /-- R_β: π-rotation about e₁. -/
  R_beta : Matrix (Fin 3) (Fin 3) ℝ
  /-- R_α has order 3 in SO(3): R_α³ = I. -/
  R_alpha_cubed : R_alpha * R_alpha * R_alpha = 1
  /-- R_β has order 2 in SO(3): R_β² = I. -/
  R_beta_sq : R_beta * R_beta = 1

/-- R_β is the π-rotation about e₁: diag(1, -1, -1). -/
-- Ref: [manuscript] Chapter 4
def R_beta_matrix : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 0, 0; 0, -1, 0; 0, 0, -1]

/-- R_β² = I by direct computation. -/
-- Ref: [manuscript] Chapter 4
theorem R_beta_involution :
    R_beta_matrix * R_beta_matrix = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [R_beta_matrix, Matrix.mul_apply, Fin.sum_univ_three] <;>
    ring

end QOU
