---
# qou-glbl
title: 'Gap A: VSide CLOSED, routing settled, t(c) DIFFERENTIABLE (phi=0 exception removed); what remains is composing Y1 Y2 Y3'
status: todo
type: task
priority: high
tags:
    - lean
    - 5two
    - qou-trns
    - envelope
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-08-09T07:30:00Z
---

## What is open

`hasDerivAt_envelopeS` (`S′ = 2φ`) and `envelopeS_total` (`S(π) − S(0) = π²`)
are proved in `QOU/QBeta/FiveTwoTransport.lean`, but they take the root
labelling `Y₁, Y₂, Y₃ : ℝ → ℂ` as **given, differentiable functions**. Supplying
that labelling is the single remaining hypothesis in the transport chain —
every other input in the table is proved.

## Why it is narrow, and much narrower than it was

Three measurements have shrunk it:

1. **`S` is symmetric in the roots**, so as a function of `φ` it needs no
   labelling to be *defined* — only to be *differentiated term by term*, which
   is local. `envelope_integrate` already tolerates one exceptional point.
2. **Route 32 G8: the real root never collides.** `|∂p/∂y|` at the positive real
   root never drops below **1.75** on the arc. Only the *other two* roots
   collide, and only at `φ₀ = 137.9206708879635°`.
3. **The symmetric functions of the colliding pair are smooth.** With `t` the
   real root, `y₂ + y₃ = 2c − t` and `y₂y₃ = 1/t` — both differentiable wherever
   `t` is, with no exceptional point.

So the obstruction is confined to **splitting one quadratic with smooth
coefficients**, at one point where its discriminant vanishes.

## 2026-08-08 — AUDITED. B1-vs-B2 was a FALSE CHOICE; the glue is already proved.

The bean said "decide between B1 and B2 by inspection". Inspected. The decision
does not arise, because **`envelopeS_total` already has the exceptional-point
form**:

```
envelopeS_total (hcont : ContinuousOn (envelopeS Y₁ Y₂ Y₃) (Icc 0 π))
                (hderiv : ∀ φ ∈ Ico 0 π, φ ≠ c → HasDerivAt (envelopeS …) (2φ) φ) :
  envelopeS Y₁ Y₂ Y₃ π = envelopeS Y₁ Y₂ Y₃ 0 + π²
```

One exceptional point `c` is already tolerated. So B2's machinery is **built**,
and Gap A is not "construct a global labelling" — it is two smaller things:

* **(a)** a *locally* differentiable labelling on `[0,π] ∖ {φ₀}` — the scalar
  IFT (`QOU.MathlibExt.ImplicitScalar`, proved) supplies this, with
  non-degeneracy from `|∂p/∂y| ≥ 1.75` at the real root (Route 32 G8);
* **(b)** a *continuous* labelling on all of `[0,π]`, including `φ₀`.

**(b) is much easier than what this bean feared**, and the reason is worth
stating: at `φ₀` the two colliding roots converge *to the same value*. So any
labelling has both branches tending to a common limit — **continuity survives
exactly what differentiability does not.** The bean's title ("globally
differentiable") named the wrong requirement.

### ✅ (b) IS PROVED — `continuous_otherRoots`, 2026-08-08

    continuous_otherRoots : Continuous (fun p : ℝ × ℝ => otherRoots p.1 p.2)

`QOU/QBeta/FiveTwoRootStructure.lean`, sorry-free, `lake`-verified, axioms
`[propext, Classical.choice, Quot.sound]`. Checked at an actual collision
(`γ = β²/4`), where the two roots genuinely coincide.

`otherRoots` is piecewise on the sign of `β² − 4γ` — and that sign change **is**
the collision. It is continuous anyway, because at `β² − 4γ = 0` **both branches
give `(−β/2, −β/2)`**: `Real.sqrt 0 = 0` on one side, and the imaginary part
vanishes on the other. `Continuous.if_le` is exactly the right shape, and its
boundary obligation is precisely that agreement.

So the *labelling of the colliding pair* is continuous through the collision,
while not being differentiable there. **That asymmetry is what makes Gap A
tractable**, and it is now a theorem rather than an argument.

