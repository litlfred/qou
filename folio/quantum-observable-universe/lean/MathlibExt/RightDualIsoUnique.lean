/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic

/-!
# QOU.MathlibExt.RightDualIsoUnique — uniqueness of the right-dual comparison

Mathlib defines `CategoryTheory.rightDualIso`, the canonical comparison between two right duals of
the same object, and then proves exactly one thing about it: `rightDualIso_id`.  Anything that
needs to *identify* a map as the comparison, or to compose two comparisons, has to re-derive the
characterisation first.

This file supplies that characterisation and its two immediate consequences:

* `rightDualIso_hom_evaluation` — the comparison is compatible with the evaluations;
* `rightDualIso_hom_unique` — and it is the **only** map that is, so exhibiting any map with that
  property identifies it;
* `rightDualIso_hom_trans` — comparisons compose.

The engine is `whiskerRight_evaluation_injective`: pairing against an evaluation is injective,
because `tensorRightHomEquiv` carries `g ↦ (g ▷ Y') ≫ ε` to `g ≫ (λ_ Y).inv`, and a unitor is a
mono.  That is the snake identity doing its job, with the morphism carried out of the way by the
adjunction rather than by a string-diagram argument.

Nothing here needs a braiding, and nothing needs rigidity beyond the exact pairings named in each
statement — which is why these live in their own file rather than alongside the pivotal structures
that first motivated them.
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory

variable {C : Type*} [Category C] [MonoidalCategory C]

