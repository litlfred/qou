/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.BraidedSlide
import QOU.MathlibExt.RigidTensorDual
import QOU.MathlibExt.PivotalCategory
import QOU.MathlibExt.Ribbon

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

/-- **The two pairings differ by exactly the inverse monodromy.**

`X ⊗ Y` is a right dual of `Y' ⊗ X'` in two ways — swap-then-tensor (left) and tensor-then-swap
(right) — and their evaluations differ by `((β_ X Y).hom ≫ (β_ Y X).hom)⁻¹` applied to `X ⊗ Y`.

Both pushes, assembled: `evaluation_swap_tensor_step` removes the `Y`-over-`X'` crossing, one
interchange separates the two evaluations (they act on disjoint strands), and
`braiding_cap_monodromy` removes the `X`-over-`Y'` crossing and delivers the monodromy. -/
theorem evaluation_swap_tensor_eq_monodromy {X X' Y Y' : C}
    (p : ExactPairing X X') (r : ExactPairing Y Y') :
    (β_ (X ⊗ Y) (Y' ⊗ X')).hom ≫ (𝟙 _ ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ ε_ Y Y')
      = ((β_ Y X).inv ≫ (β_ X Y).inv) ▷ (Y' ⊗ X')
          ≫ (𝟙 _ ⊗≫ X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ▷ X'
                ⊗≫ ((β_ X X').hom ≫ ε_ X X')) := by
  rw [evaluation_swap_tensor_step p r]
  have hX := whisker_exchange (ε_ Y Y') ((β_ X X').hom ≫ ε_ X X')
  have hG := braiding_cap_monodromy (X := X) r
  calc _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
            ⊗≫ (β_ X Y').hom ▷ (Y ⊗ X')
            ⊗≫ Y' ◁ ((β_ Y X).inv ▷ X')
            ⊗≫ ((Y' ⊗ Y) ◁ ((β_ X X').hom ≫ ε_ X X') ≫ (ε_ Y Y') ▷ 𝟙_ C)
            ⊗≫ 𝟙 (𝟙_ C) := by monoidal
    -- the two evaluations act on disjoint strands, so they may be taken in either order
    _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ X ◁ ((β_ Y Y').hom ▷ X')
            ⊗≫ (β_ X Y').hom ▷ (Y ⊗ X')
            ⊗≫ Y' ◁ ((β_ Y X).inv ▷ X')
            ⊗≫ ((ε_ Y Y') ▷ (X ⊗ X') ≫ 𝟙_ C ◁ ((β_ X X').hom ≫ ε_ X X'))
            ⊗≫ 𝟙 (𝟙_ C) := by rw [hX]
    -- `X'` is a spectator to the whole `Y`-cap argument
    _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ ((𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ X ◁ (β_ Y Y').hom ⊗≫ (β_ X Y').hom ▷ Y
                  ⊗≫ Y' ◁ (β_ Y X).inv ⊗≫ ε_ Y Y' ▷ X ⊗≫ 𝟙 X) ▷ X')
            ⊗≫ ((β_ X X').hom ≫ ε_ X X') := by monoidal
    _ = 𝟙 ((X ⊗ Y) ⊗ Y' ⊗ X')
            ⊗≫ ((𝟙 ((X ⊗ Y) ⊗ Y') ⊗≫ ((β_ Y X).inv ≫ (β_ X Y).inv) ▷ Y'
                  ⊗≫ X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ⊗≫ 𝟙 X) ▷ X')
            ⊗≫ ((β_ X X').hom ≫ ε_ X X') := by rw [hG]
    _ = _ := by monoidal

/-- **Swap-then-tensor and tensor-then-swap are compared by the inverse monodromy.**

The dual-uniqueness isomorphism between the two pairings of `Y' ⊗ X'` with `X ⊗ Y` is *not* the
identity: it is `((β_ X Y).hom ≫ (β_ Y X).hom)⁻¹`.  In a **symmetric** category the monodromy is
trivial and the two pairings agree; in a genuinely braided one they do not. -/
theorem rightDualIso_swap_tensor {X X' Y Y' : C}
    (p : ExactPairing X X') (r : ExactPairing Y Y') :
    (rightDualIso
        (@BraidedCategory.exactPairing_swap C _ _ _ (X ⊗ Y) (Y' ⊗ X') (tensorExactPairing X X' Y Y'))
        (@tensorExactPairing C _ _ Y' Y X' X
          (BraidedCategory.exactPairing_swap Y Y') (BraidedCategory.exactPairing_swap X X'))).hom
      = (β_ Y X).inv ≫ (β_ X Y).inv := by
  refine (rightDualIso_hom_unique _ _ _ ?_).symm
  show ((β_ Y X).inv ≫ (β_ X Y).inv) ▷ (Y' ⊗ X')
        ≫ (𝟙 _ ⊗≫ X ◁ ((β_ Y Y').hom ≫ ε_ Y Y') ▷ X'
              ⊗≫ ((β_ X X').hom ≫ ε_ X X'))
      = (β_ (X ⊗ Y) (Y' ⊗ X')).hom ≫ (𝟙 _ ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ ε_ Y Y')
  exact (evaluation_swap_tensor_eq_monodromy p r).symm

/-! ### The ribbon repair

The monodromy is exactly what a **balancing** cancels, so while `drinfeldIso` is not monoidal, its
twisted form `θ ≫ drinfeldIso` is.  That is the classical statement — a ribbon element `v` makes
`uv⁻¹` grouplike — and `twist_drinfeld_monoidal` below is its categorical form.
-/

section Ribbon

variable [RightRigidCategory C]

/-- Swap-then-tensor: `X ⊗ Y` as a right dual of `Yᘁ ⊗ Xᘁ`, via `exactPairing_swap` of the
tensor pairing. -/
noncomputable def swapTensorPairing (X Y : C) :
    ExactPairing ((Y : C)ᘁ ⊗ (X : C)ᘁ) (X ⊗ Y) :=
  @BraidedCategory.exactPairing_swap C _ _ _ (X ⊗ Y) ((Y : C)ᘁ ⊗ (X : C)ᘁ)
    (tensorExactPairing X ((X : C)ᘁ) Y ((Y : C)ᘁ))

/-- Tensor-then-swap: the same objects, the other pairing.  `rightDualIso_swap_tensor` says these
two differ by the inverse monodromy. -/
noncomputable def tensorSwapPairing (X Y : C) :
    ExactPairing ((Y : C)ᘁ ⊗ (X : C)ᘁ) (X ⊗ Y) :=
  @tensorExactPairing C _ _ ((Y : C)ᘁ) Y ((X : C)ᘁ) X
    (BraidedCategory.exactPairing_swap Y ((Y : C)ᘁ))
    (BraidedCategory.exactPairing_swap X ((X : C)ᘁ))

/-- `Xᘁᘁ ⊗ Yᘁᘁ` as a right dual of `Yᘁ ⊗ Xᘁ`. -/
noncomputable def doubleDualTensorPairing (X Y : C) :
    ExactPairing ((Y : C)ᘁ ⊗ (X : C)ᘁ) ((((X : C)ᘁ : C)ᘁ) ⊗ (((Y : C)ᘁ : C)ᘁ)) :=
  tensorExactPairing ((Y : C)ᘁ) (((Y : C)ᘁ : C)ᘁ) ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ)

/-- **The comparison a monoidal pivotal structure must satisfy**, `X ⊗ Y ≅ Xᘁᘁ ⊗ Yᘁᘁ`.

Built by dual-uniqueness between two pairings of `Yᘁ ⊗ Xᘁ`, which is what makes it directly
comparable with the componentwise `drinfeldIso`s.

It **is** the canonical comparison: `drinfeldIso_comp_tensorDoubleDualIso` below proves
`drinfeldIso (X ⊗ Y) ≫ (tensorDoubleDualIso X Y).hom = (pivotorTensor X Y).hom`, so the
monoidality results here can be read against either form.

*An earlier revision recorded this as open and predicted the route: transporting a pairing along
`tensorRightDualIso X Y` via Mathlib's `exactPairingCongrLeft`, plus a `rightDualIso` compatibility
lemma nobody had written.  **Neither was needed.**  `tensorRightDualIso` is itself a `rightDualIso`,
so it already carries an evaluation identity, and `braiding_naturality_right` moves it across the
braiding `drinfeldIso` contributes.* -/
noncomputable def pivotorTensor (X Y : C) :
    (X ⊗ Y) ≅ ((((X : C)ᘁ : C)ᘁ) ⊗ (((Y : C)ᘁ : C)ᘁ)) :=
  rightDualIso (swapTensorPairing X Y) (doubleDualTensorPairing X Y)

/-- **`drinfeldIso` fails monoidality by exactly the inverse monodromy.**

Not `(drinfeldIso X).hom ⊗ₘ (drinfeldIso Y).hom`, as a monoidal pivotal structure would require,
but that composed with `((β_ X Y).hom ≫ (β_ Y X).hom)⁻¹`.  In a symmetric category the correction
is the identity and monoidality does hold; in a genuinely braided one it does not.

Three lemmas compose: `rightDualIso_hom_trans` factors the comparison through the intermediate
tensor-then-swap pairing, `rightDualIso_swap_tensor` evaluates the first factor as the inverse
monodromy, and `rightDualIso_tensorExactPairing` evaluates the second as the tensor of the two
`drinfeldIso`s. -/
theorem pivotorTensor_hom (X Y : C) :
    (pivotorTensor X Y).hom
      = ((β_ Y X).inv ≫ (β_ X Y).inv)
          ≫ ((drinfeldIso X).hom ⊗ₘ (drinfeldIso Y).hom) := by
  rw [pivotorTensor, ← rightDualIso_hom_trans (swapTensorPairing X Y) (tensorSwapPairing X Y)
        (doubleDualTensorPairing X Y)]
  congr 1
  · exact rightDualIso_swap_tensor (HasRightDual.exact (X := X)) (HasRightDual.exact (X := Y))
  · exact rightDualIso_tensorExactPairing
      (BraidedCategory.exactPairing_swap Y ((Y : C)ᘁ)) (HasRightDual.exact (X := (Y : C)ᘁ))
      (BraidedCategory.exactPairing_swap X ((X : C)ᘁ)) (HasRightDual.exact (X := (X : C)ᘁ))

omit [RightRigidCategory C] in
/-- The monodromy commutes with a tensor of endomorphisms — braiding naturality, twice. -/
theorem monodromy_inv_comm {X Y : C} (f : X ⟶ X) (g : Y ⟶ Y) :
    (f ⊗ₘ g) ≫ ((β_ Y X).inv ≫ (β_ X Y).inv)
      = ((β_ Y X).inv ≫ (β_ X Y).inv) ≫ (f ⊗ₘ g) := by
  rw [← Category.assoc, braiding_inv_naturality f g, Category.assoc,
      braiding_inv_naturality g f, ← Category.assoc]

/-- **The ribbon repair: `θ ≫ drinfeldIso` IS monoidal.**

`drinfeldIso` misses monoidality by the inverse monodromy (`pivotorTensor_hom`); the balancing
axiom `θ_{X ⊗ Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)` supplies exactly the monodromy, and the two
cancel.  The step that makes the cancellation go through is `monodromy_inv_comm`: `θ_X ⊗ θ_Y`
commutes past the monodromy by braiding naturality, so the `β β` from the balancing axiom meets its
own inverse.

This is the categorical form of the classical fact that a ribbon element `v` makes `uv⁻¹`
grouplike, and it is why **ribbon**, not merely braided, is the hypothesis under which a rigid
category is pivotal in the monoidal sense. -/
theorem twist_drinfeld_monoidal [BalancedCategory C] (X Y : C) :
    BalancedCategory.twist (X ⊗ Y) ≫ (pivotorTensor X Y).hom
      = (BalancedCategory.twist X ≫ (drinfeldIso X).hom)
          ⊗ₘ (BalancedCategory.twist Y ≫ (drinfeldIso Y).hom) := by
  rw [pivotorTensor_hom, BalancedCategory.twist_tensor]
  calc _ = (β_ X Y).hom ≫ (β_ Y X).hom
            ≫ ((BalancedCategory.twist X ⊗ₘ BalancedCategory.twist Y)
                ≫ ((β_ Y X).inv ≫ (β_ X Y).inv))
            ≫ ((drinfeldIso X).hom ⊗ₘ (drinfeldIso Y).hom) := by simp
    _ = (β_ X Y).hom ≫ (β_ Y X).hom
            ≫ (((β_ Y X).inv ≫ (β_ X Y).inv)
                ≫ (BalancedCategory.twist X ⊗ₘ BalancedCategory.twist Y))
            ≫ ((drinfeldIso X).hom ⊗ₘ (drinfeldIso Y).hom) := by
          rw [monodromy_inv_comm]
    _ = _ := by simp [← tensorHom_comp_tensorHom]

/-- **The two comparisons agree** — `pivotorTensor` is the canonical one.

`pivotorTensor X Y` was built by dual-uniqueness between two pairings of `Yᘁ ⊗ Xᘁ`, which is the
convenient form for comparing against the componentwise `drinfeldIso`s.  The *canonical* monoidal
structure map of the double-dual functor is instead `drinfeldIso (X ⊗ Y)` followed by
`tensorDoubleDualIso X Y`, which routes through `(X ⊗ Y)ᘁᘁ`.  This says they are the same map, so
the monoidality statement below can be read either way.

The two are characterised against pairings on *different* base objects — `Yᘁ ⊗ Xᘁ` on one side,
`(X ⊗ Y)ᘁ` on the other — so `rightDualIso_hom_unique` does not compare them directly.  The bridge
is that `tensorRightDualIso X Y : (X ⊗ Y)ᘁ ≅ Yᘁ ⊗ Xᘁ` is itself a dual comparison, so it carries
its own evaluation identity, and `braiding_naturality_right` moves it across the braiding that
`drinfeldIso` contributes.  Four evaluation identities and one interchange, no diagram chase. -/
theorem drinfeldIso_comp_tensorDoubleDualIso (X Y : C) :
    (drinfeldIso (X ⊗ Y)).hom ≫ (tensorDoubleDualIso X Y).hom = (pivotorTensor X Y).hom := by
  refine rightDualIso_hom_unique (swapTensorPairing X Y) (doubleDualTensorPairing X Y) _ ?_
  have h2 : ((tensorRightDualIso ((Y : C)ᘁ) ((X : C)ᘁ)).hom ▷ ((Y : C)ᘁ ⊗ (X : C)ᘁ))
        ≫ (doubleDualTensorPairing X Y).evaluation'
      = ε_ ((Y : C)ᘁ ⊗ (X : C)ᘁ) (((Y : C)ᘁ ⊗ (X : C)ᘁ : C)ᘁ) :=
    rightDualIso_hom_evaluation _ _
  have h4 : ((drinfeldIso (X ⊗ Y)).hom ▷ ((X ⊗ Y : C)ᘁ))
        ≫ ε_ ((X ⊗ Y : C)ᘁ) (((X ⊗ Y : C)ᘁ : C)ᘁ)
      = (β_ (X ⊗ Y) ((X ⊗ Y : C)ᘁ)).hom ≫ ε_ (X ⊗ Y) ((X ⊗ Y : C)ᘁ) :=
    rightDualIso_hom_evaluation _ _
  have h6 : ((tensorRightDualIso X Y).inv ▷ (X ⊗ Y)) ≫ ε_ (X ⊗ Y) ((X ⊗ Y : C)ᘁ)
      = (tensorExactPairing X ((X : C)ᘁ) Y ((Y : C)ᘁ)).evaluation' :=
    rightDualIso_hom_evaluation _ _
  show (((drinfeldIso (X ⊗ Y)).hom ≫ (tensorDoubleDualIso X Y).hom) ▷ ((Y : C)ᘁ ⊗ (X : C)ᘁ))
      ≫ (doubleDualTensorPairing X Y).evaluation'
    = (swapTensorPairing X Y).evaluation'
  rw [tensorDoubleDualIso, Iso.trans_hom, rightDualMapIso_hom, comp_whiskerRight,
      comp_whiskerRight, Category.assoc, Category.assoc, h2,
      rightAdjointMate_comp_evaluation, ← Category.assoc, ← whisker_exchange,
      Category.assoc, h4, ← Category.assoc, braiding_naturality_right,
      Category.assoc, h6]
  rfl

/-- **The ribbon repair, in canonical form.**

`twist_drinfeld_monoidal` stated against `pivotorTensor`; this states the same thing against the
canonical comparison `drinfeldIso (X ⊗ Y) ≫ tensorDoubleDualIso X Y`, which is the shape a
`PivotalCategory` monoidality field would take. -/
theorem twist_drinfeld_monoidal_tensorDoubleDualIso [BalancedCategory C] (X Y : C) :
    BalancedCategory.twist (X ⊗ Y)
        ≫ ((drinfeldIso (X ⊗ Y)).hom ≫ (tensorDoubleDualIso X Y).hom)
      = (BalancedCategory.twist X ≫ (drinfeldIso X).hom)
          ⊗ₘ (BalancedCategory.twist Y ≫ (drinfeldIso Y).hom) := by
  rw [drinfeldIso_comp_tensorDoubleDualIso]
  exact twist_drinfeld_monoidal X Y

/-- **A ribbon category is pivotal** — in the literature's monoidal sense.

This replaces the `pivotalOfBraided` instance that `QOU.MathlibExt.PivotalCategory` used to carry.
Braiding alone is not enough: `drinfeldIso` misses monoidality by the inverse monodromy.  A
balancing supplies exactly that monodromy (`BalancedCategory.twist_tensor`), so `θ ≫ drinfeldIso`
is monoidal and the class is satisfied.

The classical statement behind it is that a ribbon element `v` makes `uv⁻¹` grouplike.

`Ribbon.lean` makes every symmetric category balanced (`θ = 𝟙`, the double braid being trivial), so
this instance still fires for `FGModuleCat K` and every other symmetric rigid category — no
linear algebra involved, exactly as before. -/
noncomputable instance (priority := 100) pivotalOfRibbon [BalancedCategory C] :
    PivotalCategory C :=
  PivotalCategory.ofPointwise
    (fun X => BalancedCategory.twistIso X ≪≫ drinfeldIso X)
    (fun {X Y} f => by
      simp only [Iso.trans_hom, BalancedCategory.twistIso_hom, Category.assoc]
      rw [← drinfeldIso_naturality f, ← Category.assoc, ← Category.assoc,
          BalancedCategory.twist_naturality f])
    (fun X Y => by
      simp only [Iso.trans_hom, BalancedCategory.twistIso_hom, Category.assoc]
      exact twist_drinfeld_monoidal_tensorDoubleDualIso X Y)

end Ribbon

end QOU.MathlibExt
