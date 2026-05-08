/-!
# QOU.Descartes.baryonProductFromAlt — Alt-isotype identification of the baryon integrand

The product `∏_k dc_k/dz` of color-tube prolongations equals the
projection of `(dc_1/dz) ⊗ (dc_2/dz) ⊗ (dc_3/dz)` onto the sign
isotype of `R[S_3]`.  This is purely algebraic — it lives over the
categorical base ring `R` and does not invoke the archimedean
embedding `R ↪ ℂ`.

LaTeX label: `prop:baryon-product-from-alt`

## References

- [fulton1991] Representation Theory: A First Course, §2 (Frobenius character formula).
- [macdonald1995] Symmetric Functions and Hall Polynomials, §I.2.
- [manuscript] §6/baryon-product-from-alt

## Witness

- [baryon-product-from-alt.witness.json](../../../folio-assistant/computations/baryon-product-from-alt.witness.json)
  — pointwise + thimble-period numerical certificate of the Alt^3
  isotype identification.
-/

import Mathlib.Data.Real.Basic
import Mathlib.GroupTheory.Perm.Sign

namespace QOU.Descartes

/-- The sign character `sgn : S_3 → ℤ`, viewed as the character of
    the alternating representation `Alt^3`. -/
-- Ref: [fulton1991] §2.1 (Frobenius character of the sign representation)
def signCharacter (σ : Equiv.Perm (Fin 3)) : ℤ :=
  Equiv.Perm.sign σ

/-- The sign character takes only the values `±1`. -/
-- Ref: [fulton1991] §2.1
lemma signCharacter_eq_one_or_neg_one (σ : Equiv.Perm (Fin 3)) :
    signCharacter σ = 1 ∨ signCharacter σ = -1 := by
  unfold signCharacter
  rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;>
    simp [h]

/-- The sign character is a group homomorphism: `sgn(σ τ) = sgn(σ) sgn(τ)`. -/
-- Ref: [fulton1991] §2.1
lemma signCharacter_mul (σ τ : Equiv.Perm (Fin 3)) :
    signCharacter (σ * τ) = signCharacter σ * signCharacter τ := by
  unfold signCharacter
  push_cast
  rw [map_mul]

/-- The sign character of the identity is `1`. -/
-- Ref: [fulton1991] §2.1
lemma signCharacter_one : signCharacter (1 : Equiv.Perm (Fin 3)) = 1 := by
  unfold signCharacter
  simp

/-- **Proposition: the baryon integrand is the Alt-isotype.**
    The product `∏_k dc_k/dz` of three colour-sheet velocities is the
    Frobenius–character projection of the rank-3 tensor onto the sign
    representation of `S_3`, equivalently the wedge product
    `(dc_1/dz) ∧ (dc_2/dz) ∧ (dc_3/dz)` in `Λ^3 V` after the
    canonical isomorphism `Λ^3 V ≅ R`.

    Statement-level only; the categorical proof (Frobenius character
    formula + diagonal-Jacobian reduction + Vandermonde discriminant)
    is given in `baryon-product-from-alt.md`.

    The `True` payload is a deliberate placeholder until the
    GB / fibre-functor infrastructure is formalised in Mathlib;
    the conditional-correctness chain is recorded in the `.md` sibling
    and in `proof-objects.json`. -/
-- Ref: [fulton1991] §2 (Frobenius character formula, sign-isotype projection)
-- Ref: [macdonald1995] §I.2 (Vandermonde discriminant identity)
-- Ref: [manuscript] https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/descartes-universe/baryon-product-from-alt.md
theorem baryonProductFromAlt :
    ∀ (sign_isotype_projection : True),
      -- The S_3-sign-isotype projection of the rank-3 colour-velocity
      -- tensor equals the determinantal product ∏_k dc_k/dz, an
      -- R-rational quantity computable without reference to ℂ.
      sign_isotype_projection := by
  intro h; exact h

end QOU.Descartes
