---
# qou-ph1k
title: 'GAP: complex Li₂ — extend LiTwo to ℂ and |z|>1, with the complex reflection identity'
status: todo
type: task
created_at: 2026-08-03T14:48:28Z
updated_at: 2026-08-03T14:48:28Z
---


## What exists already — do NOT start from scratch

**Mathlib has no polylogarithm** (checked 2026-08-03: no `Polylog`, no `dilog`,
no `Real.dilog`). But **QOU has its own**, and it is substantial:

- `QOU/Archimedean/DilogarithmArchimedeanLimit.lean` —
  `noncomputable def LiTwo (x : ℝ) : ℝ := ∑' k, x^(k+1)/((k:ℝ)+1)^2`
- `QOU/Archimedean/DilogReflection.lean` — **sorry-free**, and proves the Euler
  reflection identity:

      LiTwo_reflection' (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
        LiTwo x + LiTwo (1 - x) = π^2/6 - log x * log (1 - x)

  plus the derivative infra Mathlib lacks (`hasDerivAt_LiTwo`,
  `dilogDerivSeries_tsum`), boundary limits, and `LiTwo_half`.

There is also extensive **quantum** dilogarithm infra (`li2_q`, Faddeev `Φ_b`,
`QuantumDilogarithm*`, ~20 files) — a *different* object; do not conflate.

## The actual gap

`LiTwo` is `ℝ → ℝ` and the proved reflection identity is restricted to
`0 < x < 1`. The 5₂ saddle sum rule (bean `qou-0yqu`) needs `Li₂` at the three
roots of `y³−2y²+3y−1`:

| root | value | covered by `LiTwo`? |
|---|---|---|
| `y₃` | `0.430159709…` | **YES** — in `(0,1)`, `LiTwo_reflection'` applies directly |
| `y₁` | `0.78492 + 1.30714i` | no — complex, and `\|y₁\| = 1.52 > 1` |
| `y₂` | `conj(y₁)` | no |

So the gap is precisely: **a complex `Li₂` (or at minimum `|z| > 1` via the
inversion formula) together with the complex reflection identity.** One of the
three roots is already in range — this is an extension, not a rebuild.

## Why it is worth doing

It is the blocker on the Lean side for `qou-0yqu`. `QOU/QBeta/FiveTwoSaddleSumRule.lean`
currently proves the reflection reduction with `Li : ℂ → ℂ` **abstract** and the
reflection identity as an explicit hypothesis. With a complex `LiTwo` that
hypothesis becomes dischargeable and the theorem stops being conditional.

Cost is real but bounded: branch cuts on `(1,∞)` are the hard part, and the
inversion formula `Li₂(z) + Li₂(1/z) = −π²/6 − (1/2)log²(−z)` is what carries
`|z| > 1`.

## Not required for

The Kubert/distribution relation (the *second* missing relation in `qou-0yqu`)
would need further infra beyond this. This bean unblocks the reduction, not the
whole sum rule.

## Refs

- `QOU/Archimedean/DilogReflection.lean` (sorry-free, the exemplar to extend)
- `QOU/QBeta/FiveTwoSaddleSumRule.lean` (the abstract-`Li` consumer)
- bean `qou-0yqu` (the sum-rule proof gap this unblocks)
