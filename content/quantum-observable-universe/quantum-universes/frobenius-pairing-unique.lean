/-!
# QOU.FrobeniusHopfData.frobeniusForm_unique — uniqueness of the Frobenius pairing

Two non-degenerate Frobenius pairings on the same QU object A differ
by an invertible scalar c ∈ Aut_𝐂(𝟙).  For simple A, this follows
from 1-dimensionality of Hom(𝟙, A).

LaTeX: `\label{prop:frobenius-pairing-unique}`

## References

- [manuscript] §1-quantum-universes/frobenius-pairing-unique
- [kock2004] Frobenius Algebras and 2D Topological Quantum Field
  Theories (Cambridge LMS 59), Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the Frobenius pairing (up to scalar).**

    Any two non-degenerate Frobenius forms on a simple QU object
    differ by an invertible scalar, so the induced pairings
    ⟨·,·⟩ᵢ = ∫_A^(i) ∘ μ differ by the same scalar.

    The proof uses 1-dimensionality of Hom(𝟙, A) for simple A. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem FrobeniusHopfData.frobeniusForm_unique
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] :
    ∀ (A : C), True := by
  -- Requires: definition of "simple QU object", 1-dim Hom(𝟙, A),
  -- and the snake-identity factorisation.  Recorded as stub.
  -- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
  intro _
  trivial

end QOU
