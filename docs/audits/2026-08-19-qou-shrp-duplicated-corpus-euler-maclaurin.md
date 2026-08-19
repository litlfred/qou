# qou-shrp duplicated a composite Euler–Maclaurin rule the corpus already had

**Date**: 2026-08-19 · **Bean**: `qou-shrp` · **PR**: #5297 (merged) ·
**Verdict**: two of the three files in #5297 are substantially redundant. The
mathematics in them is correct and sorry-free; the *claim that they closed an
infrastructure gap* was wrong, and I did not run the corpus-grep that would
have caught it.

## What I claimed

Across the bean, `docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md`
§RE-CORRECTION, the #5297 PR body, and three Lean file headers:

> Mathlib has no Euler–Maclaurin formula, so this is a genuine infra gap.

## What is actually true

**Mathlib** has no Euler–Maclaurin formula — that half is correct and remains
correct. **This corpus does**, and had since **2026-08-08 22:33 UTC**, eleven days
before my step-2 commit (`4331bc97a`, 2026-08-19 12:31 UTC):

| Corpus file (pre-existing) | What it provides |
|---|---|
| [`QOU/MathlibExt/CompositeEulerMaclaurin.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/CompositeEulerMaclaurin.lean) | `abs_integral_sub_composite_le_osc` — the **composite** rule: trapezoid + the `B₂` term `h²/12·(g′(b) − g′(a))`, with an `O(h²)·osc(g″)` error |
| [`QOU/MathlibExt/TrapezoidRule.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/TrapezoidRule.lean) | the trapezoid rule it is built from |
| [`QOU/Knot/LogSincNearZero.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/LogSincNearZero.lean) | `abs_sum_logSinc_sub_euler_maclaurin` — that rule **already applied to `logSinc`**, plus `hasDerivAt_logSinc`, `hasDerivAt_logSinc_deriv`, `antitoneOn_logSinc_deriv` |

And `logSinc` is my `φ`:

    logSinc x = log(sin x) − log x          (KashaevEndpointSplit.lean)
    phi     x = log(2 sin x) − log x  =  log 2 + logSinc x

so `phiDeriv = logSinc′` **identically**, not merely up to a constant.

## Per-file assessment

| File from #5297 | Status |
|---|---|
| `LogSineSharpConstant.lean` — `phi_smooth_defect_sharp` | **Subsumed.** See below: the corpus result is one full order stronger on the same quantity. `hasDerivAt_phi'` / `hasDerivAt_phiDeriv` / `phiDeriv_antitoneOn` duplicate `hasDerivAt_logSinc` / `hasDerivAt_logSinc_deriv` / `antitoneOn_logSinc_deriv` outright. |
| `EulerMaclaurinFirst.lean` — first-order bracket | **Largely redundant for this application**, but not strictly: it needs only `f′` antitone, where the composite rule needs a continuous `g″`. As weaker-hypothesis, Mathlib-style material it can stand; it should not have been built as a *gap closure*. |
| `SincDeriv.lean` — `Real.sinc` differentiability | **Stands.** Genuinely absent from Mathlib *and* from this corpus — `LogSincNearZero` deliberately avoids `Real.sinc` by starting the grid at `h`. Upstreamable as claimed. |

## Why "subsumed" and not merely "overlapping"

Normalise both to the same quantity (divide mine through by `h`, and use
`smooth_defect_eq_riemann_defect` to rewrite the cell-defect sum as
`h·Σφ(x_{i+1}) − ∫φ`). Writing `g = logSinc`, `a = h`, `b = nh`:

* **Mine** bounds the `O(h)` term:

      | Σ g(x_{i+1}) − (1/h)∫_a^b g − ½(g(b) − g(a)) |  ≤  (h/2)·(g′(a) − g′(b))

* **The corpus** *identifies* it and bounds the remainder one order down:

      Σ … − … − ½(g(b) − g(a))  =  (h/12)·(g′(b) − g′(a))  +  O(h²)

`(h/12)` versus a bound of `(h/2)` — my bound is **exactly 6× loose and
non-identifying**.

**My own probe measured that 6 and I misread it.**
`computations/logsine_sharp_constant_check.py` reports `bound/residual` =
**6.0008, 5.9988, 6.0007, 6.0010** at `N = 200…1600`. I described that in the
commit message as the inequality holding "with headroom". A ratio that is
constant to four digits across a decade of `h` is not headroom — it is the
true coefficient sitting in plain view, `1/2 ÷ 1/12 = 6`. The evidence that
the sharp constant was already available was inside my own verification run.

## Root cause

`AGENTS.md` §"Before declaring 'open' math / questions / gaps" requires the
corpus-grep checklist before any "open"/"gap" declaration in a durable
artifact. An infra-gap declaration is exactly that, and I ran only the
*Mathlib* inventory. `grep -rln "EulerMaclaurin\|Euler-Maclaurin" content/`
returns `CompositeEulerMaclaurin.lean` immediately. One grep, nine days stale,
never run.

Note this is **not** the sanctioned parallel-exploration case: the corpus work
was not in flight, it was **landed on `main`** before I started, and the
question was not open-outcome research but settled infrastructure with one
right answer. The "measured research-overlap is PERMITTED" relaxation does not
cover it.

## The sharpest form of the failure: I ran a duplication check and passed it

#5297's body carries a "State-of-main check" section, written after rebasing
onto `main`, which states:

> No E–M or `sinc` work landed from anyone else and the epic's other bricks are
> untouched — no duplication.

`CompositeEulerMaclaurin.lean` was **in my working tree** when I wrote that
(`git cat-file -e 4331bc97a^:…/CompositeEulerMaclaurin.lean` succeeds). So this
was not a case of missing information: the duplication check was performed,
reported, and wrong. What it actually checked was the *commit log since my
fork point* — new landings — rather than the *state of the tree*. A file that
had been sitting on `main` for eleven days is invisible to that check by
construction, which is precisely why the corpus-grep checklist is a grep over
`content/` and not a scan of recent commits.

## Relation to the calibration note in #5297

#5297's body records that my difficulty estimates on this front run high when
the target is a *bound* rather than a *limit*. That note stands, but it was
the smaller of the two problems and it framed the misses as estimation noise.
The larger one is procedural: **I declared a gap without grepping the corpus**,
and the estimate-calibration story is not an explanation for it.

## Actions

1. Headers corrected in `EulerMaclaurinFirst.lean`, `LogSineSharpConstant.lean`,
   `LogSineRiemannForm.lean`, and the §RE-CORRECTION of
   `2026-08-11-l41-euler-maclaurin-feasibility.md`, so no later agent inherits
   the false gap claim.
2. `qou-shrp` updated; the smooth half of L4-1 should be assembled from
   `abs_sum_logSinc_sub_euler_maclaurin`, not from `phi_smooth_defect_sharp`.
3. Nothing is deleted. The proofs are correct and the weaker-hypothesis
   first-order bracket may still be wanted; per the repo's standing rule,
   findings get re-scoped, not silently removed.

---

# Addendum: the wider overlap audit (2026-08-19)

Having found one nine-day-old overlap, assuming it was the only one would have
been the same mistake again. So I audited the rest of the L4 / Whitehead epic
against the `qou-mlgp` lane before writing any more of it.

## The lane

`main` carries an **18-file `Kashaev*` lane** in `QOU/Knot/` — `…Argmax`,
`…Asymptotic`, `…AsymptoticBounds`, `…BeyondWindow`, `…CSigma`,
`…EndpointSplit`, `…FullSum`, `…LogAsymptotic`, `…PeakValue`, `…ProdEndpoint`,
`…RatioExpansion`, `…ReflectionTrapezoid`, `…SaddleWindow`, `…TailBound`,
`…WindowAssembly`, `…WindowIndex`, `…WindowSum`, plus `LogSincNearZero` — over
generic infra in `QOU/MathlibExt/`.

## The distinction that matters, and that I got wrong once already

**Target: different. Machinery: the same.**

* **Different target.** `kashaevProd` is defined in `FigureEightVolume.lean` —
  the whole lane is **4₁**. Van der Veen's Lemma 4 is the **Whitehead link**'s
  Fresnel non-cancellation. `VdVWhiteheadLemma4` has **no instance anywhere in
  the corpus**, so the epic's target is genuinely still open. The epic is not
  redundant.
* **Same machinery.** The generic pieces my remaining bricks planned to build
  already exist, in `MathlibExt`, stated generically:

  | Remaining brick | Already in the corpus |
  |---|---|
  | `qou-vy77` — L4-2 Gaussian window | `GaussianWindowSum` (`sum_Icc_tilted_eq`, `abs_sum_Icc_tilted_sub_le`), `GaussianTailBound` (`tsum_gaussian_sub_sum_Icc_le`), `GaussianSumBound` (`sum_exp_neg_mul_sq_le`, `integral_exp_neg_mul_sq_le`), `GaussianTiltedSum`, `GaussianThetaBound`, `GaussianShearIntegral` |
  | anything needing a quadrature rule | `CompositeEulerMaclaurin`, `CorrectedTrapezoid` (9 theorems, incl. `abs_corrected_trapezoid_sub_integral_le_osc`), `TrapezoidRule` |

  These live in `MathlibExt` — the corpus's *generic* namespace — so they are
  not 4₁-specific and apply to the Whitehead Gaussian directly.

This is exactly the shape of the E–M miss, one level less severe. There, the
lane had not merely built shared machinery but had **already applied it to my
exact function** (`logSinc = φ − log 2`), which is why that case is subsumption
rather than overlap.

## Consequence for the epic

`qou-u1b5`'s remaining bricks are **re-scoped from "build" to "assemble"**:

* `qou-vy77` (L4-2) — assemble from the six generic `Gaussian*` files. Do not
  write a Gaussian tail or window-sum bound.
* `qou-kc8h` (L4-3), `qou-epy2` (L4-5), `qou-9r2q` (L4-6 erfc) — grep
  `MathlibExt/` and the `Kashaev*` lane **first**; `GaussianShearIntegral`
  already mentions `erfc`.

**Standing rule for this epic from here on:** before any new brick, run
`grep -rln "<topic>" content/quantum-observable-universe/lean/QOU/MathlibExt/
content/quantum-observable-universe/lean/QOU/Knot/`. The corpus-grep checklist
is not optional, and "I checked what landed since my fork point" is not it.

## What is NOT claimed here

That the epic is redundant — it is not; `VdVWhiteheadLemma4` is open and no
instance exists. That the Kashaev lane proves anything about the Whitehead
link — it does not; it is 4₁. Sharing machinery is not sharing a theorem, and
conflating the two is the failure mode `AGENTS.md` §"Grep the claim SHAPE"
describes.
