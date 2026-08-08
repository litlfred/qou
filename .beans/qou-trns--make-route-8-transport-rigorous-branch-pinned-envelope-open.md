---
# qou-trns
title: 'Route 8 transport: branch integer now PINNED by the base point; envelope theorem still open'
status: in-progress
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - analysis
created_at: 2026-08-07T21:15:00Z
updated_at: 2026-08-08T07:05:00Z
parent: 0yqu
---


## Why this bean

After Route 11 (`qou-fivt`) **derived** the three numerators from the five-term
relation, the 5₂ sum rule's only remaining mathematical gap moved to **Route 8's
analytic transport** — and it is analytic, not arithmetic. This bean tracks
closing it.

Two sub-gaps were listed in `qou-8v3k`:

1. the branch integer `k = 0` on `|x| = 1` — **now closed, see below**;
2. the envelope theorem itself — **still open**.

## ✅ Sub-gap 1 CLOSED: `k = 0` is pinned by the base point, not assumed

Previously `k = 0` was argued from *integrality + local constancy on a
collision-free arc*. That shows `k` is **constant**; it does not say **which**
constant. The stronger argument determines it:

Let `g(x) := Σⱼ Log[(1 − yⱼ/x)/(1 − x·yⱼ)]`, continued **continuously** from
`x = 1` along the arc.

1. `exp(g(x)) = ∏ⱼ[(1 − yⱼ/x)/(1 − x·yⱼ)] = (1/x)/x = 1/x²` — exact Vieta, and
   **already Lean-proved** (`prod_one_sub_x_mul`, `prod_x_sub` in
   `QOU/QBeta/FiveTwoCyclotomicBloch.lean`).
2. The three branches `yⱼ(x)` are continuous and never collide on the arc
   (`min |disc| = 0.348`), so `g` is continuous.
3. Hence `g(x) + 2·log x` is continuous and valued in `2πiℤ`, therefore
   **constant**.
4. **At `x = 1` every factor is exactly `(1 − yⱼ)/(1 − yⱼ) = 1`**, so `g(1) = 0`,
   and `log 1 = 0`. The constant is **0**.
5. Therefore `g(x) = −2·log x` on the continuous branch — `k = 0` is *forced*.

**Verified:** 2000 points on `φ ∈ [0, π]` with continuous root tracking and
unwrapped per-root logs; worst `|g(x) + 2iφ| = 1.6e-30`.

Consequence, with `x = e^{iφ}`:

    S(e^{iφ}) − S(1) = Re ∫₀^φ (g/x)·(i·x) dt = ∫₀^φ 2t dt = φ²

so **`S(−1) = S(1) + π²`** — the transport step, now branch-pinned.

## ⚠ Two errors made getting here — recorded so they are not repeated

1. **A probe whose printed conclusion contradicted its own data.** The first
   branch-tracking script hard-coded "no jump" while its own output showed
   `|diff| = 6.2832 = 2π` at `φ = π`. Cause: it summed **principal** `Log`s,
   which wrap, instead of unwrapping them. **Never hard-code a verdict string
   that the run cannot falsify.**
2. **Comparing against the wrong branch.** The corrected run still showed
   `|diff| = 4π`, because it compared continuous `g` against mpmath's
   **principal** `log x`, which jumps at `φ = π` (`exp(1j*π)` lands just below
   the cut, so `arg = −π`). The mathematics was fine; the comparison was not.
   Compare against `log x = iφ`.

## ❌ Sub-gap 2 STILL OPEN: the envelope theorem

`d/dx V(x, yⱼ(x)) = ∂V/∂x` needs:

* `V` differentiable in both arguments along the path — for the complex `Li₂`
  terms this touches `qou-clx8`/`qou-ph1k`;
* `yⱼ(x)` differentiable, which follows from the implicit function theorem given
  non-vanishing discriminant (**have it**: `min |disc| = 0.348` on the arc), but
  is not written down;
* `∂V/∂y = 0` at `yⱼ`, which is the curve — **already Lean-proved algebraically**.

So the residual analytic content is differentiation of the complex dilogarithm
along a path, plus the implicit function theorem. **That is ordinary analysis,
not a research problem** — but it is not done, and it is the last mathematical
gap in the whole chain.

