/-
Copyright (c) 2026 litlfred. All rights reserved.

# Pivotal and spherical structure — the infra Mathlib lacks, and what it buys `rtqd`

**Bean `rtqd`.** `KeystoneRibbonCategory.lean` (bean `rtrb`) proved the ribbon layer but
left one gap open, deliberately unproved rather than `sorry`'d:

    qDimObj (Xᘁ) = qDimObj X          -- the corpus fact `qDim_conj`, categorically

The blocker recorded there: `qDimObj (Xᘁ)` traverses the **double dual** `Xᘁᘁ`, which a
braided right-rigid category does not identify with `X`. That identification is a
**pivotal structure**, and `CategoryTheory.Monoidal.Rigid.*` provides none — confirmed
again here (`rightAdjointMate`, `comp_rightAdjointMate`, `ExactPairing` exist; no
`PivotalCategory`). Per the standing rule *build the needed Mathlib infra rather than
beaning it*, this file builds it.

## What is built (infra)

* `leftQDim` — the **left** quantum dimension, the mirror trace taken with the *inverse*
  braiding `(β_ Xᘁ X).inv` in place of `(β_ X Xᘁ).hom`. A genuinely different morphism
  from `qDimObj` (the right dimension); the two coincide exactly when the category is
  spherical.
* `SphericalStructure` — the standard "left trace = right trace" class.

`PivotalStructure` used to be built here too. It has **moved** to
[`QOU/MathlibExt/PivotalCategory.lean`](../MathlibExt/PivotalCategory.lean), where it is
`PivotalCategory`, stated in the shape Mathlib's own "Future work" list asks for — a
natural isomorphism `𝟭 C ≅ ᘁᘁ` — together with the `rightDualFunctor` /
`doubleDualFunctor` that shape needs and Mathlib also lacks. It still does **not** carry
`qDimObj (Xᘁ) = qDimObj X` as a field (that would be the self-assuming projection
§3b-cond item 5 forbids). Moving it keeps the Mathlib-gap classes in one upstreamable
place and, more to the point, avoids the duplicate the ribbon layer had accumulated:
`RibbonCategory` had been declared twice under two namespaces before this tranche.

## What is proved

* `leftQDim_eq_qDimObj_of_symmetric` (**sorry-free, unconditional**) — every *symmetric*
  right-rigid category is spherical: the symmetry `β_{Y,X} ≫ β_{X,Y} = 𝟙` makes the
  inverse braiding equal the forward one, so `leftQDim = qDimObj`. This is a real
  theorem, and it is the **non-vacuity** witness for `SphericalStructure`: the class is
  inhabited on a whole family of Mathlib categories, not conditional-on-`False`.
* `spherical_of_symmetric` — that theorem packaged as an instance.
* `qDim_conj_of_pivotalTransport_of_spherical` (**§3b-cond, sorry-free**) — the gap,
  *factored*: `qDimObj (Xᘁ) = qDimObj X` follows from exactly two named classical inputs,
  each an explicit hypothesis,

  1. **pivotal transport** `qDimObj (Xᘁ) = leftQDim X` — the right dimension of the dual
     is the left dimension of the object (the standard pivotal identity), and
  2. **sphericality** `leftQDim X = qDimObj X`.

  Neither hypothesis *is* the conclusion; their composition is. This converts `rtqd` from
  "not expressible on the available data" into "expressible, and reduced to two named
  statements" — and input 2 is now **proved** in the symmetric case above.

## Honest scope (STRICT)

The residual is input 1, the pivotal transport lemma, whose classical proof is a
string-diagram coherence argument (`ribbon ⇒ spherical`, Deligne/Yetter; Bakalov–Kirillov
ch. 2). It is **not** proved here and **not** axiomatised — it is an explicit hypothesis
of the conditional theorem, and stays open in bean `rtqd`.

