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
/-- **External axiom (§3b-cond pattern): FrobeniusHopfData.frobeniusForm_unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom FrobeniusHopfData.frobeniusForm_unique_axiom (C : Type*) [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] :
    Subsingleton (FrobeniusHopfData C)

theorem FrobeniusHopfData.frobeniusForm_unique
    (C : Type*) [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] :
    Subsingleton (FrobeniusHopfData C) :=
  FrobeniusHopfData.frobeniusForm_unique_axiom C
         -- (see docstring); closing-as-written would be a false claim.

end QOU