/-- Pairing a morphism against the evaluation is, under `tensorRightHomEquiv`, the morphism itself
(up to a unitor).  The snake identity, with the morphism carried out of the way by
`whisker_exchange`. -/
theorem tensorRightHomEquiv_whiskerRight_evaluation {X Y Y' : C} (g : X ⟶ Y) [ExactPairing Y' Y] :
    (tensorRightHomEquiv X Y' Y (𝟙_ C)) ((g ▷ Y') ≫ ε_ Y' Y) = g ≫ (λ_ Y).inv := by
  simp only [tensorRightHomEquiv, Equiv.coe_fn_mk]
  calc _ = 𝟙 X ⊗≫ (X ◁ η_ Y' Y ≫ g ▷ (Y' ⊗ Y)) ⊗≫ ε_ Y' Y ▷ Y ⊗≫ 𝟙 _ := by monoidal
    _ = 𝟙 X ⊗≫ (g ▷ 𝟙_ C ≫ Y ◁ η_ Y' Y) ⊗≫ ε_ Y' Y ▷ Y ⊗≫ 𝟙 _ := by rw [whisker_exchange]
    _ = g ⊗≫ (Y ◁ η_ Y' Y ⊗≫ ε_ Y' Y ▷ Y) ⊗≫ 𝟙 _ := by monoidal
    _ = _ := by rw [ExactPairing.coevaluation_evaluation'']; monoidal

/-- **Pairing against the evaluation is injective.**  This is what makes a mate identifiable from
the identity it satisfies, and is the cancellation step in `swap_mate_mate`. -/
theorem whiskerRight_evaluation_injective {X Y Y' : C} [ExactPairing Y' Y] :
    Function.Injective (fun g : X ⟶ Y => (g ▷ Y') ≫ ε_ Y' Y) := by
  intro a b hab
  have h := congrArg (tensorRightHomEquiv X Y' Y (𝟙_ C)) hab
  rw [tensorRightHomEquiv_whiskerRight_evaluation, tensorRightHomEquiv_whiskerRight_evaluation] at h
  exact (cancel_mono _).mp h

/-- **The evaluation identity that characterises `rightDualIso`.**  `rightAdjointMate` of the
identity, read through `rightAdjointMate_comp_evaluation`. -/
theorem rightDualIso_hom_evaluation {A B₁ B₂ : C}
    (p₁ : ExactPairing A B₁) (p₂ : ExactPairing A B₂) :
    (((rightDualIso p₁ p₂).hom) ▷ A) ≫ ε_ A B₂ = ε_ A B₁ := by
  simpa using (@rightAdjointMate_comp_evaluation C _ _ A A ⟨B₂⟩ ⟨B₁⟩ (𝟙 A))

/-- **The comparison of two right duals is unique.**  Any map commuting with the evaluations *is*
`rightDualIso`.  Mathlib has `rightDualIso` and `rightDualIso_id` and nothing else about it, so
this is the missing characterisation — and it is what makes the comparison usable in proofs, since
it turns "construct the map" into "check one identity". -/
theorem rightDualIso_hom_unique {A B₁ B₂ : C}
    (p₁ : ExactPairing A B₁) (p₂ : ExactPairing A B₂)
    (f : B₁ ⟶ B₂) (h : (f ▷ A) ≫ ε_ A B₂ = ε_ A B₁) :
    f = (rightDualIso p₁ p₂).hom :=
  whiskerRight_evaluation_injective (h.trans (rightDualIso_hom_evaluation p₁ p₂).symm)

/-- **Comparisons of right duals compose.**  Immediate from uniqueness. -/
theorem rightDualIso_hom_trans {A B₁ B₂ B₃ : C}
    (p₁ : ExactPairing A B₁) (p₂ : ExactPairing A B₂) (p₃ : ExactPairing A B₃) :
    (rightDualIso p₁ p₂).hom ≫ (rightDualIso p₂ p₃).hom = (rightDualIso p₁ p₃).hom := by
  refine rightDualIso_hom_unique p₁ p₃ _ ?_
  rw [comp_whiskerRight, Category.assoc, rightDualIso_hom_evaluation,
      rightDualIso_hom_evaluation]

/-- **The coevaluation identity that characterises `rightDualIso`** — the mirror of
`rightDualIso_hom_evaluation`.

Where the evaluation form says the comparison of two right duals commutes with the two evaluations,
this says it carries one coevaluation to the other.  Proved by transporting both sides through
`tensorLeftHomEquiv` *for the pairing `p₁`* — the choice matters: the `p₂` equivalence leaves a
mixed `η_{p₂}` against `ε_{p₁}` that is no snake, while the `p₁` one reduces each side to
`(ρ_ B₁).hom ≫ (rightDualIso p₁ p₂).hom` after one use of the evaluation form. -/
theorem coev_comp_rightDualIso {A B₁ B₂ : C}
    (p₁ : ExactPairing A B₁) (p₂ : ExactPairing A B₂) :
    @ExactPairing.coevaluation _ _ _ A B₁ p₁ ≫ A ◁ (rightDualIso p₁ p₂).hom
      = @ExactPairing.coevaluation _ _ _ A B₂ p₂ := by
  apply (tensorLeftHomEquiv (𝟙_ C) A B₁ B₂).symm.injective
  simp only [tensorLeftHomEquiv, Equiv.coe_fn_symm_mk]
  have hL : B₁ ◁ (@ExactPairing.coevaluation _ _ _ A B₁ p₁ ≫ A ◁ (rightDualIso p₁ p₂).hom)
        ≫ (α_ B₁ A B₂).inv ≫ ε_ A B₁ ▷ B₂ ≫ (λ_ B₂).hom
      = (ρ_ B₁).hom ≫ (rightDualIso p₁ p₂).hom := by
    rw [MonoidalCategory.whiskerLeft_comp, Category.assoc,
      MonoidalCategory.associator_inv_naturality_right_assoc, whisker_exchange_assoc,
      ExactPairing.coevaluation_evaluation_assoc]
    simp
  have hR : B₁ ◁ (@ExactPairing.coevaluation _ _ _ A B₂ p₂)
        ≫ (α_ B₁ A B₂).inv ≫ ε_ A B₁ ▷ B₂ ≫ (λ_ B₂).hom
      = (ρ_ B₁).hom ≫ (rightDualIso p₁ p₂).hom := by
    rw [← rightDualIso_hom_evaluation p₁ p₂, comp_whiskerRight, Category.assoc,
      ← MonoidalCategory.associator_inv_naturality_left_assoc, whisker_exchange_assoc,
      ExactPairing.coevaluation_evaluation_assoc]
    simp
  rw [hL, hR]

end QOU.MathlibExt
