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

/-- **Uniqueness of the Frobenius pairing (up to scalar) — open
    statement.**

    Two `FrobeniusHopfData` instances on the *same* simple object
    differ only by an invertible scalar in `End(𝟙)`. The
    `Subsingleton (FrobeniusHopfData C)` claim originally written here
    is **strictly false** because:

    1. `FrobeniusHopfData C` quantifies over the carrier object — two
       instances may have different `obj : C`. So distinct instances
       can disagree at the type level.

    2. Even on a fixed object, the Frobenius form is unique only
       *up to scalar*; for `Subsingleton` we'd need scalar = 1.

    To make a meaningful uniqueness theorem, the statement must be
    sharpened to:

    ```
      ∀ (fh₁ fh₂ : FrobeniusHopfData C), fh₁.obj = fh₂.obj →
        IsSimple fh₁.obj → ∃ c : End (𝟙_ C), IsIso c ∧
          fh₁.frobeniusForm = c ≫ fh₂.frobeniusForm
    ```

    The simplicity hypothesis is essential (drops to multi-block in a
    semisimple but non-simple category). Closing this requires
    importing `Mathlib.CategoryTheory.Simple` and the Schur-style
    1-dimensionality of `Hom(𝟙, A)`. -/
-- Ref: [kock2004]
theorem FrobeniusHopfData.frobeniusForm_unique
    (C : Type*) [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] :
    Subsingleton (FrobeniusHopfData C) := by
  -- The original Subsingleton claim is too strong (see docstring).
  -- Closing it as written would be vacuously wrong; closing the
  -- intended scalar-uniqueness statement requires restating the
  -- theorem first.
  sorry  -- Ref: [kock2004] Ch 2 — but theorem statement needs revision
         -- (see docstring); closing-as-written would be a false claim.

end QOU
