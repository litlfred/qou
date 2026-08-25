/-
Copyright (c) 2026 litlfred. All rights reserved.

# The ribbon-category layer: dual-compatible twist + a conjugation-symmetric quantum dimension

`KeystoneBalancedRibbon.lean` (bean `rtrb`, RT-1) added the balancing twist Mathlib lacks — a
`BalancedCategory C` = braided category with a natural twist `θ_X : X ⟶ X`, `θ_{𝟙} = 𝟙`, and the
Joyal–Street balancing axiom.  `KeystoneRibbonMTCInput.lean` defined the categorical quantum
dimension `qDimObj X = η_X ≫ β_{X,Xᘁ} ≫ ε_X ∈ End(𝟙_C)`.  This file (bean `rtrb`, RT-1 extension)
closes the gap from *balanced* to a full **ribbon category** and studies the conjugation symmetry of
that quantum dimension.

## What is proved (sorry-free)

* `RibbonCategory C` — a `BalancedCategory` over a Mathlib braided **right-rigid** category with the
  extra **dual-compatibility ribbon axiom** `θ_{Xᘁ} = (θ_X)ᘁ` (`twist_dual`, using Mathlib's
  `rightAdjointMate`).  The fields are content-bearing categorical axioms (not `True`).
* `RibbonCategory.ofSymmetric` — **non-vacuity**: every symmetric right-rigid category is ribbon with
  the trivial twist `θ = 𝟙`.  The ribbon axiom reduces to Mathlib's `rightAdjointMate_id`
  (`(𝟙_X)ᘁ = 𝟙_{Xᘁ}`).  So the class is inhabited on a whole family of Mathlib categories, not
  conditional-on-`False`.
* `RibbonCategory.twist_dualDual` — derived: the twist commutes with double-dualization,
  `θ_{Xᘁᘁ} = (θ_X)ᘁᘁ` (the ribbon axiom applied twice).  A genuine conjugation-symmetry statement
  for the twist datum.
* `qDim_of_unitPairing` — for the unit object's exact pairing `𝟙_C ⊣ Y`, the braided quantum
  dimension of `𝟙_C` collapses to the identity: `η ≫ β ≫ ε = 𝟙_{𝟙_C}` (snake identity +
  `braiding_tensorUnit_left`).  Generic in `Y` and its pairing.
* `qDim_unit` — the categorical quantum dimension of the monoidal unit (the vacuum object) is `1`:
  `qDimObj (𝟙_C) = 𝟙 (𝟙_C)`.  This is the categorical statement behind the RT-input normalization
  `RibbonMTCInput.vac_dim_one` (there carried as a hypothesis): when the vacuum label's simple object
  is the unit, its categorical dimension is genuinely `1`, not merely assumed.  It is also the trivial
  case of conjugation symmetry (`dim(𝟙) = dim(𝟙ᘁ) = 1`).

## The conjugation-symmetry goal, and its residual gap (STRICT, §Axiomatization-is-NOT-a-Proof)

The corpus fact `qDim_conj` states the categorical quantum dimension is conjugation-symmetric,
`qDimObj (Xᘁ) = qDimObj X` for **every** object `X`.  This file proves the **unit case** (`qDim_unit`)
and the **twist-level** conjugation symmetry (`twist_dualDual`), but **NOT** the general-object
statement.  That is an honest, structural gap, **not** a `sorry` and **not** something axiomatised
here:

* `qDimObj (Xᘁ)` traverses the **double dual** `Xᘁᘁ`, which a plain `[BraidedCategory C]
  [RightRigidCategory C]` does **not** identify with `X`.  A *pivotal* (or ribbon-with-pivotal)
  structure — a natural monoidal iso `X ≅ Xᘁᘁ` — is required, and Mathlib provides no such class.
  Without it the general equality is not merely unproved but *not expressible as a computation on the
  existing data* — hence no `sorry` (a `sorry` would falsely claim the statement is one lemma away).
* Adding the pivotal iso as a `RibbonCategory` field and *asserting* the equality would be
  anti-laundering-forbidden (§Axiomatization-is-NOT-a-Proof): it assumes the conclusion.  The honest
  move is to bean the gap (bean `rtrb`, see the branch note) — a pivotal-structure class plus the
  coherence derivation of `qDimObj (Xᘁ) = qDimObj X` from it is the next real step.

No fit; nothing wired; L2 unchanged (2/7).  Base ring (§7c): everything is stated over a generic
Mathlib braided right-rigid category `C`; no `ℝ`.

-- Ref: [manuscript] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneBalancedRibbon
import QOU.BraidKnot.KeystoneRibbonMTCInput
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

namespace QOU.BraidKnot.Ribbon

open CategoryTheory MonoidalCategory BraidedCategory
open QOU.BraidKnot.Balanced QOU.BraidKnot.RibbonMTC

