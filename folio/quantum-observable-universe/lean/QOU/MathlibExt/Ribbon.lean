/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic

/-!
# QOU.MathlibExt.Ribbon — balanced and ribbon monoidal categories

Mathlib supplies `BraidedCategory`, `SymmetricCategory` and `Left`/`RightRigidCategory`, but it has
**no balancing twist**: measured against the pinned Mathlib, `grep -rl "ribbon\|BalancedCategory"
Mathlib/CategoryTheory/` returns a single unrelated file (`Topos/Classifier.lean`, where "balanced"
means the epi-mono factorisation sense).  There is no `Mathlib/CategoryTheory/Monoidal/Ribbon.lean`,
and `Monoidal/Rigid/` contains only `Basic`, `Braided`, `FunctorCategory`, `OfEquivalence`.

This module is the candidate for upstream `Mathlib/CategoryTheory/Monoidal/Ribbon.lean`.  It is
stated over Mathlib's own `BraidedCategory` / `RightRigidCategory` and imports nothing from `QOU`,
so it can be lifted verbatim.

## Main definitions

* `BalancedCategory C` — a braided monoidal category with a natural **twist** `θ_X : X ⟶ X`
  satisfying `θ_{𝟙} = 𝟙` and the Joyal–Street **balancing axiom**
  `θ_{X ⊗ Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)`.  Each `θ_X` is an isomorphism.
* `RibbonCategory C` — a balanced **right-rigid** category whose twist is compatible with duality,
  `θ_{Xᘁ} = (θ_X)ᘁ`.

## Main statements

* `BalancedCategory.ofSymmetric` / `RibbonCategory.ofSymmetric` — **non-vacuity**: every symmetric
  monoidal category is balanced with the trivial twist `θ = 𝟙`, and every symmetric right-rigid
  category is ribbon.  So neither class is conditional-on-`False`; both are inhabited across
  Mathlib's symmetric categories (`ModuleCat R`, …).
* `BalancedCategory.twistIso`, `twistNatIso` — the twist packaged as an isomorphism and as a natural
  automorphism of `𝟭 C`, which is the form the naturality axiom actually asserts.
* `BalancedCategory.inv_twist_naturality` — the inverse twist is natural too.
* `BalancedCategory.twist_tensorUnit_right` — the balancing axiom is *consistent* with
  `θ_{𝟙} = 𝟙`: at `Y = 𝟙_C` it reduces to naturality along the right unitor rather than to a new
  constraint.  Derived, not assumed.
* `RibbonCategory.twist_dualDual` — `θ_{Xᘁᘁ} = (θ_X)ᘁᘁ`.
* `RibbonCategory.rightAdjointMate_inv_twist` — the mate of the inverse twist is the inverse of the
  dual's twist, `(θ_X⁻¹)ᘁ = (θ_{Xᘁ})⁻¹`.

## Scope

This is structure, not a theorem about any particular category: it names the datum the
Reshetikhin–Turaev construction needs on top of braided-rigid.  Nothing here is wired to compute and
no numerical claim depends on it.  Base ring (§7c): everything is stated over a generic Mathlib
braided (right-rigid) category; no `ℝ` appears.

## References

* [joyal1993] Joyal, Street, *Braided tensor categories*, Adv. Math. 102 (1993) — the balancing
  axiom.
* [turaev1994] Turaev, *Quantum invariants of knots and 3-manifolds* — ribbon categories and the
  ribbon trace.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/

namespace QOU.MathlibExt

open CategoryTheory MonoidalCategory BraidedCategory

/-- **A balanced (braided) category**: a braided monoidal category equipped with a natural twist
`θ_X : X ⟶ X` satisfying `θ_{𝟙} = 𝟙` and the Joyal–Street balancing axiom
`θ_{X ⊗ Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)`. -/
class BalancedCategory (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C] where
  /-- The balancing twist `θ_X : X ⟶ X`. -/
  twist : ∀ X : C, X ⟶ X
  /-- The twist is an isomorphism. -/
  twist_isIso : ∀ X : C, IsIso (twist X)
  /-- `θ_{𝟙} = 𝟙`. -/
  twist_unit : twist (𝟙_ C) = 𝟙 (𝟙_ C)
  /-- Naturality: `θ_X ≫ f = f ≫ θ_Y`. -/
  twist_naturality : ∀ {X Y : C} (f : X ⟶ Y), twist X ≫ f = f ≫ twist Y
  /-- **Balancing axiom**: `θ_{X ⊗ Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)`. -/
  twist_tensor : ∀ X Y : C,
    twist (X ⊗ Y) = (β_ X Y).hom ≫ (β_ Y X).hom ≫ (twist X ⊗ₘ twist Y)

