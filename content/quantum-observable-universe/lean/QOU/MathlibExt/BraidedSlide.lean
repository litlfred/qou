/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

/-!
# QOU.MathlibExt.BraidedSlide — sliding a strand across a cap or a cup

In a braided category, a morphism `c : A ⊗ B ⟶ 𝟙_ C` behaves like a **cap** joining `A` to `B`,
and `u : 𝟙_ C ⟶ A ⊗ B` like a **cup**.  The four lemmas here say that a strand `W` passing across
such a cap or cup may be pushed off it, at the cost of braiding `W` past each of the two legs
separately:

```
   W over the cap        =        W past A, then past B, then the cap
```

Nothing is assumed of `c` and `u` beyond their type — no rigidity, no exact pairing, not even that
they are related to each other.  Each lemma is the corresponding `braiding_naturality_*` at the cap
or cup, with the hexagon `braiding_tensor_*_hom` expanding `β` at the tensor `A ⊗ B`.

## Why these are worth naming

They are the mechanism by which the **monodromy** appears in rigid braided categories.  When `A` and
`B` are a dual pair and `c` is the evaluation, a strand crossing *one* leg cannot simply be deleted:
pushing it off supplies a braiding past the *other* leg as well, and after the cap closes, that
second braiding is a crossing of `W` with the original object.  Two such pushes — one for each of a
pair of dual legs — produce `β ≫ β`, which is precisely the discrepancy that obstructs monoidality
of the Drinfeld isomorphism and that a ribbon twist cancels.  See
`QOU.MathlibExt.PivotalCategory` for that argument.

## Naming

`W` slides "right" when it starts on the left of the cap and ends on its right, matching
`braiding_naturality_right`; "left" is the mirror image, from `braiding_naturality_left`.
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory Category BraidedCategory

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]

/-- **A strand slides across a cap**, braiding past each leg in turn.

`W` starts to the left of `A ⊗ B` and ends to its right. -/
theorem braiding_slide_cap_right {W A B : C} (c : A ⊗ B ⟶ 𝟙_ C) :
    𝟙 ((W ⊗ A) ⊗ B) ⊗≫ (β_ W A).hom ▷ B ⊗≫ A ◁ (β_ W B).hom ⊗≫ c ▷ W ⊗≫ 𝟙 W
      = 𝟙 ((W ⊗ A) ⊗ B) ⊗≫ W ◁ c ⊗≫ 𝟙 W := by
  have h := braiding_naturality_right W c
  rw [braiding_tensor_right_hom] at h
  calc _ = 𝟙 ((W ⊗ A) ⊗ B) ⊗≫ (((α_ W A B).inv ≫ (β_ W A).hom ▷ B ≫ (α_ A W B).hom
              ≫ A ◁ (β_ W B).hom ≫ (α_ A B W).inv) ≫ c ▷ W) ⊗≫ 𝟙 W := by monoidal
    _ = 𝟙 ((W ⊗ A) ⊗ B) ⊗≫ (W ◁ c ≫ (β_ W (𝟙_ C)).hom) ⊗≫ 𝟙 W := by rw [← h]
    _ = _ := by simp [monoidalComp]

/-- **A strand slides across a cap**, mirror image of `braiding_slide_cap_right`.

`W` starts to the right of `A ⊗ B` and ends to its left. -/
theorem braiding_slide_cap_left {W A B : C} (c : A ⊗ B ⟶ 𝟙_ C) :
    𝟙 ((A ⊗ B) ⊗ W) ⊗≫ A ◁ (β_ B W).hom ⊗≫ (β_ A W).hom ▷ B ⊗≫ W ◁ c ⊗≫ 𝟙 W
      = 𝟙 ((A ⊗ B) ⊗ W) ⊗≫ c ▷ W ⊗≫ 𝟙 W := by
  have h := braiding_naturality_left c W
  rw [braiding_tensor_left_hom] at h
  calc _ = 𝟙 ((A ⊗ B) ⊗ W) ⊗≫ (((α_ A B W).hom ≫ A ◁ (β_ B W).hom ≫ (α_ A W B).inv
              ≫ (β_ A W).hom ▷ B ≫ (α_ W A B).hom) ≫ W ◁ c) ⊗≫ 𝟙 W := by monoidal
    _ = 𝟙 ((A ⊗ B) ⊗ W) ⊗≫ (c ▷ W ≫ (β_ (𝟙_ C) W).hom) ⊗≫ 𝟙 W := by rw [← h]
    _ = _ := by simp [monoidalComp]