## Status of the full chain

    sum rule
      --Route 8--> cyclotomic identity at Q(zeta_7)+   [transport: branch PINNED,
                                                        envelope OPEN]
      --Route 9--> Re[2L(w_k)+L(-w_k)] = m_k pi^2/42   [algebra Lean-proved]
      --Route 11-> m = (17,5,-1)                       [DERIVED from five-term]

**Sum rule: verified to 80 dps. Numerators derived. Transport branch-pinned.
Envelope theorem open. Still not proved.**

## Refs

* `qou-8v3k` (Route 8), `qou-fivt` (Routes 10–11), `qou-b7cy` (Route 9)
* `QOU/QBeta/FiveTwoCyclotomicBloch.lean` — the Vieta products this argument uses

---

## ✅ 2026-08-07 (later) — the envelope step is CONFIRMED TRUE. The gap is purely formalization.

Before treating the envelope theorem as a formalization task, it was worth
checking it is actually *true*. It is.

**(A) Real `x`, real parts, all three branches.** Finite-difference total
derivative `d/dx Re V(x, yⱼ(x))` (with the branch tracked) against
`Re ∂V/∂x = Re[(1/x)log((1−yⱼ/x)/(1−x·yⱼ))]`, at `x = 0.7, 1.3, 2.0`:
**agreement to `3.4e-24`** across all nine (x, branch) pairs.

**(C) On the arc, the cleanest check — it involves no logarithm at all.**
Finite-difference `d/dφ S(e^{iφ})` against the predicted `2φ` (which is what
`S = S(1) + φ²` asserts), at `φ/π = 0.25, 0.5, 0.75, 0.9`:
**agreement to `1.7e-28` at every point.** This is branch-free — no `Log` is
evaluated — so it confirms the transport independently of any branch convention.

### The third instance of the same trap

Check **(B)** compared `d/dφ S` against `Re[Σⱼ (∂V/∂x)·i·x]` and matched to
`1e-28` at `φ/π = 0.25, 0.5, 0.75` — then differed by exactly `6.2832 = 2π` at
`φ/π = 0.9`. Cause: **principal `Log` inside my evaluation of `∂V/∂x` wraps**;
the mathematics is unaffected, as (C) shows.

That is the **third** time in this bean's history that a principal-vs-continuous
`Log` has produced a spurious `2π`. It is now the single most reliable source of
false alarms in this work. **Any probe here that evaluates `log` of a
root-dependent ratio must use a continued branch, or compare against a
log-free quantity as in (C).**

### Status of the envelope gap

**Mathematically: confirmed.** The step is true, to `1e-24`–`1e-28`, on real `x`
per branch and on the arc.

**Formally: still open**, and now precisely scoped:

* `d/dz Li₂(z) = −log(1−z)/z` for complex `z` along the path — this is the
  *defining* derivative, much weaker than the full continuation `qou-clx8` needs;
* the implicit function theorem for `yⱼ(x)`, whose hypothesis **holds**
  (`min |disc| = 0.348` on the arc);
* `∂V/∂y = 0` at `yⱼ` — **already Lean-proved algebraically**.

So the last mathematical gap in the whole 5₂ chain is **not a mathematical doubt**
— it is ordinary analysis awaiting formalization, and it needs strictly less than
the complex-`Li₂` continuation that has blocked `qou-clx8` all along.

---

## ⚠⚠ 2026-08-08 — REFUTED: `min |disc| = 0.348` IS WRONG. The discriminant VANISHES on the arc.

**Sub-gap 1 is REOPENED.** Probe
`computations/probes/qbeta_5two_route16_discriminant_vanishes_probe.py`,
6 gates, all pass.

### The fact

Two of the three `y`-branches **collide exactly** on the transport arc:

| | |
|---|---|
| `θ₀` | **137.9206708879635°** |
| `x₀` | `−0.74221766588 + 0.67015888896i`, `\|x₀\| = 1` |
| `\|disc(x₀)\|` | `1.1e-49` — zero to 50 dps |
| colliding roots | `y₂ = y₃ = −1.13224188231190019…`, separation `9.4e-26` |

