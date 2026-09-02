/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.PivotalCategory
import QOU.MathlibExt.BraidedTensorDual
import QOU.MathlibExt.TwistedQuantumDimension

/-!
# QOU.MathlibExt.SphericalCategory — the spherical condition, and every ribbon category satisfies it

[`QOU/MathlibExt/PivotalCategory.lean`](PivotalCategory.lean) supplies the two entries of Mathlib's
rigid-category "Future work" list that concern dualisation as a functor and pivotal categories, and
closes with a section headed *"What is still not proved"* whose entire content is:

> Sphericality — that the left and right quantum dimensions agree — is a separate condition and is
> not touched here.  A pivotal structure does not imply it.

This file supplies it.

## Main definitions

* `qDimPivotalRight X`, `qDimPivotalLeft X` — the two quantum dimensions of an object in a pivotal
  category, closing the loop through the pivotor in the two possible directions.  **Neither mentions
  a braiding**, which is what makes the class below the right shape for Mathlib and distinguishes it
  from `QOU.BraidKnot.SphericalStructure` (see the comparison below).
* `SphericalCategory C` — a pivotal category in which the two agree, for every object.

## Main statements

* `qDimPivotalRight_eq_qDimTwistedWith`, `qDimPivotalLeft_eq_qDimTwistedLeftWith` — under
  `pivotalOfRibbon`, the two pivotal dimensions **are** the twisted braided closures
  `qDimTwistedWith X Xᘁ` and `qDimTwistedLeftWith X Xᘁ` of
  [`TwistedQuantumDimension.lean`](TwistedQuantumDimension.lean).  These are the bridge: the pivotal
  side is braiding-free by construction, the twisted side is where the geometry was done.
* `sphericalOfRibbon` — **every ribbon right-rigid category is spherical.**  Barrett–Westbury's
  classical statement, and the reason the pivotal structure of a ribbon category is the one worth
  having.  Derived, not assumed: the field is discharged by `qDimTwistedLeftWith_eq`.
## Relation to `QOU.BraidKnot.KeystonePivotalSpherical.SphericalStructure`

That class is a **different object** and both should stay. It is stated over the *twistless* braided
closure `η ≫ β ≫ ε`, and its `leftQDim_eq` is an **asserted hypothesis**: bean `qou-djk4` established
that no axiom of a braided rigid category forces the two twistless closures together, because they
differ by the monodromy `(β_ B A).inv` against `(β_ A B).hom`.  So `SphericalStructure` is the right
object exactly where there is no twist available, and it is not derivable from ribbon at any twist,
including the trivial one.

`SphericalCategory` below is the opposite trade: it asks for a pivotal structure, and in exchange
the condition it names *is* derivable — that is `sphericalOfRibbon`.

## Non-vacuity

`qDimPivotalLeft X = qDimPivotalRight X := rfl` is **rejected** by the elaborator, so the class
field relates two genuinely distinct morphisms rather than restating one.  (Checked, not assumed —
the same check `qou-djk4` applied to `qDimTwistedLeftWith`.)
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory BraidedCategory

variable {C : Type*} [Category C] [MonoidalCategory C]

section Pivotal

open QOU.MathlibExt.PivotalCategory

variable [RightRigidCategory C]

/-- **The right quantum dimension of an object in a pivotal category**: open the loop with the
coevaluation of `X ⊣ Xᘁ`, cross to the double dual with the pivotor, and close with the evaluation
of `Xᘁ ⊣ Xᘁᘁ`.  No braiding. -/
noncomputable def qDimPivotalRight [PivotalCategory C] (X : C) : (𝟙_ C ⟶ 𝟙_ C) :=
  η_ X ((X : C)ᘁ) ≫ ((pivotorApp X).hom ▷ ((X : C)ᘁ)) ≫ ε_ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ)

/-- **The left quantum dimension**: the mirror image — open with the coevaluation of `Xᘁ ⊣ Xᘁᘁ`,
come back along the pivotor, and close with the evaluation of `X ⊣ Xᘁ`.  No braiding. -/
noncomputable def qDimPivotalLeft [PivotalCategory C] (X : C) : (𝟙_ C ⟶ 𝟙_ C) :=
  η_ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ) ≫ (((X : C)ᘁ) ◁ (pivotorApp X).inv) ≫ ε_ X ((X : C)ᘁ)

/-- **A spherical category**: a pivotal category whose two quantum dimensions agree.

