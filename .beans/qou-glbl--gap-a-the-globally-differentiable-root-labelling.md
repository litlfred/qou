---
# qou-glbl
title: 'Gap A: continuity, non-degeneracy and 4/6 of VSide PROVED — what remains is the concrete labelling'
status: todo
type: task
priority: high
tags:
    - lean
    - 5two
    - qou-trns
    - envelope
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-08-09T00:40:00Z
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
| `VSide` — 4 of its 6 fields | ✅ `vSide_of_notCut_mul_div` (2026-08-08, below) |
| **concrete `Y₁ Y₂ Y₃` + `VSide`'s last two fields + the two `log(−y)` routes** | **open** |

What is left is building the concrete labelling and discharging the remaining
per-root side conditions. That is bookkeeping over proved parts — which this
lane's record says is *exactly* where unexamined regions hide, so it should not
be called trivial in advance.

### 2026-08-08 — `VSide` measured first, then 4 of 6 fields proved

`VSide` is the hypothesis that was once **vacuous** (correction 6 on #4701), so
it was measured before any Lean was written for it. **Route 36**
(`qbeta_5two_route36_vside_nonvacuity_probe.py`, 6 gates, all pass):

* **G1 non-vacuity** — all six conditions hold *simultaneously* at all 597 checks
  (199 arc points × 3 roots). The correction-6 version scores 199 failures under
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

**Still open in `VSide`:** `x·y ∈ notCut` and `y/x ∈ notCut`. G3 measured both —
carried by `Im ≠ 0` at all 597 checks with `min |Im| = 0.00676`, a genuine margin,
so neither needs a case split. `exists_pinning_data` already gives `(x·y₃).im < 0`
and `(x·y₂).im < 0` once `c < 0`; the gap is `y₂` when `c ≥ 0`, plus the real
root, where `Im(x·t) = t·sin φ > 0` should be cheap.

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
