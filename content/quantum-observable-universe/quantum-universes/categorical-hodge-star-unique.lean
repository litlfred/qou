/-!
# QOU.CategoricalHodgeStar.unique — uniqueness of the categorical Hodge star

Given ∫_A and vol, ⋆ is uniquely determined by the wedge pairing
non-degeneracy.

LaTeX: `\label{prop:categorical-hodge-star-unique}`

## References

- [manuscript] §1-quantum-universes/categorical-hodge-star-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Hodge star.**

    On a fixed object `X`, two `CatHodgeInvolution X` terms with the
    same Frobenius pairing + volume form coincide. -/
-- Ref: [kock2004]
theorem CategoricalHodgeStar.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) :
    Subsingleton (CatHodgeInvolution X) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  -- Ref: [kock2004]
  sorry

end QOU
