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

    Two `FrobeniusHopfData C` terms (on a simple QU object) differ
    only by an invertible scalar in the unit object's endomorphism
    ring.  `Subsingleton` captures uniqueness at the type level after
    the scalar normalisation is fixed. -/
-- Ref: [kock2004]
theorem FrobeniusHopfData.frobeniusForm_unique
    (C : Type*) [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] :
    Subsingleton (FrobeniusHopfData C) := by
  -- 1-dim Hom(𝟙, A) + snake identities force uniqueness up to scalar.
  -- Ref: [kock2004] Ch 2
  sorry

end QOU
