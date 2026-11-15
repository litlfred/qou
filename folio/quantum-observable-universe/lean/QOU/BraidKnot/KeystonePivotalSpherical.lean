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

The residual is input 1, the pivotal transport lemma `qDimObj (Xᘁ) = leftQDim X`. It is
still **not proved** — it is an explicit hypothesis of the conditional theorems below, and
that is unchanged.

**And the two inputs are not two.** `transport_iff_spherical` proves them equivalent,
unconditionally, modulo the conjugation symmetry. So the residual recorded against this
file was never two conditions of which one might fall — it is one condition wearing two
names, and it is *not* unconditionally provable, because sphericality is not.

`pivotalTransport_of_symmetric` discharges it for the whole symmetric class, which is the
first unconditional case. `qDim_twist_eq_leftQDim` says exactly what stands in the way in
general: the two traces differ by the twist factor `θ_{Xᘁ} ⊗ θ_X`, so the classical
`ribbon ⇒ spherical` — a theorem about the *twisted* trace — does not reach these
*twistless* ones.

**What has also changed is that the goal those inputs served no longer needs them.**
`QOU.BraidKnot.Ribbon.qDim_conj_object` proves `qDimObj (Xᘁ) = qDimObj X` outright, in any
braided right-rigid category, with no pivotal, spherical or transport hypothesis — via
`QOU.MathlibExt.qDimWith_rightDual`, which observes that the quantum dimension is
independent of the choice of dual and that `X` is itself a right dual of `Xᘁ`.

So the factoring below is now one route among two rather than the only one. Its theorems
remain valid and are kept: a conditional result is not invalidated by an unconditional
proof of its conclusion, and the transport identity is worth having in its own right —
sphericality, which input 2 supplies in the symmetric case, is a separate condition that
the unconditional route says nothing about.

The pivotal *structure* is no longer part of that residual. `QOU.MathlibExt.pivotalOfRibbon`
proves every **ribbon** right-rigid category pivotal, sorry-free — and since a symmetric category
is balanced, that covers the symmetric case this file cares about. What remains is the transport
identity itself, which is about the traces rather than about the double dual. This file does **not** close
`bwse`, and adds no physics. No fit; nothing wired; L2 unchanged.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneRibbonMTCInput
import QOU.MathlibExt.PivotalCategory
import QOU.MathlibExt.BraidedQuantumDimension
import QOU.MathlibExt.Ribbon

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

**The pivotal structure now exists — under a ribbon hypothesis.**
`QOU.MathlibExt.pivotalOfRibbon` makes every **ribbon** right-rigid category pivotal, sorry-free:
the pivotor is `θ ≫ drinfeldIso`, its naturality combines `BalancedCategory.twist_naturality` with
`drinfeldIso_naturality`, and its monoidality is `twist_drinfeld_monoidal_tensorDoubleDualIso`.

*An earlier revision of this paragraph claimed the stronger thing — that `pivotalOfBraided` makes
**every braided** right-rigid category pivotal, unconditionally.  That is **false** and the
instance has been removed.  `drinfeldIso` is natural but not monoidal, missing by exactly the
inverse monodromy (`QOU.MathlibExt.rightDualIso_swap_tensor`); braiding alone does not give a
pivotal structure in the literature's sense, which is the sense Barrett–Westbury needs.*

In practice the hypothesis costs this file nothing: `Ribbon.lean` makes every symmetric category
balanced, so the datum is still supplied for the whole class of categories the keystone cares
about rather than for one example.

That does **not** discharge `hTransport` below.  The transport identity
`qDimObj (Xᘁ) = leftQDim X` is a statement about the two *traces*; having the pivotor is a
prerequisite for it, not a proof of it.  The hypothesis is still carried.
-/

/-- **Sphericality**, in the standard form: the left and right quantum dimensions agree on
every object. (Equivalently, the left and right traces agree — here specialised to the
identity, which is the case the keystone consumes.)

**Why this is a hypothesis and not a theorem, and when you do not need it.**

`leftQDim` and `qDimObj` are the two *twistless* closures, and they differ by the monodromy
`(β_ Xᘁ X).inv` against `(β_ X Xᘁ).hom`.  No axiom of a braided rigid category forces the
monodromy to vanish, so this class cannot be derived here — it is a genuine condition, which is
what `spherical_of_symmetric` below witnesses from the other side (symmetric ⇒ monodromy trivial ⇒
spherical).

The classical `ribbon ⇒ spherical` is a theorem about the **twisted** traces, and it does not reach
these two.  If a `BalancedCategory` is in scope, do not carry this hypothesis: use
`QOU.MathlibExt.qDimTwistedLeftWith_eq`, which *proves* left = right for
`qDimTwistedLeftWith` / `qDimTwistedWith` in any `RibbonCategory`.  Its companion
`qDimTwistedLeftWith_eq_of_cap` shows the balancing axiom does all the geometric work and the
ribbon axiom is used exactly once, on the cap.

So the division of labour is: **this class is the right object precisely where there is no twist
available** — as here, where the variable block is braided right-rigid and no `θ` exists.  Where a
twist does exist, sphericality is a theorem and this class is the wrong thing to assume.  Nothing
in this file needs migrating on that account: the results below are true at braided right-rigid
generality, and requiring a ribbon structure to obtain them would be a loss, not a gain. -/
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

/-! ### The two inputs are ONE input

