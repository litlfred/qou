/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Braided

/-!
# QOU.MathlibExt.PivotalCategory — the dual functors and pivotal categories

Mathlib's `Mathlib/CategoryTheory/Monoidal/Rigid/Basic.lean` carries a **"Future work"** list, and
two of its five entries are exactly this file's subject, quoted verbatim:

> * Show that `ᘁ` gives an equivalence of categories `C ≅ (Cᵒᵖ)ᴹᵒᵖ`.
> * Define pivotal categories (rigid categories equipped with a natural isomorphism `ᘁᘁ ≅ 𝟙 C`).

Neither exists yet: `grep -n "Functor" Mathlib/CategoryTheory/Monoidal/Rigid/Basic.lean` returns
nothing, so right-dualisation is not even a functor in Mathlib, and `[Pp]ivotal` occurs in the whole
of `Mathlib/CategoryTheory/` only in that one TODO line.  So the pivotal class *cannot* be stated in
Mathlib's own requested form until the functor exists.  This file supplies both, in that order.

It imports only Mathlib and is stated over Mathlib's `RightRigidCategory` / `BraidedCategory`, so it
can be lifted upstream verbatim.  Companion module:
[`QOU/MathlibExt/Ribbon.lean`](Ribbon.lean) (the balancing twist, the other missing half).

## Main definitions

* `rightDualFunctor C : Cᵒᵖ ⥤ C` — right-dualisation as a functor.  It is contravariant, which is
  why the source is `Cᵒᵖ`; functoriality is `rightAdjointMate_id` and `comp_rightAdjointMate`.
* `doubleDualFunctor C : C ⥤ C` — `X ↦ Xᘁᘁ`, `f ↦ (fᘁ)ᘁ`.  Covariant, being dualisation twice.
* `PivotalCategory C` — Mathlib's requested shape: a natural isomorphism `𝟭 C ≅ ᘁᘁ`.

## Main statements

* `pivotalOfBraided` — **every braided right-rigid category is pivotal.**  The instance, built from
  `drinfeldIso` and its naturality.
* `rightAdjointMate_congr_dual` — the mate is independent of the choice of dual, up to
  `rightDualIso`.  Mathlib has no naturality lemma for `rightDualIso`.
* `swap_mate_mate` — the double mate against swapped pairings is the identity; the braided form of
  Mathlib's "left adjoint mate of the right adjoint mate is the morphism itself" entry.
* `PivotalCategory.ofPointwise` / `pivotor_naturality` — the functorial form and the pointwise form
  (an `X ≅ Xᘁᘁ` for each `X`, plus a naturality square against the double mate) carry the same data.
  The pointwise form is what a string-diagram argument produces; the functorial form is what Mathlib
  asked for.  Having both means a proof in either style lands.
* `drinfeldIso` — **in a braided right-rigid category every object is isomorphic to its double
  dual**, `X ≅ Xᘁᘁ`.  Both `X` and `Xᘁᘁ` are right duals of `Xᘁ` — the first because
  `BraidedCategory.exactPairing_swap` turns the pairing `X ⊣ Xᘁ` around — and right duals are unique
  up to canonical isomorphism (`rightDualIso`).  Sorry-free and unconditional.

## The naturality, and a correction

