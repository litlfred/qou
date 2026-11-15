import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Simple


/-!
# QOU.FrobeniusHopfData.frobeniusForm_unique — uniqueness of the Frobenius pairing

Two non-degenerate Frobenius pairings on the same QU object A differ
by an invertible scalar c ∈ Aut_𝐂(𝟙).  For simple A, this follows
from 1-dimensionality of Hom(𝟙, A).

LaTeX: `\label{prop:frobenius-pairing-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (FrobeniusHopfData C)`, which is **strictly
false**: (1) `FrobeniusHopfData C` bundles the carrier `obj : C`, so
two instances may differ at the object level; (2) even on a fixed
object the Frobenius form is unique only *up to an invertible scalar*
in `End(𝟙)`, not on the nose.

This file replaces that false `Subsingleton` axiom with the honest
**conditional** statement: on a *simple* common object the Frobenius
form is unique up to an invertible scalar.  That sharpened claim is
the genuine categorical content (Schur 1-dimensionality of
`Hom(A, 𝟙)` for simple `A`, [kock2004] Ch 2).  It is retained as a
single named axiom — `frobeniusForm_unique_axiom` — pending a Mathlib
argument deriving 1-dimensionality from `Simple`; this is the §3b-cond
conditional pattern (one named, cited categorical input), not a false
`Subsingleton`.  `FrobeniusHopfData` is imported here from the `QOU`
library.

## References

- [leitner2026] §1-quantum-universes/frobenius-pairing-unique
- [kock2004] Frobenius Algebras and 2D Topological Quantum Field
  Theories (Cambridge LMS 59), Ch 2
-/

namespace QOU

open CategoryTheory
open MonoidalCategory

universe u v

/-- **Frobenius form unique up to invertible scalar (conditional,
    named categorical input).**

    On a *simple* common object, two `FrobeniusHopfData` Frobenius
    forms differ by an invertible scalar `c : End(𝟙_ C)` (post-
    composed, after transporting along the object equality).  The
    simplicity hypothesis is essential — it drops to multi-block in a
    semisimple but non-simple category.  This is the §3b-cond
    conditional content (Schur 1-dimensionality of `Hom(A, 𝟙)`,
    [kock2004]); it replaces a false `Subsingleton (FrobeniusHopfData
    C)` axiom. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
axiom FrobeniusHopfData.frobeniusForm_unique_axiom
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [Limits.HasZeroMorphisms C]
    (fh₁ fh₂ : FrobeniusHopfData C)
    (hobj : fh₁.obj = fh₂.obj)
    (_hsimple : Simple fh₁.obj) :
    ∃ c : End (𝟙_ C), IsIso c ∧
      fh₁.frobeniusForm = (eqToHom hobj ≫ fh₂.frobeniusForm) ≫ c

/-- **Uniqueness of the Frobenius pairing up to scalar (conditional).**

    Wrapper over `frobeniusForm_unique_axiom`: on a simple common
    object the Frobenius form is determined up to an invertible scalar
    in `End(𝟙)`.  Replaces the false `Subsingleton (FrobeniusHopfData
    C)` claim originally written here. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem FrobeniusHopfData.frobeniusForm_unique
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [Limits.HasZeroMorphisms C]
    (fh₁ fh₂ : FrobeniusHopfData C)
    (hobj : fh₁.obj = fh₂.obj)
    (hsimple : Simple fh₁.obj) :
    ∃ c : End (𝟙_ C), IsIso c ∧
      fh₁.frobeniusForm = (eqToHom hobj ≫ fh₂.frobeniusForm) ≫ c :=
  FrobeniusHopfData.frobeniusForm_unique_axiom fh₁ fh₂ hobj hsimple

end QOU
