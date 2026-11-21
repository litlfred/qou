import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Frobenius self-pairing chirality factor

For a self-dual Frobenius algebra `(A, τ)` with antipode
`star : A → A` (the anti-involution `σ_i ↦ σ_i⁻¹`, reverse word
order), the **chirality factor** of a braid word `β ∈ A` is the
normalised Frobenius self-pairing

```
a_K(β) := τ(β · star β) / τ(1 · 1).
```

This is the normalised Frobenius norm of `β` in the self-dual
pairing. The definition is categorical (monoidal-category
self-duality) and universal: it applies to any unital ring `A`
equipped with a trace `τ : A → R` and an antipode `star : A → A`.

-- Ref: [leitner2026] def:frobenius-self-pairing-chirality
-- Ref: [jones1987] V.F.R. Jones, "Hecke algebra representations of braid groups and link polynomials," Ann. of Math. 126 (1987)
-/

namespace QOU.BraidKnot

variable {A : Type*} {R : Type*} [Ring A] [DivisionRing R]

/-- The **Frobenius self-pairing chirality factor** of `β ∈ A` with
respect to a trace `τ : A → R` and an antipode `star : A → A`:
`a_K(β) = τ(β · star β) / τ(1 · 1)`. -/
noncomputable def chiralityFactor
    (τ : A → R) (star : A → A) (β : A) : R :=
  τ (β * star β) / τ ((1 : A) * (1 : A))

/-- The chirality factor of the identity braid is `1` whenever the
self-pairing of `1` is non-degenerate (`star 1 = 1` and
`τ (1 * 1) ≠ 0`). -/
theorem chiralityFactor_one
    (τ : A → R) (star : A → A)
    (hstar : star (1 : A) = 1) (hτ : τ ((1 : A) * (1 : A)) ≠ 0) :
    chiralityFactor τ star (1 : A) = 1 := by
  unfold chiralityFactor
  rw [hstar]
  exact div_self hτ

end QOU.BraidKnot
