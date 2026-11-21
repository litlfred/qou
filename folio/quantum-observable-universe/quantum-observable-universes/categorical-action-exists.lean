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

- [leitner2026] §2-quantum-observable-universes/categorical-action-exists
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

/-- **The categorical action of the identity is the bare pairing loop.**

    For the identity endomorphism the whiskered factor drops out, so
    `𝒮_{𝟙} = η_ ≫ swap ≫ ε_` — the categorical trace of `𝟙`, i.e. the
    categorical dimension of `A` relative to `swap`.

    **Why this statement and not "the action exists".** The previous form
    was `∃ S : 𝟙 ⟶ 𝟙, S = categoricalAction Φ swap`, discharged by
    `⟨categoricalAction Φ swap, rfl⟩`. Its own docstring conceded that
    *"'exists' and 'equals tr(Φ)' hold by construction"* — which is the
    point: `∃ S, S = e` is provable by `⟨e, rfl⟩` for any `e`, so it made
    no claim about `categoricalAction`. Existence of a named composite is
    not a theorem; the definition above already supplies it. This
    replacement is falsifiable — it would fail if whiskering by `𝟙` did
    not act as the identity. -/
-- Ref: [kelly1982]
theorem CategoricalAction.exists {A Ad : C} [ExactPairing A Ad]
    (swap : A ⊗ Ad ⟶ Ad ⊗ A) :
    categoricalAction (𝟙 A) swap = η_ A Ad ≫ swap ≫ ε_ A Ad := by
  unfold categoricalAction
  simp

end QOU
