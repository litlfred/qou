import QOU.BraidKnot.KeystoneBalancedRibbon
import QOU.BraidKnot.KeystonePivotalSpherical

/-!
# Ribbon = balanced + dual compatibility, and the sphericality it buys

`KeystoneBalancedRibbon` (bean `rtrb`) gives `BalancedCategory`: a twist with
`θ_𝟙 = 𝟙`, naturality, and the Joyal–Street balancing axiom.  It stops one
axiom short of a **ribbon** category — the dual-compatibility condition

    θ_{Xᘁ} = (θ_X)ᘁ

which `rtrb`'s own note flags as the next step.  #5262 arrived at the same
missing field independently, from the mass side: it is what stands between the
merged twist and `rtqd`'s `qDim_conj`, whose consumer chain runs
`dim_q → G⁻¹ → the mass chain`.

This file adds that axiom as an **extension**, leaving `BalancedCategory`
untouched so nothing already depending on it changes shape.

## Scope

`RibbonCategory` here is *balanced + dual-compatible*.  The classical case
survives: `ofSymmetric` gives `θ = 𝟙`, and `𝟙ᘁ = 𝟙`, so a symmetric rigid
category is ribbon with the trivial twist — `q = 1` stays a describable member
rather than an excluded one, which is the whole reason the fix is "add the
twist" and not "forbid symmetric".

-- Ref: [manuscript] docs/coordination/s5-so3-keystone.md
-/

open CategoryTheory MonoidalCategory

namespace QOU.BraidKnot.Balanced

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C]
  [RightRigidCategory C]

/-- **A ribbon category**: balanced, with the twist compatible with duals.

    The single field is the axiom `BalancedCategory` lacks.  Stated with
    `rightAdjointMate` (`ᘁ`), which is the dual Mathlib supplies. -/
class RibbonCategory (C : Type*) [Category C] [MonoidalCategory C]
    [BraidedCategory C] [RightRigidCategory C] extends BalancedCategory C where
  /-- `θ_{Xᘁ} = (θ_X)ᘁ`. -/
  twist_dual : ∀ X : C, twist (Xᘁ) = (twist X)ᘁ

/-! ### Non-vacuity

An earlier revision of this file recorded the instance as blocked, saying the
`KeystonePivotalSpherical` dodge — omitting `[BraidedCategory C]` so the
braiding comes from `SymmetricCategory` — "does not transfer directly" because
`RightRigidCategory` and `BalancedCategory` both want the braiding as a
parameter.

**That was wrong, and it is retracted.** The dodge transfers exactly. Declaring
the section without a `[BraidedCategory C]` binder resolves the diamond with
`[RightRigidCategory C]` present, and the instance below elaborates. The error
was reasoning about what the elaborator would do instead of asking it.
-/

section Symmetric

variable {C : Type*} [Category C] [MonoidalCategory C] [SymmetricCategory C]
  [RightRigidCategory C]

/-- **A symmetric rigid category is ribbon, with the trivial twist.**

    `ofSymmetric` supplies `θ = 𝟙`, and the mate of an identity is an identity,
    so `twist_dual` holds on the nose. This is the non-vacuity witness for
    `RibbonCategory`, and it is what keeps the classical limit *inside* the
    category: `θ = 𝟙` means `q = 1`, a describable member rather than an
    exclusion. -/
instance (priority := 100) ribbonOfSymmetric : RibbonCategory C where
  __ := BalancedCategory.ofSymmetric
  twist_dual := fun X => by
    show 𝟙 (Xᘁ) = (𝟙 X)ᘁ
    simp

end Symmetric

end QOU.BraidKnot.Balanced
