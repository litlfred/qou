import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.So3Generators

The images of the Dic₃ generators under the adjoint map to SO(3):
R_α (rotation by 2π/3 about e₃) and R_β (π-rotation about e₁).

LaTeX label: `def:so3-generators`

## References

- [manuscript] Chapter 4, §SU(2)–SO(3)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **SO(3) generator data**: rotation matrices from the adjoint map. -/
-- Ref: [manuscript] Chapter 4
structure So3Generators where
  /-- R_α: rotation by 2π/3 about e₃. -/
  R_alpha : Matrix (Fin 3) (Fin 3) R_q
  /-- R_β: π-rotation about e₁. -/
  R_beta : Matrix (Fin 3) (Fin 3) R_q
  /-- R_α has order 3 in SO(3): R_α³ = I. -/
  R_alpha_cubed : R_alpha * R_alpha * R_alpha = 1
  /-- R_β has order 2 in SO(3): R_β² = I. -/
  R_beta_sq : R_beta * R_beta = 1

/-- R_β is the π-rotation about e₁: diag(1, -1, -1). -/
-- Ref: [manuscript] Chapter 4
def R_beta_matrix : Matrix (Fin 3) (Fin 3) R_q :=
  !![1, 0, 0; 0, -1, 0; 0, 0, -1]

/-- R_β² = I by direct computation. -/
-- Ref: [manuscript] Chapter 4
theorem R_beta_involution :
    R_beta_matrix * R_beta_matrix = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [R_beta_matrix, Matrix.mul_apply, Fin.sum_univ_three]

end

end QOU

