/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import QOU.MathlibExt.RightDualIsoUnique

/-!
# QOU.MathlibExt.RigidTensorDual — duals of a tensor product

Mathlib's `Mathlib/CategoryTheory/Monoidal/Rigid/Basic.lean` opens with a **"Future work"**
list. This module supplies its first entry, quoted verbatim:

> * Show that `X ⊗ Y` and `Yᘁ ⊗ Xᘁ` form an exact pairing.

Nothing in Mathlib implements it: there is no `ExactPairing (X ⊗ Y) _`, and no `HasRightDual`
instance for a tensor product.  Duals reversing order is the fact every downstream monoidal
statement needs — in particular one cannot even *state* that a pivotal structure is **monoidal**
without it, since that statement compares `a_{X ⊗ Y}` against `a_X ⊗ a_Y` through the comparison
isomorphism `(X ⊗ Y)ᘁᘁ ≅ Xᘁᘁ ⊗ Yᘁᘁ` built from this pairing.

Imports only Mathlib, so it lifts upstream verbatim.  Companions:
[`Ribbon.lean`](Ribbon.lean), [`PivotalCategory.lean`](PivotalCategory.lean),
[`BraidedQuantumDimension.lean`](BraidedQuantumDimension.lean).

## Main definition

* `tensorExactPairing` — `ExactPairing (X ⊗ Y) (Y' ⊗ X')` from `ExactPairing X X'` and
  `ExactPairing Y Y'`.  The coevaluation nests `η_Y` inside `η_X`; the evaluation runs `ε_X` on the
  inner pair and then `ε_Y`.

## The proof, and why the obvious routes fail