### ✅ (a)'s NON-DEGENERACY IS PROVED — and Route 32 G8's `1.75` is exactly `7/4`

    unitCubic_deriv_ge (ht0 : 0 < t) (ht1 : t < 1) (hp : unitCubic c t = 0) :
      7/4 ≤ 3t² − 4ct + (2c+1)

    unitCubic_deriv_ne_zero : … → 3t² − 4ct + (2c+1) ≠ 0

`exists_hasDerivAt_root` needs exactly `curveDy ≠ 0`. On `|x| = 1` the curve is
`x · unitCubic c`, so `curveDy = x·(3t² − 4ct + 2c+1)` and — `x ≠ 0` — the
non-degeneracy is a statement about the **real cubic alone**.

Two exact facts prove it, with `c` eliminated by the root relation:

* `(3t² − 4ct + 2c+1)·t(1−t) = −t⁴ + 2t³ + t² − 2t + 1` — a **`c`-free quartic**;
* that quartic satisfies `q(t) − 7/16 = (2t−1)²(9 + 4t − 4t²)/16 ≥ 0` on `(0,1)`,
  and `t(1−t) ≤ 1/4`.

Dividing gives `∂p/∂y ≥ (7/16)/(1/4) = 7/4`.

**The bound is TIGHT, not a lossy estimate.** At `c = 3/4` the root `t = 1/2`
gives `∂p/∂y = 7/4` exactly — verified in Lean — and `c = 3/4 = cos φ` is on the
arc. So Route 32 G8's measured minimum of `1.75` is *attained*, and the measured
and proved values agree exactly rather than approximately.