The pivotal *structure* is no longer part of that residual. `QOU.MathlibExt.pivotalOfBraided`
proves every braided right-rigid category pivotal, sorry-free. What remains is the transport
identity itself, which is about the traces rather than about the double dual. This file does **not** close
`bwse`, and adds no physics. No fit; nothing wired; L2 unchanged.

-- Ref: [manuscript] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneRibbonMTCInput
import QOU.MathlibExt.PivotalCategory

namespace QOU.BraidKnot.PivotalSpherical

open CategoryTheory MonoidalCategory BraidedCategory
open QOU.BraidKnot.RibbonMTC

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]
  [RightRigidCategory C]

/-- **The left quantum dimension.** The mirror of `qDimObj`: the same coevaluation and
evaluation, but crossing the strand with the **inverse** braiding `(β_ Xᘁ X).inv` instead
of the forward `(β_ X Xᘁ).hom`. In a general braided rigid category the two traces differ;
a category in which they agree for every object is *spherical*. -/
noncomputable def leftQDim (X : C) : (𝟙_ C ⟶ 𝟙_ C) :=
  η_ X Xᘁ ≫ (β_ Xᘁ X).inv ≫ ε_ X Xᘁ

/-! ### The pivotal structure

`PivotalStructure` used to be declared here, pointwise: a `∀ X, X ≅ Xᘁᘁ` plus a naturality field.
It has moved to [`QOU/MathlibExt/PivotalCategory.lean`](../MathlibExt/PivotalCategory.lean) as
`PivotalCategory`, stated the way Mathlib's own "Future work" list asks for it — a natural
isomorphism `𝟭 C ≅ ᘁᘁ` — with `PivotalCategory.ofPointwise` and `PivotalCategory.pivotor_naturality`
showing the two presentations carry the same data.  That file also supplies the `rightDualFunctor` /
`doubleDualFunctor` the functorial statement needs, which Mathlib does not have either.

**The pivotal structure now exists.** `QOU.MathlibExt.pivotalOfBraided` makes **every braided
right-rigid category pivotal**, unconditionally and sorry-free: the pivotor is `drinfeldIso`, and
its naturality is `drinfeldIso_naturality`.  So the datum this file's docstring describes as
"the infra Mathlib lacks" is supplied, and it is supplied for the whole class of categories the
keystone cares about rather than for one example.

That does **not** discharge `hTransport` below.  The transport identity
`qDimObj (Xᘁ) = leftQDim X` is a statement about the two *traces*; having the pivotor is a
prerequisite for it, not a proof of it.  The hypothesis is still carried.
-/

/-- **Sphericality**, in the standard form: the left and right quantum dimensions agree on
every object. (Equivalently, the left and right traces agree — here specialised to the
identity, which is the case the keystone consumes.) -/
class SphericalStructure (C : Type*) [Category C] [MonoidalCategory C]
    [BraidedCategory C] [RightRigidCategory C] where
  /-- Left trace = right trace. -/
  leftQDim_eq : ∀ X : C, leftQDim X = qDimObj X

/-! ### A symmetric right-rigid category is spherical (proved, unconditional)

The braiding here must come **from** `SymmetricCategory` rather than from a second,
independent `[BraidedCategory C]` binder — otherwise `SymmetricCategory.symmetry` is stated
about `inst.toBraidedCategory` while the goal mentions the separate instance, and the two
do not unify (an instance diamond). Hence the local `variable` line below deliberately omits
`[BraidedCategory C]`. -/

section Symmetric

variable {C : Type*} [Category C] [MonoidalCategory C] [SymmetricCategory C]
  [RightRigidCategory C]

