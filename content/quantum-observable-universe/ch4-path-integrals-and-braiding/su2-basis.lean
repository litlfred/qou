/-!
# QOU.Su2Basis

The standard basis of 𝔰𝔲(2): eₐ = −(i/2)τₐ (Pauli matrices),
with Lie bracket [eₐ, e_b] = ε_{abc} e_c.

LaTeX label: `def:su2-basis`

## References

- [manuscript] Chapter 4, §SU(2)–SO(3)
-/

import QOU.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fin.Basic

namespace QOU

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
  killing : LieAlg → LieAlg → ℝ
  /-- Normalisation: ⟨eₐ, eₐ⟩ = -1/2. -/
  normalised : ∀ a : Fin 3, killing (basis a) (basis a) = -1/2
  /-- Orthogonality: ⟨eₐ, e_b⟩ = 0 for a ≠ b. -/
  orthogonal : ∀ a b : Fin 3, a ≠ b → killing (basis a) (basis b) = 0

end QOU