### ✅ `heⱼ` — the envelope condition — is DISCHARGED, and Route 30's leak with it

    exists_int_dVdy_mul (hx : x ≠ 0) (hy : y ≠ 0) … (hc : curve x y = 0) :
      ∃ k : ℤ, dVdy x y * y = −(k · 2πi)

    re_dVdy_mul_eq_zero_of_real … (hc : curve x (t : ℂ) = 0) :
      (dVdy x t · t').re = 0

**The general statement is cleaner than either special case.** Route 30 G2
refuted "the envelope hypothesis is free on the curve": `∂V/∂y = 0` at two roots
but `2πi/t` at the positive real one, because `−t` sits on `log`'s cut. Behind
both is one fact — on the curve the **exponentiated** saddle holds exactly, so
the logarithmic one holds *up to* `2πi`, hence

    ∂V/∂y · y ∈ 2πi·ℤ

at **every** point of the curve. `k = 0` recovers the two easy roots; `k = ∓1`
is the real root's leak. **Nothing has to be known in advance about which root
is which** — which is the point, since that classification is exactly what the
labelling problem makes awkward.

The second theorem then discharges `heⱼ` at the real root: `dVdy·y ∈ 2πi·ℤ`
makes `dVdy` purely imaginary when `y` is real, and a real `Y'` leaves nothing
in the real part. Route 30's correction, proved rather than assumed.

### What remains: assembly only

| piece | status |
|---|---|
| continuity through the collision | ✅ `continuous_otherRoots` |
| IFT non-degeneracy off the collision | ✅ `unitCubic_deriv_ne_zero` (tight at 7/4) |
| local differentiable labelling | ✅ `exists_hasDerivAt_root` (pre-existing) |
| the envelope condition `heⱼ` | ✅ `re_dVdy_mul_eq_zero_of_real` / `exists_int_dVdy_mul` |
| the log-sum conditions `hA`, `hB` | ✅ `logSumA_eq_log`, `logSumB_eq_neg_log` (pre-existing) |
| one-exceptional-point glue | ✅ `envelopeS_total` (pre-existing) |
| **`VSide`, all six fields, every root on the OPEN arc** | ✅ `vSide_of_root` |
| ⚠ `VSide` at `φ = π` | **FALSE — Route 36 G7, below. Prove over `Ico`, never `Icc`.** |
| the `log(−y)` **routing** — which root takes which route | ✅ `log_neg_route` |
| the labelling's *shape* + route 2's path condition | ✅ forced, Route 36 G9 |
| `t(c)` single-valued and differentiable | ✅ `eq_realRoot'`, `hasDerivAt_realRoot` |
| `Y₁` (real branch), `Y₂ Y₃` continuous through the collision | ✅ `Yreal`, `continuous_Ypair` |
| `Y₂ Y₃` **differentiable** off the collision | ✅ `hasDerivAt_Ypair_fst/snd` |
| all three branches are **curve** roots | ✅ `curve_Yreal`, `curve_Ypair` |
| `VSide` + the `log(−y)` derivatives at the CONCRETE branches | ✅ `FiveTwoEnvelopeInstance.lean` |
| **`heⱼ` for the pair, `hA`/`hB` concretely, `hcont` at `φ = π`** | **open** |

What is left is building the concrete labelling and discharging the remaining
per-root side conditions. That is bookkeeping over proved parts — which this
lane's record says is *exactly* where unexamined regions hide, so it should not
be called trivial in advance.

### 2026-08-08 — `VSide` measured first, then 4 of 6 fields proved

`VSide` is the hypothesis that was once **vacuous** (correction 6 on #4701), so
it was measured before any Lean was written for it. **Route 36**
(`qbeta_5two_route36_vside_nonvacuity_probe.py`, **12 gates**, all pass — G3 is a
**retraction** and G7 a recorded *refutation*, both below):

* **G1 non-vacuity** — all six conditions hold *simultaneously* at all 597 checks
  (199 **interior** arc points × 3 roots; the endpoints are not sampled — G7). The correction-6 version scores 199 failures under
  the same gate, so the gate is falsifiable rather than decorative.
* **G2 a trap** — `polyroots` returns `|Im| ~ 2.6e-41` for the real root at **one**
  arc point, so a naive `Im ≠ 0` disjunct test misattributes it. It bites 1 time
  in 597: rare enough that a spot check sees a clean split and concludes the
  naive test is fine. Classified by root type instead.
* **G5, unanticipated** — there are **291** real roots over 199 arc points, not
  199. On `|x| = 1` the cubic has real coefficients, the arc crosses the
  discriminant (`16c⁴−48c³+28c²+12c−31`, unique root in `[−1,1]` at
  `c* = −0.74221766588`), and at **46** of the points *all three* roots are real.
  Two consequences: `continuous_otherRoots`' collision branch is **live**, not
  defensive; and the real branch of `y ∈ notCut` must cover three roots there.
* **G6** — the arc's real roots climb to `2cos(π/7) − 1`, the largest level-7
  root, as `φ → π`. The transport's endpoint **is** the level-7 configuration
  `sum_re_deformedV_at_neg_one` evaluates, not merely near it.

Proved on the back of that (`FiveTwoRootStructure`, `FiveTwoTransport`, both
`lake`-verified per module, sorry-free, axioms `[propext, Classical.choice,
Quot.sound]`):

* `unitCubic_shift` / `unitCubic_pos_of_one_le` / `unitCubic_root_lt_one` —
  expanding about `t = 1` gives `1 + (4−2c)s + (3−2c)s² + s³`, **all coefficients
  positive for `c ≤ 1`**, so no real root reaches 1. This bounds *every* real
  root, which G5 says is required: `exists_pinning_data`'s distinguished
  `t ∈ (0,1)` would leave two of three unhandled at those 46 points.
* `root_mem_notCut` — the real/complex case split, discharged.
* `root_ne_zero`, `mul_root_ne_zero`, `div_root_ne_zero`, and
  `vSide_of_notCut_mul_div`, which reduces `VSide` to exactly its two
  root-dependent fields — the residue is now in a **signature**, not in prose.

⚠ **`|x| = 1` in `root_mem_notCut` is load-bearing, and G6 proves it exactly.**
The curve is quadratic in `x`, so fixing a bad `y` and solving gives a
counterexample outright: at `y = 2`, `2x² − 9x + 2 = 0` gives `x = (9±√65)/4`,
both real, neither on the unit circle, with `y = 2 ∉ notCut`. Drop the hypothesis
and the theorem is false. Recorded in the docstring so it is not later "simplified".

### ⚠⚠ 2026-08-08 — `VSide` is **FALSE at `φ = π`**. Route 36 G7.

Found while attacking the last two fields, by measuring instead of assuming. It
is the single most important thing in this bean.

At the endpoint `x = −1` the three roots are the **level-7 roots** and are all
real, so for each of them `Im(x·y) = y·sin φ` — and every imaginary part vanishes
*simultaneously*. Two roots are still carried by `Re < 1`. The third,
`y = −2.2469796`, gives `x·y = +2.2469796`: real, `Re ≥ 1`, sitting exactly on
Li₂'s cut. **`VSide.hc₂` and `hc₃` are false there.**

So: **prove `VSide` over `Ico 0 π`, never `Icc 0 π`.** Any attempt at the closed
interval is an attempt at something false.

Three things this exposes, each worth keeping:

1. **G1 structurally could not see it.** It samples `φ = π(i+1)/(N+1)` — the
   *open* interval. "Holds at all 597 checks" would have been read as covering a
   point it never tested. The sampling was right by luck, not by design.
2. **A naive evaluation reports the endpoint as FINE.** `exp(iπ)` returns
   `−1 + 4.1e-43i`, and that spurious imaginary part satisfies `notCut`'s first
   disjunct. This is **the same trap G2 documents, in a second place** — and the
   first time it would have produced a false *pass* rather than a wrong reason.
   `x` must be built exactly as `mpc(-1, 0)`.
3. **The transport is unaffected, and the reason is structural, not lucky.**
   `envelopeS_total` asks for `ContinuousOn … (Icc 0 π)` but `HasDerivAt` only on
   `Ico 0 π`. The endpoint needs a **value**, not differentiability — and
   `sum_re_deformedV_at_neg_one` (`qou-asem`) already supplies that value at
   `x = −1` with no differentiability hypothesis in it. The two results meet
   exactly where this one has to stop.

Recorded in the `VSide` docstring so it cannot be re-attempted quietly.

### ✅✅ `VSide` IS CLOSED on the open arc — all six fields, every root

    vSide_of_root (hx : |x| = 1) (hxim : x.im ≠ 0) (hc : curve x y = 0) : VSide x y

No root structure, no labelling, no case analysis left to the caller. Sorry-free,
`lake`-verified (2584 jobs), axioms `[propext, Classical.choice, Quot.sound]`.
Supersedes the intermediate `vSide_of_real_root` (real roots only), which is
removed rather than left as clutter.

`hxim` is the open-arc condition and it is load-bearing, not decorative: at
`φ = π` it is exactly what fails, and `VSide` fails with it. The theorem and G7's
refutation are the same fact seen from two sides.

The two hard fields went as follows.

**`hc₂` (`x·y ∈ notCut`) — the disjunction, used as a disjunction.**

    mul_mem_notCut : x*y ∈ notCut

If `Im(x·y) ≠ 0`, done. If `x·y` is real — which G3 shows *does* happen, once, on
`(0,π)` — then:

    quintic_of_mul_real (hx : |x|=1) (hxim : x.im ≠ 0) (hc : curve x y = 0)
      (hxy : x*y = r) : r⁵ − r³ + 1 = 0
    quintic_root_lt_one (h : r⁵ − r³ + 1 = 0) : r < 1

pins the value and puts it below 1. **`quintic_of_mul_real` needs no Vieta and no
root tracking**, which is what made it cheap: substituting `x·y = r` into the
curve (times `x²`) gives a cubic in `x` with *real* coefficients; on `|x| = 1` the
quadratic `x² + 1 = 2·(Re x)·x` is the minimal polynomial of a non-real `x` over
`ℝ`, so that cubic reduces to `α·x + β` with `α, β` real; `x.im ≠ 0` forces both
to vanish; and `r⁵ − r³ + 1 = α + (r² + 2c)·β` identically. Both certificates
were checked at generic `(r, c, x)` **off** the locus before any Lean was written.

`unitCircle_quadratic` was extracted from inside `curve_eq_unitCubic` for this,
and `curve_eq_unitCubic` now uses it — one line instead of a repeated `nlinarith`.

**`hc₃` (`y/x ∈ notCut`) — free, via an involution nobody had noticed.**

    curve_inv (hx0 : x ≠ 0) (y : ℂ) : curve x⁻¹ y * x² = curve x y

`x ↦ x⁻¹` maps the curve to itself, so `y/x` is just `x·y` read at `x⁻¹` — which
on `|x| = 1` differs only by the sign of `Im x`. `hc₃` needs no argument of its
own, and this also **explains** G3's observation that the two crossings sit at the
same `φ` with the same value: they are the same crossing.

### ✅ The `log(−y)` routing is settled — `log_neg_route`

    log_neg_route (hx0 : x ≠ 0) (hc : curve x y = 0) :
      −y ∈ slitPlane ∨ (0 < y.re ∧ y.im = 0)

`−y ∈ slitPlane` unfolds to `Re y < 0 ∨ Im y ≠ 0`, so it fails **precisely** at a
positive real `y`. Route 36 **G8** measures that neither route is droppable:
exactly **one** root per arc point is positive real (199 of 597 — route 2), and
the other 398 take route 1, either as a genuine complex pair (153 points) or, past
the discriminant flip, as *negative* reals (46 points). Dropping route 2 would
repeat correction 6 in a new place — a statement carrying only `slitPlane` is
vacuous at that root.

⚠ **This settles the routing, not the derivative.** Route 2's lemma is stated for
a path `fun u => ((t u : ℝ) : ℂ)` — it needs `Yⱼ` **real-valued near `φ`**, not
merely real *at* `φ`. That is a condition on the labelling rather than on the
root, so it folds into the concrete `Y₁ Y₂ Y₃` and is now the *only* thing the
`log(−y)` hypotheses still want.

### ✅ The concrete labelling is FORCED — every piece is already a theorem

Route 36 **G9**. The construction is not a design choice; it is the only one that
works, and it discharges G8's residue instead of inheriting it:

    Y₁ φ = ((t (cos φ) : ℝ) : ℂ)        t(c) = the unique root of `unitCubic c` in (0,1)
    (Y₂ φ, Y₃ φ) = otherRoots (t − 2c) (t² − 2ct + 2c + 1)

Four facts make it well defined, and **all four are already proved**:

| need | supplied by |
|---|---|
| `t` exists | `exists_root_mem_Ioo` |
| `t` is **single-valued** | `real_root_neg_of_ne` — the other real roots are negative |
| `t` is differentiable in `c` | `ImplicitScalar` + `unitCubic_deriv_ne_zero` (`∂p/∂y ≥ 7/4`) |
| `(Y₂,Y₃)` continuous through the collision | `continuous_otherRoots` |

Measured on 399 arc points: the `(0,1)` root is unique at every one, `t` ranges over
**`[0.4301680, 0.8019354]`** — bounded away from both ends, so
`unitCubic_deriv_ge`'s `0 < t < 1` holds with margin — and `|dt/dφ| ≲ 0.233`. The
endpoints cross-check against G6 independently: `t → 0.4301597` at `φ = 0` (the
real root at `x = +1`) and `t → 0.8019377 = 2cos(π/7) − 1` at `φ = π`, the largest
level-7 root.

**And it closes G8's residue.** G8 noted that route 2's lemma is stated for a path
`fun u => ((t u : ℝ) : ℂ)`, so it needs `Y` real-valued *near* `φ`, not merely real
*at* `φ` — a condition on the labelling rather than the root. `Y₁` above is
real-valued **by construction**, which is exactly that shape. Better: G9 measures
that the `(0,1)` root *is* the unique **positive real** root, i.e. precisely the one
`log_neg_route` sends to route 2. The two fit without adjustment.

**Still open:** the Lean assembly — defining `t(c)` from the existence and
uniqueness theorems and differentiating it through `ImplicitScalar`. The pieces
are proved; what is missing is putting them together, and this lane's record says
that is exactly where unexamined regions hide.

### ✅ `realRoot` is a differentiable function of `c` — `FiveTwoRootLabelling.lean`

    realRoot (c : ℝ) : ℝ                       the root of `unitCubic c` in (0,1)
    eq_realRoot'  (hc : c < 3/2) (h0 : 0 < r) (hp : unitCubic c r = 0) : r = realRoot c
    hasDerivAt_realRoot (hc : c < 3/2) :
      HasDerivAt realRoot (−(−2t² + 2t) / (3t² − 4ct + 2c + 1)) c

The derivative was checked against a numerical derivative at seven values of `c`
spanning the arc, agreeing to **5.7e-42**, *before* any Lean was written. At
`c = 3/4` it is exactly `−2/7` — the point where `unitCubic_deriv_ge`'s bound
`7/4` is attained, so the two results meet on the nose.

**`eq_realRoot` came out stronger than drafted.** It was written with `r < 1` and
Lean flagged that hypothesis as unused — correctly: `real_root_neg_of_ne` makes
every root other than `realRoot c` negative, so *any positive* root equals it, no
upper bound needed. That is Route 36 G8's "exactly one positive real root per arc
point", in the form a proof can use.

### ⚠→✅ The `φ = 0` endpoint: a real obstruction, then removed

A first version carried `hc : c < 1`, excluding `c = 1` — which is `φ = 0`, an
endpoint of the transport. That would have cost an **exceptional point**, and
`envelopeS_total` tolerates exactly one, already spent on the collision at
`φ₀ = 137.9206708879635°`. Two exceptions would have meant **Gap A does not close
by assembling what is already proved** — the opposite of what this bean's
remaining-work line implied. It was recorded as such before being attacked.

It is removed, and the fix is algebra rather than analysis. Uniqueness has a
**second, independent proof** near `c = 1`: `∂p/∂t = 3t² − 4ct + (2c+1)` has
discriminant-in-`t` equal to `16c² − 24c − 12`, negative on
`c ∈ (−0.3956…, 1.8956…)`. So on `[1/2, 3/2]` the cubic is strictly *increasing*,
hence injective, hence has at most one real root anywhere — `strictMono_unitCubic`,
with no root structure at all.

| regime | covers | via |
|---|---|---|
| `real_root_neg_of_ne` | `c ≤ 1` | the other real roots are negative |
| `strictMono_unitCubic` | `[1/2, 3/2]` | positive derivative ⟹ injective |

They overlap on `[1/2, 1]`, so together they give uniqueness for every `c < 3/2`
— the entire arc range `[−1,1]` *plus* a two-sided neighbourhood of the endpoint.
`c = 1` is interior; `φ = 0` needs no exception; `envelopeS_total`'s one exception
stays available for `φ₀`, which is what it was for.

⚠ `unitCubic_deriv_pos` is **not** `unitCubic_deriv_ge`. The latter bounds the
derivative *at a root in `(0,1)`*; the former has no root hypothesis and no
constraint on `t`, which is exactly what monotonicity needs. Conflating them
would give a strictly weaker statement that does not prove injectivity.

**Still open:** composing `realRoot` with `cos` to get `Y₁`, building `(Y₂, Y₃)`
from `otherRoots`, and feeding the three into `hasDerivAt_envelopeS`.

### ⚠⚠ G3 RETRACTED — `x·y` **does** become real, and the crossing is exact

The original G3 claimed `x·y` and `y/x` are **never** real on the arc, so their
`notCut` membership "needs no case split at all". **False.** The gate passed on a
grid minimum of `|Im(x·y)|` tested against `1e-6` — and a grid minimum is not a
lower bound. Refining the grid shrank it like `1/N` (`0.00587` at N = 399,
`0.00215` at N = 999), which is the signature of a simple **zero crossing**.

There is exactly one on `(0,π)`, found by bisecting the *symmetric*
`∏ⱼ Im(x·yⱼ)` so the search needs no branch tracking. At it `x·y` is real with

    r = −1.2365057033914990243   the unique real root of   r⁵ − r³ + 1 = 0

and `c = r(1+r)/2`, `t = 1/r²` — all three matching to **20 digits**. Vieta gives
it: `x·y₂ = r` real with `|x| = 1` forces `y₂ = r·conj x`, hence `y₃ = r·x`, and
substituting into the curve makes `x` a root of a cubic with **real**
coefficients; `x` is non-real on the open arc, so `conj x` is a root too and the
third is `−r²`. (`x·y₂` and `y₃/x` are the *same* real number there, which is why
both crossings coincide.)

`notCut` still holds — **via `Re < 1`, not via `Im ≠ 0`.** So the proof obligation
is the *opposite* of what the retracted claim said, and the disjunction is
genuinely needed.

✅ The Lean consequence that makes it benign is proved:

    quintic_root_lt_one (h : r⁵ − r³ + 1 = 0) : r < 1

because `r ≥ 1` forces `r⁵ − r³ + 1 = r³(r²−1) + 1 ≥ 1 > 0`.

**Both retractions this session share one shape:** a *negative* claim ("never
real", "holds everywhere") backed by *positive samples on a grid*. Neither can be
established that way. Where Route 36 now asserts a "never" it evaluates an exact
endpoint or bisects a symmetric function — not a denser grid.

**`VSide` is no longer open** — see the section above. `exists_pinning_data`'s
sign facts turned out not to be needed for it at all: the route through the
crossing (`Im ≠ 0` away from `φ*`, `quintic_root_lt_one` at it) is uniform in the
root and needs no per-root labelling, which is what made `hc₂` land in one
theorem instead of a case analysis over `y₂`, `y₃` and `c`'s sign.

⚠ Note also what G3's *other* number meant: `min |Im(x·y)| = 0.00676` at
`φ = 0.0157` belongs to the **real** root (`t·sin φ → 0` as `φ → 0`), not the
pair. That one is harmless — `Re(x·t) = t·cos φ < 1` carries it — but it is the
*same* degeneration that is fatal at `φ = π`, where `Re` does not.

### The original "what remains: (a) only" note, superseded

A locally differentiable labelling on `[0,π] ∖ {φ₀}`, and the real root `t(φ)`
globally. The scalar IFT (`QOU.MathlibExt.ImplicitScalar`, proved) supplies it,
with non-degeneracy from `|∂p/∂y| ≥ 1.75` at the real root (Route 32 G8). Then
`envelopeS_total`'s exceptional-point form closes the transport.

Note the pieces now sit on both sides of `φ₀`: `continuous_otherRoots` handles
the collision, the IFT handles everything else, and `envelopeS_total` glues them
with one point excluded.

## What the hypotheses actually demand — measured, not assumed

Every *algebraic* hypothesis in the envelope chain is **symmetric**:

| hypothesis | form |
|---|---|
| `h₁, h₂, h₃` | the elementary symmetric functions `Σyⱼ`, `Σyᵢyⱼ`, `y₁y₂y₃` |
| `hA`, `hB` | log **sums** over the fiber |

The only per-root demands are `hYⱼ : HasDerivAt Yⱼ Yⱼ' φ` and
`heⱼ : (∂V/∂y · Yⱼ').re = 0`. And `heⱼ` says the derivative is **annihilated** —
so `Yⱼ'` enters the conclusion only through a product that vanishes.

**The hypothesis demands strictly more than the conclusion uses.** That is the
precise statement of Gap A, and it is why the fix is a reformulation rather than
a construction.

## The Lagrangian frame — why this is the native way to see it

Raised in conversation, and it is right. The deformed curve `p(x,y) = 0` is a
**Lagrangian** in `(ℂ*)²` for `ω = dlog x ∧ dlog y`; `V` is its generating
function; and "`∂V/∂y = 0` on the curve" is exactly the statement that `dV`
restricted to the Lagrangian is the tautological one-form. **The envelope
theorem *is* that statement.**

What the frame buys is not a new technique but the right diagnosis: upstairs on
the curve there is no labelling problem at all. `S(φ)` is a **pushforward** — a
sum over the fiber of `C → x`-line — and a fiber sum is insensitive to how the
sheets are named. The branch point is an artefact of projecting down. That is
the same conclusion the hypothesis audit reaches from the other side, which is
the useful part: two independent routes to "work symmetrically".

## Reeb flow — assessed and set aside

Also raised. I do not see a route, and would rather say so than force one:

* The corpus's Reeb material (`QOU/AlgebraicSubstrate/ReebEpsilon.lean`) is the
  Reeb **infinitesimal `ε`** from Conway's surreals — the substrate clock. That
  is a different object from the contact-geometry Reeb vector field.
* Gap A is a branched triple cover of a real interval. There is no contact
  structure in play, and no periodic-orbit question. Reeb flow answers
  "does this contact manifold carry a closed orbit"; Gap A asks "can I name
  three sheets smoothly through a collision".

Recorded so it is not re-derived. If a specific contact structure on the
spectral curve is intended, that would change the assessment — the objection is
to the unspecified version, not to the idea in principle.

## Attack vectors (B1/B2 SUPERSEDED — see the audit above)

### B1 — Split the labelling: `t` globally, the pair symmetrically
Prove `t : ℝ → ℝ` differentiable on all of `[0,π]` directly from the scalar IFT
(`QOU/MathlibExt/ImplicitScalar.lean`, already proved), using `|∂p/∂y| ≥ 1.75`
as the non-degeneracy hypothesis — **no exceptional point at all** for `t`.
Then handle `y₂, y₃` only through `y₂ + y₃` and `y₂y₃`, never individually.
**This is the intended route** and the reason Route 32 measured the 1.75 bound.
The question to settle first: does `Σⱼ ∂V/∂x` and the envelope collapse actually
factor through the symmetric functions, or does some step need `y₂` alone? If
the latter, B1 fails and B2/B3 are needed.

### B2 — Accept the exceptional point and use what already exists
`constant_of_hasDerivWithinAt_zero_off_point`
(`QOU/Archimedean/ConstantOffOnePoint.lean`, proved) is built for exactly this:
continuous everywhere, derivative zero off **one** point. If the labelling can
be made differentiable on `[0,π] ∖ {φ₀}` and `S` shown merely *continuous* at
`φ₀`, the theorem closes with no global labelling at all. Continuity of `S` at
`φ₀` should be easy — `S` is symmetric, and the roots vary continuously through
a collision even though the labelling does not. **This may be strictly easier
than B1** and it reuses a lemma already in the tree.

### B3 — Local IFT on each side, glued
Two applications of the scalar IFT on `[0, φ₀)` and `(φ₀, π]`, then glue. The
gluing is where it gets delicate: `dy/dφ` **diverges** like
`0.65040643/√|φ−φ₀|` (Route 31 G6, `C = 2.6016257` stable over five decades), so
the labelled derivative does not extend. What saves it is that `∂V/∂y = 0`
annihilates the divergent `y′`, leaving the labelled *term's* derivative bounded
at **2.7268867** all the way in. That is the envelope theorem visible
numerically — but turning "the product stays bounded" into a Lean derivative
statement at `φ₀` needs care, and a first draft of Route 31 G6 got the reason
wrong (it claimed the terms *jump*; they do not).

### B4 — Puiseux / square-root parametrisation through the collision
The two colliding roots separate like `C·√|φ−φ₀|`, so `y₂, y₃` are analytic in
`√(φ−φ₀)`, not in `φ`. A labelling in the Puiseux variable would be globally
smooth. **Costly**: Mathlib has no Puiseux-series API for this, and it would be
new infrastructure for one point. Listed for completeness; do not start here.

## Do this first

**Decide between B1 and B2 by inspection, not by proving either.** Read
`FiveTwoEnvelopeSum.lean` and `FiveTwoEnvelopeWiring.lean` and answer one
question: does any proved step need an individual `y₂`, or do they all factor
through `y₂+y₃` and `y₂y₃`? That single answer picks the route and saves
attempting the wrong one.

## ⚠ What this does NOT get you

Closing this proves `S(π) − S(0) = π²`. **That is not the sum rule.**
`S(0) = −3π²/2` *is* the 5₂ sum rule (residual 1e-30) and `S(0) = 3·S(π)`, so
the transport **reformulates** the sum rule rather than approaching it. Anyone
picking this up should know that before starting: it closes a named gap in a
proved chain, it does not move the headline.

## Refs

* `qou-trns` (parent), `qou-0yqu`, `qou-rstq`
* Proved and waiting on this: `QOU/QBeta/FiveTwoTransport.lean`
* Tools already in tree: `QOU/MathlibExt/ImplicitScalar.lean`,
  `QOU/Archimedean/ConstantOffOnePoint.lean`
* Probes: Route 31 (G4 non-vacuity, G6 the bounded-derivative measurement),
  Route 32 (G8 the 1.75 bound)

**The 5₂ sum rule remains verified to 80 dps, unproved.**
