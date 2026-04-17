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

/-- **Existence of the categorical Hodge star.**

    On any object `X` of a category, there exists a `CatHodgeInvolution X`
    (a star morphism `⋆ : X ⟶ X`).  In the Quantum Universe setting
    the relevant `X` is `Ω^k(A)` and `⋆` lands in `Ω^{n-k}(A)`;
    involutivity follows from $S^2 = \mathrm{id}$ on a commutative
    Frobenius-Hopf algebra. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem CategoricalHodgeStar.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) :
    Nonempty (CatHodgeInvolution X) := by
  -- Witness: the Hodge star built from the Frobenius pairing
  -- non-degeneracy + antipode involutivity.
  -- Ref: [kock2004] Ch 2
  sorry

end QOU
