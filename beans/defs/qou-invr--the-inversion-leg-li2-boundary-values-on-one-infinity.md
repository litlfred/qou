---
# qou-invr
title: 'CLOSED: the inversion leg for w₁ = 2.24698 — extend ≡ Re L is proved in all three regimes'
status: completed
type: task
priority: high
tags:
    - lean
    - dilogarithm
    - qou-rstq
    - 5two
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-09-26T11:03:16Z
---

## ✅ CLOSED 2026-08-08 — and so is `qou-rstq` item 4

    extend_eq_re_cRogersL (hx0 : x ≠ 0) (hx1 : x ≠ 1) :
      extend (π²/6) rogersL x = Re (cLiTwoExt x + log x · log(1−x) / 2)

All three regimes, hence **all six arguments** `extended_sum` uses. Sorry-free,
`lake`-verified, axioms `[propext, Classical.choice, Quot.sound]`, non-vacuity
checked at one argument from each regime including `w₁ = 2.24698`.

The chain that closed the inversion regime, in the order it had to be built:

1. **`intervalIntegrable_clog_one_sub_div_ofReal`** — the integrand is
   integrable at `x > 1`. Without it `cLiTwoExt x` there is the junk value `0`.
2. **`continuousAt_liTwoKernel_ofReal`** — the kernel is continuous on the cut
   along the real ray. `slitPlane` was sufficient, not necessary.
3. **`hasDerivAt_cLiTwoExt_ofReal`** — `d/dx cLiTwoExt(x) = −log(1−x)/x`
   **on the cut**, by taking the ray direction to be `1` once the endpoint cap
   was removed.
4. **`cLiTwoExt_one = π²/6`** — the branch point, reachable because `cLiTwoExt`
   along the reals is a *primitive* and primitives of integrable functions are
   continuous. Both existing boundary lemmas exclude `1` exactly.
5. **`re_inversion_identity`** — `Re Li₂(x) + Li₂(1/x) + ½log²x = π²/3`.
6. **`extend_eq_re_cRogersL_of_one_lt`** — log bookkeeping onto `extend`.

### Three predictions this bean made that were wrong

Recorded because the pattern matters more than the result:

* **"needs a genuine boundary value"** — false. Route 35: `Re L` is continuous
  across the cut, nothing to take a limit of.
* **"`notCut` is used only for integrability"** — false. Three uses; two were
  *sufficient conditions* that survive on the real ray.
* **"the s-derivative vs x-derivative conversion is circular"** — false. An
  artefact of the `t ≤ 1` cap, which came from integrability being known only
  on `[0,1]`.

Each was stated as a blocker and each dissolved on contact. **"Recorded
blocker" should be read as "not yet priced", not "hard"** — and separately, an
elaboration timeout (63 s, twice) turned out to be a stray `rw [one_div]`, not
mathematics.

## The original framing (superseded, kept for the record)

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

### ✅ Step (1) CRUX LANDED — 2026-08-08, later the same day

**Superseding the "NOT landed" note that stood here.** It named the affine
composition of `intervalIntegrable_log'` as the blocker. That blocker was
avoidable and no longer exists.

`QOU/MathlibExt/ComplexDilogarithmOnCut.lean`, six theorems, sorry-free,
`lake`-verified, axioms `[propext, Classical.choice, Quot.sound]`:

```
intervalIntegrable_clog_one_sub_mul (x a b : ℝ) :
  IntervalIntegrable (fun t => Complex.log (1 - x*t)) volume a b
```

on **any** interval — logarithmic singularity at `t = 1/x` and branch jump
included. Non-vacuity checked at `x = 2`, where the singularity is strictly
inside `[0,1]`.

Two things priced as hard were not:

* **The branch jump is not an obstacle.** `arg (1 − x·t)` for real arguments is
  an explicit **two-valued step function** (`0`, then `π`) — bounded and
  measurable, integrable for free.
