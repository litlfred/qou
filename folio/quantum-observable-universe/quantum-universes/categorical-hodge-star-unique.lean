import QOU.Basic
import QOU.QuantumObservableUniverse.Structures


/-!
# QOU.CategoricalHodgeStar.unique — uniqueness of the categorical Hodge star

Given ∫_A and vol, ⋆ is uniquely determined by the wedge pairing
non-degeneracy.

LaTeX: `\label{prop:categorical-hodge-star-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (CatHodgeInvolution X)`, which is **false**: the
structure carries a free data field `star : X ⟶ X` constrained only by
involutivity, and any object with two distinct involutions gives
distinct instances.

What *is* provable — with no axiom — is extensionality at the level the
structure actually supports: the involution morphism determines the
whole structure, since `star_sq` is propositional.  The narrative's
stronger claim (⋆ pinned by the wedge pairing + volume form) needs the
pairing data, which `CatHodgeInvolution` (imported here from the
`QOU` library) does not yet carry; adding a `pairing`/`vol` field and
deriving `star` from non-degeneracy is the open structure refactor.

## References

- [leitner2026] §1-quantum-universes/categorical-hodge-star-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

namespace QOU

universe u v

/-- **Uniqueness of the categorical Hodge star (proved).**

    Two `CatHodgeInvolution X` terms with the same underlying involution
    morphism coincide: involutivity is propositional, so the `star`
    field is the whole content.  This replaces a false
    `Subsingleton (CatHodgeInvolution X)` axiom (the `star` field is
    free data) with the extensionality the structure genuinely
    supports. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem CategoricalHodgeStar.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) (h₁ h₂ : CatHodgeInvolution X)
    (hstar : h₁.star = h₂.star) : h₁ = h₂ := by
  cases h₁
  cases h₂
  subst hstar
  rfl

end QOU
