---
# qou-rhyp
title: 'Discharge the nine Rogers-L hypotheses in FiveTwoLevelSevenLadder (reflection / inversion / Landen / five-term)'
status: todo
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - lean
    - mathlib-gap
created_at: 2026-08-07T22:05:00Z
updated_at: 2026-08-07T22:05:00Z
parent: 0yqu
---


## Why this bean exists

`QOU/QBeta/FiveTwoLevelSevenLadder.lean` proves the three level-7 numerators
**from nine hypotheses**, with `L` abstract. Those hypotheses were, until now,
only prose inside `qou-fivt` — not a tracked gap. They are the concrete remaining
Lean work, so they get their own bean.

**All nine are verified true** against the real Rogers `L` at the actual `wₖ`
(residuals `≤ 3.4e-41`), so none is vacuous. What is missing is *proof*.

## The nine, grouped by difficulty

### 1. Reflection ×4 — **should be nearly free, do this first**

`hrw`, `hrq`, `hrr`, `hrs`: `L(1−x) = L1 − L x`.

The corpus already has, **sorry-free**, in `QOU/Archimedean/DilogReflection.lean`:

```lean
theorem LiTwo_reflection' (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    LiTwo x + LiTwo (1 - x) = Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x)
```

With Rogers `L(x) := LiTwo x + log x · log(1−x)/2` the two `½ log log` terms add to
a full `log x · log(1−x)`, which **exactly cancels** the correction term:

    L(x) + L(1−x) = LiTwo x + LiTwo(1−x) + log x·log(1−x) = π²/6

So Rogers reflection follows from `LiTwo_reflection'` by `linear_combination`,
after rewriting `1 − (1 − x) = x`. All four points lie in `(0,1)`
(`w₂, q, r, s` and their reflections), so the side conditions hold.
**Note `LiTwo` lives in namespace `QOU.QPochhammer`,** not `QOU.Archimedean`.

### 2. Inversion ×1 and Landen ×3 — real analysis, not yet in the corpus

`hinv1`: `L x + L(1/x) = 2·L1` for `x > 1`.
`hlan1/2/3`: `L x + L(x/(x−1)) = 0` for `x < 0`.

Verified on **generic** points (`qou-fivt`, gate G1), not just our `wₖ` — so they
are the standard extensions, not coincidences. Neither is in Mathlib (see
`qou-mlbg`: Mathlib has no `Li₂` at all). Each is a one-variable identity
provable the same way `LiTwo_reflection'` is — constancy of a derivative — so the
corpus's existing proof is the template.

### 3. The five-term relation ×3 — the real work

`hA`, `hB`, `hC` are instances of

    L(x) + L(y) − L(xy) − L(x(1−y)/(1−xy)) − L(y(1−x)/(1−xy)) = 0

with all arguments in `(0,1)`. This is the one genuinely substantial item. It is
classical (Abel), and it is the single input the whole Route-11 derivation rests
on.

## ⚠ Queued for roasting

* **The four reflection instances** claim their arguments lie in `(0,1)`. That is
  true for `w₂, q, r, s` numerically — but the Lean statement does **not** carry
  the side conditions, because `L` is abstract. When `L` is instantiated with the
  concrete Rogers `L`, those `0 < x < 1` obligations appear and must be
  discharged. **Do not assume they come for free.**
* `hinv1` bundles inversion *with* the algebraic accident `1/w₁ = 1 − w₂`. If
  someone instantiates it carelessly they will prove inversion at the wrong
  point. Keep the two facts separate when discharging.

## Refs

* `QOU/QBeta/FiveTwoLevelSevenLadder.lean` — the four theorems taking these hypotheses
* `QOU/Archimedean/DilogReflection.lean` — `LiTwo_reflection'`, the template and the input
* `qou-fivt` (Routes 10–11), `qou-mlbg` (Mathlib has no `Li₂`)