/-- **A ribbon category**: a `BalancedCategory` over a braided **right-rigid** monoidal category
carrying the **dual-compatibility ribbon axiom** `θ_{Xᘁ} = (θ_X)ᘁ`, i.e. the balancing twist is
compatible with right duality.  Together with the balancing axiom (inherited from `BalancedCategory`)
this is the datum the Reshetikhin–Turaev construction needs: `twist_dual` is what makes the ribbon
trace well-behaved under duality (`qDimObj (Xᘁ)` relates to `qDimObj X`). -/
class RibbonCategory (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    [RightRigidCategory C] extends BalancedCategory C where
  /-- **Ribbon (dual-compatibility) axiom**: `θ_{Xᘁ} = (θ_X)ᘁ`, where `(·)ᘁ = rightAdjointMate`. -/
  twist_dual : ∀ X : C, rightAdjointMate (BalancedCategory.twist X) = BalancedCategory.twist Xᘁ

namespace RibbonCategory

/-- **Non-vacuity: every symmetric right-rigid category is ribbon with the trivial twist `θ = 𝟙`.**
The balancing axiom holds (inherited from `BalancedCategory.ofSymmetric`), and the ribbon axiom
`(𝟙_X)ᘁ = 𝟙_{Xᘁ}` is Mathlib's `rightAdjointMate_id`.  Inhabits `RibbonCategory` on all of Mathlib's
symmetric right-rigid categories, so the class is not conditional-on-`False`.  (Binders are explicit
here so the braided structure is taken from `SymmetricCategory`, avoiding a braiding diamond.) -/
instance (priority := 100) ofSymmetric (C : Type*) [Category C] [MonoidalCategory C]
    [SymmetricCategory C] [RightRigidCategory C] : RibbonCategory C where
  twist_dual := fun X => by
    show rightAdjointMate (𝟙 X) = 𝟙 Xᘁ
    exact rightAdjointMate_id

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]
variable [RibbonCategory C]

/-- **The twist commutes with double-dualization**: `θ_{Xᘁᘁ} = (θ_X)ᘁᘁ`.  Applying the ribbon axiom
`twist_dual` twice — a genuine conjugation-symmetry statement for the twist datum (the double dual is
where the general quantum-dimension conjugation symmetry `qDimObj (Xᘁ) = qDimObj X` would live; see the
module docstring for why that broader statement needs a pivotal structure Mathlib lacks). -/
theorem twist_dualDual (X : C) :
    BalancedCategory.twist (C := C) Xᘁᘁ
      = rightAdjointMate (rightAdjointMate (BalancedCategory.twist X)) := by
  rw [twist_dual, twist_dual]

end RibbonCategory

section QuantumDimension

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]

omit [RightRigidCategory C] in
/-- **The braided quantum dimension of the unit collapses to the identity.**  For the exact pairing
`𝟙_C ⊣ Y` of the monoidal unit with any right dual `Y`, the ribbon trace
`η_{𝟙,Y} ≫ β_{𝟙,Y} ≫ ε_{𝟙,Y}` equals `𝟙_{𝟙_C}`.  The braiding of the unit is a pair of unitors
(`braiding_tensorUnit_left`), and the snake identity (`ExactPairing.evaluation_coevaluation'`),
whiskered by `𝟙_C` (conjugation by the right unitor), forces the composite to be the identity.
(`RightRigidCategory` is omitted — only the unit's exact pairing is needed.) -/
theorem qDim_of_unitPairing (Y : C) [ExactPairing (𝟙_ C) Y] :
    η_ (𝟙_ C) Y ≫ (β_ (𝟙_ C) Y).hom ≫ ε_ (𝟙_ C) Y = 𝟙 (𝟙_ C) := by
  -- Whiskering by `𝟙_C` is conjugation by the right unitor, so it suffices to prove `g ▷ 𝟙 = 𝟙`.
  have key : ∀ g : 𝟙_ C ⟶ 𝟙_ C, g ▷ 𝟙_ C = 𝟙 (𝟙_ C ⊗ 𝟙_ C) → g = 𝟙 (𝟙_ C) := by
    intro g hg
    calc g = (ρ_ (𝟙_ C)).inv ≫ (g ▷ 𝟙_ C) ≫ (ρ_ (𝟙_ C)).hom := by rw [whiskerRight_id]; simp
      _ = 𝟙 (𝟙_ C) := by rw [hg]; simp
  apply key
  rw [braiding_tensorUnit_left]
  -- The snake identity for `𝟙_C ⊣ Y`, with `(λ_ 𝟙).hom ≫ (ρ_ 𝟙).inv = 𝟙` (unit unitors agree).
  have h := ExactPairing.evaluation_coevaluation' (X := 𝟙_ C) (Y := Y)
  rw [unitors_equal, Iso.hom_inv_id] at h
  have step :
      (η_ (𝟙_ C) Y ≫ ((λ_ Y).hom ≫ (ρ_ Y).inv) ≫ ε_ (𝟙_ C) Y) ▷ 𝟙_ C
        = η_ (𝟙_ C) Y ▷ 𝟙_ C ≫ (α_ (𝟙_ C) Y (𝟙_ C)).hom ≫ 𝟙_ C ◁ ε_ (𝟙_ C) Y := by
    simp only [comp_whiskerRight]; monoidal
  exact step.trans h

/-- **The categorical quantum dimension of the monoidal unit (the vacuum object) is `1`.**
`qDimObj (𝟙_C) = 𝟙 (𝟙_C)`.  This is the categorical fact behind the RT-input normalization
`RibbonMTCInput.vac_dim_one`: when the vacuum label's simple object is the unit, its dimension is
genuinely the identity endomorphism of `𝟙_C`, not merely a posited scalar.  It is also the trivial
case of conjugation symmetry — `dim(𝟙) = 1 = dim(𝟙ᘁ)`. -/
theorem qDim_unit : qDimObj (𝟙_ C) = 𝟙 (𝟙_ C) := by
  unfold qDimObj
  exact qDim_of_unitPairing _

end QuantumDimension

end QOU.BraidKnot.Ribbon
