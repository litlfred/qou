/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.SchurWeyl.HeckeInclusion

/-!
# The Hecke tower grows strictly

Bean `qou-p8yg`. The tower inclusion `H_m(q) → H_{m+1}(q)` is **never onto**, so the concrete
Iwahori–Hecke filtration is strictly increasing at every level and at every `m` — not just at
`m = 0`, which was all `HeckeTowerWitness` could reach.

## What this needed, and the one thing it did NOT need

`qou-p8yg` names the general-`n` blocker as the **lower** bound `dim H_n(q) ≥ (n+1)!`, citing
`qou-uoal`'s closing note that only the upper bound `finrank_le_factorial` was proved. That is
**stale**: `HeckeWedderburnGeneral.finrank_hecke_eq_factorial` is an *equality*, and its own
docstring says the lower bound "is forced by the surjection onto a space of dimension `(n+1)!`".
So the blocker was already discharged, exactly as the bean's own LEAD suspected.

🛑 **And strictness does not need `heckeIncl_injective`.** `qou-ejde` lists "the FILTRATION is
strict" among the things its injectivity result buys. Measured here: it does not. Non-surjectivity
follows from a dimension count alone —

`finrank (range) ≤ finrank H_m = (m+1)! < (m+2)! = finrank H_{m+1}`

— where the first step is `LinearMap.finrank_range_le`, which has no injectivity hypothesis. So
`heckeIncl_range_lt_top` below holds over any characteristic-zero field at generic `q`, with
injectivity nowhere in its cone.

What injectivity *does* buy is the sharp value: `finrank_range_heckeIncl` upgrades that `≤` to `=`,
pinning the image at exactly `(m+1)!`. That is a strictly stronger statement and it is the one that
inherits the `ℝ` scope, because `heckeIncl_injective` does.

## Scope, stated per statement rather than for the file

| statement | base | needs injectivity | file |
|---|---|---|---|
| `heckeIncl_range_lt_top` | any `[Field K] [CharZero K]`, `q ≠ 0`, `NotRootOfUnity q` | **no** | this one |
| `finrank_range_heckeIncl` | `ℝ` | yes | `HeckeTowerStrictSharp` |

**The independence is structural, not a claim in prose.** This file does **not** import
`HeckeInclInjective` — read its import list. So `heckeIncl_injective` is not in
`heckeIncl_range_lt_top`'s cone, and the compiler enforces that rather than the docstring asserting
it. The sharp value lives in a separate file precisely so that this one's imports carry the
evidence.

Genericity is irreducible in both: `finrank_hecke_eq_factorial` needs semisimplicity, and at a root
of unity `H_n(q)` is not semisimple.

## What this does NOT give

This is the **concrete** Hecke tower. It says nothing about `twH` in
`MathlibExt/HeckeTowerWitness`, whose `twH_zero_lt_one` is proved through a rank-2 collapse that
provably cannot separate `H 1` from `H 2` — transferring this there needs the bridge, which
`qou-ejde` measures as a separate and unbuilt thing. Nor does it touch `ofLim` injectivity or
`trLim` faithfulness.

`qou-p8yg` also records a **refuted** proof sketch for `twH 1 < twH 2` (an algebra map sending
`g m ↦ q·1` for `m ≥ 2`); nothing here revives it, and it remains refuted by that bean's own
`braid(1)` argument.

-- Ref: [leitner2026] beans qou-p8yg, qou-ejde; Geck-Pfeiffer, *Characters of Finite Coxeter Groups
--      and Iwahori-Hecke Algebras*, §8.1.
-/

namespace QOU.SchurWeyl

open QOU.SchurWeyl.HeckeInclusion

/-- **The tower inclusion is never onto**, so the Hecke filtration grows strictly. Needs only the
dimension count `(m+1)! < (m+2)!` — *not* injectivity; see the module docstring. -/
theorem heckeIncl_range_lt_top {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    LinearMap.range (heckeIncl K q q⁻¹ m).toLinearMap < ⊤ := by
  haveI := finiteDimensional_hecke (K := K) q q⁻¹ m
  haveI := finiteDimensional_hecke (K := K) q q⁻¹ (m + 1)
  refine lt_of_le_of_ne le_top fun htop => ?_
  have hle : Module.finrank K (LinearMap.range (heckeIncl K q q⁻¹ m).toLinearMap)
      ≤ Module.finrank K (Hecke K q q⁻¹ m) :=
    LinearMap.finrank_range_le _
  rw [htop, finrank_top, finrank_hecke_eq_factorial q hq0 hq2 (m + 1),
    finrank_hecke_eq_factorial q hq0 hq2 m] at hle
  have hlt : (m + 1).factorial < (m + 1 + 1).factorial := by
    have hs := Nat.factorial_succ (m + 1)
    have hp := Nat.factorial_pos (m + 1)
    nlinarith [hs, hp]
  omega

end QOU.SchurWeyl