**`min |disc|` on the arc is `0`, not `0.348`.**

### The proof uses no numerics at all

`disc_y` of the GGM curve `x·y³ − (x²+1)y² + (x²+x+1)y − x` is, exactly in `ℤ[x]`,

    disc(x) = x⁸ − 6x⁷ + 11x⁶ − 12x⁵ − 11x⁴ − 12x³ + 11x² − 6x + 1

which is **palindromic**, so `disc(x)/x⁴ = Q(u)` with `u = x + 1/x` and

    Q(u) = u⁴ − 6u³ + 7u² + 6u − 31

A point of `|x| = 1` is a root of `disc` **iff** `u = 2cos θ` is a real root of
`Q` in `[−2,2]`. And, in integers,

    Q(−2) = 16 + 48 + 28 − 12 − 31 = **+49**
    Q(−1) =  1 +  6 +  7 −  6 − 31 = **−23**

IVT gives a root in `(−2,−1) ⊂ [−2,2]`. **That is the whole proof.** Everything
else in the probe is confirmation.

### Where `0.348` came from — and the lesson

The dip is narrow (`|disc'| ≈ 87` there), so an `N`-point scan of `[0,π]` reports
roughly `87·π/(2N)`:

| N | grid minimum |
|---|---|
| 360 | ≈ 0.38 ← **the 0.348 that was recorded** |
| 2 000 | 0.068 |
| 20 000 | 0.0068 |
| → ∞ | **0** |

**A grid minimum was reported as if it were the true minimum.** The zero was
always there; the sampling stepped over it. `qou-rstq` roast item 2 said exactly
this could happen — "measured on a sampled arc; a finer sweep could in principle
find a near-collision". It is not a near-collision.

### What this breaks

1. **Sub-gap 1's step 2** — "the three branches are continuous and never collide
   on the arc, so `g` is continuous". False. The `k = 0` pinning argument rests
   on it, so **`k = 0` is no longer established**. Status reverts to open.
2. **The envelope theorem's IFT hypothesis** — "follows from the implicit
   function theorem given non-vanishing discriminant (**have it**)". We do not
   have it. The IFT does not apply at `x₀`.
3. Anything downstream that inherited `min |disc| = 0.348` as a fact — see
   `qou-8v3k`.

### What it does NOT break

The sum rule. This probe says nothing against it, and `S(−1) = S(1) + π²` is
still numerically solid.

### The likely repair — NOT done, NOT assumed

**`Σⱼ Vⱼ` is a symmetric function of the roots**, and symmetric functions of the
roots of a polynomial remain analytic across a branch point even though the
individual branches do not — only the *labelling* breaks. So the transport
probably survives if it is rewritten to use the symmetric combination
throughout, or if the path is deformed off `|x| = 1` around `x₀`.

Both are plausible and **neither is written**. Until one is, the transport is
open, and the per-root `g(x) = Σⱼ Log[…]` formulation is actively misleading —
it presumes a branch labelling that does not survive the arc.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — the refutation is now a LEAN THEOREM, and the conclusion is SAFE

### Lean

`QOU/QBeta/FiveTwoDiscriminant.lean`, sorry-free, `lake` green:

```lean
theorem exists_unit_circle_disc_zero : ∃ x : ℂ, ‖x‖ = 1 ∧ disc x = 0
```

Ingredients, all small: `disc_eq_cubic_formula` (`ring` — `disc` *is* the standard
cubic discriminant of the GGM curve), `disc_eq_Q` (`field_simp; ring` — the
palindromic reduction `disc x = x⁴·Q(x + 1/x)`), `Q_neg_two`/`Q_neg_one`
(`norm_num` — `49` and `−23`), `exists_root_Q` (IVT), and `onCircle` with
`norm_onCircle`, `onCircle_add_inv` (the `u ↦ x` bridge: `u ∈ [−2,2]` gives
`x = u/2 + i√(1 − u²/4)` on the unit circle with `x + 1/x = u`).

So the refutation is not merely measured — it is **proved**.

### And the conclusion survives — Route 17

`computations/probes/qbeta_5two_route17_symmetric_transport_probe.py`, 5 gates.

