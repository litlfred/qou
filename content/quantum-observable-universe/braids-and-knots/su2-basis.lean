import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.Su2Basis

The standard basis of 𝔰𝔲(2): eₐ = −(i/2)τₐ (Pauli matrices),
with Lie bracket [eₐ, e_b] = ε_{abc} e_c.

LaTeX label: `def:su2-basis`

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

/-- **𝔰𝔲(2) basis data**: three generators e₁, e₂, e₃ with
    structure constants given by the Levi-Civita symbol. -/
-- Ref: [manuscript] Chapter 4
structure Su2Basis where
  /-- The Lie algebra carrier. -/
  LieAlg : Type*
  /-- The three basis vectors eₐ for a = 1, 2, 3. -/
  basis : Fin 3 → LieAlg
  /-- The Lie bracket operation. -/
  bracket : LieAlg → LieAlg → LieAlg
  /-- [e₁, e₂] = e₃. -/
  comm_12 : bracket (basis 0) (basis 1) = basis 2
  /-- [e₂, e₃] = e₁. -/
  comm_23 : bracket (basis 1) (basis 2) = basis 0
  /-- [e₃, e₁] = e₂. -/
  comm_31 : bracket (basis 2) (basis 0) = basis 1

/-- The Killing form is negative definite on 𝔰𝔲(2):
    ⟨eₐ, eₐ⟩ = −½ for the standard normalisation. -/
-- Ref: [manuscript] Chapter 4
structure Su2KillingForm extends Su2Basis where
  /-- The Killing form. -/
  killing : LieAlg → LieAlg → R_q
  /-- Normalisation: 2 * ⟨eₐ, eₐ⟩ = -1. -/
  normalised : ∀ a : Fin 3, 2 * killing (basis a) (basis a) = -1
  /-- Orthogonality: ⟨eₐ, e_b⟩ = 0 for a ≠ b. -/
  orthogonal : ∀ a b : Fin 3, a ≠ b → killing (basis a) (basis b) = 0

end

end QOU