/-- **The inverse form of `braiding_slide_cap_right`** — the one an assembly actually uses.

Read left to right: a strand `W` that crosses only the *second* leg `B` before the cap can still be
pushed off, but it leaves behind an **inverse** braiding past the first leg `A`.  That leftover is
where a monodromy comes from: apply this twice, once for each leg of a dual pair, and the two
leftovers compose to a double braid. -/
theorem braiding_slide_cap_right_inv {W A B : C} (c : A ⊗ B ⟶ 𝟙_ C) :
    𝟙 ((A ⊗ W) ⊗ B) ⊗≫ A ◁ (β_ W B).hom ⊗≫ c ▷ W ⊗≫ 𝟙 W
      = 𝟙 ((A ⊗ W) ⊗ B) ⊗≫ (β_ W A).inv ▷ B ⊗≫ W ◁ c ⊗≫ 𝟙 W := by
  have h := braiding_slide_cap_right (W := W) c
  calc _ = 𝟙 ((A ⊗ W) ⊗ B) ⊗≫ (β_ W A).inv ▷ B
            ⊗≫ (𝟙 ((W ⊗ A) ⊗ B) ⊗≫ (β_ W A).hom ▷ B ⊗≫ A ◁ (β_ W B).hom
                  ⊗≫ c ▷ W ⊗≫ 𝟙 W) := by
            simp [monoidalComp]
    _ = _ := by rw [h]; simp [monoidalComp]

/-- **A strand slides across a cup**, braiding past each leg in turn.

The cup-shaped dual of `braiding_slide_cap_right`. -/
theorem braiding_slide_cup_right {W A B : C} (u : 𝟙_ C ⟶ A ⊗ B) :
    𝟙 W ⊗≫ u ▷ W ⊗≫ 𝟙 ((A ⊗ B) ⊗ W)
      = 𝟙 W ⊗≫ W ◁ u ⊗≫ (β_ W A).hom ▷ B ⊗≫ A ◁ (β_ W B).hom ⊗≫ 𝟙 ((A ⊗ B) ⊗ W) := by
  have h := braiding_naturality_right W u
  rw [braiding_tensor_right_hom] at h
  calc _ = 𝟙 W ⊗≫ ((β_ W (𝟙_ C)).hom ≫ u ▷ W) ⊗≫ 𝟙 ((A ⊗ B) ⊗ W) := by
            simp [monoidalComp]
    _ = 𝟙 W ⊗≫ (W ◁ u ≫ ((α_ W A B).inv ≫ (β_ W A).hom ▷ B ≫ (α_ A W B).hom
              ≫ A ◁ (β_ W B).hom ≫ (α_ A B W).inv)) ⊗≫ 𝟙 ((A ⊗ B) ⊗ W) := by rw [h]
    _ = _ := by monoidal

/-- **A strand slides across a cup**, mirror image of `braiding_slide_cup_right`. -/
theorem braiding_slide_cup_left {W A B : C} (u : 𝟙_ C ⟶ A ⊗ B) :
    𝟙 W ⊗≫ W ◁ u ⊗≫ 𝟙 (W ⊗ A ⊗ B)
      = 𝟙 W ⊗≫ u ▷ W ⊗≫ A ◁ (β_ B W).hom ⊗≫ (β_ A W).hom ▷ B ⊗≫ 𝟙 (W ⊗ A ⊗ B) := by
  have h := braiding_naturality_left u W
  rw [braiding_tensor_left_hom] at h
  calc _ = 𝟙 W ⊗≫ ((β_ (𝟙_ C) W).hom ≫ W ◁ u) ⊗≫ 𝟙 (W ⊗ A ⊗ B) := by
            simp [monoidalComp]
    _ = 𝟙 W ⊗≫ (u ▷ W ≫ ((α_ A B W).hom ≫ A ◁ (β_ B W).hom ≫ (α_ A W B).inv
              ≫ (β_ A W).hom ▷ B ≫ (α_ W A B).hom)) ⊗≫ 𝟙 (W ⊗ A ⊗ B) := by rw [h]
    _ = _ := by monoidal

end QOU.MathlibExt
