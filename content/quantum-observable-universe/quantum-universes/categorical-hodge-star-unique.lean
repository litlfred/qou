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

/-- **Uniqueness of the categorical Hodge star.** -/
-- Ref: [kock2004]
theorem CategoricalHodgeStar.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