**`S(e^{iφ}) − S(1) = φ²` holds to `4e-40` across the whole arc, INCLUDING at the
branch point** — residual `0.0` at `φ₀` and at `φ₀ ± 1e-5`, and `0.0` at the
endpoint `S(−1) − S(1) = π²`. There is no feature there at all.

The reason is structural and was worth finding: **`S(x) = Σⱼ Re V(x, yⱼ)` sums
over all roots, so it is symmetric in them.** A collision *permutes* roots; a
symmetric function cannot notice a permutation. Only the per-root labelling
dies — and only the argument used labels.

### Where that leaves this bean

| | |
|---|---|
| the transport **conclusion** `S(−1) = S(1) + π²` | ✅ not in danger |
| the transport **argument** (`k = 0` via per-root `g`) | ❌ **dead** — it presumes a labelling that does not survive the arc |
| a symmetric replacement | ❌ **not written** |

**Do not repair the `g(x) = Σⱼ Log[…]` formulation.** It is the wrong object.
The right ones are the elementary symmetric functions, which Vieta makes
*rational* in `x` —

    e₁ = (x²+1)/x,  e₂ = (x²+x+1)/x,  e₃ = 1

(Route 17 gate G5) — hence analytic on the whole arc, branch point included. And
their two products are **already Lean-proved**: `prod_one_sub_x_mul`,
`prod_x_sub` in `FiveTwoCyclotomicBloch.lean`.

That is the concrete next step: derive `S′(x) = −2 log x / x` from the symmetric
functions alone, never naming a branch.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — the transport argument is REPAIRED. One analytic step left.

`qbeta_5two_route19_transport_repaired_probe.py`, 5 gates.

### The repair

The dead argument tracked `g(x) = Σⱼ Log[(1 − yⱼ/x)/(1 − x·yⱼ)]` with **per-root
continuous logs** — a branch *labelling*, which is exactly what a collision
destroys. Work instead with the two symmetric Vieta products, **both already
sorry-free in Lean** since #4658:

    ∏ⱼ (1 − x·yⱼ) = x        (`prod_one_sub_x_mul`)
    ∏ⱼ (x − yⱼ)   = x²        (`prod_x_sub`)  ⟹  ∏ⱼ (1 − yⱼ/x) = 1/x

Neither vanishes on `|x| = 1`, so each has an unambiguous continuous log there.
Measured over 4001 points spanning the branch point:

| | |
|---|---|
| max step in `Σⱼ log(1 − x·yⱼ)` | **2.5e-5** (a `2π` jump would be `6.28`) |
| `max \| Σⱼ log(1 − x·yⱼ) − log x \|` | **9.7e-41** |
| same for `Σⱼ log(1 − yⱼ/x)` vs `−log x` | same order |

So the sum of per-root logs **is** the continuous log of the symmetric product,
branch integer **0**, straight through the collision.

### Why — and this is the point the old argument was missing

**At the collision the two colliding roots are `y₂ = y₃` exactly.** So the two
log-terms being permuted are **identical**, and a sum cannot notice a
relabelling of equal terms. The monodromy acts on labels; the sum has none.

With both sums pinned,

    Σⱼ ∂V/∂x = (1/x)·( Σⱼ log(1 − yⱼ/x) − Σⱼ log(1 − x·yⱼ) ) = −2·log(x)/x

and integrating along `x = e^{iφ}` gives `S(e^{iφ}) − S(1) = φ²`, hence
**`S(−1) = S(1) + π²`**.

### What is still missing — now one named step, not a hole

The envelope theorem needs `dyⱼ/dx`, which **does not exist at the branch
point**. The fix is removability:

* off the branch point the discriminant is non-zero, so the IFT applies and the
  envelope argument is valid;
* `S` is continuous at the branch point (Route 17, residual `0.0` there);
* an analytic function on a punctured neighbourhood, continuous at the puncture,
  extends analytically (Riemann).

So `S′(x) = −2 log x / x` holds on the whole arc. **That is ordinary analysis and
it is not written.** It is now the only gap in the transport.

### A measurement note worth keeping

