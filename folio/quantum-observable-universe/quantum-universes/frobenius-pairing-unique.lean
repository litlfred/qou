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
`Hom(A, 𝟙)` for simple `A`, [kock2004] Ch 2).  It is proved here as
`frobeniusForm_unique_of_schur`, under the Schur hypotheses it needs
(preadditive with kernels, monoidal-preadditive, simple unit). A former
named axiom stating it without those hypotheses had no Lean consumer
and was deleted on owner approval, 2026-11-23.  `FrobeniusHopfData` is imported here from the `QOU`
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

    Whether the statement holds without these hypotheses (no linear
    structure, no simplicity of `𝟙`) is open (bean `qou-n2un`); the former
    axiom asserting that was deleted on owner approval, 2026-11-23. -/
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

end QOU
