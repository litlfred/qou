import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.Group.Invertible.Defs
import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.Su2Basis

The standard basis of 𝔰𝔲(2): eₐ = −(i/2)τₐ (Pauli matrices),
with Lie bracket [eₐ, e_b] = ε_{abc} e_c.

LaTeX label: `def:su2-basis`

## References

- [leitner2026] Chapter 4, §SU(2)–SO(3)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.

**Base ring for the Killing form** (§7c): the 𝔰𝔲(2) Killing form is
`q`-independent, and the *only* thing its normalisation needs is that
`2` be invertible — the value `-1/2` is not in `R_q = ℤ[q, q⁻¹]`, but
it is in `ℤ[1/2]`, so no field is required. The codomain is therefore a
generic `(K : Type*) [CommRing K] [Invertible (2 : K)]` with `-⅟(2 : K)`
in place of `-1/2`; `K = ℚ` (the previous hard-wired codomain) and
`K = ℤ[1/2][q^{±1}]` are both instances.
-/

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
noncomputable def q_param : R_q := LaurentPolynomial.T 1
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **𝔰𝔲(2) basis data**: three generators e₁, e₂, e₃ with
    structure constants given by the Levi-Civita symbol. -/
-- Ref: [leitner2026] Chapter 4
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
-- Ref: [leitner2026] Chapter 4
structure Su2KillingForm (K : Type*) [CommRing K] [Invertible (2 : K)]
    extends Su2Basis where
  /-- The Killing form. Codomain a generic commutative ring in which `2`
      is invertible: the 𝔰𝔲(2) Killing form is q-independent, and its
      normalisation `-1/2` is not an element of `R_q = ℤ[q, q⁻¹]` but
      needs nothing beyond `⅟2` (so `ℚ` is one instance, not the
      requirement). -/
  killing : LieAlg → LieAlg → K
  /-- Normalisation: ⟨eₐ, eₐ⟩ = -1/2. -/
  normalised : ∀ a : Fin 3, killing (basis a) (basis a) = -⅟(2 : K)
  /-- Orthogonality: ⟨eₐ, e_b⟩ = 0 for a ≠ b. -/
  orthogonal : ∀ a b : Fin 3, a ≠ b → killing (basis a) (basis b) = 0

end QOU
