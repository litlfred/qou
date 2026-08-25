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
* `PivotalStructure` — the missing class: a natural isomorphism `X ≅ Xᘁᘁ` with the
  naturality square against double mates. Content-bearing; it does **not** carry
  `qDimObj (Xᘁ) = qDimObj X` as a field (that would be the self-assuming projection
  §3b-cond item 5 forbids).
* `SphericalStructure` — the standard "left trace = right trace" class.

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
of the conditional theorem, and stays open in bean `rtqd`. This file does **not** close
`bwse`, and adds no physics. No fit; nothing wired; L2 unchanged.

-- Ref: [manuscript] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneRibbonMTCInput

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

/-- **The pivotal structure Mathlib lacks.** A natural isomorphism `X ≅ Xᘁᘁ` identifying
each object with its double dual, compatible with morphisms via the double mate. This is
the datum whose absence blocks `qDimObj (Xᘁ) = qDimObj X` from even being expressible on
the `η_` / `ε_` / `β_` / `rightAdjointMate` data.

The fields are the *standard* pivotal axioms — the isomorphism and its naturality square.
The class deliberately does **not** carry the conjugation symmetry as a field. -/
class PivotalStructure (C : Type*) [Category C] [MonoidalCategory C]
    [RightRigidCategory C] where
  /-- The pivotor: each object is identified with its double dual. -/
  pivotor : ∀ X : C, X ≅ (Xᘁ)ᘁ
  /-- Naturality: the pivotor commutes with the double right-adjoint mate. -/
  pivotor_naturality : ∀ {X Y : C} (f : X ⟶ Y),
    f ≫ (pivotor Y).hom = (pivotor X).hom ≫ (fᘁ)ᘁ

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
