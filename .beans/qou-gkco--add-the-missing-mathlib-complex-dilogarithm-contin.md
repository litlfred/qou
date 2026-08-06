---
# qou-gkco
title: 'Add the missing Mathlib: complex dilogarithm (continuation + reflection + inversion), upstreamable'
status: todo
type: task
created_at: 2026-08-06T22:48:21Z
updated_at: 2026-08-06T22:48:21Z
---


## Goal

Build the complex dilogarithm Mathlib lacks, in Mathlib style, so it can be
offered upstream — and so the 5₂ saddle sum rule (`qou-0yqu`) stops being
blocked on a missing special function.

**Mathlib has no polylogarithm at all** (verified 2026-08-06: no `Polylog`,
no `dilog`, no `Real.dilog`). This is a genuine gap in Mathlib, not just a
QOU inconvenience — `Li₂` is standard special-function territory.

## Landed so far (this bean's first brick)

`QOU/MathlibExt/ComplexDilogarithm.lean` — lean-direct exit 0, sorry-free:

- `cLiTwo z = ∑' k, z^(k+1)/((k:ℂ)+1)^2` — the defining series
- `cLiTwo_zero`
- `cLiTwo_term_norm_le` — `‖z^(k+1)/(k+1)²‖ ≤ ‖z‖^(k+1)`
- `cLiTwo_summable` — convergence on the **open unit disc**

Written with **no QOU-specific imports** (Mathlib only), deliberately, so it
stays upstreamable.

## Remaining bricks, in dependency order

1. **Analytic continuation past `|z| = 1`.** The series is the definition; the
   function is not. Needed because `|y₁| = 1.52 > 1` at the 5₂ saddle.
2. **Inversion formula** `Li₂ z + Li₂ (1/z) = −π²/6 − ½·log(−z)²`. The standard
   route to `|z| > 1`, and probably the cheapest way to get (1) for the
   specific arguments needed.
3. **Complex Euler reflection** `Li₂ z + Li₂ (1−z) = π²/6 − log z · log(1−z)`.
   This is the one that discharges `hrefl` in
   `QOU.QBeta.FiveTwo.sum_reflection_of_branch`.
4. **Agreement with the real theory** — `cLiTwo ∘ ofReal = LiTwo` on `(0,1)`,
   tying this to `QOU.Archimedean.LiTwo`. Deliberately NOT in the MathlibExt
   file (would break upstreamability); belongs in a QOU-side bridge file.

## Reuse — do not start from scratch

`QOU/Archimedean/DilogReflection.lean` is **sorry-free** and already proves the
*real* Euler reflection on `(0,1)`, plus `hasDerivAt_LiTwo`,
`dilogDerivSeries_tsum`, boundary limits, `LiTwo_half`. Brick 3 may well be
reachable by analytic continuation from that real result via the identity
theorem, rather than by redoing the complex computation. Try that first.

## Branch-cut warning

`Li₂` has a cut on `[1, ∞)`. Mathlib's `Complex.log` cut is `(−∞, 0]`. The two
do not line up, and getting the reflection identity's branch bookkeeping right
across both is the real difficulty — not the convergence. Budget accordingly.

## Upstream criteria (before offering to Mathlib)

- no QOU imports;
- `Real.dilog` + `Complex.dilog` naming, not `cLiTwo` (rename on the way out);
- docstrings in Mathlib style;
- the reflection + inversion identities, which are what make it useful to
  anyone else.

## Refs

- `QOU/MathlibExt/ComplexDilogarithm.lean` (this bean's landed brick)
- `QOU/Archimedean/DilogReflection.lean` (the real exemplar to continue from)
- `QOU/QBeta/FiveTwoSaddleSumRule.lean` (the consumer; `hrefl` is what brick 3 discharges)
- beans `qou-ph1k` (the complex-Li₂ gap), `qou-0yqu` (the sum-rule proof)
