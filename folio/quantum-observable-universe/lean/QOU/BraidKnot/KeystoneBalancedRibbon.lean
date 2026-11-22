/-
Copyright (c) 2026 litlfred. All rights reserved.

# The balancing twist — moved to `QOU.MathlibExt.Ribbon`

Mathlib provides `BraidedCategory` and `Left`/`RightRigidCategory` but **no balancing twist** — the
`θ_X : X ⟶ X` that upgrades a braided category to a *balanced* (and, with rigidity, a *ribbon*)
category.  That is a Mathlib gap, so the class now lives with the other Mathlib gaps, in
[`QOU/MathlibExt/Ribbon.lean`](../MathlibExt/Ribbon.lean), stated so it can be lifted upstream
verbatim.

This file is a **forwarding alias**, kept so `QOU.BraidKnot.Balanced.BalancedCategory` — which
`CategoricalFoundations.lean` names explicitly in the `QuantumUniverse` axiom binder — keeps
resolving.  It declares nothing of its own; there is exactly one `BalancedCategory` in the tree.

Why the move: `RibbonCategory` had been declared **twice**, here-adjacent in
`KeystoneRibbonCategory.lean` (namespace `…Ribbon`) and in `RibbonFromBalanced.lean` (namespace
`…Balanced`), with `twist_dual` written in opposite orientations — `rightAdjointMate (twist X) =
twist Xᘁ` against `twist Xᘁ = (twist X)ᘁ`.  Those are the same equation, so the two classes were the
same object under two names, each with its own `ofSymmetric` instance at priority 100.  Neither had
a single consumer, so consolidating cost nothing.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.MathlibExt.Ribbon

namespace QOU.BraidKnot.Balanced

export QOU.MathlibExt (BalancedCategory)

end QOU.BraidKnot.Balanced
