/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Braided
import QOU.MathlibExt.RightDualIsoUnique
import QOU.MathlibExt.RigidTensorDual

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

* `PivotalCategory` — the class, carrying **both** the pivotor and its monoidality
  (`pivotor_tensor`).  The instance satisfying it is `QOU.MathlibExt.pivotalOfRibbon`, which lives
  downstream of the twist; there is deliberately no braided-only instance, and the note further
  down says why.
* `rightAdjointMate_congr_dual` — the mate is independent of the choice of dual, up to
  `rightDualIso`.  Mathlib has no naturality lemma for `rightDualIso`.
* `rightDualIso_hom_unique` / `rightDualIso_hom_trans` — the comparison of two right duals is
  *uniquely* determined by commuting with the evaluations, and such comparisons compose.  Mathlib
  carries `rightDualIso` and `rightDualIso_id` and nothing else about it; uniqueness is what makes
  the comparison usable, since it turns "construct the map" into "check one identity".
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

Composing them gives `drinfeldIso_naturality` — the Drinfeld isomorphism is a natural isomorphism
`𝟭 C ≅ ᘁᘁ` on **every** braided right-rigid category, unconditionally and sorry-free.

*That is naturality only.*  An earlier revision promoted it to an instance
`pivotalOfBraided : PivotalCategory C` and claimed every braided right-rigid category pivotal; with
the monoidality field present that instance is unconstructible, because the claim is false.  What
survives, and is enough for `FGModuleCat K`, is `pivotalOfRibbon`: symmetric ⇒ balanced ⇒ ribbon,
so the symmetric rigid categories are still pivotal with no linear algebra involved.

## Sphericality — no longer open

Sphericality — that the left and right quantum dimensions agree — is a separate condition and is
still not *implied* by a pivotal structure, which is why it is a class of its own rather than a
theorem here.  It is, however, no longer unproved: `QOU.MathlibExt.SphericalCategory` states it in
the braiding-free pivotal form, and `QOU.MathlibExt.sphericalOfRibbon` derives it for every ribbon
right-rigid category (Barrett–Westbury), via the two bridges identifying the pivotal dimensions of
`pivotalOfRibbon` with the twisted braided closures of
`QOU.MathlibExt.TwistedQuantumDimension`.

*This section previously read "not touched here" with nothing further, and that was accurate when
written.  It is corrected rather than deleted so the reader can see that the gap was named before
it was closed.*

## `PivotalCategory` carries the monoidality field — and `drinfeldIso` cannot satisfy it

A pivotal structure in the literature is a **monoidal** natural isomorphism: on top of naturality it
must satisfy

```
pivotor (X ⊗ Y) ≫ (tensorDoubleDualIso X Y).hom = pivotor X ⊗ₘ pivotor Y
```

against the comparison `(X ⊗ Y)ᘁᘁ ≅ Xᘁᘁ ⊗ Yᘁᘁ` (`QOU.MathlibExt.tensorDoubleDualIso`).  The class
below carries that as `pivotor_tensor`, so `[PivotalCategory C]` now means what the literature
means and Barrett–Westbury applies to it with no side condition.

*Earlier revisions of this file omitted the field, and said so with a warning not to add it while
`pivotalOfBraided` existed.  Both are resolved: the field is here and that instance is gone.*

**`drinfeldIso` is natural but NOT monoidal.**  A braided right-rigid category is therefore *not*
pivotal in the monoidal sense — braiding alone is not enough.  Two independent arguments:

* **Hopf-algebraic.**  For a quasitriangular Hopf algebra the Drinfeld element `u` implements `S²`
  and satisfies `Δ(u) = (u ⊗ u)(R₂₁R)⁻¹` (Kassel, *Quantum Groups* XIV.6).  `u` is grouplike — which
  is what monoidality of the induced `X ⟶ Xᘁᘁ` means — exactly when the monodromy `R₂₁R` is trivial,
  i.e. essentially only in the symmetric case.  In `Rep U_q(sl₂)` it is not.
* **Diagrammatic.**  Monoidality reduces (see `rightDualIso_tensorExactPairing`) to comparing two
  exact pairings on `Yᘁ ⊗ Xᘁ`: `exactPairing_swap` of `tensorExactPairing`, against
  `tensorExactPairing` of the two `exactPairing_swap`s.  Expanding the block braiding
  `β_{X ⊗ Y, Yᘁ ⊗ Xᘁ}` by the two hexagons gives four crossings.  Two of them pair off with the two
  caps and reproduce the componentwise comparisons; the surviving two are `X` over `Yᘁ` and `Y` over
  `Xᘁ`.  Closing the caps joins `X` to `Xᘁ` and `Y` to `Yᘁ` into two loops, and — *counting with the
  orientation reversal at each cap*, which is the step that makes this come out non-trivial — those
  two crossings have the **same** sign.  The loops are Hopf-linked, not unlinked: the discrepancy is
  the monodromy `(β_ X Y).hom ≫ (β_ Y X).hom`, not the identity.

This retracts the scoping of the monoidality step, which had been recorded as "the last hard step"
of a proof that was expected to go through.  It does not affect anything already proved here:
`drinfeldIso` and `drinfeldIso_naturality` are statements about naturality only and stand
unchanged.  What it did cost was the instance built from them — see the note where
`pivotalOfBraided` used to be.

