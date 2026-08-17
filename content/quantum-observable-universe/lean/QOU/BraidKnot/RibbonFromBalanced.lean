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

/-! ### Non-vacuity is NOT yet instantiated — and the obstacle is known

`RibbonCategory.ofSymmetric` (θ = 𝟙, whose mate is 𝟙, so `twist_dual` holds on
the nose) is the obvious inhabitant, and it does **not** elaborate here.  It
fails on the instance diamond `KeystonePivotalSpherical` already documents:

```
BalancedCategory.twist_tensor  has  (@BraidedCategory.braiding C _ _ SymmetricCategory.toBraidedCategory X Y).hom
                              wants (@BraidedCategory.braiding C _ _ inst✝³              X Y).hom
```

`SymmetricCategory` carries its own `toBraidedCategory`, which does not unify
with a separate `[BraidedCategory C]` binder.  `KeystonePivotalSpherical` hit
this exact wall and solved it by *omitting* the `[BraidedCategory C]` binder so
the braiding comes from `SymmetricCategory` — but `RightRigidCategory` and
`BalancedCategory` both want the braiding as a parameter here, so the same
dodge does not transfer directly.

**This is stated rather than papered over.**  A `class` with no instance is the
honest encoding of "not yet inhabited"; fabricating one — or weakening
`twist_dual` until something typechecks — is the §3b-tax anti-pattern.  The
mathematics is not in doubt (a symmetric rigid category is ribbon with the
trivial twist); the elaboration is.  Tracked as the next step on bean `rtrb`.

Until it is inhabited, `RibbonCategory` supplies the *statement* of the missing
axiom and nothing more — in particular it does **not** yet discharge `rtqd`'s
`hSpherical`, which was the point of adding it.
-/

end QOU.BraidKnot.Balanced
