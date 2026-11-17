---
# qou-gkco
title: 'Add the missing Mathlib: complex dilogarithm (continuation + reflection + inversion), upstreamable'
status: in-progress
pr: 8233
updated_at: 2026-11-17T06:46:41Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-06T22:48:21Z
updated_at: 2026-10-04T15:16:17Z
parent: qou-r9ih
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

## STATUS CHANGE 2026-08-06 — no longer blocks the 5₂ sum rule

This bean was scoped as *the* blocker for `qou-0yqu` (the 5₂ saddle sum rule):
the reflection identity was needed at `y₁` with `|y₁| = 1.52 > 1`, hence a
complex `Li₂` and analytic continuation past the unit disc.

**Route 5 in `qou-0yqu` removes that dependency.** The sum rule restates as

    −∫₀¹ log(1 − 2z + 3z² − z³)/z dz
        = −½·log²(y₃) + (2/3)·(θ−π)² − π²/6,
      θ = arccos((2−y₃)√y₃/2)

with **no dilogarithm and no complex numbers**. The series `Σ pₙ/n²` diverges
(that was the whole reason continuation looked mandatory), but the *integral*
runs where the integrand is regular — now Lean-proved:
`QOU.QBeta.FiveTwo.recipCubic_pos`, from `recipCubic_eq`
(`1−2z+3z²−z³ = (1−z)³+z`). So the sum-rule route needs only
`intervalIntegral`, `Real.log`, `Real.arccos`.

**Re-scoped, not closed.** This bean stays open on its own merits:

* a complex `Li₂` is still wanted for the *general* saddle machinery (any
  `Vⱼ` at a non-real root, other knots), independent of 5₂;
* `QOU.MathlibExt.cLiTwo` exists and is sorry-free on the disc, so the work is
  started and the upstreaming goal is live;
* the Clausen precedent and the two traps recorded above still apply.

What changed is only its **priority and its dependents**: it is no longer on
the critical path to `qou-0yqu`. Anyone picking it up for the sum rule's sake
should read Route 5 first.

## 2026-08-07 — state, and the concrete next brick

### Landed so far (all sorry-free, lean-direct exit 0)

* `QOU/MathlibExt/ComplexDilogarithm.lean` — `cLiTwo` by its power series;
  `cLiTwo_zero`, `cLiTwo_term_norm_le`, `cLiTwo_summable` (converges on the
  open unit disc). Mathlib-only, so it stays upstreamable.
* `QOU/Archimedean/ComplexDilogBridge.lean` — `cLiTwo_ofReal` (unconditional
  bridge to the real `QOU.QPochhammer.LiTwo`) and `cLiTwo_reflection_ofReal`
  (the Euler reflection identity **on the real segment `(0,1)`**, in ℂ).
* `QOU/QBeta/BlochFiveTerm.lean` — the five-term relation's algebraic halves
  (Lyness period-5; `Σ (zᵢ)∧(1−zᵢ) = 0`) and `three_smul_wedge_eq_zero`.

`cLiTwo_reflection_ofReal` is the *input* to an identity-theorem continuation:
it establishes the reflection identity on a set with an accumulation point.
What is missing is analyticity, so the identity theorem cannot yet be applied.

### THE NEXT BRICK — `cLiTwo` is analytic on the open unit disc

Mathlib has the right tool, found 2026-08-07:
**`FormalMultilinearSeries.ofScalars`** (`Mathlib/Analysis/Analytic/OfScalars.lean`),
with `ofScalarsSum_eq_tsum : ofScalarsSum c = fun x => ∑' n, c n • x ^ n` and
the radius lemmas `ofScalars_radius_eq_inv_of_tendsto` /
`ofScalars_radius_eq_of_tendsto`.

Route:

1. Reindex. `ofScalars` sums `cₙ·xⁿ`; `cLiTwo` is written `z^(k+1)/(k+1)²`.
   Take `c n = if n = 0 then 0 else (n:ℂ)⁻¹^2` and prove
   `cLiTwo = ofScalarsSum c`. **Do not redefine `cLiTwo`** — `cLiTwo_ofReal`
   and the bridge depend on the current indexing; prove the equality instead.
2. Radius `= 1`, from `|c_{n+1}/c_n| → 1`.
3. Conclude `AnalyticOnNhd ℂ cLiTwo (Metric.ball 0 1)`.

Then the identity theorem
(`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`) applies with
`cLiTwo_reflection_ofReal` as the frequently-equal hypothesis, giving the
complex reflection identity **on the disc**. Extending past `|z| = 1` still
needs the inversion formula and is a separate step.

### Literature status — none needed for this bean

The constructions here (power series, radius of convergence, identity theorem,
inversion formula) are standard textbook material and Mathlib has the tools.
The literature search was needed for the *sum-rule identity* (`qou-0yqu`), not
for building `Li₂`. Do not spend search effort here.

### Reminder on priority

