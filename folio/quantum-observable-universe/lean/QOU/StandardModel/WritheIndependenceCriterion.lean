/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# The proton/neutron test does not establish writhe-independence

`folio/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md`
states the requirement that drives the whole hypercharge programme:

> The writhe map is falsified as a hypercharge assignment: the proton and
> neutron share `Y = +1` while their writhes differ.  The framework therefore
> requires a second crossing invariant, **independent of the writhe**, to
> instantiate `Y`.

The originating audit
(`docs/audits/2026-06-02-u1-hypercharge-assignment.md`) gives the same
argument — "FALSIFIED as a hypercharge-Y map by the sharp proton/neutron
same-Y test (Y(p)=Y(n)=+1, but writhe splits them)" — with the derived
framing writhes `w(p) = +2`, `w(n) = −2`.

**The premise is right; the inference is not.**  Equal `Y` at *distinct*
writhes falsifies an **injective** writhe→`Y` map (in particular the linear
`Y = c·w` that the framing phase `q^{w·c}` would give).  It says nothing
against a *non-injective* function of the writhe, because a function is
perfectly entitled to take the same value at two different points.

Concretely, `Y = w²/4` reproduces both rows: `(+2)²/4 = 1` and
`(−2)²/4 = 1`.  So the proton/neutron test is *consistent* with `Y` factoring
through the writhe, and cannot be what forces a second invariant to be
independent of it.

## What is proved

* `pn_test_admits_writhe_only_map` — an explicit writhe-only map reproducing
  `Y(p) = Y(n) = +1` from `w = ±2`.  The p/n data alone does not exclude
  factoring through `w`.
* `injective_writhe_map_is_falsified` — what the p/n test *does* establish:
  no **injective** function of the writhe can do it.  This is the honest
  content of the original argument.
The general criterion is **not** restated here: `sm-hypercharge-invariant.lean`
already proves `factors_through_iff` (`Y` factors through `w` iff `Y` is
constant on the fibres of `w`) and
`HyperchargeInvariant.exists_writhe_degenerate_pair`.  What that file lacks,
and this one supplies, is the demonstration that the *published p/n argument*
does not establish the hypothesis those theorems consume.

## Status of the requirement itself

The requirement is probably still correct — it is the *stated reason* that
fails, not necessarily the conclusion.  The corpus already contains the right
shape of argument: `SecondCrossingInvariant.lean`'s
`baryon_vacuum_separating` exhibits two states of **equal writhe** (`0`, the
Borromean baryon per the s5-so3 audit) with **different** baryon number
(`1` vs `0`) — the hypothesis `exists_writhe_degenerate_pair` needs.

But that lemma takes its writhe and `B` values as **hypotheses**; it does not
derive them from the framework.  So independence is currently *supported by a
correct argument shape whose premises are assumed*, not *proved*.  Supplying
those two writhe values as derived facts would close it.

## Honest scope

**Scope-(a)** — a statement about what the published argument establishes,
not about hypercharge.  It does **not** show `Y` factors through the writhe
(it almost certainly does not), and it does not weaken the search for a second
invariant.  It shows the *stated justification* is insufficient and names the
test that would suffice.

Nothing here is archimedean: `ℤ`-valued writhe, `ℚ`-valued charge, no
ordering, no `Real` (§7c).
-/

import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

namespace QOU.StandardModel

/-- **The p/n test admits a writhe-only map.**

With the derived framing writhes `w(p) = +2`, `w(n) = −2`, the map
`Y = w²/4` returns `+1` on both.  So `Y(p) = Y(n) = +1` at distinct writhes
is *consistent* with `Y` being a function of the writhe alone, and cannot by
itself force a second invariant independent of it. -/
theorem pn_test_admits_writhe_only_map :
    ∃ f : ℤ → ℚ, f 2 = 1 ∧ f (-2) = 1 := by
  refine ⟨fun w => ((w : ℚ) * (w : ℚ)) / 4, ?_, ?_⟩ <;> norm_num

/-- **What the p/n test actually establishes.**

No *injective* function of the writhe can assign the proton and neutron the
same hypercharge, since their writhes differ.  This is the honest content of
the published argument: it falsifies the linear/injective map `Y = c·w` (the
framing phase `q^{w·c}`), not every function of `w`. -/
theorem injective_writhe_map_is_falsified
    {S : Type*} (w : S → ℤ) (Y : S → ℚ) (p n : S)
    (hw : w p ≠ w n) (hY : Y p = Y n)
    (f : ℤ → ℚ) (hinj : Function.Injective f)
    (hfac : ∀ s, Y s = f (w s)) :
    False := by
  apply hw
  apply hinj
  rw [← hfac p, ← hfac n, hY]

-- NOTE: the general criterion is NOT restated here.  It is already proved in
-- `folio/quantum-observable-universe/appendix-standard-model/sm-hypercharge-invariant.lean`
-- as `factors_through_iff` (`Y` factors through `w` iff `Y` is constant on the
-- fibres of `w`) with the corollary `HyperchargeInvariant.exists_writhe_degenerate_pair`.
-- This file supplies only what that file lacks: the demonstration that the
-- *published p/n argument* does not establish the hypothesis those theorems need.

end QOU.StandardModel