/-- In a symmetric category the inverse braiding **is** the forward braiding of the swapped
pair: `(β_ X Xᘁ).hom = (β_ Xᘁ X).inv`, directly from `SymmetricCategory.symmetry`. -/
theorem braiding_inv_eq_hom_of_symmetric (X : C) :
    (β_ X Xᘁ).hom = (β_ Xᘁ X).inv := by
  have hs : (β_ Xᘁ X).hom ≫ (β_ X Xᘁ).hom = 𝟙 (Xᘁ ⊗ X) := SymmetricCategory.symmetry Xᘁ X
  calc (β_ X Xᘁ).hom
      = 𝟙 (X ⊗ Xᘁ) ≫ (β_ X Xᘁ).hom := by rw [Category.id_comp]
    _ = ((β_ Xᘁ X).inv ≫ (β_ Xᘁ X).hom) ≫ (β_ X Xᘁ).hom := by rw [Iso.inv_hom_id]
    _ = (β_ Xᘁ X).inv ≫ ((β_ Xᘁ X).hom ≫ (β_ X Xᘁ).hom) := by rw [Category.assoc]
    _ = (β_ Xᘁ X).inv ≫ 𝟙 (Xᘁ ⊗ X) := by rw [hs]
    _ = (β_ Xᘁ X).inv := by rw [Category.comp_id]

/-- **Every symmetric right-rigid category is spherical.** The two traces are built from the
same coevaluation and evaluation, differing only in the crossing; symmetry identifies the
two crossings, so `leftQDim = qDimObj`. Sorry-free and unconditional — this is the
non-vacuity witness for `SphericalStructure`. -/
theorem leftQDim_eq_qDimObj_of_symmetric (X : C) :
    leftQDim X = qDimObj X := by
  unfold leftQDim qDimObj
  rw [← braiding_inv_eq_hom_of_symmetric X]

/-- The symmetric case as an instance: `SphericalStructure` is inhabited. -/
instance (priority := 100) spherical_of_symmetric : SphericalStructure C where
  leftQDim_eq := leftQDim_eq_qDimObj_of_symmetric

/-- **Symmetric case: the gap reduces to pivotal transport alone.** Sphericality is
discharged by `leftQDim_eq_qDimObj_of_symmetric`, so in a symmetric right-rigid category
the conjugation symmetry is exactly one classical lemma away. -/
theorem qDim_conj_of_pivotalTransport_symmetric (X : C)
    (hTransport : qDimObj (Xᘁ) = leftQDim X) :
    qDimObj (Xᘁ) = qDimObj X := by
  rw [hTransport, leftQDim_eq_qDimObj_of_symmetric X]

end Symmetric

/-! ### The `rtqd` gap, factored into two named classical inputs -/

/-- **The conjugation symmetry, conditional on the two standard inputs (§3b-cond).**

`qDimObj (Xᘁ) = qDimObj X` follows from

1. `hTransport` — the **pivotal transport** identity `qDimObj (Xᘁ) = leftQDim X`: the right
   dimension of the dual is the left dimension of the object. This is the classical
   pivotal statement; its proof is a string-diagram coherence argument and it is **not**
   proved here (open, bean `rtqd`), carried as an explicit hypothesis rather than an
   axiom; and
2. `hSpherical` — **sphericality**, `leftQDim X = qDimObj X`, which
   `leftQDim_eq_qDimObj_of_symmetric` **proves** in the symmetric case.

Neither hypothesis is the conclusion — the conclusion is their composite. This is the
honest factoring of the gap the bean asked for. -/
theorem qDim_conj_of_pivotalTransport_of_spherical (X : C)
    (hTransport : qDimObj (Xᘁ) = leftQDim X)
    (hSpherical : leftQDim X = qDimObj X) :
    qDimObj (Xᘁ) = qDimObj X := by
  rw [hTransport, hSpherical]

/-- The same, drawing sphericality from the class rather than a bare hypothesis: in a
spherical category only the pivotal transport remains. -/
theorem qDim_conj_of_pivotalTransport [SphericalStructure C] (X : C)
    (hTransport : qDimObj (Xᘁ) = leftQDim X) :
    qDimObj (Xᘁ) = qDimObj X := by
  rw [hTransport, SphericalStructure.leftQDim_eq X]

end QOU.BraidKnot.PivotalSpherical
