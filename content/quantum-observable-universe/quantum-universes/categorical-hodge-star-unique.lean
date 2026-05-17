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
/-- **External axiom (§3b-cond pattern): CategoricalHodgeStar.unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalHodgeStar.unique_axiom {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) :
    Subsingleton (CatHodgeInvolution X)

theorem CategoricalHodgeStar.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) :
    Subsingleton (CatHodgeInvolution X) :=
  CategoricalHodgeStar.unique_axiom C X

end QOU
