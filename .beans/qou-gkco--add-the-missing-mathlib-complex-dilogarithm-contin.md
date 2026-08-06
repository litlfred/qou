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

## In-repo precedent — DO NOT build the continuation from scratch (2026-08-06)

A survey of the QOU lib for continuation/branch infrastructure turned up a
close working precedent. Use it rather than reinventing.

**`QOU/Knot/Clausen.lean` — sorry-free, and the same shape as this brick.**
The Clausen function is `Im Li₂` on the unit circle, so it is dilog-adjacent,
and the file already walks the exact path this bean needs — complex power
series → local uniform convergence → analyticity → `EqOn` identification:

- `hasSum_pow_div_neg_log {w : ℂ} (hw : ‖w‖ < 1)` — a **complex** `HasSum`
  for `−log`, directly reusable alongside Mathlib's
  `Complex.hasSum_taylorSeries_neg_log`;
- `tendstoLocallyUniformlyOn_tsum_rpow_cos` — local uniform convergence of a
  series family, which is what upgrades a power series to `AnalyticOnNhd`;
- `analyticOnNhd_two_sin_half` — `AnalyticOnNhd` usage precedent;
- `hasDerivAt_Cl_2_series`, `clausen_eqOn_Cl_2` — the identification step, i.e.
  the same `EqOn`-on-a-connected-set argument the reflection continuation needs.

Note `Cl_2` lives in `QOU.Archimedean`, the same namespace as this brick.

**Also available (all sorry-free):** a meromorphic-continuation stack for `Φ_b`
— `QOU/QBeta/PhiBProdUniquenessMeromorphic.lean`,
`PhiBProdFactorAnalytic.lean`, `PhiBProdZeroIsolation.lean`,
`MeromorphicPuncturedBounded.lean`, `MeromorphicSameOrder.lean` — plus
`QOU/Mathlib/ArgumentPrinciple.lean`. Precedent for uniqueness-by-continuation
arguments in this repo.

**Branch cuts:** `QOU/Archimedean/DilogPartBBranchPhase.lean` already proves
`clog_one_sub_of_gt_one` and `clog_one_sub_pole_phase_split` for real `w > 1`
— exactly the `1 − z` branch behaviour past the cut.

## Namespace trap (cost a compile cycle)

`LiTwo` is in **`QOU.QPochhammer`**, not `QOU.Archimedean`, despite living in
`QOU/Archimedean/DilogarithmArchimedeanLimit.lean` — the namespace does not
follow the directory. Its *theory* (`LiTwo_reflection'`, `hasDerivAt_LiTwo`, …,
`DilogReflection.lean`) **is** in `QOU.Archimedean`. Open both.

## Stale cache-branch warning

The `lake-cache/qou-v4-24-0` orphan branch olean for
`DilogarithmArchimedeanLimit` is **stale**: it exports `LiTwo` but **not**
`LiTwo_one` (unknown identifier even fully qualified). A `cLiTwo_one` corollary
was dropped from `ComplexDilogBridge.lean` rather than shipped unverified.
Reseed the cache branch against current `main` before relying on it.

## Follow-on (no separate bean)

Upstreaming `cLiTwo` to Mathlib is premature until the continuation and
reflection land; tracked here rather than as its own bean.
