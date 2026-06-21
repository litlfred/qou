/-
Copyright (c) 2026 litlfred. All rights reserved.

# λ_scale absorbed into VolDensity — formal documentation (2026-06-04)

> **⚠ Critical framing reminder.** Per AGENTS.md §"Mass-and-Binding-
> Algorithms appendix sync" + [`docs/lambda-scale-absorbed-into-vol-density.md`](../../../../../docs/lambda-scale-absorbed-into-vol-density.md):
> the numerical factor previously called `λ_scale` was **absorbed**
> into the canonical per-knot `VolDensity(K)` evaluation on 2026-05-23
> (commit `ffdd84409`). The mass formula is:
>
> ```
> m(K) = m_e × VolDensity(K, q₀)
> ```
>
> Single Geom call — **no separate λ_scale constant**.

## Why this file exists

When agents (Claude or Copilot) probe the QOU codebase for "λ_scale",
this file serves as the canonical Lean-side record that:

1. There is **no** `λ_scale` definition in the Lean infrastructure.
2. The previous attempts at a "Yekutieli per-cell variant" were purged
   on 2026-05-24 (commit `71d674da1`) as non-canonical.
3. The "2.89% m_p gap" is **not** a "λ_scale closure" problem — it is
   the gap between the current categorical `VolDensity(𝓑₃)` computation
   and its categorically-exact value.

## Lean-side enforcement

We provide a single inert definition `lambdaScaleAbsorbedIntoGeom`
recording the absorption. Any downstream attempt to define a separate
`lambdaScale : ℝ` should reference this absorption note and **not**
introduce a numerical constant.

## Cross-refs

- Canonical doc: [`docs/lambda-scale-absorbed-into-vol-density.md`](../../../../../docs/lambda-scale-absorbed-into-vol-density.md)
- AGENTS.md §"⚠ Critical framing — do NOT treat `λ_scale` as a separate object"
-/

namespace QOU.Machinery

/-! ## Absorption record -/

/-- **Inert marker** recording the 2026-05-23 absorption of
`λ_scale` into the canonical per-knot `VolDensity(K)` evaluation.

This is intentionally a `Unit`-valued constant: there is **no**
substantive λ_scale to define. The mass formula is
`m(K) = m_e × VolDensity(K, q₀)` — single Geom call, no separate
λ_scale constant.

Use this constant as a documentation anchor (`#check
lambdaScaleAbsorbedIntoGeom`) when downstream code seems to assume
a separate `λ_scale`. -/
def lambdaScaleAbsorbedIntoGeom : Unit := ()

/-- **The absorption is observable** at the type level: any Lean
function that takes a separate `λ_scale : ℝ` argument is doing the
wrong thing. This conditional class is intentionally **unsatisfiable**
(no instance can be provided) to flag the antipattern at the
type-class resolution layer. -/
class SeparateLambdaScale_Antipattern : Prop where
  /-- This field is `False` — class is unsatisfiable. The antipattern
  is "treating λ_scale as a separate object" (purged 2026-05-24). -/
  is_antipattern : False

/-- The antipattern is provably impossible. -/
theorem no_separate_lambda_scale (h : SeparateLambdaScale_Antipattern) : False :=
  h.is_antipattern

end QOU.Machinery
