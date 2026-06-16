import Mathlib.Data.Real.Basic
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Tactic.Ring


/-!
# QOU.Archimedean.baryonProductFromAlt — Alt-isotype identification of the baryon integrand

The product `∏_k dc_k/dz` of the three colour-tube prolongations equals the
projection of `(dc_1/dz) ⊗ (dc_2/dz) ⊗ (dc_3/dz)` onto the sign isotype of
`R[S_3]`.  In determinantal form this is the `3×3` Vandermonde determinant in the
colour-sheet velocities, which factors as the discriminant product.  This is
purely algebraic — it lives over the categorical base ring `R` and does not
invoke the archimedean embedding `R ↪ ℂ`.

LaTeX label: `prop:baryon-product-from-alt`

## References

- [fulton-harris1991] Representation Theory: A First Course, §2 (Frobenius character formula).
- [macdonald1995] Symmetric Functions and Hall Polynomials, §I.2.
- [manuscript] §6/baryon-product-from-alt

## Witness

- [baryon-product-from-alt.witness.json](../../../computations/baryon-product-from-alt.witness.json)
  — pointwise + thimble-period numerical certificate of the Alt^3
  isotype identification.
-/

namespace QOU.Archimedean

/-- The sign character `sgn : S_3 → ℤ`, viewed as the character of
    the alternating representation `Alt^3`. -/
-- Ref: [fulton-harris1991] §2.1 (Frobenius character of the sign representation)
def signCharacter (σ : Equiv.Perm (Fin 3)) : ℤ :=
  Equiv.Perm.sign σ

/-- The sign character takes only the values `±1`. -/
-- Ref: [fulton-harris1991] §2.1
lemma signCharacter_eq_one_or_neg_one (σ : Equiv.Perm (Fin 3)) :
    signCharacter σ = 1 ∨ signCharacter σ = -1 := by
  unfold signCharacter
  rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;>
    simp [h]

/-- The sign character is a group homomorphism: `sgn(σ τ) = sgn(σ) sgn(τ)`. -/
-- Ref: [fulton-harris1991] §2.1
lemma signCharacter_mul (σ τ : Equiv.Perm (Fin 3)) :
    signCharacter (σ * τ) = signCharacter σ * signCharacter τ := by
  unfold signCharacter
  rw [map_mul, Units.val_mul]

/-- The sign character of the identity is `1`. -/
-- Ref: [fulton-harris1991] §2.1
lemma signCharacter_one : signCharacter (1 : Equiv.Perm (Fin 3)) = 1 := by
  unfold signCharacter
  simp

/-- **The baryon integrand is the Alt-isotype (Vandermonde discriminant).**

    The `S_3`-sign-isotype projection of the rank-3 colour-velocity tensor is the
    signed permutation sum `Σ_{σ ∈ S_3} sgn(σ) ∏_i a_{σ(i)}^{\,i}`, which is the
    cofactor (Laplace) expansion of the `3×3` Vandermonde determinant in the
    colour-sheet velocities `(a, b, c)`:

      `(b·c² − c·b²) − a·(c² − b²) + a²·(c − b)`

    (the three signed `2×2` minors along the first column).  It factors as the
    discriminant product `(b − a)(c − a)(c − b)` — an `R`-rational quantity
    computable without reference to the archimedean embedding `R ↪ ℂ`.

    The non-vanishing of the discriminant for distinct `(a, b, c)` selects the
    sign isotype `Alt^3` (rather than `Sym^3`) as the baryon channel — the
    statement made categorically in `baryon-product-from-alt.md`. -/
-- Ref: [fulton-harris1991] §2 (Frobenius character formula, sign-isotype projection)
-- Ref: [macdonald1995] §I.2 (Vandermonde discriminant identity)
-- Ref: [manuscript] https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/predicted-spectra/baryon-product-from-alt.md
theorem baryonProductFromAlt (a b c : ℝ) :
    (b * c ^ 2 - c * b ^ 2) - a * (c ^ 2 - b ^ 2) + a ^ 2 * (c - b)
      = (b - a) * (c - a) * (c - b) := by
  ring

end QOU.Archimedean
