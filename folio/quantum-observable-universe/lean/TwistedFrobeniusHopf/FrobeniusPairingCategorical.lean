import Mathlib.CategoryTheory.Monoidal.Rigid.Basic

/-!
# The categorical half of the Frobenius-pairing claim

`QOU/FrobeniusHopfData/frobeniusForm.lean` states only that the Frobenius
pairing is **bijective**, because `FrobeniusFormContext` models `A` and `A^∨`
as plain `Type` — no category is in scope there, so the manuscript's
categorical side (the pairing induces an iso `A ≅ A^∨`, via the snake
identities with a coevaluation `η̃ : 𝟏 → A ⊗ A`) cannot be written against it.

That was recorded on 2026-09-07 as needing "the rigid-monoidal apparatus",
which was wrong: Mathlib carries `CategoryTheory.Monoidal.Rigid` at the pin.
This file is the correction made constructive.

**And the manuscript's non-degeneracy condition IS Mathlib's `ExactPairing`.**
That class asks for exactly what the manuscript asks for — a coevaluation and
an evaluation satisfying two triangle (snake) identities
(`Rigid/Basic.lean:73-87`). So the categorical half needs no new
infrastructure at all; it needed the right model.

## What is and is not claimed

`Nondegenerate` is stated over the pairing the data actually carries, so it is
not satisfiable by choosing a proposition — the failure mode that made the
`is_iso : Prop` field of `FrobeniusFormContext` assert nothing.
`exactPairing_of_nondegenerate` turns it into Mathlib's class, which is where
the downstream rigid-monoidal API lives.

This says nothing about the manuscript's *equivalence* with bijectivity: that
needs a faithful fibre functor `τ` reflecting isomorphisms, which is a further
step and is deliberately not asserted here.
-/

namespace QOU.FrobeniusHopfData

open CategoryTheory MonoidalCategory

universe v u

variable (C : Type u) [Category.{v} C] [MonoidalCategory C]

/-- Frobenius pairing data in a monoidal category: an object, a candidate
    dual, and the evaluation `A^∨ ⊗ A ⟶ 𝟏` induced by `∫_A ∘ μ`. -/
structure FrobeniusPairingData where
  /-- The algebra object `A`. -/
  obj : C
  /-- The candidate dual `A^∨`. -/
  dual : C
  /-- The Frobenius pairing as an evaluation morphism. -/
  eval : dual ⊗ obj ⟶ 𝟙_ C

variable {C}

/-- **Non-degeneracy of the Frobenius pairing.**  There is a coevaluation
    `η̃ : 𝟏 ⟶ A ⊗ A^∨` whose two snake composites with `d.eval` are the
    unitors — the manuscript's condition, written against the pairing `d`
    actually carries. -/
def FrobeniusPairingData.Nondegenerate (d : FrobeniusPairingData C) : Prop :=
  ∃ coev : 𝟙_ C ⟶ d.obj ⊗ d.dual,
    (d.dual ◁ coev ≫ (α_ _ _ _).inv ≫ d.eval ▷ d.dual
      = (ρ_ d.dual).hom ≫ (λ_ d.dual).inv) ∧
    (coev ▷ d.obj ≫ (α_ _ _ _).hom ≫ d.obj ◁ d.eval
      = (λ_ d.obj).hom ≫ (ρ_ d.obj).inv)

/-- A non-degenerate Frobenius pairing IS an exact pairing in Mathlib's
    sense, so the rigid-monoidal API applies to it. -/
theorem exactPairing_of_nondegenerate (d : FrobeniusPairingData C)
    (h : d.Nondegenerate) : Nonempty (ExactPairing d.obj d.dual) := by
  obtain ⟨coev, h₁, h₂⟩ := h
  exact ⟨{ coevaluation' := coev
           evaluation' := d.eval
           coevaluation_evaluation' := h₁
           evaluation_coevaluation' := h₂ }⟩

end QOU.FrobeniusHopfData