`drinfeldIso` is pointwise; a `PivotalCategory` instance needs its **naturality**,
`f ≫ drinfeldIso Y = drinfeldIso X ≫ (fᘁ)ᘁ`.  An earlier revision of this file recorded that as
open, on the strength of a probe in which `simp [drinfeldIso, rightDualIso, rightAdjointMate]`
unfolded the goal to a ~20-term identity resembling Mathlib's `coevaluation_evaluation_braided'`.

**That assessment was wrong, and it is retracted.**  The error was attacking the *definition* of the
mate instead of its *algebra*.  Nothing here needs a Whitney move; the proof is two general lemmas
Mathlib is missing, each of which follows from lemmas Mathlib already has:

* `rightAdjointMate_congr_dual` — **the mate does not depend on the choice of dual**, up to
  `rightDualIso`.  Both sides rewrite, via `comp_rightAdjointMate` with explicit instance arguments,
  to the *mixed* mate taken with one object's first dual and the other's second.  Mathlib has no
  naturality lemma for `rightDualIso` at all — `rightDualIso_id` is the only lemma about it.
* `swap_mate_mate` — **taking the mate twice, the second time against the swapped pairings, is the
  identity**: `(fᘁ)ᘁ = f` when `X` is read as the right dual of `Xᘁ` via
  `BraidedCategory.exactPairing_swap`.  This is the braided form of Mathlib's "Future work" entry
  *"Show that the left adjoint mate of the right adjoint mate of a morphism is the morphism
  itself."*  Proved by evaluating both sides against `ε` and cancelling: the map
  `g ↦ (g ▷ Yᘁ) ≫ ε` is injective because `tensorRightHomEquiv` carries it to `g ≫ (λ_ Y).inv`.

Composing them gives `drinfeldIso_naturality`, and hence `pivotalOfBraided` — **every braided
right-rigid category is pivotal**, unconditionally and sorry-free.  Since `FGModuleCat K` is
symmetric and right-rigid, it is now pivotal too, with no linear algebra involved.

## What is still not proved

Sphericality — that the left and right quantum dimensions agree — is a separate condition and is
not touched here.  A pivotal structure does not imply it.

## References

* Mathlib, `CategoryTheory/Monoidal/Rigid/Basic.lean`, "Future work" (the two entries above).
* [turaev1994] Turaev, *Quantum invariants of knots and 3-manifolds* — pivotal and spherical
  categories, and the Drinfeld morphism in the braided case.

-- Ref: [manuscript] docs/coordination/s5-so3-keystone.md
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory Opposite

section Functors

universe v u

variable (C : Type u) [Category.{v} C] [MonoidalCategory C] [RightRigidCategory C]

/-- **Right-dualisation as a functor** `Cᵒᵖ ⥤ C`.  `rightAdjointMate` is contravariant
(`fᘁ : Yᘁ ⟶ Xᘁ` for `f : X ⟶ Y`), so the source is `Cᵒᵖ`.  This is the functor Mathlib's
"Future work" entry *"`ᘁ` gives an equivalence of categories `C ≅ (Cᵒᵖ)ᴹᵒᵖ`"* presupposes. -/
@[simps]
def rightDualFunctor : Cᵒᵖ ⥤ C where
  obj X := (unop X)ᘁ
  map f := (f.unop)ᘁ
  map_id _ := rightAdjointMate_id
  map_comp _ _ := comp_rightAdjointMate

/-- **The double-dual endofunctor** `X ↦ Xᘁᘁ`.  Dualising twice is covariant, so this is an
endofunctor of `C` — the `ᘁᘁ` of Mathlib's pivotal-category TODO. -/
def doubleDualFunctor : C ⥤ C where
  obj X := ((X : C)ᘁ : C)ᘁ
  map {_ _} f := rightAdjointMate (rightAdjointMate f)
  map_id _ := by rw [rightAdjointMate_id, rightAdjointMate_id]
  map_comp _ _ := by rw [comp_rightAdjointMate, comp_rightAdjointMate]

@[simp] theorem doubleDualFunctor_obj (X : C) :
    (doubleDualFunctor C).obj X = ((X : C)ᘁ : C)ᘁ := rfl

@[simp] theorem doubleDualFunctor_map {X Y : C} (f : X ⟶ Y) :
    (doubleDualFunctor C).map f = rightAdjointMate (rightAdjointMate f) := rfl

end Functors

/-- **A pivotal category**, in the shape Mathlib's "Future work" list asks for: a right-rigid
monoidal category equipped with a natural isomorphism `𝟭 C ≅ ᘁᘁ`.

The single field is *data*, not an assertion — the pivotor is a choice, and different choices give
different (spherical or not) theories.  See `ofPointwise` for the equivalent object-wise
presentation. -/
class PivotalCategory (C : Type*) [Category C] [MonoidalCategory C] [RightRigidCategory C] where
  /-- The pivotor: a natural isomorphism identifying each object with its double dual. -/
  pivotor : 𝟭 C ≅ doubleDualFunctor C

namespace PivotalCategory

variable {C : Type*} [Category C] [MonoidalCategory C] [RightRigidCategory C]

section

variable [PivotalCategory C]

/-- The pivotor at an object: `X ≅ Xᘁᘁ`. -/
def pivotorApp (X : C) : X ≅ ((X : C)ᘁ : C)ᘁ := (pivotor (C := C)).app X

/-- **Naturality of the pivotor**, object-wise: it commutes with the double mate.  This is the form
a string-diagram argument produces, and it is exactly `NatTrans.naturality` for `pivotor`. -/
theorem pivotor_naturality {X Y : C} (f : X ⟶ Y) :
    f ≫ (pivotorApp Y).hom = (pivotorApp X).hom ≫ rightAdjointMate (rightAdjointMate f) :=
  (pivotor (C := C)).hom.naturality f

end

/-- **Build a pivotal structure from object-wise data.**  A choice of `X ≅ Xᘁᘁ` for each `X`, plus
the naturality square, *is* a natural isomorphism `𝟭 C ≅ ᘁᘁ`.  Together with `pivotor_naturality`
this says the two presentations carry the same data, so a proof in either style lands. -/
def ofPointwise (p : ∀ X : C, X ≅ ((X : C)ᘁ : C)ᘁ)
    (hp : ∀ {X Y : C} (f : X ⟶ Y),
      f ≫ (p Y).hom = (p X).hom ≫ rightAdjointMate (rightAdjointMate f)) :
    PivotalCategory C where
  pivotor := NatIso.ofComponents p (fun f => hp f)

end PivotalCategory

section Braided

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]

/-- **In a braided right-rigid category every object is isomorphic to its double dual**,
`X ≅ Xᘁᘁ` — the Drinfeld isomorphism.

The argument is uniqueness of duals, twice over.  `X` and `Xᘁ` form an exact pairing by rigidity;
`BraidedCategory.exactPairing_swap` turns that pairing around, so `X` is a right dual **of** `Xᘁ`.
But `Xᘁᘁ` is the chosen right dual of `Xᘁ`, and right duals are unique up to canonical isomorphism
(`rightDualIso`).

Pointwise and unconditional; its naturality is `drinfeldIso_naturality` below. -/
noncomputable def drinfeldIso (X : C) : X ≅ ((X : C)ᘁ : C)ᘁ :=
  rightDualIso (BraidedCategory.exactPairing_swap X Xᘁ) (HasRightDual.exact (X := Xᘁ))

end Braided

/-! ### Naturality of the Drinfeld isomorphism

Two general lemmas Mathlib lacks, then the instance.  Neither needs a string-diagram argument; see
the module docstring for the retraction of the claim that they did. -/

/-- **The right adjoint mate does not depend on the choice of duals**, up to `rightDualIso`.

Both sides are the *mixed* mate — taken with `X`'s second dual and `Y`'s first — reached by
`comp_rightAdjointMate` with explicit instance arguments, composing `f` with an identity on either
side.  Mathlib has no naturality lemma for `rightDualIso`; `rightDualIso_id` is the only one. -/
theorem rightAdjointMate_congr_dual {C : Type*} [Category C] [MonoidalCategory C] {X Y : C}
    (f : X ⟶ Y) (dX₁ dX₂ : HasRightDual X) (dY₁ dY₂ : HasRightDual Y) :
    (@rightAdjointMate C _ _ X Y dX₁ dY₁ f) ≫ (rightDualIso dX₁.exact dX₂.exact).hom
      = (rightDualIso dY₁.exact dY₂.exact).hom ≫ (@rightAdjointMate C _ _ X Y dX₂ dY₂ f) := by
  show _ ≫ (@rightAdjointMate C _ _ X X dX₂ dX₁ (𝟙 X)) = _
  rw [← @comp_rightAdjointMate C _ _ X X Y dX₂ dX₁ dY₁ (𝟙 X) f]
  show _ = (@rightAdjointMate C _ _ Y Y dY₂ dY₁ (𝟙 Y)) ≫ _
  rw [← @comp_rightAdjointMate C _ _ X Y Y dX₂ dY₂ dY₁ f (𝟙 Y)]
  rw [Category.id_comp, Category.comp_id]

section Evaluation

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

end Evaluation

section BraidedNaturality

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]

/-- `X` as a right dual **of** `Xᘁ`, via `BraidedCategory.exactPairing_swap`.  Deliberately a `def`
and not an instance: `Xᘁ` already has a right dual from `RightRigidCategory`, and this is the other
one. -/
noncomputable def swapRightDual (X : C) : HasRightDual (Xᘁ) where
  rightDual := X
  exact := BraidedCategory.exactPairing_swap X Xᘁ

/-- **Taking the mate twice, the second time against the swapped pairings, is the identity.**

The braided form of Mathlib's "Future work" entry *"Show that the left adjoint mate of the right
adjoint mate of a morphism is the morphism itself."*

Both `(fᘁ)ᘁ` and `f` satisfy the same identity against the evaluation — for `f` by braiding
naturality on each side plus `rightAdjointMate_comp_evaluation` — and pairing against the
evaluation is injective. -/
theorem swap_mate_mate {X Y : C} (f : X ⟶ Y) :
    @rightAdjointMate C _ _ (Yᘁ) (Xᘁ) (swapRightDual Y) (swapRightDual X) (fᘁ) = f := by
  letI eY : ExactPairing (Yᘁ) Y := BraidedCategory.exactPairing_swap Y Yᘁ
  letI eX : ExactPairing (Xᘁ) X := BraidedCategory.exactPairing_swap X Xᘁ
  apply whiskerRight_evaluation_injective (Y' := Yᘁ)
  have key := @rightAdjointMate_comp_evaluation C _ _ (Yᘁ) (Xᘁ)
      (swapRightDual Y) (swapRightDual X) (fᘁ)
  simp only []
  rw [key]
  show (X ◁ fᘁ) ≫ ((β_ X (Xᘁ)).hom ≫ ε_ X (Xᘁ))
      = (f ▷ (Yᘁ)) ≫ ((β_ Y (Yᘁ)).hom ≫ ε_ Y (Yᘁ))
  rw [← Category.assoc, BraidedCategory.braiding_naturality_right, ← Category.assoc,
      BraidedCategory.braiding_naturality_left, Category.assoc, Category.assoc,
      rightAdjointMate_comp_evaluation]

/-- **Naturality of the Drinfeld isomorphism.**  `rightAdjointMate_congr_dual` compares the two
duals of `Xᘁ`; `swap_mate_mate` identifies the mate taken against the swapped pairings with `f`. -/
theorem drinfeldIso_naturality {X Y : C} (f : X ⟶ Y) :
    f ≫ (drinfeldIso Y).hom
      = (drinfeldIso X).hom ≫ rightAdjointMate (rightAdjointMate f) := by
  conv_lhs => rw [← swap_mate_mate f]
  exact rightAdjointMate_congr_dual (fᘁ) (swapRightDual Y) inferInstance
    (swapRightDual X) inferInstance

/-- **Every braided right-rigid category is pivotal.**

The pivotor is the Drinfeld isomorphism.  Unconditional and sorry-free, so the class is inhabited
across every braided rigid category Mathlib has — `FGModuleCat K` among them, since it is symmetric,
with no linear algebra involved. -/
noncomputable instance (priority := 100) pivotalOfBraided : PivotalCategory C :=
  PivotalCategory.ofPointwise drinfeldIso (fun f => drinfeldIso_naturality f)

end BraidedNaturality

end QOU.MathlibExt
