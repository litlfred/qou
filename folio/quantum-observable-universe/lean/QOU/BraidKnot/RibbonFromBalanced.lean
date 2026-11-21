/-
Copyright (c) 2026 litlfred. All rights reserved.

# Ribbon = balanced + dual compatibility — moved to `QOU.MathlibExt.Ribbon`

`BalancedCategory` stops one axiom short of a **ribbon** category: the dual-compatibility condition
`θ_{Xᘁ} = (θ_X)ᘁ`.  Mathlib has neither, so both now live in
[`QOU/MathlibExt/Ribbon.lean`](../MathlibExt/Ribbon.lean) as an upstream candidate.

This file is a **forwarding alias** for `QOU.BraidKnot.Balanced.RibbonCategory`.

The scope note this file carried is preserved there and still holds: `ofSymmetric` gives `θ = 𝟙` and
`𝟙ᘁ = 𝟙`, so a symmetric rigid category is ribbon with the trivial twist — `q = 1` stays a
describable member rather than an excluded one, which is why the fix is "add the twist" and not
"forbid symmetric".

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.MathlibExt.Ribbon

namespace QOU.BraidKnot.Balanced

export QOU.MathlibExt (RibbonCategory)

end QOU.BraidKnot.Balanced
