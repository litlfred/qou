/-
Copyright (c) 2026 litlfred. All rights reserved.

# The quantum dimension of the vacuum, and where conjugation symmetry stops

The ribbon layer itself — `BalancedCategory`, `RibbonCategory`, and the twist API — moved to
[`QOU/MathlibExt/Ribbon.lean`](../MathlibExt/Ribbon.lean), because Mathlib has neither class and the
module is written to be lifted upstream.  `RibbonCategory.twist_dualDual` (`θ_{Xᘁᘁ} = (θ_X)ᘁᘁ`) went
with it, as generic API rather than QOU content.

What stays here is the part that is about `qDimObj` — the categorical quantum dimension
`qDimObj X = η_X ≫ β_{X,Xᘁ} ≫ ε_X ∈ End(𝟙_C)` defined in `KeystoneRibbonMTCInput.lean`.

## What is proved (sorry-free)

* `qDim_of_unitPairing` — for the unit object's exact pairing `𝟙_C ⊣ Y`, the braided quantum
  dimension of `𝟙_C` collapses to the identity: `η ≫ β ≫ ε = 𝟙_{𝟙_C}` (snake identity +
  `braiding_tensorUnit_left`).  Generic in `Y` and its pairing.
* `qDim_conj_object` — **the categorical quantum dimension is conjugation-symmetric**,
  `qDimObj (Xᘁ) = qDimObj X`, for every object, unconditionally.  See the correction below.
* `qDim_unit` — the categorical quantum dimension of the monoidal unit (the vacuum object) is `1`:
  `qDimObj (𝟙_C) = 𝟙 (𝟙_C)`.  This is the categorical statement behind the RT-input normalization
  `RibbonMTCInput.vac_dim_one` (there carried as a hypothesis): when the vacuum label's simple object
  is the unit, its categorical dimension is genuinely `1`, not merely assumed.  It is also the
  trivial case of conjugation symmetry (`dim(𝟙) = dim(𝟙ᘁ) = 1`).

## The conjugation-symmetry goal — CLOSED, and a correction to what this file used to say

The corpus fact `qDim_conj` states the categorical quantum dimension is conjugation-symmetric,
`qDimObj (Xᘁ) = qDimObj X` for **every** object `X`.  `qDim_conj_object` below now proves it,
unconditionally, in any braided right-rigid category — no pivotal, spherical or transport
hypothesis.  It is a one-line consequence of `QOU.MathlibExt.qDimWith_rightDual`.

**An earlier revision of this docstring said that was impossible, and the reasoning was wrong.**  It
read:

> `qDimObj (Xᘁ)` traverses the **double dual** `Xᘁᘁ`, which a plain `[BraidedCategory C]
> [RightRigidCategory C]` does **not** identify with `X`.  A *pivotal* structure … is required, and
> Mathlib provides no such class.  Without it the general equality is not merely unproved but *not
> expressible as a computation on the existing data*.

The premise is correct — that data really does not identify `Xᘁᘁ` with `X` — and the conclusion
does not follow from it.  The **dimension** never needs the identification.  It needs only that the
dimension of a fixed object is the same whichever dual computes it, and `X` is *also* a right dual
of `Xᘁ` via `BraidedCategory.exactPairing_swap`.  Dual-**independence** is strictly weaker than
double-dual **identification**, and it is what the trace actually consumes.

Two things that were right and stay right: refusing to `sorry` it (a `sorry` would have claimed it
was one lemma away from the route being attempted, which it was not), and refusing to axiomatise it
as a class field (§Axiomatization-is-NOT-a-Proof).  The error was in the impossibility claim, not in
the discipline that surrounded it.

The conditional theorems in `KeystonePivotalSpherical.lean` remain valid.  They are no longer the
only route, and their hypotheses are not needed for this conclusion.  Sphericality is a genuinely
separate condition and is untouched.

No fit; nothing wired; L2 unchanged.  Base ring (§7c): everything is stated over a generic Mathlib
braided right-rigid category `C`; no `ℝ`.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.KeystoneRibbonMTCInput
import QOU.MathlibExt.BraidedQuantumDimension
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

namespace QOU.BraidKnot.Ribbon

open CategoryTheory MonoidalCategory BraidedCategory
open QOU.BraidKnot.RibbonMTC

section QuantumDimension

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]

omit [RightRigidCategory C] in
/-- **The braided quantum dimension of the unit collapses to the identity.**  For the exact pairing
`𝟙_C ⊣ Y` of the monoidal unit with any right dual `Y`, the braided (twistless) trace
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

/-- **The categorical quantum dimension is conjugation-symmetric**: `qDimObj (Xᘁ) = qDimObj X`.

The corpus fact `qDim_conj`, at last unconditional.  `qDimObj` is by definition the braided
quantum dimension taken against the canonical right dual, so this is
`QOU.MathlibExt.qDimWith_rightDual` read through that definition. -/
theorem qDim_conj_object (X : C) :
    qDimObj ((X : C)ᘁ) = qDimObj X :=
  QOU.MathlibExt.qDimWith_rightDual X

end QuantumDimension

end QOU.BraidKnot.Ribbon