* **Integrating `log` through its own singularity is already in Mathlib**, twice:
  `intervalIntegrable_log'` unconditionally, and
  `intervalIntegrable_log_norm_meromorphicOn`, which is what this uses. `1 − x·t`
  is affine ⟹ analytic ⟹ meromorphic.

**That second lemma also dissolved the recorded blocker**: it takes the affine
map as its *hypothesis* rather than requiring it to be composed in afterwards,
so the composition never has to happen. The lesson is narrow but repeatable —
*when a composition fights you, look for the lemma that takes the inner function
as a hypothesis.*

### ✅ STEP (1) IS COMPLETE — 2026-08-08

    intervalIntegrable_clog_one_sub_div_ofReal {x : ℝ} (hx : 0 < x) :
      IntervalIntegrable (fun t => log (1 − x·t) / t) volume 0 1

Sorry-free, `lake`-verified, axioms `[propext, Classical.choice, Quot.sound]`.
**Verified at `x = 2.24698` — at `w₁` itself**, the one argument this bean is
about.

Both singularities are handled: the **logarithmic** one at `t = 1/x` (in range
exactly when `x > 1`, the whole difficulty) and the **removable** one at
`t = 0`. The second was not reproved — the `[0,c]` piece *rescales to the
existing* `intervalIntegrable_log_one_sub_div_of_slitPlane`, so the removable
singularity is handled by the proof that already existed.

**Consequence, and the reason step (1) mattered at all:** `cLiTwoExt x` for
`x > 1` is now a **provably real object** in Lean. Before this, it was an
`∫` with no integrability proof — hence the junk value `0` — so every statement
about it was vacuously true and useless.

### ⚠ A false alarm worth recording

The `[0,c]` rescaling first appeared to be a *mathematical* obstruction: it
timed out at 63 s even with a 10× heartbeat budget, twice. The cause was neither
the analysis nor `comp_mul_left`'s `finiteness` side conditions — it was a stray
`rw [one_div]` in the goal that the hypothesis did not carry, forcing `exact` to
unify `(2x)⁻¹` against `1/(2x)` under a pile of casts. Deleting that one rewrite
made it instant.

**An elaboration timeout is not evidence that a step is hard.** Given this
lane's record of mispricing steps in both directions, that is worth stating as
flatly as the mathematical findings.

### What remains: step (2) ONLY

    Re Li₂(x) + Li₂(1/x) = π²/3 − ½·log²x        for real x > 1

Route 35 G3, measured at 1e-25 over 200 points. Its partner argument `1/x` lies
in `(0,1)`, where the series converges and `cLiTwo_ofReal` bridges.

#### The route, derived 2026-08-08 — a constancy argument, and where its one subtlety is

Set `G(x) := Re cLiTwoExt(x) + LiTwo(1/x) + ½·log²x` on `(1,∞)`. Then `G' = 0`
and `G ≡ π²/3`, pinned at `x → 1⁺` where `Re Li₂(1) = LiTwo(1) = π²/6` and
`log 1 = 0`. Term by term:

| term | derivative on `x > 1` |
|---|---|
| `Re cLiTwoExt(x)` | `−log(x−1)/x` |
| `LiTwo(1/x)` | `(log(x−1) − log x)/x` |
| `½·log²x` | `log x / x` |

They cancel identically. The middle and last are routine — `1/x ∈ (0,1)` is off
the cut. **The first is the whole problem**, because `cLiTwoExt` is not
complex-differentiable on the cut.

**`hasDerivAt_cLiTwoExt_radial` is the right tool. CHECKED 2026-08-08 — and the
answer is more interesting than expected.**

I had guessed `hy : y ∈ notCut` was used only for integrability. **Wrong.**
Reading the proof, it is used in **three** places:

