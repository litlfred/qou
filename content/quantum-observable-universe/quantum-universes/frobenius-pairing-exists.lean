/-!
# QOU.FrobeniusHopfData.frobeniusForm_exists — existence of the Frobenius pairing

Every quantum universe admits a non-degenerate Frobenius pairing
⟨·,·⟩ = ∫_A ∘ μ : A ⊗ A → 𝟙.  Existence is immediate from the QU
data; non-degeneracy comes from the snake identities (rigid monoidal
structure of 𝐂 applied to the Frobenius object A).

LaTeX: `\label{prop:frobenius-pairing-exists}`

## References

- [manuscript] §1-quantum-universes/frobenius-pairing-exists
- [kock2004] Frobenius Algebras and 2D Topological Quantum Field
  Theories (Cambridge LMS 59), Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Existence of the non-degenerate Frobenius pairing.**

    Every `FrobeniusHopfData C` carries the data for a pairing
    ∫_A ∘ μ : A ⊗ A → 𝟙 satisfying the snake identities.  The
    statement records the existence of a `FrobeniusHopfData` instance
    on a quantum universe; the pairing itself is then definable as a
    term-level composition.

    Stub: witness would be provided by the QU's Frobenius-Hopf data,
    but constructing a non-trivial `FrobeniusHopfData` term on a
    specific `C` requires category-theoretic infrastructure not yet
    in `QOU.Basic`. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem FrobeniusHopfData.frobeniusForm_exists
    (C : Type*) [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] :
    Nonempty (FrobeniusHopfData C) := by
  -- Witness: the Frobenius-Hopf data on the QU object A.
  -- Ref: [kock2004] Ch 2
  sorry

end QOU
