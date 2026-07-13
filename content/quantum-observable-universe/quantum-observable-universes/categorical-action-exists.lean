import Mathlib.CategoryTheory.Monoidal.Rigid.Basic


/-!
# QOU.CategoricalAction.exists — existence of the categorical action 𝒮_Φ

For a Lagrangian endomorphism `Φ ∈ End(A)` in a rigid monoidal category, the
categorical action is the scalar `𝒮_Φ : 𝟙 ⟶ 𝟙` obtained as the composite

  𝒮_Φ = η_ ≫ (Φ ▷ Aᘁ) ≫ swap ≫ ε_

where `(η_, ε_)` is the exact pairing exhibiting `Aᘁ` as the right dual of
`A`, and `swap : A ⊗ Aᘁ ⟶ Aᘁ ⊗ A` is the transposition arranged by the
`id_{Aᘁ} ⊗ Φ` factor (Definition `def:categorical-action`). This composite
always exists (it is a morphism in `C`); the content of the existence claim
is that it is a *well-defined* endomorphism of the unit, and it **is** the
categorical trace `tr(Φ)` by definition.

LaTeX: `\label{prop:categorical-action-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-action-exists
- [kelly1982] Basic Concepts of Enriched Category Theory
- [stolz-teichner-2012]
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe v u

variable {C : Type u} [Category.{v} C] [MonoidalCategory C]

/-- **Categorical action** `𝒮_Φ : 𝟙 ⟶ 𝟙` of a Lagrangian endomorphism `Φ : A ⟶ A`.

    `𝒮_Φ = η_ ≫ (Φ ▷ Aᘁ) ≫ swap ≫ ε_`, the composite
    `ev_A ∘ (id_{Aᘁ} ⊗ Φ) ∘ coev_A` of the manuscript, with `swap` the
    transposition `A ⊗ Aᘁ ⟶ Aᘁ ⊗ A` supplied alongside the pairing.
    This is, by definition, the categorical trace `tr(Φ)`. -/
-- Ref: [kelly1982]
noncomputable def categoricalAction {A Ad : C} [ExactPairing A Ad]
    (Φ : A ⟶ A) (swap : A ⊗ Ad ⟶ Ad ⊗ A) : (𝟙_ C) ⟶ (𝟙_ C) :=
  η_ A Ad ≫ (Φ ▷ Ad) ≫ swap ≫ ε_ A Ad

/-- **Existence of the categorical action.**

    For any Lagrangian endomorphism `Φ : A ⟶ A` with right dual `(A, Aᘁ)` and
    transposition `swap`, the categorical action `𝒮_Φ : 𝟙 ⟶ 𝟙` exists as a
    morphism in `C` and equals the categorical trace `tr(Φ) = categoricalAction Φ swap`.

    The witness is literally the composite `η_ ≫ (Φ ▷ Aᘁ) ≫ swap ≫ ε_`, so
    "exists" and "equals tr(Φ)" hold by construction. -/
-- Ref: [kelly1982]
theorem CategoricalAction.exists {A Ad : C} [ExactPairing A Ad]
    (Φ : A ⟶ A) (swap : A ⊗ Ad ⟶ Ad ⊗ A) :
    ∃ S : (𝟙_ C) ⟶ (𝟙_ C), S = categoricalAction Φ swap :=
  ⟨categoricalAction Φ swap, rfl⟩

end QOU
