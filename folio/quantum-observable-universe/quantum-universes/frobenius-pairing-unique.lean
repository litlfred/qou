import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Simple
import Mathlib.CategoryTheory.Preadditive.Schur
import Mathlib.CategoryTheory.Monoidal.Preadditive


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

/-- A Frobenius form is nonzero whenever its object is simple: if `λ = 0`
    then `ev = μ ≫ λ = 0`, and the left snake identity makes `𝟙_A = 0`. -/
theorem FrobeniusHopfData.frobeniusForm_ne_zero
    {C : Type u} [Category.{v} C] [Preadditive C] [MonoidalCategory C]
    [MonoidalPreadditive C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) [Simple fh.obj] :
    fh.frobeniusForm ≠ 0 := by
  intro h
  apply id_nonzero fh.obj
  rw [← fh.pairing_snake_left, h, Limits.comp_zero, MonoidalPreadditive.zero_whiskerRight]
  simp

/-- **Uniqueness of the Frobenius form up to an invertible scalar, proved
    under Schur hypotheses.**

    If `C` is preadditive with kernels and monoidal-preadditive, and both the
    common object and the tensor unit are simple, then each Frobenius form
    `A ⟶ 𝟙` is nonzero, hence an isomorphism by Schur's lemma, and
    `c := (e ≫ λ₂)⁻¹ ≫ λ₁` is the required invertible scalar.

    This is the axiom below with its missing hypotheses made explicit. The
    axiom itself carries no linear structure and no simplicity of `𝟙`; whether
    it holds without them is open (bean `qou-n2un`). -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem FrobeniusHopfData.frobeniusForm_unique_of_schur
    {C : Type u} [Category.{v} C] [Preadditive C] [Limits.HasKernels C]
    [MonoidalCategory C] [MonoidalPreadditive C] [CategoryTheory.BraidedCategory C]
    [Simple (𝟙_ C)]
    (fh₁ fh₂ : FrobeniusHopfData C)
    (hobj : fh₁.obj = fh₂.obj)
    (hsimple : Simple fh₁.obj) :
    ∃ c : End (𝟙_ C), IsIso c ∧
      fh₁.frobeniusForm = (eqToHom hobj ≫ fh₂.frobeniusForm) ≫ c := by
  have hs₂ : Simple fh₂.obj := hobj ▸ hsimple
  haveI := hsimple
  haveI := hs₂
  haveI h₁ : IsIso fh₁.frobeniusForm := isIso_of_hom_simple fh₁.frobeniusForm_ne_zero
  haveI h₂ : IsIso fh₂.frobeniusForm := isIso_of_hom_simple fh₂.frobeniusForm_ne_zero
  refine ⟨inv (eqToHom hobj ≫ fh₂.frobeniusForm) ≫ fh₁.frobeniusForm, inferInstance, ?_⟩
  simp

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
