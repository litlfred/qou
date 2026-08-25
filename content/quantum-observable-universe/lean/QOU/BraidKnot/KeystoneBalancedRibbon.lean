/-
Copyright (c) 2026 litlfred. All rights reserved.

# The balanced/ribbon twist layer Mathlib lacks (bean rtrb, RT-1)

Mathlib provides `BraidedCategory` and `Left/RightRigidCategory` but **no balancing twist** — the
`θ_X : X ⟶ X` that upgrades a braided category to a *balanced* (and, with rigidity, a *ribbon*)
category. The ribbon structure is precisely the extra datum the Reshetikhin–Turaev construction
needs on top of braided-rigid (bean `rtep`, input (RT)): the twist is the framing anomaly of a
colored Wilson line, and the ribbon trace `tr(𝟙_X)` (the categorical quantum dimension `qDimObj`,
`KeystoneRibbonMTCInput.lean`) lives in it.

This file supplies that missing layer as a Mathlib-style class:

* `BalancedCategory C` — a braided category with a natural twist `θ_X : X ⟶ X`, `θ_{𝟙}=𝟙`, and the
  **balancing axiom** `θ_{X⊗Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)` (the double braiding dressed by
  the twists) — the standard Joyal–Street balancing.  Each `θ_X` is an isomorphism.
* `twist_unit`, `twist_naturality`, `twist_tensor` — the axioms, available as lemmas.
* `BalancedCategory.ofSymmetric` — **non-vacuity**: *every* symmetric monoidal category is balanced
  with the trivial twist `θ = 𝟙` (the double braiding is the identity, so the balancing axiom holds).
  So the class is inhabited on a whole class of Mathlib categories (e.g. `ModuleCat R`), not
  conditional-on-`False`.

## Honest scope (STRICT, §Axiomatization-is-NOT-a-Proof)

This is the **achievable** RT-1 piece: the ribbon/twist *structure*, built on Mathlib's real
braided category. It does **NOT** close `bwse`, and it is not the RT functor (bean `rttg`, large) nor
Kirby calculus (bean `rtkb`, research wall). The `BalancedCategory` fields are content-bearing
categorical axioms (not `True`); the symmetric instance *derives* them. No fit; nothing wired; L2
unchanged (2/7).

-- Ref: [manuscript] docs/coordination/s5-so3-keystone.md
-/
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

namespace QOU.BraidKnot.Balanced

open CategoryTheory MonoidalCategory BraidedCategory

/-- **A balanced (braided) category**: a braided monoidal category equipped with a natural twist
`θ_X : X ⟶ X` satisfying `θ_{𝟙} = 𝟙` and the Joyal–Street balancing axiom
`θ_{X⊗Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)`.  With right rigidity this is a *ribbon* category — the
input the Reshetikhin–Turaev construction needs on top of braided-rigid. -/
class BalancedCategory (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C] where
  /-- The balancing twist `θ_X : X ⟶ X`. -/
  twist : ∀ X : C, X ⟶ X
  /-- The twist is an isomorphism. -/
  twist_isIso : ∀ X : C, IsIso (twist X)
  /-- `θ_{𝟙} = 𝟙`. -/
  twist_unit : twist (𝟙_ C) = 𝟙 (𝟙_ C)
  /-- Naturality: `θ_X ≫ f = f ≫ θ_Y`. -/
  twist_naturality : ∀ {X Y : C} (f : X ⟶ Y), twist X ≫ f = f ≫ twist Y
  /-- **Balancing axiom**: `θ_{X⊗Y} = β_{X,Y} ≫ β_{Y,X} ≫ (θ_X ⊗ θ_Y)`. -/
  twist_tensor : ∀ X Y : C,
    twist (X ⊗ Y) = (β_ X Y).hom ≫ (β_ Y X).hom ≫ (twist X ⊗ₘ twist Y)

namespace BalancedCategory

variable {C : Type*} [Category C] [MonoidalCategory C]

attribute [instance] twist_isIso

/-- **Non-vacuity: every symmetric monoidal category is balanced with the trivial twist `θ = 𝟙`.**
The double braiding is the identity (`SymmetricCategory.symmetry`), so the balancing axiom
`𝟙 = β_{X,Y} ≫ β_{Y,X} ≫ (𝟙 ⊗ 𝟙)` reduces to it.  Inhabits `BalancedCategory` on all of Mathlib's
symmetric categories (`ModuleCat R`, …), so the class is not conditional-on-`False`. -/
instance (priority := 100) ofSymmetric [SymmetricCategory C] : BalancedCategory C where
  twist := fun X => 𝟙 X
  twist_isIso := fun X => inferInstance
  twist_unit := rfl
  twist_naturality := fun f => by rw [Category.id_comp, Category.comp_id]
  twist_tensor := fun X Y => by
    have hid : (𝟙 X ⊗ₘ 𝟙 Y) = 𝟙 (X ⊗ Y) := by simp
    rw [hid, Category.comp_id]
    exact (SymmetricCategory.symmetry X Y).symm

end BalancedCategory

end QOU.BraidKnot.Balanced