`qDim_conj_object` proved `qDimObj (Xᘁ) = qDimObj X` unconditionally. Reading the
factoring above through it collapses the two "independent classical inputs" into
each other. -/

section Collapse

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]
  [RightRigidCategory C]

/-- **Pivotal transport and sphericality are equivalent**, unconditionally.

The factoring above presents them as two independent classical inputs. They are not
independent: modulo `QOU.MathlibExt.qDimWith_rightDual` (the unconditional conjugation
symmetry) each follows from the other in one rewrite.

The consequence is worth stating plainly. Transport is **not** unconditionally provable,
because sphericality is not — the left and right traces genuinely differ in a general
braided rigid category, and a category where they agree is what *spherical* names. So the
residual recorded against this file was never two inputs of which one might fall; it is
one condition, wearing two names. -/
theorem transport_iff_spherical (X : C) :
    qDimObj ((X : C)ᘁ) = leftQDim X ↔ leftQDim X = qDimObj X := by
  have c : qDimObj ((X : C)ᘁ) = qDimObj X := QOU.MathlibExt.qDimWith_rightDual X
  exact ⟨fun t => t.symm.trans c, fun s => c.trans s.symm⟩

/-- **Sphericality supplies transport.** The half of the equivalence the conditional
theorems above actually consume. -/
theorem pivotalTransport_of_spherical [SphericalStructure C] (X : C) :
    qDimObj ((X : C)ᘁ) = leftQDim X :=
  (transport_iff_spherical X).mpr (SphericalStructure.leftQDim_eq X)

end Collapse

section SymmetricTransport

variable {C : Type*} [Category C] [MonoidalCategory C] [SymmetricCategory C]
  [RightRigidCategory C]

/-- **In a symmetric right-rigid category the transport identity holds outright.**

`leftQDim_eq_qDimObj_of_symmetric` proves sphericality there, and
`transport_iff_spherical` converts it. So the hypothesis the conditional theorems above
carry is discharged for the whole symmetric class — the first unconditional case of it. -/
theorem pivotalTransport_of_symmetric (X : C) :
    qDimObj ((X : C)ᘁ) = leftQDim X :=
  (transport_iff_spherical X).mpr (leftQDim_eq_qDimObj_of_symmetric X)

end SymmetricTransport

/-! ### Why the twist does not close it — the exact obstruction

The natural next thought, once a ribbon structure is available, is the classical
`ribbon ⇒ spherical`. It does **not** apply to `qDimObj` and `leftQDim` as defined here,
and the theorem below says precisely why. -/

section TwistObstruction

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]
  [RightRigidCategory C] [QOU.MathlibExt.BalancedCategory C]

open QOU.MathlibExt

/-- **The two traces differ by exactly the twist factor `θ_{Xᘁ} ⊗ θ_X`.**

Inserting that factor into the right trace produces the left trace on the nose. The proof
is the Joyal–Street balancing axiom, which turns the double braiding into
`θ_{Xᘁ ⊗ X}` dressed by the two component twists, followed by naturality of `θ` against
`η ≫ β⁻¹ : 𝟙_C ⟶ Xᘁ ⊗ X` — which absorbs the whole `θ_{Xᘁ ⊗ X}`, since `θ_{𝟙} = 𝟙`.

**This is why `ribbon ⇒ spherical` does not apply here.** The classical theorem concerns
the *twisted* trace, in which `θ` is already inserted; `qDimObj` and `leftQDim` are the
*twistless* traces, and between those two the twist is not a normalisation but the entire
difference. A ribbon structure supplies `θ_{Xᘁ} = (θ_X)ᘁ`, which relates the factor's two
halves — it does not make the factor disappear. So sphericality is not a consequence of
the ribbon axiom for these definitions, and by `transport_iff_spherical` neither is
transport. Scope (a): this is a statement about *these* two definitions, not a claim that
no twisted formulation closes. -/
theorem qDim_twist_eq_leftQDim (X : C) :
    η_ X ((X : C)ᘁ) ≫ (β_ X ((X : C)ᘁ)).hom
        ≫ (BalancedCategory.twist ((X : C)ᘁ) ⊗ₘ BalancedCategory.twist X) ≫ ε_ X ((X : C)ᘁ)
      = leftQDim X := by
  have hbal := BalancedCategory.twist_tensor ((X : C)ᘁ) X
  have hnat := BalancedCategory.twist_naturality
    (η_ X ((X : C)ᘁ) ≫ (β_ ((X : C)ᘁ) X).inv)
  simp only [BalancedCategory.twist_unit, Category.id_comp] at hnat
  unfold leftQDim
  calc _ = η_ X ((X : C)ᘁ) ≫ (β_ ((X : C)ᘁ) X).inv
              ≫ ((β_ ((X : C)ᘁ) X).hom ≫ (β_ X ((X : C)ᘁ)).hom
                 ≫ (BalancedCategory.twist ((X : C)ᘁ) ⊗ₘ BalancedCategory.twist X))
              ≫ ε_ X ((X : C)ᘁ) := by simp
    _ = η_ X ((X : C)ᘁ) ≫ (β_ ((X : C)ᘁ) X).inv
              ≫ BalancedCategory.twist ((X : C)ᘁ ⊗ X) ≫ ε_ X ((X : C)ᘁ) := by
          rw [← hbal]
    _ = _ := by rw [← Category.assoc, ← Category.assoc, ← hnat, Category.assoc]

end TwistObstruction

end QOU.BraidKnot.PivotalSpherical