Route 5 of `qou-0yqu` took this bean **off the critical path** for the 5₂ sum
rule. It is worth doing for the general saddle machinery and for upstreaming,
not because the sum rule is waiting on it.

## 2026-08-07 (b) — steps 1–2 LANDED; step 3 attempted and backed out

**Landed, sorry-free** (`ComplexDilogarithm.lean`):

* step 1 — `cLiTwoCoeff`, `cLiTwoCoeff_summable`, `cLiTwo_eq_tsum_coeff`
  (reindex to Mathlib's `∑ cₙzⁿ` convention without redefining `cLiTwo`);
* step 2 — `cLiTwoCoeff_norm_le_one`, `cLiTwo_radius_ge_one`. Note the shortcut:
  `le_radius_of_bound` at `r = 1` needs only `‖cₙ‖ ≤ 1`, so **no ratio test** —
  four lines instead of a filter argument. Ignore the
  `ofScalars_radius_eq_inv_of_tendsto` route suggested in the earlier entry.

New imports required: `Mathlib.Analysis.Analytic.OfScalars` **and**
`Mathlib.Analysis.Analytic.Basic` (the former does not pull in the latter).

**Step 3: LANDED 2026-08-07 (b, later same day).** The two blockers below were
both wrong-file / wrong-notation, not mathematical — resolved by grepping
instead of guessing. Kept here as the record of what they were:

1. **`HasFPowerSeriesOnBall.analyticOnNhd` does not exist** in this Mathlib.
   `HasFPowerSeriesOnBall.analyticAt` *does* (`Analytic/Basic.lean:135`), so
   `AnalyticAt ℂ cLiTwo 0` is reachable immediately; `AnalyticOnNhd` over the
   whole ball needs a different route — look in `Analytic/Within.lean` or
   `Constructions.lean`, or go via `AnalyticOnNhd` of the series sum.
2. **Extracting `‖z‖ < 1` from `z ∈ EMetric.ball 0 1`** blew the recursion
   limit with `simpa [edist_eq_enorm_sub, ← ofReal_norm_eq_enorm]`. Needs the
   right `enorm`/`ENNReal` coercion lemma; do not guess — grep for
   `mem_emetric_ball_zero_iff` / `edist_zero_right` first.

The skeleton that *did* elaborate:

```lean
theorem cLiTwo_hasFPowerSeriesOnBall :
    HasFPowerSeriesOnBall cLiTwo (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff) 0 1 := by
  have hrad : 0 < (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).radius :=
    lt_of_lt_of_le (by norm_num) cLiTwo_radius_ge_one
  refine (((FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).hasFPowerSeriesOnBall
    hrad).mono (by norm_num) cLiTwo_radius_ge_one).congr ?_
  intro z hz
  ...   -- blocker 2 here; then `rw [hsum, ← cLiTwo_eq_tsum_coeff hz']`
```

`FormalMultilinearSeries.hasFPowerSeriesOnBall (p) (0 < p.radius)`,
`.mono (0 < r') (r' ≤ r)` and `.congr (EqOn f g ball)` are all confirmed
present with those signatures — the structure is right, only the two coercion
steps are missing. Backed out rather than left broken; the file on `main` is
green at steps 1–2.

## STEP 3 LANDED — `cLiTwo` is analytic on the open unit disc

`cLiTwo_hasFPowerSeriesOnBall`, `cLiTwo_analyticOnNhd` — sorry-free,
lean-direct exit 0, bridge re-verified.

Both earlier blockers were lookup failures, not mathematics:

1. **`HasFPowerSeriesOnBall.analyticOnNhd` does exist** — in
   `Mathlib/Analysis/Analytic/ChangeOrigin.lean:362`, *not* `Basic.lean`, which
   is where I looked. Requires `import Mathlib.Analysis.Analytic.ChangeOrigin`.
2. **`‖z‖ < 1` from `z ∈ EMetric.ball 0 1`**: `mem_emetric_ball_zero_iff`
   (additive form of `Normed/Group/Basic.lean:934`) gives `‖z‖ₑ < 1`, then
   `enorm_lt_coe` (`Basic.lean:88`, `‖x‖ₑ < r ↔ ‖x‖₊ < r`, `r : ℝ≥0`) after
   recasting the `1`, then `exact_mod_cast`.
   **Trap:** write `(1 : ENNReal)`, *not* `(1 : ℝ≥0∞)` — the `ℝ≥0∞` form is
   scoped notation and this file opens only `Complex`, so it fails with a bare
   "expected token" that looks like a Unicode problem and is not one.

Required imports, in full: `Analytic.OfScalars`, `Analytic.Basic`,
`Analytic.ChangeOrigin` (none pulls in the next).

### What this unlocks, and what it does not

`AnalyticOnNhd ℂ cLiTwo (EMetric.ball 0 1)` is the hypothesis the identity
theorem `AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq` needs. With
`cLiTwo_reflection_ofReal` (reflection already proved on the real segment
`(0,1)` — a set with an accumulation point) the **complex reflection identity
on the disc** is now a connect-the-pieces step rather than an open one.

It does **not** reach `y₁` (`|y₁| = 1.52 > 1`). That still needs the inversion
formula `Li₂ z + Li₂(1/z) = −π²/6 − ½log²(−z)` to cross `|z| = 1`. And the
priority caveat stands: Route 5 of `qou-0yqu` took all of this off the critical
path for the 5₂ sum rule.

## 2026-08-07 — step 4 domain: `ball(1/2, 1/2)`, not the unit ball

I had called "connect analyticity to the reflection identity" a
connect-the-pieces step. That was wrong: **the naive unit-ball statement is
ill-posed.**

* For `z ∈ ball(0,1)`, `|1 − z|` reaches 2, so `cLiTwo (1 − z)` is *not*
  given by its power series there.
* `Complex.log z` has its branch cut running straight through `ball(0,1)`.

The natural domain is `Metric.ball (1/2 : ℂ) (1/2)` — the disc on `[0,1]` as
diameter. Three lemmas (landed, `lean-direct exit 0`, commit `1030d7daa2`,
PR #4658) are exactly the three facts that make the reflection statement
well-posed there:

| lemma | why it is needed |
|---|---|
| `norm_lt_one_of_mem_ball_half` | ball ⊆ unit disc ⇒ both `cLiTwo z`, `cLiTwo (1−z)` are their series |
| `one_sub_mem_ball_half` | `z ↦ 1−z` is reflection through the ball's centre ⇒ the reflected argument stays in range |
| `re_pos_of_mem_ball_half` | `Re z > 0` on the ball ⇒ `log z`, `log (1−z)` both off the branch cut |

Numerically pre-checked with 200 000 random samples in the ball: 0 violations.

The real segment `(0,1)` lies in this ball, so it is an accumulation set —
that is the route from the *real* `QOU.Archimedean.LiTwo_reflection'` to the
complex statement, via
`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`.

**Next:** state the reflection identity on `ball(1/2,1/2)` and discharge it by
the identity theorem. Blockers to expect: assembling `AnalyticOnNhd` for the
composite `z ↦ cLiTwo z + cLiTwo (1−z) + log z * log (1−z)` (the `log` factors
need `Complex.analyticAt_log` off the cut), and supplying `IsPreconnected` for
the ball.

## 2026-08-07 — CONTINUATION STEP CLOSED; the gap moved

**`QOU.Archimedean.cLiTwo_reflection` is proved**, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`:

    Li₂ z + Li₂ (1 − z) = π²/6 − log z · log (1 − z)    for z ∈ ball(½, ½)

by `AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`, with the accumulation
supplied by the real segment `(0,1)` through `cLiTwo_reflection_ofReal` — itself
a transport of the sorry-free real `LiTwo_reflection'`.

The only genuinely fiddly piece was `tendsto_ofReal_nhdsNE_half`: the identity
theorem wants accumulation in the **punctured** neighbourhood of `½` in ℂ, so
`ℝ → ℂ` has to carry `𝓝[≠]` to `𝓝[≠]` — continuity gives the `𝓝` half,
injectivity of `ofReal` the puncture.

**This does not reach `y₁`.** `|y₁| = 1.52` and `ball(½,½) ⊂ ball(0,1)`. The
next brick would be the inversion formula
`Li₂ z + Li₂ (1/z) = −π²/6 − ½ log(−z)²`, which is what crosses `|z| = 1` — and
it is **not** provable for `cLiTwo` as currently defined, because outside the
closed disc the `tsum` is junk-valued `0`. Crossing `|z| = 1` requires
redefining `Li₂` by its integral `−∫₀¹ log(1−tz)/t dt` on `ℂ ∖ [1,∞)` and
proving it agrees with the series on the disc.

### Route 5 may make that unnecessary — see `qou-0yqu`

The real integral route does not need the continuation at all for the **sum**:
`∏ⱼ(1 − yⱼz) = 1 − 2z + 3z² − z³` is a *real polynomial, positive on `[0,1]`*,
so `Σⱼ Li₂(yⱼ)` collapses to one real convergent integral. Three bricks of that
landed the same day (`intervalIntegrable_log_recipCubic_div`,
`LiTwo_eq_integral_unit`). Weigh that against the ℂ∖[1,∞) integral definition
before picking the next step here.

## Progress Update (PR #8233)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8233` at `0df1f54777395f7641371a1bd56d61fa352927af`).
- **Lean Formalization**: `QOU.QBeta.DilogCuspCancellationAndBorelProperTimeBrick.complex_dilog_reflection_and_inversion_compatibility` (Compatibility of Euler's dilogarithm reflection and inversion functional equations and self-inverse evaluation L(-1) = -pi^2/12.)
- **80-dps Witness**: `computations/probes/dilog-cusp-cancellation-and-borel-proper-time-brick.witness.json` (`scriptHash: 3bb3c88effd9`, `scriptCommitSha: 162d2914798b1189f0082f4e029eb8fed83ca8ee`).