## The corrected statement: ribbon, not merely braided

The monodromy is precisely what a **balancing** cancels.  With `θ` satisfying
`θ_{X ⊗ Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)` (`QOU.MathlibExt.BalancedCategory.twist_tensor`),
and using that `θ_X ⊗ θ_Y` commutes with the monodromy by naturality of the braiding, the twisted
map `θ_X ≫ drinfeldIso X` *is* monoidal.  The direction was open when this was written and is now
settled: it is `θ`, not `θ⁻¹`.  The instance is
**`QOU.MathlibExt.pivotalOfRibbon`** — a ribbon category is pivotal, which is the classical
statement (a ribbon element `v` makes `uv⁻¹` grouplike).

The diagrammatic argument above is **proved**, in `QOU.MathlibExt.BraidedTensorDual`:
`rightDualIso_swap_tensor` states that the two pairings differ by exactly the inverse monodromy,
and `twist_drinfeld_monoidal` that the balancing axiom cancels it.

**An earlier revision of this paragraph predicted the wrong route, and the prediction is
retracted.**  It said the formal content would be a lemma Mathlib also lacks — that in a braided
rigid category the braiding against a *dual* leg, `β_{X, Yᘁ}`, is the bent-round *inverse* braiding
`β_{Y,X}⁻¹`.  No such lemma was needed.  What the proof actually turns on is weaker and more
general: a strand crossing **any** cap `c : A ⊗ B ⟶ 𝟙` can be pushed off it at the cost of braiding
past each leg separately (`QOU.MathlibExt.braiding_slide_cap_right`), with nothing assumed of `c`
beyond its type — no rigidity, no exact pairing.  Applying that once per leg of a dual pair leaves
two inverse braidings, and those are the monodromy.

## References

* Mathlib, `CategoryTheory/Monoidal/Rigid/Basic.lean`, "Future work" (the two entries above).
* [turaev1994] Turaev, *Quantum invariants of knots and 3-manifolds* — pivotal and spherical
  categories, and the Drinfeld morphism in the braided case.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
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
  /-- **Monoidality**: the pivotor is compatible with `⊗`, measured against the comparison
  `(X ⊗ Y)ᘁᘁ ≅ Xᘁᘁ ⊗ Yᘁᘁ`.  Without this field the class is strictly weaker than the literature's
  *pivotal*, and Barrett–Westbury does not apply to it. -/
  pivotor_tensor : ∀ X Y : C,
    pivotor.hom.app (X ⊗ Y) ≫ (tensorDoubleDualIso X Y).hom
      = pivotor.hom.app X ⊗ₘ pivotor.hom.app Y

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

/-- **Monoidality of the pivotor**, object-wise. -/
theorem pivotorApp_tensor (X Y : C) :
    (pivotorApp (X ⊗ Y)).hom ≫ (tensorDoubleDualIso X Y).hom
      = (pivotorApp X).hom ⊗ₘ (pivotorApp Y).hom :=
  pivotor_tensor X Y

end

/-- **Build a pivotal structure from object-wise data.**  A choice of `X ≅ Xᘁᘁ` for each `X`, plus
the naturality square, *is* a natural isomorphism `𝟭 C ≅ ᘁᘁ`.  Together with `pivotor_naturality`
this says the two presentations carry the same data, so a proof in either style lands. -/
def ofPointwise (p : ∀ X : C, X ≅ ((X : C)ᘁ : C)ᘁ)
    (hp : ∀ {X Y : C} (f : X ⟶ Y),
      f ≫ (p Y).hom = (p X).hom ≫ rightAdjointMate (rightAdjointMate f))
    (hm : ∀ X Y : C, (p (X ⊗ Y)).hom ≫ (tensorDoubleDualIso X Y).hom
      = (p X).hom ⊗ₘ (p Y).hom) :
    PivotalCategory C where
  pivotor := NatIso.ofComponents p (fun f => hp f)
  pivotor_tensor := hm

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

/-! ### There is deliberately no `pivotalOfBraided`

An earlier revision of this file carried an instance `pivotalOfBraided : PivotalCategory C`, with
the Drinfeld isomorphism as pivotor, claiming *every braided right-rigid category is pivotal*.

**It has been removed, because with the monoidality field it is unconstructible — and it is
unconstructible because it is false.**  `drinfeldIso` is natural but not monoidal: it misses by
exactly the inverse monodromy `((β_ X Y).hom ≫ (β_ Y X).hom)⁻¹`
(`QOU.MathlibExt.rightDualIso_swap_tensor`).  Braiding alone does not make a rigid category pivotal
in the literature's sense.

The replacement is `QOU.MathlibExt.pivotalOfRibbon`, which asks for a balancing and uses
`θ ≫ drinfeldIso`.  It lives in `QOU.MathlibExt.BraidedTensorDual`, downstream of the twist.  Note
this costs less than it appears: `Ribbon.lean` makes every symmetric category balanced, so
`FGModuleCat K` and friends still get a pivotal structure by instance search.

The *fact* underlying the old instance is untouched and still here: `drinfeldIso` together with
`drinfeldIso_naturality` is a natural isomorphism `𝟭 C ≅ ᘁᘁ` on any braided right-rigid category.
Only its promotion to a `PivotalCategory` instance was wrong. -/

end BraidedNaturality

end QOU.MathlibExt