G4 first failed because `φ₀` was a hardcoded 25-digit constant. This is a
**square-root** branch point, so root separation near it grows like `√|Δφ|` — a
25-digit `φ₀` leaves the roots `~1e-12` apart, not `~1e-25`. The constant is now
computed at working precision inside the probe. **A truncated constant is not a
neutral convenience near a square-root singularity**, which is of a piece with
the `0.348` lesson: it was the same failure to state how a number was obtained.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — the last analytic step is now a LEAN LEMMA

`QOU/Archimedean/ConstantOffOnePoint.lean`, sorry-free, `lake` green:

```lean
theorem constant_of_hasDerivWithinAt_zero_off_point {f : ℝ → ℝ} {a b c : ℝ}
    (hcont : ContinuousOn f (Set.Icc a b))
    (hderiv : ∀ x ∈ Set.Ico a b, x ≠ c → HasDerivWithinAt f 0 (Set.Ici x) x) :
    ∀ x ∈ Set.Icc a b, f x = f a
```

**Continuous on `[a,b]`, zero derivative off one point ⟹ constant.** That is
exactly the transport's remaining shape, with no dilogarithm in it: the envelope
argument gives `dS/dφ = 2φ` wherever the IFT applies — everywhere except the one
branch point `FiveTwoDiscriminant.exists_unit_circle_disc_zero` proves exists —
and `S` is continuous throughout (Route 17).

Apply it to `f φ := S(e^{iφ}) − φ²` on `[0,π]` with `c = φ₀`.

**Riemann removability is not needed.** I first framed the fix that way; it is
overkill. This is one-variable real analysis, and the exceptional point costs
nothing.

### Why it needed proving rather than citing

Mathlib's `constant_of_has_deriv_right_zero` wants the right derivative at
**every** point of `Ico a b`. Splitting at `c` works on `[a,c]`, where `Ico a c`
excludes `c` — but fails on `[c,b]`, whose `Ico c b` *contains* `c`. The fix is
to apply it on `[t,b]` for each `t > c` and pass to the limit using continuity.

### ⚠ A process failure, recorded because it nearly shipped

I ran this file with `lean` directly, in the background, read an **empty log**,
and reported "compiled first try". It had not compiled — the `nohup … &` wrapper
returned immediately and my wait loop raced it. `lake build` then found two
**renamed** identifiers (`Ioc_mem_nhdsWithin_Ioi` → `Ioc_mem_nhdsGT`,
`nhdsWithin_Ioi_self_neBot'` → an instance) plus two type mismatches.

Two lessons, both already on this lane's list and both re-learned the hard way:

1. **An empty log is not a pass.** This is the same wrapper-exit trap logged
   earlier in the session for `lake build`.
2. **`lean` direct is more permissive than `lake`.** The lakefile sets
   `autoImplicit = false` and other `leanOptions` that a bare `lean` invocation
   does not. **Every Lean claim in this lane should be `lake`-verified, not
   `lean`-verified.** The other files were, and are fine — but only by habit,
   not by rule.

### Where the transport now stands

| step | status |
|---|---|
| symmetric Vieta products, non-vanishing on the arc | ✅ Lean (`prod_one_sub_x_mul`, `prod_x_sub`) |
| discriminant vanishes at one point of the arc | ✅ Lean (`exists_unit_circle_disc_zero`) |
| `Σⱼ log` continuous through it (colliding terms equal) | ✅ measured (Route 19), **not Lean** |
| envelope `dS/dφ = 2φ` off that point | ❌ **not written** — needs IFT + `d/dz Li₂` |
| constant-off-one-point glue | ✅ **Lean, this file** |
| `S` continuous on `[0,π]` | ✅ measured (Route 17), **not Lean** |

The one genuinely unwritten mathematical step is the **envelope derivative**,
and it now sits between two Lean-proved endpoints.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — the branch integer is now a LEAN THEOREM, and the arc turns out to END ON THE CUT

`QOU/Archimedean/BranchIntegerPinning.lean`, sorry-free, `lake` green (1893
jobs), axioms `[propext, Classical.choice, Quot.sound]`.

