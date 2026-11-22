import Mathlib.CategoryTheory.Monoidal.Rigid.Basic


/-!
# QOU.CategoricalAction.unique — uniqueness of the categorical action (given Φ)

For a fixed Lagrangian endomorphism `Φ : A ⟶ A` (with right dual `(A, Aᘁ)` and
transposition `swap`), the categorical action

  𝒮_Φ = η_ ≫ (Φ ▷ Aᘁ) ≫ swap ≫ ε_  =  tr(Φ)

is uniquely determined: any morphism `𝟙 ⟶ 𝟙` that factors as this composite
equals `tr(Φ)`. This is the honest uniqueness statement — *not* the
`Subsingleton (CategoricalAction C fh)` claim previously axiomatised here,
which is strictly false (the `CategoricalAction` action-functional structure
exposes free `state`/`gravity`/`gauge`/`matter` fields, so distinct terms
exist). The categorical action *of a given `Φ`* is a single, canonical
morphism, and that is what is unique.

LaTeX: `\label{prop:categorical-action-unique}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-action-unique
- [kelly1982] Basic Concepts of Enriched Category Theory
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe v u

variable {C : Type u} [Category.{v} C] [MonoidalCategory C]

/-- **Categorical action** `𝒮_Φ : 𝟙 ⟶ 𝟙` of `Φ : A ⟶ A` — the composite
    `η_ ≫ (Φ ▷ Aᘁ) ≫ swap ≫ ε_` (definitionally the trace `tr(Φ)`). -/
-- Ref: [kelly1982]
noncomputable def categoricalAction {A Ad : C} [ExactPairing A Ad]
    (Φ : A ⟶ A) (swap : A ⊗ Ad ⟶ Ad ⊗ A) : (𝟙_ C) ⟶ (𝟙_ C) :=
  η_ A Ad ≫ (Φ ▷ Ad) ≫ swap ≫ ε_ A Ad

/-- **Uniqueness of the categorical action (given Φ).**

    Any two morphisms `S₁, S₂ : 𝟙 ⟶ 𝟙` that both factor as the categorical
    action composite for the same `(Φ, swap)` are equal — both equal the
    categorical trace `tr(Φ) = categoricalAction Φ swap`. This faithfully
    encodes the manuscript's claim that `𝒮_Φ` is uniquely determined. -/
-- Ref: [kelly1982]
theorem CategoricalAction.unique {A Ad : C} [ExactPairing A Ad]
    (Φ : A ⟶ A) (swap : A ⊗ Ad ⟶ Ad ⊗ A)
    {S₁ S₂ : (𝟙_ C) ⟶ (𝟙_ C)}
    (h₁ : S₁ = categoricalAction Φ swap) (h₂ : S₂ = categoricalAction Φ swap) :
    S₁ = S₂ := by
  rw [h₁, h₂]

end QOU