This is a *condition* on a pivotal structure, not extra data, and it does not follow from pivotality
— see the module docstring.  `sphericalOfRibbon` below derives it from a balancing. -/
class SphericalCategory (C : Type*) [Category C] [MonoidalCategory C] [RightRigidCategory C]
    extends PivotalCategory C where
  /-- The left and right quantum dimensions of every object agree. -/
  qDimPivotalLeft_eq_qDimPivotalRight : ∀ X : C, qDimPivotalLeft X = qDimPivotalRight X

section Balanced

variable [BraidedCategory C] [BalancedCategory C]

/-- **The right pivotal dimension is the twisted braided closure.**

`pivotalOfRibbon`'s pivotor is `θ_X ≫ drinfeldIso X`, and `drinfeldIso` is by definition the
comparison of `X` and `Xᘁᘁ` as right duals of `Xᘁ`; `rightDualIso_hom_evaluation` is exactly the
statement that it converts the evaluation of `Xᘁ ⊣ Xᘁᘁ` into the swapped evaluation
`β ≫ ε`, which is the closure `qDimTwistedWith` uses. -/
theorem qDimPivotalRight_eq_qDimTwistedWith (X : C) :
    qDimPivotalRight X = qDimTwistedWith X ((X : C)ᘁ) := by
  show η_ X ((X : C)ᘁ) ≫ ((BalancedCategory.twist X ≫ (drinfeldIso X).hom) ▷ ((X : C)ᘁ))
        ≫ ε_ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ) = _
  rw [comp_whiskerRight, Category.assoc, drinfeldIso, rightDualIso_hom_evaluation]
  rfl

/-- **The left pivotal dimension is the twisted braided closure taken the other way.**

The evaluation form does not reach this one — the pivotor appears whiskered on the *left*, against a
coevaluation — which is what `coev_comp_rightDualIso` is for.  After it, the swapped coevaluation
`η ≫ β⁻¹` appears literally, and braiding naturality moves the inverse twist from one side of it to
the other. -/
theorem qDimPivotalLeft_eq_qDimTwistedLeftWith (X : C) :
    qDimPivotalLeft X = qDimTwistedLeftWith X ((X : C)ᘁ) := by
  show η_ ((X : C)ᘁ) (((X : C)ᘁ : C)ᘁ)
        ≫ (((X : C)ᘁ) ◁ ((drinfeldIso X).inv ≫ inv (BalancedCategory.twist X)))
        ≫ ε_ X ((X : C)ᘁ) = _
  rw [MonoidalCategory.whiskerLeft_comp, ← Category.assoc,
    ← coev_comp_rightDualIso (BraidedCategory.exactPairing_swap X ((X : C)ᘁ))
      (HasRightDual.exact (X := ((X : C)ᘁ)))]
  simp only [Category.assoc]
  rw [← drinfeldIso, ← MonoidalCategory.whiskerLeft_comp_assoc, Iso.hom_inv_id,
    MonoidalCategory.whiskerLeft_id, Category.id_comp]
  show (η_ X ((X : C)ᘁ) ≫ (β_ ((X : C)ᘁ) X).inv)
        ≫ (((X : C)ᘁ) ◁ inv (BalancedCategory.twist X)) ≫ ε_ X ((X : C)ᘁ) = _
  have hnat : ∀ (Z : C) (k : ((X : C)ᘁ) ⊗ X ⟶ Z),
      (β_ ((X : C)ᘁ) X).inv ≫ (((X : C)ᘁ) ◁ inv (BalancedCategory.twist X)) ≫ k
        = (inv (BalancedCategory.twist X) ▷ ((X : C)ᘁ)) ≫ (β_ ((X : C)ᘁ) X).inv ≫ k := by
    intro Z k
    rw [← Category.assoc, ← Category.assoc]
    congr 1
    rw [Iso.inv_comp_eq, ← Category.assoc, Iso.eq_comp_inv]
    exact braiding_naturality_right ((X : C)ᘁ) (inv (BalancedCategory.twist X))
  rw [qDimTwistedLeftWith, Category.assoc, hnat]

end Balanced

section Ribbon

variable [BraidedCategory C] [RibbonCategory C]

/-- **Every ribbon right-rigid category is spherical** (Barrett–Westbury).

The pivotal structure is `pivotalOfRibbon`; the condition is discharged by
`qDimTwistedLeftWith_eq`, where the ribbon axiom is used exactly once, on the cap. -/
noncomputable instance (priority := 100) sphericalOfRibbon : SphericalCategory C where
  __ := pivotalOfRibbon
  qDimPivotalLeft_eq_qDimPivotalRight X := by
    rw [qDimPivotalLeft_eq_qDimTwistedLeftWith, qDimPivotalRight_eq_qDimTwistedWith]
    exact qDimTwistedLeftWith_eq X

end Ribbon

end Pivotal

end QOU.MathlibExt