```lean
theorem eq_zero_of_continuousOn_of_exp_eq_one {F : ℝ → ℂ} {a b x : ℝ}
    (hx : x ∈ Set.Icc a b) (hcont : ContinuousOn F (Set.Icc a b))
    (hexp : ∀ y ∈ Set.Icc a b, Complex.exp (F y) = 1) (h0 : F a = 0) :
    F x = 0
```

Instantiate at `F φ := Σⱼ Log(1 − e^{iφ}·yⱼ) − iφ` on `[0, π]`. This **replaces**
the sub-gap-1 argument twice over: the original (integrality + local constancy on
a collision-free arc) was refuted with the discriminant; the Route 19 repair
argued the conclusion from a grid. This derives it, in one step, from three
inputs — and two of them are already theorems.

| input | status |
|---|---|
| `exp (F φ) = 1` | Lean-proved — it *is* `prod_one_sub_x_mul` (#4658) |
| `F 0 = 0` | Lean-proved — same Vieta identity at `x = 1` |
| `F` continuous on `[0,π]` | **open**, and now measured directly |

Connectedness plus the base point, together. The old argument needed two steps
because local constancy tells you `k` is *constant* and never which constant.

### The finding: the transport arc ends ON the branch cut, twice over

Route 20 (`qbeta_5two_route20_cut_avoidance_probe.py`, 7 gates, exit 0) measures
the **hypothesis** instead of the conclusion — the point of having the lemma. Its
first version tested the obvious sufficient condition, "no factor meets
`(−∞,0]`", and **failed**: margin `9.3e-43` at `φ/π = 1.0`, unmoved by a `1e4`
refinement. Not a grid artefact, not a tolerance. At `x = −1`,

    1 − x·y₁  =  1 − w₁  =  −1.2469796…

is exactly on the cut, with `w₁` the largest root of `w³ − 2w² − w + 1` — **the
level-7 ladder's own cubic**. And `x = −1` is on the cut as well.

### Why `hcont` survives it, and why that is uncomfortable

Continuity forbids *crossing*, not *touching*. The contact is transversal — the
margin is exactly `w₁·(π − φ)`, ratio → 1 over four orders of magnitude (G3) —
and one-sided: rising to `φ = π` the factor arrives from **above**, `arg → +π`,
which is exactly where the principal branch is defined on the cut. So `F` is
continuous on `[0,π]` and the lemma applies.

Traverse the arc **downward** and the factor arrives from below, `arg → −π`,
while principal `Log` still returns `+π`: a real `2πi` jump (G6 measures both
directions — upward residual `< 0.05`, downward `> 6.0`). **The transport's
orientation is load-bearing, and only because of where the principal branch is
declared to sit.**

### This is the mechanism behind the three spurious `2π`s recorded above

This bean records three separate occasions on which a principal-vs-continuous
`Log` produced a spurious `2π`, and calls it "the single most reliable source of
false alarms in this work". It is not luck. **The arc's endpoint is on the cut**,
in two independent ways, so any principal-branch evaluation there is one
convention away from being off by `2πi`. Naming the cause should stop the fourth
instance.

### Margin elsewhere — the collision is invisible to it

Interior minimum `0.337` at `φ/π = 0.542`; `0.775` at the branch point `φ₀` (G5).
The cut condition and the collision condition are independent — which is exactly
why the symmetric repair survives a collision that killed the per-root argument.

### What is still open

* **`hcont` is measured, not proved.** Proving it means showing from the curve
  that no factor `1 − x·yⱼ` meets `(−∞,0]` for `φ ∈ [0,π)` — a real-algebraic
  statement — plus the one-sided limit at the endpoint. **Not written.**
* **The envelope derivative `dS/dφ = 2φ`** — unchanged, still the other open
  step, still needs the IFT plus `d/dz Li₂` along a path.

### A process note

`lake` was unavailable in this container (elan blocked by the proxy, 403) and the
first build reported exit 0 while the log said `lake: command not found`. The
*wrapper's* exit code, not lake's. Same trap as the `nohup` incident, new
costume; caught only because the log gets read every time. Restored via
`scripts/lean-toolchain-cache-restore.sh` then `scripts/lean-cache-restore.sh`
(6990 oleans) — those scripts exist for exactly this firewalled case.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