| use | what it gives | survives for real `x > 1`? |
|---|---|---|
| `hint` | kernel integrable on `[0,t]` | **yes** — step (1) supplies it |
| `hcont` | kernel `ContinuousAt t`, via `1 − y·t ∈ slitPlane` | **hypothesis fails** |
| `hmeas` / `htU` | measurability near `t`, same `slitPlane` preimage | **hypothesis fails** |

So my recorded guess was wrong and the swap-one-lemma plan does not work as
stated. But the two failures are **failures of a sufficient condition, not of
the conclusion**, and that distinction is the whole finding:

> For real `x > 1` and real `u`, `1 − x·u` stays on the **real axis**. It leaves
> `slitPlane` once `u > 1/x`, but it never *crosses* the cut — it sits on one
> side of it. So `log(1 − x·u) = log|1 − x·u| + iπ` there, and that is
> **continuous in `u`** for every `u ≠ 1/x`, even though `slitPlane` (and hence
> `continuousAt_liTwoKernel`) does not apply.

This is **exactly** the phenomenon already isolated in the transport lane as
`hasDerivAt_log_neg_ofReal`: `log(−t) = log t + iπ` is smooth *along a real path*
though the complex derivative does not exist. Third appearance of the same
structure; the first two were corrections 5 and 6 on #4701.

**Revised first action.** Not "swap the integrability lemma", but: prove a
real-argument continuity lemma for the kernel —

    ContinuousAt (liTwoKernel (x : ℂ)) u,  for real x > 0 and real u with
    u ≠ 0 and 1 − x·u ≠ 0

using `arg_one_sub_mul_ofReal` (already proved, in `ComplexDilogarithmOnCut`):
the `arg` term is the step function `if 1 − x·u < 0 then π else 0`, which is
**locally constant away from `u = 1/x`**, so the whole kernel is continuous
there. Then `hcont` and `hmeas` both follow, and with step (1) for `hint` the
radial lemma generalizes to real `x > 0` at every `t ≠ 1/x`.

Note the generalized lemma must **exclude `t = 1/x`**, where the kernel genuinely
blows up — the original's `slitPlane` hypothesis excluded it implicitly, and a
generalization that silently admits it would be false.

Granting the generalisation, the radial lemma at `t = 1` gives

    HasDerivAt (fun s : ℝ => cLiTwoExt (s·x)) (−log(1 − x)) 1

and since `s ↦ cLiTwoExt(s·x)` is `G ∘ (·*x)`, the chain rule reads
`x·G'(x) = −log(1−x)`, i.e. `G'(x) = −log(1−x)/x` — the derivative wanted, with
`Re(−log(1−x)/x) = −log(x−1)/x` for `x > 1` by `re_log_ofReal`.

**⚠ THE ONE SUBTLETY, stated so it is not discovered late.** That reading uses
the chain rule *backwards*: the radial lemma differentiates in the **parameter
`s` along a fixed ray**, and the constancy argument needs the derivative in
**`x`, which moves the ray**. Recovering an `x`-derivative from an `s`-derivative
requires knowing `cLiTwoExt` is differentiable at `x` to begin with — which is
the thing being established. Options, unpriced:

* reparameterise so the ray direction is fixed at `y = 1` and the parameter *is*
  `x` — but `y = 1` fails `notCut` for a second reason and the lemma also caps
  `t ≤ 1`, so it needs extending on two axes;
* prove the `x`-derivative directly from the integral by differentiation under
  the integral sign — **note the derivative integrand `1/(1−xt)` has a SIMPLE
  POLE at `t = 1/x` and is not integrable there**, so naive DUI fails and this
  needs a principal value. Do not start here without pricing that;
* differentiate only the **real part** along the real axis, which is what the
  argument actually needs and which Route 35 G1 shows is continuous across the
  cut. Probably the most promising, and untried.

So step (2) is a constancy argument whose three derivatives are known and cancel
on paper; the open question is purely *how to differentiate `Re cLiTwoExt` in
`x` at a point on the cut*, and the three candidate answers above are unpriced.

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
