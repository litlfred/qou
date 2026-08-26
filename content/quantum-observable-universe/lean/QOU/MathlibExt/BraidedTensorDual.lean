/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.BraidedSlide
import QOU.MathlibExt.RigidTensorDual

/-!
# QOU.MathlibExt.BraidedTensorDual — where the monodromy comes from

In a braided category with two exact pairings `X ⊣ X'` and `Y ⊣ Y'` there are **two** ways to
exhibit `X ⊗ Y` as a right dual of `Y' ⊗ X'`:

* **swap-then-tensor** — build the tensor pairing `X ⊗ Y ⊣ Y' ⊗ X'`
  (`QOU.MathlibExt.tensorExactPairing`) and turn it around with
  `CategoryTheory.BraidedCategory.exactPairing_swap`;
* **tensor-then-swap** — turn each pairing around first, then tensor.

They are **not** the same pairing, and the discrepancy is the monodromy
`(β_ X Y).hom ≫ (β_ Y X).hom`.  That is the obstruction to `QOU.MathlibExt.drinfeldIso` being
monoidal, and hence the reason a braided right-rigid category is not pivotal in the monoidal sense
— see the module docstring of `QOU.MathlibExt.PivotalCategory`.

## The mechanism

Expanding the block braiding `β_{X ⊗ Y, Y' ⊗ X'}` by the two hexagons gives four crossings.  Two of
them — `Y` over `Y'` and `X` over `X'` — pair off with the two evaluations and reproduce the
componentwise comparisons.  The surviving two are `X` over `Y'` and `Y` over `X'`: each crosses only
*one* leg of a dual pair, and `braiding_slide_cap_right_inv` says such a crossing can be pushed off
only at the cost of an **inverse** braiding past the other leg.  The two leftovers are
`(β_ Y X).inv` and `(β_ X Y).inv`, whose composite is the inverse monodromy.

`evaluation_swap_tensor_step` below carries out the first of the two pushes.
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory Category BraidedCategory

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]

/-- **The first of the two pushes.**

The left-hand side is the evaluation of `exactPairing_swap` applied to `tensorExactPairing` — the
"swap-then-tensor" pairing.  The right-hand side has the `Y`-over-`X'` crossing removed: it has been
pushed off the `X`-evaluation by `braiding_slide_cap_right_inv`, leaving `(β_ Y X).inv` behind.  That
leftover is the first half of the monodromy.