Both snake identities are genuine string-diagram arguments.  Neither is reachable by
`cat_disch` (the class's own autoparam), `simp`, `monoidal`, or `aesop_cat`; roughly thirty-five
automated tactic placements were tried and none closes either field.

The reason is worth recording, because it is not obvious from the goal.  The composite fires in
the order `η_X, η_Y, ε_X, ε_Y`, and in that order **neither snake is contiguous** — `η_Y` sits
between `η_X` and `ε_X`.  Moving it out of the way is the **interchange law**, not coherence, so
`monoidal` can never reach the two-snake form no matter how the intermediate is phrased.

What works is the idiom of Mathlib's own `coevaluation_evaluation_braided'`: pad every `calc`
term with `𝟙 _ ⊗≫ … ⊗≫ 𝟙 _`, parenthesise the interesting part as a single `⊗≫` group, and
regroup until a **bare** `W ◁ g ≫ f ▷ Z` appears with no compound whiskering around it — that
bare shape is what `whisker_exchange` matches, and the compound forms hide it.  Once the
exchange fires the two snakes are contiguous and `coevaluation_evaluation''` /
`evaluation_coevaluation''` finish the job.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory

variable {C : Type*} [Category C] [MonoidalCategory C]

/-- **`X ⊗ Y` and `Y' ⊗ X'` form an exact pairing** — Mathlib's "Future work" entry 1.

The coevaluation creates the `X`-pair and nests the `Y`-pair inside it; the evaluation contracts
the inner `X`-pair first and then the outer `Y`-pair.  Duals reverse order, which is why the
right-hand object is `Y' ⊗ X'` and not `X' ⊗ Y'`. -/
noncomputable def tensorExactPairing (X X' Y Y' : C)
    [ExactPairing X X'] [ExactPairing Y Y'] : ExactPairing (X ⊗ Y) (Y' ⊗ X') where
  coevaluation' := η_ X X' ⊗≫ X ◁ η_ Y Y' ▷ X' ⊗≫ 𝟙 _
  evaluation' := 𝟙 _ ⊗≫ Y' ◁ ε_ X X' ▷ Y ⊗≫ ε_ Y Y'
  coevaluation_evaluation' := by
    calc _ = 𝟙 _ ⊗≫ (Y' ⊗ X') ◁ η_ X X'
            ⊗≫ ((Y' ⊗ X') ◁ (X ◁ η_ Y Y' ▷ X') ⊗≫ (Y' ◁ ε_ X X' ▷ Y) ▷ (Y' ⊗ X'))
            ⊗≫ ε_ Y Y' ▷ (Y' ⊗ X') ⊗≫ 𝟙 _ := by monoidal
      -- regroup until the bare `W ◁ g ≫ f ▷ Z` is visible
      _ = 𝟙 _ ⊗≫ (Y' ⊗ X') ◁ η_ X X'
            ⊗≫ (((Y' ⊗ (X' ⊗ X)) ◁ η_ Y Y' ≫ (Y' ◁ ε_ X X') ▷ (Y ⊗ Y')) ▷ X')
            ⊗≫ ε_ Y Y' ▷ (Y' ⊗ X') ⊗≫ 𝟙 _ := by monoidal
      -- the interchange: `ε_X` and `η_Y` act on disjoint strands
      _ = 𝟙 _ ⊗≫ (Y' ⊗ X') ◁ η_ X X'
            ⊗≫ (((Y' ◁ ε_ X X') ▷ 𝟙_ C ≫ (Y' ⊗ 𝟙_ C) ◁ η_ Y Y') ▷ X')
            ⊗≫ ε_ Y Y' ▷ (Y' ⊗ X') ⊗≫ 𝟙 _ := by rw [whisker_exchange]
      -- both snakes are now contiguous
      _ = 𝟙 _ ⊗≫ Y' ◁ (X' ◁ η_ X X' ⊗≫ ε_ X X' ▷ X')
            ⊗≫ (Y' ◁ η_ Y Y' ⊗≫ ε_ Y Y' ▷ Y') ▷ X' ⊗≫ 𝟙 _ := by monoidal
      _ = _ := by
            rw [ExactPairing.coevaluation_evaluation'', ExactPairing.coevaluation_evaluation'']
            monoidal
  evaluation_coevaluation' := by
    calc _ = 𝟙 _ ⊗≫ η_ X X' ▷ (X ⊗ Y)
            ⊗≫ ((X ◁ η_ Y Y' ▷ X') ▷ (X ⊗ Y) ⊗≫ (X ⊗ Y) ◁ (Y' ◁ ε_ X X' ▷ Y))
            ⊗≫ (X ⊗ Y) ◁ ε_ Y Y' ⊗≫ 𝟙 _ := by monoidal
      _ = 𝟙 _ ⊗≫ η_ X X' ▷ (X ⊗ Y)
            ⊗≫ (X ◁ (η_ Y Y' ▷ (X' ⊗ X) ≫ (Y ⊗ Y') ◁ ε_ X X') ▷ Y)
            ⊗≫ (X ⊗ Y) ◁ ε_ Y Y' ⊗≫ 𝟙 _ := by monoidal
      _ = 𝟙 _ ⊗≫ η_ X X' ▷ (X ⊗ Y)
            ⊗≫ (X ◁ (𝟙_ C ◁ ε_ X X' ≫ η_ Y Y' ▷ 𝟙_ C) ▷ Y)
            ⊗≫ (X ⊗ Y) ◁ ε_ Y Y' ⊗≫ 𝟙 _ := by rw [whisker_exchange]
      _ = 𝟙 _ ⊗≫ (η_ X X' ▷ X ⊗≫ X ◁ ε_ X X') ▷ Y
            ⊗≫ X ◁ (η_ Y Y' ▷ Y ⊗≫ Y ◁ ε_ Y Y') ⊗≫ 𝟙 _ := by monoidal
      _ = _ := by
            rw [ExactPairing.evaluation_coevaluation'', ExactPairing.evaluation_coevaluation'']
            monoidal

/-- In a right-rigid category, `X ⊗ Y` has `Yᘁ ⊗ Xᘁ` as a right dual. -/
noncomputable def hasRightDualTensor (X Y : C) [HasRightDual X] [HasRightDual Y] :
    HasRightDual (X ⊗ Y) where
  rightDual := (Y : C)ᘁ ⊗ (X : C)ᘁ
  exact := tensorExactPairing X ((X : C)ᘁ) Y ((Y : C)ᘁ)

/-- **Duals reverse order**: `(X ⊗ Y)ᘁ ≅ Yᘁ ⊗ Xᘁ`, in any right-rigid category.

Both are right duals of `X ⊗ Y` — the canonical one, and the one `tensorExactPairing` builds —
so `rightDualIso` compares them. -/
noncomputable def tensorRightDualIso [RightRigidCategory C] (X Y : C) :
    ((X ⊗ Y : C)ᘁ : C) ≅ ((Y : C)ᘁ ⊗ (X : C)ᘁ) :=
  rightDualIso (HasRightDual.exact (X := X ⊗ Y))
    (tensorExactPairing X ((X : C)ᘁ) Y ((Y : C)ᘁ))

/-- Right-dualising an isomorphism.  Contravariant, so the mate of `i.inv` is the forward map. -/
@[simps]
noncomputable def rightDualMapIso [RightRigidCategory C] {A B : C} (i : A ≅ B) :
    ((A : C)ᘁ : C) ≅ ((B : C)ᘁ : C) where
  hom := rightAdjointMate i.inv
  inv := rightAdjointMate i.hom
  hom_inv_id := by rw [← comp_rightAdjointMate, i.hom_inv_id, rightAdjointMate_id]
  inv_hom_id := by rw [← comp_rightAdjointMate, i.inv_hom_id, rightAdjointMate_id]

/-- **The double dual of a tensor product**, `(X ⊗ Y)ᘁᘁ ≅ Xᘁᘁ ⊗ Yᘁᘁ`.

`tensorRightDualIso` twice.  The order reverses on each application, so it comes back to `X, Y`
rather than staying swapped — which is exactly why the *double* dual, and not the single one, is
what a **monoidal** pivotal structure compares against. -/
noncomputable def tensorDoubleDualIso [RightRigidCategory C] (X Y : C) :
    ((((X ⊗ Y : C)ᘁ : C)ᘁ : C)) ≅ ((((X : C)ᘁ : C)ᘁ) ⊗ (((Y : C)ᘁ : C)ᘁ)) :=
  rightDualMapIso (tensorRightDualIso X Y) ≪≫ tensorRightDualIso ((Y : C)ᘁ) ((X : C)ᘁ)

/-- **The dual comparison of a tensor product is the tensor of the dual comparisons.**

Both `tensorExactPairing X X₁ Y Y₁` and `tensorExactPairing X X₂ Y Y₂` exhibit a right dual of
`X ⊗ Y`, so `rightDualIso` compares them; the claim is that this comparison factors as the tensor
of the two componentwise comparisons.  Note the **order reversal** on the right: the dual of a
tensor is the tensor of the duals *in the opposite order*, so the `Y`-comparison comes first.

Proved by uniqueness (`rightDualIso_hom_unique`): it suffices that the right-hand side satisfies
the same evaluation identity, and that is the two componentwise identities plus one application of
the interchange law.  Purely formal — no braiding, no rigidity beyond the two pairings. -/
theorem rightDualIso_tensorExactPairing {X X₁ X₂ Y Y₁ Y₂ : C}
    (p₁ : ExactPairing X X₁) (p₂ : ExactPairing X X₂)
    (r₁ : ExactPairing Y Y₁) (r₂ : ExactPairing Y Y₂) :
    (rightDualIso (tensorExactPairing X X₁ Y Y₁) (tensorExactPairing X X₂ Y Y₂)).hom
      = (rightDualIso r₁ r₂).hom ⊗ₘ (rightDualIso p₁ p₂).hom := by
  refine (rightDualIso_hom_unique _ _ _ ?_).symm
  have hX := rightDualIso_hom_evaluation p₁ p₂
  have hY := rightDualIso_hom_evaluation r₁ r₂
  set rX := (rightDualIso p₁ p₂).hom
  set rY := (rightDualIso r₁ r₂).hom
  show ((rY ⊗ₘ rX) ▷ (X ⊗ Y)) ≫ (𝟙 _ ⊗≫ Y₂ ◁ ε_ X X₂ ▷ Y ⊗≫ ε_ Y Y₂)
      = 𝟙 _ ⊗≫ Y₁ ◁ ε_ X X₁ ▷ Y ⊗≫ ε_ Y Y₁
  rw [tensorHom_def]
  calc _ = (rY ▷ X₁) ▷ (X ⊗ Y) ⊗≫ Y₂ ◁ (((rX ▷ X) ≫ ε_ X X₂) ▷ Y) ⊗≫ ε_ Y Y₂ := by
            monoidal
    -- the `X`-comparison is absorbed into the inner evaluation
    _ = 𝟙 _ ⊗≫ (rY ▷ ((X₁ ⊗ X) ⊗ Y) ≫ Y₂ ◁ (ε_ X X₁ ▷ Y)) ⊗≫ ε_ Y Y₂ := by
            rw [hX]; monoidal
    -- interchange: `rY` and the inner evaluation act on disjoint strands
    _ = 𝟙 _ ⊗≫ (Y₁ ◁ (ε_ X X₁ ▷ Y) ≫ rY ▷ (𝟙_ C ⊗ Y)) ⊗≫ ε_ Y Y₂ := by
            rw [← whisker_exchange rY (ε_ X X₁ ▷ Y)]
    _ = 𝟙 _ ⊗≫ Y₁ ◁ (ε_ X X₁ ▷ Y) ⊗≫ ((rY ▷ Y) ≫ ε_ Y Y₂) := by monoidal
    -- and now the `Y`-comparison
    _ = _ := by rw [hY]

end QOU.MathlibExt
