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

* `PivotalCategory.ofPointwise` / `pivotor_naturality` — the functorial form and the pointwise form
  (an `X ≅ Xᘁᘁ` for each `X`, plus a naturality square against the double mate) carry the same data.
  The pointwise form is what a string-diagram argument produces; the functorial form is what Mathlib
  asked for.  Having both means a proof in either style lands.
* `drinfeldIso` — **in a braided right-rigid category every object is isomorphic to its double
  dual**, `X ≅ Xᘁᘁ`.  Both `X` and `Xᘁᘁ` are right duals of `Xᘁ` — the first because
  `BraidedCategory.exactPairing_swap` turns the pairing `X ⊣ Xᘁ` around — and right duals are unique
  up to canonical isomorphism (`rightDualIso`).  Sorry-free and unconditional.

## What is NOT proved here (STRICT, §Axiomatization-is-NOT-a-Proof)

`drinfeldIso` is **pointwise**.  Upgrading it to a `PivotalCategory` instance needs its
**naturality** — `f ≫ drinfeldIso Y = drinfeldIso X ≫ (fᘁ)ᘁ` — which is a string-diagram coherence
argument, not a rewrite of the pieces above.  That step is open and is deliberately *not* added as a
class field: asserting it would assume the conclusion.  Consequently `PivotalCategory` is declared
without an instance, which is the honest representation of that open state.  The concrete route with
the fewest unknowns is `FGModuleCat K` (Mathlib's one `RightRigidCategory` instance), where the
pivotor is `Module.evalEquiv`.

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

Pointwise and unconditional.  Its **naturality** — which is what would make this a
`PivotalCategory` instance — is a string-diagram argument and is not proved here; see the module
docstring. -/
noncomputable def drinfeldIso (X : C) : X ≅ ((X : C)ᘁ : C)ᘁ :=
  rightDualIso (BraidedCategory.exactPairing_swap X Xᘁ) (HasRightDual.exact (X := Xᘁ))

end Braided

end QOU.MathlibExt
