---
# qou-clx8
title: 'Prove cLiTwoExt analytic on ℂ ∖ [1,∞) — closes the last Route 5 plumbing link'
status: todo
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - lean
    - mathlib-gap
created_at: 2026-08-07T15:20:00Z
updated_at: 2026-08-07T15:20:00Z
parent: 0yqu
---


## What is open

    cLiTwoExt y := −∫₀¹ log(1 − yz)/z dz    is analytic on   ℂ ∖ [1,∞)

`cLiTwoExt` is **defined** and proved to agree with `cLiTwo` on the disc
(`cLiTwoExt_eq_cLiTwo`, `cLiTwo_eq_intervalIntegral`, both sorry-free,
`QOU/MathlibExt/ComplexDilogarithm.lean`). Analyticity off the disc is **not**
proved. Without it "the analytic continuation" is a **name, not a theorem**, and
`cLiTwoExt(y₁)` is not *identified* with the `Li₂(y₁)` the sum rule refers to —
which matters because `‖y₁‖ = 1.52`, so the defining series diverges there.

## Why this is worth its own bean — one brick, two gaps

The integral converges for **every** `y ∉ [1,∞)` regardless of `|y|`, unlike the
series. So proving this both closes this link *and* supplies the complex
dilogarithm that `qou-ph1k` and `qou-gkco` are blocked on. Mathlib has no
polylogarithm at all (checked 2026-08-03), so this is a genuine Mathlib gap.

## Two routes, from `qou-0yqu`

1. **Termwise integration.** `−Log(1−w) = Σₙ wⁿ/n`
   (`Complex.hasSum_taylorSeries_neg_log`, `‖w‖ < 1`) → `Σₙ yⁿ/n²`. **Already
   done on the disc** — this is exactly `cLiTwo_eq_intervalIntegral`, via
   `intervalIntegral.hasSum_integral_of_dominated_convergence` with geometric
   bound `‖y‖^(k+1)`. Establishes the disc case only; `|y| > 1` still needs a
   separate continuation argument.
2. **Identity theorem in `y`.** `cLiTwo` is analytic on the unit ball
   (`cLiTwo_analyticOnNhd`) and the real case holds on `(0,1)`
   (`LiTwo_eq_integral_unit`), so the real segment is an accumulation set — the
   same shape that worked for `cLiTwo_reflection`. **Missing input: analyticity
   of the RHS in the parameter `y`, i.e. differentiation under the integral
   sign.** Reuses machinery already on this branch and is probably shorter, but
   that one input is not a Mathlib one-liner.

## ⚠ Read before starting — this does NOT approach the sum rule

Route 5 is a **restatement**. Closing this link makes the restatement rigorous;
it does not move the number. Even with the whole chain closed one gets

    Σⱼ Re Vⱼ = −3π²/2  ⟺  −∫₀¹ log P(z)/z dz = −π²/6 − ½log²y₃ + (2/3)(θ−π)²

with the RHS an **unevaluated real integral**. The outgoing agent on PR #4658
was explicit that eleven such theorems landed and none approached the hard part.
Take this bean for the **Mathlib gap it closes** (`qou-ph1k`/`qou-gkco`), not
expecting sum-rule progress.

## Also open, smaller

Integrability of `z ↦ Re log(1 − yⱼz)/z` on `[0,1]` per root was **closed** on
PR #4658 by deriving it via `Integrable.re` (six hypotheses down to three).
Nothing left there.

## Refs

* parent: `qou-0yqu`; siblings `qou-ph1k`, `qou-gkco`
* `QOU/MathlibExt/ComplexDilogarithm.lean`, `QOU/QBeta/FiveTwoSumRuleIntegrand.lean`
* PR #4658
