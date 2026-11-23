import Mathlib.CategoryTheory.Monoidal.Rigid.Basic


/-!
# QOU.CategoricalAction.unique — uniqueness of the categorical action (given Φ)

For a fixed Lagrangian endomorphism `Φ : A ⟶ A` (with right dual `(A, Aᘁ)` and
transposition `swap`), the categorical action

  𝒮_Φ = η_ ≫ (Φ ▷ Aᘁ) ≫ swap ≫ ε_  =  tr(Φ)

does not depend on the choice of right dual: for two exact pairings
`(A, D₁)` and `(A, D₂)`, transporting `swap` along the canonical iso
`D₁ ≅ D₂` (`rightDualIso`) gives the same morphism `𝟙 ⟶ 𝟙`. This replaces a
statement of the form `S₁ = 𝒮_Φ → S₂ = 𝒮_Φ → S₁ = S₂`, which holds by
transitivity of equality and says nothing about `𝒮_Φ` (bean `qou-jy1r`,
owner card 2026-11-22). It is also *not* the
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

/-- Transport of the transposition `swap` along the canonical isomorphism
    `D₁ ≅ D₂` between two right duals of `A`. -/
-- Ref: [kelly1982]
def transportSwap {A D₁ D₂ : C} (p₁ : ExactPairing A D₁) (p₂ : ExactPairing A D₂)
    (swap : A ⊗ D₁ ⟶ D₁ ⊗ A) : A ⊗ D₂ ⟶ D₂ ⊗ A :=
  (A ◁ (rightDualIso p₁ p₂).inv) ≫ swap ≫ ((rightDualIso p₁ p₂).hom ▷ A)

/-- **Uniqueness of the categorical action (given Φ).**

    `𝒮_Φ` is independent of the choice of right dual of `A`: computing it
    with the pairing `(A, D₂)` and the transported `swap` gives the same
    morphism `𝟙 ⟶ 𝟙` as computing it with `(A, D₁)` and `swap`. Since right
    duals are unique up to the canonical iso `rightDualIso`, `𝒮_Φ` is
    determined by `Φ` and `swap` alone.

    Proof: the coevaluations and evaluations of the two pairings are related
    by that iso (`coevaluation_comp_rightAdjointMate`,
    `rightAdjointMate_comp_evaluation` at `f = 𝟙 A`), and `Φ ▷ _` commutes
    past `A ◁ _` by the interchange law. -/
-- Ref: [kelly1982]
theorem CategoricalAction.unique {A D₁ D₂ : C} (p₁ : ExactPairing A D₁)
    (p₂ : ExactPairing A D₂) (Φ : A ⟶ A) (swap : A ⊗ D₁ ⟶ D₁ ⊗ A) :
    @categoricalAction C _ _ A D₂ p₂ Φ (transportSwap p₁ p₂ swap) =
      @categoricalAction C _ _ A D₁ p₁ Φ swap := by
  have hη : @ExactPairing.coevaluation C _ _ A D₁ p₁ ≫ A ◁ (rightDualIso p₁ p₂).hom =
      @ExactPairing.coevaluation C _ _ A D₂ p₂ := by
    have := @coevaluation_comp_rightAdjointMate C _ _ A A ⟨D₂⟩ ⟨D₁⟩ (𝟙 A)
    simpa [rightDualIso] using this
  have hε : (rightDualIso p₁ p₂).hom ▷ A ≫ @ExactPairing.evaluation C _ _ A D₂ p₂ =
      @ExactPairing.evaluation C _ _ A D₁ p₁ := by
    have := @rightAdjointMate_comp_evaluation C _ _ A A ⟨D₂⟩ ⟨D₁⟩ (𝟙 A)
    simpa [rightDualIso] using this
  unfold categoricalAction transportSwap
  rw [← hη, ← hε]
  simp only [Category.assoc]
  rw [← whisker_exchange_assoc]
  simp

end QOU
