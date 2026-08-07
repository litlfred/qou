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

---

## 2026-08-07 (PR #4658 takeover) — groundwork done; Lean BLOCKED in this environment

### ⚠ Lean could not be built or checked here

`elan`/`lake` are absent and the environment's network policy **denies
`release.lean-lang.org:443` (403 on CONNECT)**, so the `leanprover/lean4:v4.24.0`
toolchain cannot be installed and `lake exe cache get` cannot run. **No Lean was
written**, deliberately: writing unverifiable Lean would violate the corpus's
no-stub discipline. A session with toolchain access should pick this up.

What follows is the mathematical groundwork, which needs no build.

### 1. The statement is TRUE — verified before anyone formalizes it

`cLiTwoExt y := −∫₀¹ Log(1 − yz)/z dz` (principal `Log`) equals `Li₂(y)`:

* **exactly (diff `0.0` at 40 dps) at all three 5₂ roots** — including `y₁` with
  `‖y₁‖ = 1.52`, which is precisely the identification `qou-0yqu` lists as
  missing. So `cLiTwoExt(y₁) = Li₂(y₁)` is *true*; only the proof is open.
* on a 28-point grid off the real axis (`Re y ∈ [−4,6]`, `Im y ∈ [0.05,3]`):
  **28/28 agree to `< 1e-25`.**

### 2. The side condition in the current bricks is SUFFICIENT BUT NOT NECESSARY

`intervalIntegrable_log_one_sub_div` requires `Re(1 − yz) > 0` on `[0,1]`,
i.e. `Re(1 − y) > 0`. That **fails** at e.g. `y = 1.5 + 0.3i` and `y = 3 + 0.001i`
**while the identity still holds**. Do not formalize `Re(1−y) > 0` as if it were
the real hypothesis — it needlessly excludes most of `ℂ ∖ [1,∞)`.

**The right hypothesis is geometric and much cleaner:**

> For `Im y ≠ 0`, the segment `{1 − yz : z ∈ [0,1]}` meets the real axis **only**
> at `z = 0` (the point `1`), because `Im(1 − yz) = −z·Im y` vanishes on `[0,1]`
> only at `z = 0`. Hence the path never meets the principal cut `(−∞,0]`, and
> `Log(1 − yz)` is continuous along it for **every** `y` off the real axis.

That is the natural statement to prove, and it covers `ℂ ∖ ℝ` in one step; the
real interval `(−∞,1)` is then the easy real-analytic case, and `[1,∞)` is
genuinely excluded (see 3).

### 3. Why the cut is exactly `[1,∞)`

For real `y > 1` the integrand is singular **inside** the interval: `1 − yz = 0`
at `z = 1/y ∈ (0,1)`. That is the actual obstruction, and it is what makes
`[1,∞)` — not `|y| ≥ 1` — the right cut.

### 4. ⚠ Numerical trap, recorded because the corpus verifies numerically

When `0 < Re(1/y) < 1` the integrand has a near-logarithmic singularity at
`z ≈ 1/y`. Plain `quad([0,1])` **silently** returns a wrong answer — at
`y = 3 + 0.001i` it is off by `1.15e-2` while reporting no error. Splitting the
quadrature at `Re(1/y)` restores exactness (diff `0.0`). Any probe evaluating
`cLiTwoExt` off the disc **must** split at `Re(1/y)`.

### Still open, unchanged

The Lean proof itself (differentiation under the integral sign for analyticity
in the parameter `y`). Route 2 of the two listed above remains the shorter path.
**Nothing stubbed. Sum rule status: verified to 80 dps, unproved.**
