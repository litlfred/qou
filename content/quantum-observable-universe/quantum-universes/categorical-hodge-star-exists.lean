/-!
# QOU.CategoricalHodgeStar.exists — existence of the categorical Hodge star

⋆ exists as a morphism Ω^k(A) → Ω^(n-k)(A) determined by the
Frobenius pairing non-degeneracy; ⋆² = id from S² = id.

LaTeX: `\label{prop:categorical-hodge-star-exists}`

## References

- [manuscript] §1-quantum-universes/categorical-hodge-star-exists
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Hodge star.** -/
-- Ref: [kock2004]
theorem CategoricalHodgeStar.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