The proof is: two hexagons to expand the block braiding, one interchange to bring the crossing next
to the evaluation it must cross, and the inverse slide. -/
theorem evaluation_swap_tensor_step {X X' Y Y' : C}
    (p : ExactPairing X X') (r : ExactPairing Y Y') :
    (β_ (X ⊗ Y) (Y' ⊗ X')).hom ≫ (𝟙 _ ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ ε_ Y Y')
      = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
        ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
        ⊗≫ (β_ X Y').hom ▷ (Y ⊗ X')
        ⊗≫ Y' ◁ ((β_ Y X).inv ▷ X')
        ⊗≫ Y' ◁ (Y ◁ ((β_ X X').hom ≫ ε_ X X'))
        ⊗≫ ε_ Y Y' := by
  have hE := whisker_exchange (β_ X Y').hom (β_ Y X').hom
  have hS := braiding_slide_cap_right_inv (W := Y) (A := X) (B := X')
      ((β_ X X').hom ≫ ε_ X X')
  calc _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
            ⊗≫ X ◁ (Y' ◁ (β_ Y X').hom)
            ⊗≫ ((β_ X Y').hom ▷ X') ▷ Y
            ⊗≫ Y' ◁ (((β_ X X').hom ≫ ε_ X X') ▷ Y)
            ⊗≫ ε_ Y Y' := by
          rw [braiding_tensor_left_hom, braiding_tensor_right_hom, braiding_tensor_right_hom]
          monoidal
    -- interchange: the `X`-over-`Y'` and `Y`-over-`X'` crossings act on disjoint strands
    _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
            ⊗≫ ((X ⊗ Y') ◁ (β_ Y X').hom ≫ (β_ X Y').hom ▷ (X' ⊗ Y))
            ⊗≫ Y' ◁ (((β_ X X').hom ≫ ε_ X X') ▷ Y)
            ⊗≫ ε_ Y Y' := by monoidal
    _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
            ⊗≫ ((β_ X Y').hom ▷ (Y ⊗ X') ≫ (Y' ⊗ X) ◁ (β_ Y X').hom)
            ⊗≫ Y' ◁ (((β_ X X').hom ≫ ε_ X X') ▷ Y)
            ⊗≫ ε_ Y Y' := by rw [hE]
    -- regroup so the crossing sits bare against the `X`-cap, then push it off
    _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
            ⊗≫ (β_ X Y').hom ▷ (Y ⊗ X')
            ⊗≫ Y' ◁ (𝟙 ((X ⊗ Y) ⊗ X') ⊗≫ X ◁ (β_ Y X').hom
                  ⊗≫ ((β_ X X').hom ≫ ε_ X X') ▷ Y ⊗≫ 𝟙 Y)
            ⊗≫ ε_ Y Y' := by monoidal
    _ = _ := by rw [hS]; monoidal

/-- **The second push, and the monodromy it leaves.**

Three strands: `X` crossing the closed `Y`-pair.  Pushing the `X`-over-`Y'` crossing off the
`Y`-cap leaves the **inverse monodromy** `((β_ X Y).hom ≫ (β_ Y X).hom)⁻¹` acting on `X ⊗ Y` at
the top.

The proof is three moves and no diagram chase.  Write `(β_ Y X).inv = M⁻¹ ≫ (β_ X Y).hom`, which
splits the crossing into a monodromy and an *honest* braiding.  Recognise the two leading crossings
as the block braiding `β_{X ⊗ Y, Y'}` (`braiding_tensor_left_hom`), so that
`braiding_naturality_left` carries the monodromy from the middle to the top.  What is left is
exactly `braiding_slide_cap_right` at the `Y`-cap. -/
theorem braiding_cap_monodromy {X Y Y' : C} (r : ExactPairing Y Y') :
    𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ X ◁ (β_ Y Y').hom ⊗≫ (β_ X Y').hom ▷ Y
        ⊗≫ Y' ◁ (β_ Y X).inv ⊗≫ ε_ Y Y' ▷ X ⊗≫ 𝟙 X
      = 𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ ((β_ Y X).inv ≫ (β_ X Y).inv) ▷ Y'
        ⊗≫ X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ⊗≫ 𝟙 X := by
  have hinv : (β_ Y X).inv
      = ((β_ Y X).inv ≫ (β_ X Y).inv) ≫ (β_ X Y).hom := by simp
  have hnat := braiding_naturality_left ((β_ Y X).inv ≫ (β_ X Y).inv) Y'
  have hhex := braiding_tensor_left_hom X Y Y'
  have hslide := braiding_slide_cap_right (W := X) (A := Y') (B := Y) (ε_ Y Y')
  calc _ = 𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ ((β_ (X ⊗ Y) Y').hom
              ≫ Y' ◁ ((β_ Y X).inv ≫ (β_ X Y).inv))
            ⊗≫ Y' ◁ (β_ X Y).hom ⊗≫ ε_ Y Y' ▷ X ⊗≫ 𝟙 X := by
          rw [hhex]; conv_lhs => rw [hinv]
          monoidal
    -- naturality of the block braiding carries the monodromy to the top
    _ = 𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ (((β_ Y X).inv ≫ (β_ X Y).inv) ▷ Y' ≫ (β_ (X ⊗ Y) Y').hom)
            ⊗≫ Y' ◁ (β_ X Y).hom ⊗≫ ε_ Y Y' ▷ X ⊗≫ 𝟙 X := by
          rw [hnat]
    _ = 𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ ((β_ Y X).inv ≫ (β_ X Y).inv) ▷ Y'
            ⊗≫ X ◁ (β_ Y Y').hom
            ⊗≫ (𝟙 ((X ⊗ Y') ⊗ Y) ⊗≫ (β_ X Y').hom ▷ Y ⊗≫ Y' ◁ (β_ X Y).hom
                  ⊗≫ ε_ Y Y' ▷ X ⊗≫ 𝟙 X) := by
          rw [hhex]; monoidal
    _ = _ := by rw [hslide]; monoidal

end QOU.MathlibExt