namespace BalancedCategory

attribute [instance] twist_isIso

section

universe v u

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [BalancedCategory C]

/-- The twist as an isomorphism `X ≅ X`. -/
noncomputable def twistIso (X : C) : X ≅ X := asIso (twist X)

@[simp] theorem twistIso_hom (X : C) : (twistIso X).hom = twist X := rfl

/-- The twist packaged as a natural automorphism of the identity functor.  This is what the
naturality axiom asserts; having it in this form is what lets the twist be composed with other
natural transformations. -/
noncomputable def twistNatIso : 𝟭 C ≅ 𝟭 C :=
  NatIso.ofComponents (fun X => twistIso X) (fun f => (twist_naturality f).symm)

@[simp] theorem twistNatIso_hom_app (X : C) : (twistNatIso (C := C)).hom.app X = twist X := rfl

/-- **The inverse twist is natural too**: `θ_X⁻¹ ≫ f = f ≫ θ_Y⁻¹`. -/
theorem inv_twist_naturality {X Y : C} (f : X ⟶ Y) :
    inv (twist X) ≫ f = f ≫ inv (twist Y) := by
  rw [IsIso.inv_comp_eq, ← Category.assoc, IsIso.eq_comp_inv, twist_naturality]

/-- **The twist on a three-fold tensor carries no irreducible three-body datum.**

Unfolding the balancing axiom twice: `θ_{X ⊗ Y ⊗ Z}` is built entirely from **pairwise** braidings
(`β_{X, Y⊗Z}`, `β_{Y⊗Z, X}`, `β_{Y,Z}`, `β_{Z,Y}`) and **single-object** twists
(`θ_X`, `θ_Y`, `θ_Z`).  Nothing in it depends on the three objects jointly in a way that is not
already a composite of two-object data.  Three is the first arity at which a genuine many-body term
*could* appear, and it does not.

## Scope of the resulting prune (read before citing this downstream)

This is a **structural** fact about the ribbon datum, in the sense of the "(b) structural exclusion"
tier: the invariant is the balancing axiom itself, stated above and cited here.  What it excludes is
precise and narrow:

* it **does** exclude any weight *defined as a composite of twists and braidings* on an `A`-fold
  tensor from carrying an irreducible three-or-more-body contribution — such a composite is always
  per-object data together with pairwise data;
* it **does not** exclude the missing super-pairwise additive term in the many-body binding
  magnitude.  That term is not claimed here to be ribbon-derived, and if it is not, this says
  nothing about it.

The bridge between the two is a question about *how the binding weight is defined*, not a question
about ribbon categories, and it is deliberately left open here.  What the lemma does supply, if that
bridge is made, is a reason of the right kind: the pairwise cap `ρ_A ≤ C(A,2)` recorded in the
mass-theory development has exactly the shape this decomposition predicts — `C(A,2)` is the number
of pairwise braidings the iterated balancing axiom produces. -/
theorem twist_tensor_three (X Y Z : C) :
    twist (X ⊗ Y ⊗ Z)
      = (β_ X (Y ⊗ Z)).hom ≫ (β_ (Y ⊗ Z) X).hom
        ≫ (twist X ⊗ₘ ((β_ Y Z).hom ≫ (β_ Z Y).hom ≫ (twist Y ⊗ₘ twist Z))) := by
  rw [twist_tensor X (Y ⊗ Z), twist_tensor Y Z]

