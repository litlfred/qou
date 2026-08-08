---
# qou-invr
title: 'THE sharpest open item: the inversion leg for w₁ = 2.24698 — NOT a boundary-value problem (A2 settled it)'
status: todo
type: task
priority: high
tags:
    - lean
    - dilogarithm
    - qou-rstq
    - 5two
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-08-08T18:05:00Z
---

## What is open, stated as narrowly as it now can be

`qou-rstq` item 4 asks that the corpus's **piecewise** `extend` be identified
with `Re` of the **analytic** Rogers `L`. As of 2026-08-08 that is proved for
**five of the six arguments** `extended_sum` uses:

| arguments | regime | status |
|---|---|---|
| two in `[0,1]` | identity | done — `extend` is `f`, `cLiTwo_ofReal` bridges |
| three negative | Landen | done — `extend_eq_re_cRogersL_of_neg` (PR #4701) |
| **`w₁ = 2.24698`** | **inversion** | **OPEN — this bean** |

So the whole of what remains is **one argument, in one regime**. Everything
else in the level-7 chain is proved around it.

## ⚠ SUPERSEDED SECTION — kept because the reasoning was wrong in an instructive way

> **The paragraph below is refuted by A2 (Route 35), recorded further down.** It
> is kept rather than deleted because it is a clean example of this lane's
> commonest error: reasoning about the object (`Li₂`, discontinuous across the
> cut) instead of the quantity actually needed (`Re L`, which is *continuous*
> across it). The conclusion "what is needed is a boundary value" was false, and
> nothing measured it for a full round.

The Landen leg closed because `x < 0` is *off* `cLiTwoExt`'s cut, so a
vanishing derivative plus one base point sufficed — and the base point could be
taken at the limit `z → 0⁻`, needing no special value at all.

`x > 1` lies **on** the cut. `notCut = {w | w.im ≠ 0 ∨ w.re < 1}` excludes real
`x ≥ 1` precisely because `cLiTwoExt` has a genuine discontinuity across
`[1,∞)`. ~~There is no constant of integration to pin: the object itself is not
defined at the point in question. What is needed is a boundary value — the
limit from one side, which exists and is what `Re L` means there.~~ **False —
see A2 below. The real part is continuous across the cut, so there is no limit
to take.**

`ComplexDilogarithmBoundary` deliberately stops short of this: it reaches the
closed unit ball *off* the cut, and its docstring says so. Route 34 G5 checks
adversarially that the Landen theorem does **not** silently cover `t = 2.24698`
(the combination is visibly nonzero there). A proof appearing to reach it is
wrong.

## ✅ A2 IS SETTLED — 2026-08-08, Route 35. The problem changed shape.

A2 asked whether `Re Li₂` is continuous across the cut even though `Li₂` is not.
**It is**, and cleanly:

* `Li₂`'s jump across `[1,∞)` is **exactly `2πi·log x`** — purely imaginary.
  Measured `Re` jump: **zero**. Measured `Im` jump: nonzero and matching the
  prediction, which is what makes the zero meaningful rather than a null result.
* The same holds for the **full Rogers `L`**, which is what is actually needed.
  Both its terms jump — `Li₂`, and `log x·log(1−x)/2` because `log(1−x)` crosses
  log's own cut — and **both jumps are purely imaginary**. Checking `Li₂` alone
  would not have settled it.

So there is no boundary value to obtain: **there is nothing to take a limit of.**

### What the leg reduces to

    Re Li₂(x) + Li₂(1/x) = π²/3 − ½·log²x        for real x > 1

A **real** identity, verified at 1e-25 over 200 points, in which the partner
argument `1/x` lies safely in `(0,1)` — where the series converges and
`cLiTwo_ofReal` already bridges. No cut, no boundary theory, no new analytic
infrastructure. This is a different and much smaller problem than the one
originally recorded below.

### A measured detail that corrects a guess

Lean's own definition `cLiTwoExt y = −∫₀¹ log(1−yt)/t dt` at real `x > 1` lands
on **`Li₂(x − i0)`**, the *lower* boundary value. I predicted the upper one from
`arg(negative real) = +π` and **was wrong**. It does not affect the conclusion —
the real part agrees with both sides — but branch signs are exactly what this
lane has repeatedly got wrong, so the corrected guess is in the record.

### What still remains — item 4 is NOT closed

Two things, both smaller than a boundary-value theory, neither free:

1. **Integrability at `x > 1`.** `intervalIntegrable_log_one_sub_div_of_notCut`
   assumes `notCut`, which **fails** here. So `cLiTwoExt` at `x > 1` is
   currently a Lean `integral` with no proof its integrand is integrable — and
   an unproved-integrable integral is the **junk value 0**. The singularity at
   `t = 1/x` is logarithmic, hence integrable, but that needs proving. *This is
   now the main obstacle and it is an integrability lemma, not a branch theory.*
2. **The real identity of G3**, above.

**Next action: prove (1).** It is a self-contained Mathlib-flavoured lemma and
it unblocks everything else here. The vectors below are superseded except where
noted.

## Attack vectors (A1 and A3 are now SUPERSEDED by A2's result)

Ordered by my estimate of tractability. None has been attempted.

### A1 — ~~Boundary value as a one-sided limit~~ SUPERSEDED: no limit is needed
Define `Li₂` on `[1,∞)` as `lim_{ε→0⁺} cLiTwoExt(x + iε)` and prove the limit
exists by showing `cLiTwoExt` extends continuously from the upper half plane to
the closed upper half plane near `(1,∞)`. Mathlib has no such
"continuous extension to the boundary" API for this shape, but the integral
definition `∫₀¹ −log(1−yt)/t dt` may make it direct: for `y = x + iε` with
`x > 1`, the integrand's singularity at `t = 1/x ∈ (0,1)` is *logarithmic*, hence
integrable, and dominated convergence should give the limit with an explicit
`iπ` jump. **This is the route I would try first** — it works with the definition
the corpus actually has, rather than importing new machinery.

### A2 — Only the REAL PART is needed, which may dodge the branch entirely
The identification is about `Re L`, not `L`. Across the cut the discontinuity of
`Li₂` is `2πi·log x`, which is **purely imaginary** for real `x > 1`. So
`Re Li₂` may be *continuous* across `[1,∞)` even though `Li₂` is not — in which
case the boundary value is not needed at all, only continuity of a real
function. **Check this numerically before doing any Lean**: if `Re cLiTwoExt`
extends continuously across `(1,∞)` from both sides to the same value, A2
collapses the problem to a real-analysis statement and A1 becomes unnecessary.
This is the cheapest thing on the list and it might be the whole answer.

### A3 — Inversion via the reflection formula — PARTLY SURVIVES as the source of G3's identity
`Li₂(x) + Li₂(1/x) = −π²/6 − ½·log(−x)²` is the inversion formula. For `x > 1`
the partner `1/x ∈ (0,1)` is **safely inside the disc**, where the series
converges and `cLiTwo_ofReal` already bridges. If the identity can be proved by
the same zero-derivative technique on a path that stays off the cut — e.g. in
the upper half plane, then taking real parts — the cut is never crossed. The
obstruction is that the natural path from a base point to `x > 1` must cross
`[1,∞)` or go around it; going around means a connectedness argument in
`ℂ ∖ [1,∞)`, for which `isPathConnected_notCut` **already exists** in
`ComplexDilogarithmDeriv.lean`. Worth pricing.

### A4 — Sidestep: re-derive `extended_sum` so `w₁` never appears
The six arguments come from the level-7 orbit `{1/(1−x), x, (x−1)/x}` and its
negatives. `w₁ = 1/(1−x) = 2.24698` is the only one above 1. If the cyclotomic
identity can be restated using a different representative of the same orbit —
the orbit is a `ℤ/3` action, and `extend`'s own functional equations relate
members — the inversion regime might be avoidable entirely. **Caution: this is
the kind of move that produces a correct theorem about the wrong quantity.**
Any reformulation must be checked to still be the identity `extended_sum`
proves, at the six original arguments, numerically, before any Lean.

## Do this first (ORIGINAL, now done)

**A2, as a probe.** — DONE, Route 35. It is ~20 lines of mpmath and it decides whether A1/A3 are
needed at all. Sample `Re cLiTwoExt(x ± iε)` for `x ∈ (1, 5)` across `ε → 0`
from both sides and check the two limits agree. If they do, say so with the
measured convergence rate; if they do not, that kills A2 outright and the
number by which they differ tells you which of A1/A3 is cheaper.

Standing discipline applies: `mpf("...")` constants, `int(nint(x))` not
`round(float(x))`, run `scripts/probe-float64-guard.py --diff`, and check the
identity at points **off** the configuration it will be used on.

## Refs

* `qou-rstq` item 4 (parent), `qou-trns`, `qou-0yqu`
* Proved around it: `QOU/MathlibExt/ComplexDilogarithmLanden.lean`,
  `QOU/QBeta/FiveTwoExtendIdentification.lean`,
  `QOU/MathlibExt/ComplexDilogarithmBoundary.lean` (which stops short, by design)
* Probes: Route 33 (per-regime gap), Route 34 (Landen closed; G5 adversarial on
  exactly this argument)
* PRs #4776 (analytic layer), #4701 (the lane)

**The 5₂ sum rule remains verified to 80 dps, unproved.**
