import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.frobenius_relation — Frobenius relation

The Frobenius relation: sliding multiplication past comultiplication.
`(μ ⊗ id) ∘ (id ⊗ Δ) = Δ ∘ μ`

This is the defining compatibility between the algebra and coalgebra
structures of a Frobenius object.

LaTeX label: `prop:frobenius-relation`
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Frobenius relation** (categorical form).

    For a Frobenius–Hopf object `(A, μ, Δ)` in a monoidal category,
    the Frobenius relation states that the two morphisms
    `A ⊗ A → A ⊗ A` obtained by:

    (1) `(id ⊗ Δ) ≫ (α⁻¹) ≫ (μ ⊗ id)`, and
    (2) `μ ≫ Δ`

    are equal.  This is already part of the `FrobeniusHopfData` axioms
    (`frobenius_relation` field).

    LaTeX: `\label{prop:frobenius-relation}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
theorem frobenius_relation_holds {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (fh : FrobeniusHopfData C) :
    fh.mul ≫ fh.comul =
      (fh.comul ▷ fh.obj) ≫ (α_ fh.obj fh.obj fh.obj).hom ≫
      (fh.obj ◁ fh.mul) := by
  exact fh.frobenius_relation

/-- The Frobenius relation in "left" form:
    `(Δ ▷ A) ≫ α ≫ (A ◁ μ) = μ ≫ Δ`.

    This is the direct field from `FrobeniusHopfData`. -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
theorem frobenius_relation_left {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (fh : FrobeniusHopfData C) :
    (fh.comul ▷ fh.obj) ≫ (α_ fh.obj fh.obj fh.obj).hom ≫
      (fh.obj ◁ fh.mul) = fh.mul ≫ fh.comul := by
  exact fh.frobenius_relation.symm

end QOU
