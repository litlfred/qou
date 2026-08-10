---
# hypr
title: 'Discharge conj:surreal-limit-transfer from Mathlib Hyperreal (ℝ* is a SurrealField)'
status: todo
type: task
priority: high
tags:
    - lean
    - surreals
    - nonstandard
    - conjecture-discharge
created_at: 2026-08-09T19:15:46Z
updated_at: 2026-08-09T19:15:46Z
---

`QOU/AppendixSurreals/SurrealLimitTransfer.lean` carries `conj:surreal-limit-transfer`
as a content-bearing class with **no instance**, on the stated grounds that an
ω-evaluation "exists model-theoretically (Robinson ultrapower; Berarducci–Mantova germ
evaluation at ω), but is not constructible from the abstract `SurrealField` interface
alone".

That is right about the *abstract* interface — and it is the reason no instance was
fabricated, correctly. But the Robinson ultrapower it names **is already in Mathlib**,
and every class field appears to be exactly a Mathlib lemma. Checked 2026-08-09 against
the vendored Mathlib:

| `SurrealLimitTransfer` field | Mathlib |
|---|---|
| `evalOmega : (ℕ → ℝ) → K` | `Hyperreal.ofSeq` (`ℝ* = Germ (hyperfilter ℕ) ℝ`) |
| `evalOmega_const` | `Germ.const` / `Hyperreal.ofReal = const` |
| `evalOmega_add`, `evalOmega_mul` | `Germ` ring structure |
| `evalOmega_le_of_eventuallyLE` | `Germ` order + `Nat.hyperfilter_le_atTop` |
| `evalOmega_isClose_of_tendstoReal` | `Hyperreal.isSt_of_tendsto` |

And `SurrealField` extends `Field K, LinearOrder K, IsStrictOrderedRing K` — `ℝ*` has
all three as instances in `Mathlib/Analysis/Real/Hyperreal.lean` (lines 30/33/36), plus
`ofReal := const`. So `SurrealField ℝ*` looks close to free, and
`SurrealLimitTransfer ℝ*` follows.

**Payoff.** Discharges a standing no-instance primary conjecture, and makes the two
derived theorems (`standardPart_evalOmega_of_tendstoReal`,
`tendstoReal_le_of_eventuallyLE`) unconditional. Everything downstream that takes
`[SurrealLimitTransfer]` as a hypothesis becomes unconditional at `K = ℝ*`.

**⚠ The one thing that will bite, and the reason to scope this carefully.**
`Hyperreal.isSt_ofSeq_iff_tendsto : IsSt (ofSeq f) r ↔ Tendsto f (hyperfilter ℕ) (𝓝 r)`,
and `Nat.hyperfilter_le_atTop` means hyperfilter convergence is **strictly weaker** than
`atTop` convergence. The arrow `Tendsto atTop → IsSt` is available
(`isSt_of_tendsto`); the **converse is false**. So this instance lets you *push* real
limits into the surreal/hyperreal world, but does **not** let you discharge a
`Tendsto … atTop` goal by a standard-part computation. `IsSt (ofSeq f) r` is `f(ω) ≈ r`
for one specific `ω`, not "for all infinite hypernaturals", which is what a genuine NSA
limit argument needs and which Mathlib does not package.

Consequence: this bean is worth doing on its own merits, but it does **not** on its own
let surreal/standard-part machinery replace an ε–δ argument whose *goal* is
`Tendsto … atTop` — see the "what this cannot do" note in bean `thmb`.

Related: `QOU/AppendixSurreals/ClassicalLimitStpart.lean` currently defines
`abbrev StandardPart := ℝ → ℝ` — an explicit **surrogate**, "represented as a real
function for the formal Lean shell", carrying no surreal content. If `ℝ*` lands, that
surrogate should be revisited too.