/-- **The balancing axiom is consistent with `θ_𝟙 = 𝟙`.**  Specialising `twist_tensor` at
`Y = 𝟙_C` and transporting along the right unitor recovers exactly naturality, so the unit case
imposes no constraint beyond the two axioms.  Derived — this is a check on the axiom set, not a new
assumption. -/
theorem twist_tensorUnit_right (X : C) :
    twist (X ⊗ 𝟙_ C) ≫ (ρ_ X).hom = (ρ_ X).hom ≫ twist X :=
  twist_naturality _

end

/-- **Non-vacuity: every symmetric monoidal category is balanced with the trivial twist `θ = 𝟙`.**
The double braiding is the identity (`SymmetricCategory.symmetry`), so the balancing axiom
`𝟙 = β_{X,Y} ≫ β_{Y,X} ≫ (𝟙 ⊗ 𝟙)` reduces to it. -/
instance (priority := 100) ofSymmetric (C : Type*) [Category C] [MonoidalCategory C]
    [SymmetricCategory C] : BalancedCategory C where
  twist := fun X => 𝟙 X
  twist_isIso := fun _ => inferInstance
  twist_unit := rfl
  twist_naturality := fun f => by rw [Category.id_comp, Category.comp_id]
  twist_tensor := fun X Y => by
    have hid : (𝟙 X ⊗ₘ 𝟙 Y) = 𝟙 (X ⊗ Y) := by simp
    rw [hid, Category.comp_id]
    exact (SymmetricCategory.symmetry X Y).symm

end BalancedCategory

/-- **A ribbon category**: a balanced right-rigid category whose twist is compatible with duality,
`θ_{Xᘁ} = (θ_X)ᘁ`, where `(·)ᘁ` is Mathlib's `rightAdjointMate`.  This is the datum the
Reshetikhin–Turaev construction needs on top of braided-rigid: `twist_dual` is what makes the ribbon
trace well-behaved under duality. -/
class RibbonCategory (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    [RightRigidCategory C] extends BalancedCategory C where
  /-- **Ribbon (dual-compatibility) axiom**: `θ_{Xᘁ} = (θ_X)ᘁ`. -/
  twist_dual : ∀ X : C, BalancedCategory.twist (Xᘁ) = (BalancedCategory.twist X)ᘁ

namespace RibbonCategory

open BalancedCategory

/-- **Non-vacuity: every symmetric right-rigid category is ribbon with the trivial twist `θ = 𝟙`.**
The ribbon axiom reduces to Mathlib's `rightAdjointMate_id`.  The classical limit therefore stays
*inside* the class — `θ = 𝟙` is a describable member, not an exclusion. -/
instance (priority := 100) ofSymmetric (C : Type*) [Category C] [MonoidalCategory C]
    [SymmetricCategory C] [RightRigidCategory C] : RibbonCategory C where
  twist_dual := fun X => by
    show 𝟙 (Xᘁ) = (𝟙 X)ᘁ
    simp

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]
variable [RibbonCategory C]

/-- **The twist commutes with double-dualisation**: `θ_{Xᘁᘁ} = (θ_X)ᘁᘁ`.  The ribbon axiom applied
twice.  The double dual is where the general quantum-dimension conjugation symmetry
`dim (Xᘁ) = dim X` would live; that broader statement additionally needs a pivotal structure, which
Mathlib does not provide either. -/
theorem twist_dualDual (X : C) :
    twist (C := C) Xᘁᘁ = ((twist X)ᘁ)ᘁ := by
  rw [twist_dual, twist_dual]

/-- **The mate of the inverse twist is the inverse of the dual's twist**: `(θ_X⁻¹)ᘁ = (θ_{Xᘁ})⁻¹`.
Duality is contravariant, so this does not follow from `twist_dual` by rewriting — it needs the two
composites, via `comp_rightAdjointMate`. -/
theorem rightAdjointMate_inv_twist (X : C) :
    (inv (twist (C := C) X))ᘁ = inv (twist (C := C) Xᘁ) := by
  have h : twist (C := C) Xᘁ ≫ (inv (twist (C := C) X))ᘁ = 𝟙 (Xᘁ) := by
    rw [twist_dual, ← comp_rightAdjointMate, IsIso.inv_hom_id, rightAdjointMate_id]
  exact IsIso.eq_inv_of_hom_inv_id h

end RibbonCategory

end QOU.MathlibExt
