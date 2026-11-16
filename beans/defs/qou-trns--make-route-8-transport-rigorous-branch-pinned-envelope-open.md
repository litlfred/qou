---
# qou-trns
title: 'Route 8 transport: branch integer now PINNED by the base point; envelope theorem still open'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - qbeta
    - dilogarithm
    - 5two
    - analysis
created_at: 2026-08-07T21:15:00Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-n4nr
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

---

## 2026-08-08 (later) — `hcont` on the OPEN arc is now PROVED, and it is real algebra

`QOU/QBeta/FiveTwoCutAvoidance.lean`, sorry-free, `lake` green (1749 jobs),
axioms `[propext, Classical.choice, Quot.sound]`. Route 21, 7 gates, exit 0.

The entry above said `hcont` was "measured, not proved" and that proving it "means
bounding `Re`/`Im` of `1 − x·yⱼ` on `|x| = 1` from the curve, which is a
real-algebraic statement and is NOT written". It is written now, and it needed no
complex analysis at all.

### The observation that does the work

**On `|x| = 1` all three elementary symmetric functions of the GGM curve are
real:**

    e₁ = (x²+1)/x = x + 1/x = 2c,   e₂ = (x²+x+1)/x = 1 + 2c,   e₃ = 1

So the cubic in `y` on the arc is `Y³ − 2cY² + (1+2c)Y − 1`, `c = cos φ` — **real
coefficients**. The 5₂ polynomial is its `c = 1` member and minus the Watson
cubic is its `c = −1` member, which is why the endpoint factor is `1 − w₁`.

Route 17 already noted `e₁, e₂, e₃` are rational in `x`; what was not used is
that on `|x| = 1` they are *real*, which collapses the whole question.

### The elimination

A factor meets the cut iff `t := x·y` is real with `t ≥ 1`. Put `y = t/x =
t(c − is)`, substitute, split real/imaginary. Divide the imaginary part by `s·t`
(valid for `φ ∈ (0,π)`; `t ≠ 0` because `e₃ = 1`), use `s² = 1 − c²`:

    I  = −4c²t² + 4c²t − 2c + t² − 1
    II = 4c³t³ − 4c³t² + 2c²t − 3ct³ + 2ct² + ct − 1

    Res_c(I, II) = 64 · t³ · (t−1)⁴ · (t⁵ − t³ + 1)

Lean checks the elimination by `linear_combination` with explicit Bézout
cofactors — the resultant is **verified, not imported from a CAS**:

    A = −t⁴(t−1)⁴(2c²t² + c − t²),   B = −t³(t−1)⁴(2ct² + 1)

Each branch dies: `t = 0` is refused by `II` directly; `t = 1` forces `c = 0`
from `I` and then `II` reads `−1 = 0`; and `t⁵ − t³ + 1 > 0` for all `t > 0`
(for `t ≤ 1` it is `t⁵ + (1−t³)`, for `t > 1` it exceeds 1 — no critical-point
analysis needed).

**Conclusion: `t < 0`.** Stronger than required — on the open arc `1 − x·yⱼ` is
not merely off the cut, it is `> 1`.

### The eliminant is sharp, and that is also the vacuity check

`t⁵ − t³ + 1` has exactly one real root, `−1.2365057…`, negative — and it is
**attained**. At `φ/π = 0.453289155972`, where the conjugate pair has
`φ + θ = π`, `x·y` is real and equals that root to 40 dps, deviation `0.0`
(G5). So the quintic's one real root *is* the one real value `x·y` takes on the
open arc.

That gate exists because `xy_neg` is a **no-solution theorem**, and a no-solution
theorem with unsatisfiable hypotheses proves nothing. Without G5 the whole file
would be unfalsifiable. Worth making a habit: every "no such configuration"
result needs a witness that the configuration is expressible.

### What is still open

* **The continuity packaging** — "`F` continuous" ⟸ "no factor meets the cut" is
  `Log`'s continuity off `(−∞,0]` composed with continuity of the root multiset.
  Standard, not formalised.
* **The endpoint `φ = π`** — genuinely on the cut, so cut-avoidance does not
  apply. Continuity there is one-sided and holds by the sign of
  `Im(1 − x·y) = −y·sin φ > 0` for `y < 0`. Not formalised.
* **The envelope derivative `dS/dφ = 2φ`** — untouched.

So `hcont` is not yet a theorem end to end; what was a real-algebraic gap is now
a routine-analysis gap. Different debt, much smaller.

### A measurement note

The first check of the real-coefficient reduction reported a max discrepancy of
`2.64` and looked like a refutation. It was a **sort key**: comparing two root
lists ordered by `(re, im)` puts a conjugate pair in different orders when the
real parts differ in the last bits. Replaced with a nearest-match multiset
distance; worst is now `< 1e-30`. A root-list comparison must never be done by
sorting on floating-point keys.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (later still) — the DEFORMED saddle condition is the curve, and its branch data

`QOU/QBeta/FiveTwoDeformedSaddle.lean`, sorry-free, `lake` green (1893 jobs).
Route 22, 7 gates, exit 0. The purely algebraic theorems need only
`[propext, Quot.sound]` — not even `Classical.choice`.

`FiveTwoSaddleSumRule.lean` had the **base point** versions —
`cubic_iff_sq_eq_cube` and `branch_data_of_cubic`, the latter described there as
"the sole source of the `π²` in the sum rule". The **deformed** versions, the
ones the transport travels along, were missing.

### The saddle condition is free

`y·∂V/∂y = 2log(−y) − log(1−y) − log(1−xy) − log(1−y/x)`. Exponentiating turns
`∂V/∂y = 0` into `y² = (1−y)(1−xy)(1−y/x)`, and cleared of the `1/x`:

    x·y² = (1−y)(1−x·y)(x−y)   ⟺   curve(x,y) = 0

**identically**, over any commutative ring (`deformed_saddle_iff_curve`, checked
at generic off-curve points in G2 so it is the ring identity and not an
equivalence-at-roots). At `x = 1` it collapses to `y² = (1−y)³`.

This matters for scoping the envelope: the saddle hypothesis is not a thing to
be established, it **is** the curve the roots were defined by. What the envelope
still needs is `dyⱼ/dx` and `d/dz Li₂` along a path.

### The third Vieta product

`prod_one_sub`: `∏ⱼ(1 − yⱼ) = 1`, joining `prod_one_sub_x_mul` (`= x`) and
`prod_x_sub` (`= x²`) from #4658. Together they give
`exp(Σⱼ branchTerm) = 1` **from Vieta alone** — the saddle condition is not
needed for the sum, only for the individual terms. That is exactly the `hexp`
hypothesis of `BranchIntegerPinning`, so the same lemma pins this sum too.

### Two things measured rather than assumed

**The corpus's `k = (+1,−1,0)` is CORRECT** (G5) — checked, not taken on trust.

**But the convention matters and was unstated.** The corpus uses `log(y)`;
`branchTerm` must use `log(−y)`, forced by the `log(−y)²` term in `V`. The two
differ by `2(log(−y) − log y) = ±2πi` per root. Measured: corpus `(−1,0,+1)`,
sum `0`; `branchTerm` `(0,1,0)`, sum **1**. Same mathematics, different integers.

**And the principal-branch sum jumps at the endpoint** (G7): it is constant `= 1`
on `[0,π)` and drops to `0` at `φ = π`. A **fourth** independent way the endpoint
sits on the cut — at `x = −1` the factors `−y` (at the positive root) and `1+y`
(at `y = −w₁`, twice over) are all real negative. Note `hexp` is blind to this,
because `exp` sees no branch; `hcont` is precisely what it violates.

### What this does NOT close

The envelope derivative. `Li₂` outside the unit disc is needed and the corpus's
`cLiTwo` is analytic only on `‖z‖ < 1` (`cLiTwo_analyticOnNhd`), while the arc's
roots reach `|y| = w₁ = 2.247`. That is `qou-clx8`, untouched.

### ⚠ A float64 defect in my own probe, and the gate that now exists

Route 22's first run failed G1/G4 at exactly `4.3e-16` — float64 epsilon. Cause:
an off-arc test point written `1 + 0.4j`, a Python complex literal, instead of
`mpf(1) + 1j*mpf("0.4")`. The same probe also used `round(float(...))` three
times to pull integers out of mpfs (`int(nint(...))` is the correct form).

There were already **four** beans about exactly this failure (`j0th`,
`qou-gqt5`, `qou-ny4j`, `qou-t0rf`) and no gate. There is one now:
`scripts/probe-float64-guard.py` + `.github/workflows/probe-float64-gate.yml`,
bean **`qou-f64g`**, with the backlog measured (17546 hits / 2184 files) and the
12 sharpest named.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — the IFT the envelope needs, built as Mathlib infra

`QOU/MathlibExt/ImplicitScalar.lean`, sorry-free, **no warnings**, `lake` green
(1967 jobs), axioms `[propext, Classical.choice, Quot.sound]`.

```lean
theorem exists_hasDerivAt_implicit [CompleteSpace 𝕜]
    (hf : HasStrictFDerivAt f f' (x₀, y₀)) (h0 : f (x₀, y₀) = 0)
    (hB : f' (0, 1) ≠ 0) :
    ∃ g : 𝕜 → 𝕜, g x₀ = y₀ ∧ (∀ᶠ x in 𝓝 x₀, f (x, g x) = 0) ∧
      HasDerivAt g (-(f' (1, 0)) / f' (0, 1)) x₀
```

Over any complete nontrivially-normed field — `ℂ` for this lane, `ℝ` for free.

### Why it was a Mathlib gap

Mathlib **has** an implicit function theorem, `Analysis/Calculus/Implicit.lean`,
but it is the general Banach version built on `ImplicitFunctionData`: it presents
the solution set through a complemented-subspace splitting, with
`implicitFunction : F → G → E` taking a point of `ker f'`. Right shape for a
submanifold, wrong shape for "solve for `y` as a function of `x`" — and it is
imported by nothing else in Mathlib. The scalar case in the form everyone
actually uses was simply absent.

### The construction

Straighten the graph with `Φ(x,y) = (x, f x y)`, derivative
`L(a,b) = (a, A·a + B·b)`, invertible exactly when `B = ∂f/∂y ≠ 0`, inverse
`L⁻¹(a,b) = (a, (b − A·a)/B)` written down explicitly via
`ContinuousLinearEquiv.equivOfInverse`. Then Mathlib's *inverse* function
theorem applies to `Φ`, and `g x := (Φ.localInverse (x,0)).2`.
`eventually_right_inverse` gives `Φ(Ψ(x,0)) = (x,0)`, whose first component says
`Ψ(x,0) = (x, g x)` and whose second says `f x (g x) = 0`. The derivative comes
from `to_localInverse` composed with `a ↦ (a,0)`, and `L⁻¹(1,0) = (1, −A/B)` is
where the IFT formula appears.

### Usability, checked end to end

`exists_sqrt_branch`: instantiated on `f(x,y) = y² − x` at `(1,1)`, where
`∂f/∂y = 2 ≠ 0` and `∂f/∂x = −1`, the theorem returns a branch of `√x` through
`1` with `g′(1) = −(−1)/2 = 1/2` — the derivative of `√x` at `1`, as it must be.
An existence theorem whose hypotheses nothing satisfies is worthless; this is
that check.

### ⚠ Where it does NOT apply on the arc, and why that was expected

`∂curve/∂y ≠ 0` is exactly "`y` is a **simple** root", i.e. the discriminant is
nonzero. On this arc the discriminant **vanishes**, at `θ = 137.9206708879635°`
— `exists_unit_circle_disc_zero`, proved in `FiveTwoDiscriminant.lean`. Two
branches collide there and no differentiable labelling of individual roots
survives it.

So this gives the branches on `[0,π] ∖ {φ₀}` and cannot give them at `φ₀`. That
is not a defect — it is why `ConstantOffOnePoint.lean` exists.
`constant_of_hasDerivWithinAt_zero_off_point` glues a derivative identity holding
off one point into a statement on the whole interval, using continuity there.
**The two bricks were built for each other**, a year apart in this lane's
reckoning, and only now meet.

### What still stands between this and `dS/dφ = 2φ`

1. **`HasStrictFDerivAt` for the GGM curve** as a function of `(x,y)` — mechanical
   (polynomial), verbose, not written. That is the next brick and it is what
   plugs this in.
2. The chain rule assembling `d/dφ Σⱼ V(x, yⱼ(φ))`, where the `y′` terms die
   because `∂V/∂y = 0` — and *that* is already free, via
   `deformed_saddle_iff_curve`: the saddle condition **is** the curve.
3. `Σⱼ ∂V/∂x = −2 log x / x` from the Vieta products plus branch pinning.
4. The `[0,π] ∖ {φ₀}` → `[0,π]` gluing, which is `ConstantOffOnePoint`.

Note the envelope never needs the *value* of `dyⱼ/dx` — only that it exists,
because `∂V/∂y = 0` annihilates it. The IFT is used for existence alone.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (later) — the IFT is plugged in, and the envelope collapse is measured

`QOU/QBeta/FiveTwoCurveDeriv.lean`, sorry-free, no warnings, `lake` green (2039
jobs). Route 26, 6 gates, exit 0.

```lean
theorem hasStrictFDerivAt_curve (x₀ y₀ : ℂ) :
    HasStrictFDerivAt (fun q : ℂ × ℂ => curve q.1 q.2)
      (curveDx x₀ y₀ • fst + curveDy x₀ y₀ • snd) (x₀, y₀)

theorem exists_hasDerivAt_root (hc : curve x₀ y₀ = 0) (hdy : curveDy x₀ y₀ ≠ 0) :
    ∃ g, g x₀ = y₀ ∧ (∀ᶠ x in 𝓝 x₀, curve x (g x) = 0) ∧
      HasDerivAt g (-(curveDx x₀ y₀) / curveDy x₀ y₀) x₀
```

with `∂ₓc = y³ − 2xy² + (2x+1)y − 1` and `∂_yc = 3xy² − 2(x²+1)y + (x²+x+1)`.
`∂_yc ≠ 0` is exactly "`y` is a **simple** root".

### The hypothesis holds where it must, and fails only where it must

`min_j |curveDy| ≥ 1.6158` everywhere on `|x| = 1` away from the branch point,
and **vanishes at `φ₀`**. Crucially, `φ₀` is **solved for, not sampled**: the
lane's own proved characterisation gives `Q(2cos φ₀) = 0` with
`Q(u) = u⁴ − 6u³ + 7u² + 6u − 31`, so

    φ₀/π = 0.76622594937757503001,   u₀ = −1.4844353317658568752

and `min|curveDy|` there is `1.8e-25` — the square-root accuracy floor for a
**double** root at 50 dps, which is exactly what it is.

**A near-miss worth recording.** G3's first draft quoted a refinement sequence
`0.695 → 0.133 → 0.0449 → 0.0177 → 0.0249`. That last value goes back *up*: the
samples were **bracketing** `φ₀`, not converging to it. Quoting a grid value as a
minimum is precisely the defect this lane already found once, in
`min|disc| = 0.348`. Caught and replaced with the exact solve. Also: the gate's
*claim text* still described the old method after the code changed — corrected,
because a claim that misdescribes its own gate is the same failure one level up.

### ⚠ The payoff, measured

**The envelope collapse holds to 1e-31.** G6 tracks a root along the arc by
continuity and checks

    d/dφ V(x, y(φ))  =  (∂V/∂x)·dx/dφ

by finite differences — worst deviation `3.5e-31` at `φ/π ∈ {0.2, 0.45}`. The
`dy/dφ` term drops out because `∂V/∂y = 0` on the curve, which
`deformed_saddle_iff_curve` already makes free. This is the identity the whole
IFT brick exists to license, and it is now checked directly rather than assumed.

G4 also confirms the IFT *value*: `dy/dφ` from finite differences matches
`−(∂ₓc/∂_yc)·dx/dφ` to 1e-12. The envelope does not need that value — only that
the derivative exists — but a wrong value would mean a wrong partial.

### What is left for `dS/dφ = 2φ`

1. Assemble the collapse over the three roots **in Lean** (G6 is numerical).
2. `Σⱼ ∂V/∂x = −2 log x / x` from the Vieta products plus branch pinning — the
   products are proved, the pinning lemma is proved, the assembly is not.
3. Glue `[0,π] ∖ {φ₀}` → `[0,π]` with `constant_of_hasDerivWithinAt_zero_off_point`.

Each is now a named, bounded task with its inputs in hand. None is written.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (later still) — the envelope's second ingredient, and the endpoint bites again

`QOU/QBeta/FiveTwoEnvelopeSum.lean`, sorry-free, no warnings, `lake` green (1894
jobs). Route 26 extended to 8 gates, exit 0.

```lean
exp_sum_log_one_sub_x_mul : exp(Σⱼ log(1 − x·yⱼ)) = x        -- from Vieta alone
exp_sum_log_one_sub_div   : exp(Σⱼ log(1 − yⱼ/x)) = x⁻¹      -- from Vieta alone
sum_div_of_pinned         : the assembly, pure algebra
sum_dVdx_of_pinned        : Σⱼ ∂V/∂x = −2·log x / x, given the pinned sums
envelope_value            : (−2 log x / x)·(i·x) = 2φ when log x = iφ
```

The first two are the `hexp` inputs the pinning lemma consumes; they need **no
analysis**. The last three are algebra. The *pinning* is taken as a hypothesis —
it needs `hcont`, still open — which is the honest factoring: analysis separated
from algebra, and only the algebra done here.

### ⚠ A finding: the pinned identity FAILS at the endpoint, and it is forced

G8 measures the branch integers with **principal** branches rather than assuming
them:

    k_A = 0  everywhere on the arc
    k_B = 0  on [0, π)   and   **1 at φ = π**

So `sum_dVdx_of_pinned`'s hypothesis is **false at the endpoint**. And it is
forced, not accidental: at `x = −1` the two expressions `1 − x·y` and `1 − y/x`
are *literally the same*, `1 + y`, so `Σ_A = Σ_B` — while the two identities
demand `+log x` and `−log x`, which differ by `2πi` when `log(−1) = +iπ`. Hence
`k_B − k_A = 1` there necessarily.

**Harmless, for a reason worth stating precisely.** `π` is an **endpoint**:
`S(π) − S(0)` needs the derivative only on the *open* interval plus continuity on
the closed one. So the identity holding on `[0,π)` rather than `[0,π]` costs
nothing, and **`φ₀` remains the only interior exceptional point** — which is what
`constant_of_hasDerivWithinAt_zero_off_point` is shaped for.

This is a **fifth** independent way this arc's endpoint sits on the branch cut,
after: `1 − x·y₁ = 1 − w₁` on the cut; `x = −1` itself on the cut; the
principal-branch saddle sum jumping there (Route 22 G7); and cut-avoidance
holding only on the *open* arc (Route 21 G7).

### Also measured

G7: both Vieta products hold along the whole arc to `7.2e-51` — `∏(1−x·yⱼ) = x`
and `∏(1−yⱼ/x) = 1/x`.

### What is left for `dS/dφ = 2φ`

1. Assemble the collapse over the three roots **in Lean** — G6 checks it
   numerically (to 1e-31); the Lean chain rule is not written.
2. Discharge the branch pinning from `hcont` — the `hexp` inputs are now proved,
   the continuity is not.
3. Glue across `φ₀` with `constant_of_hasDerivWithinAt_zero_off_point`.

Item 2 shrank today: the pinning lemma's *algebraic* inputs are all proved, and
what remains is exactly `hcont`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — items 1, 2, 3 all joined. `hcont` is now the ONLY open input

`QOU/QBeta/FiveTwoEnvelopeAssembly.lean`, sorry-free, no warnings, `lake` green
(2058 jobs), axioms `[propext, Classical.choice, Quot.sound]`. The three tasks
the previous entry listed are each one section.

### 1. The envelope theorem, in general

```lean
theorem hasDerivAt_of_partial_y_eq_zero
    (hF : HasFDerivAt F F' (x t, y t))
    (hx : HasDerivAt x x' t) (hy : HasDerivAt y y' t)
    (hzero : F' (0, 1) = 0) :
    HasDerivAt (fun s => F (x s, y s)) (F' (1, 0) * x') t
```

`y′` never appears in the conclusion — that is the whole reason the envelope
argument needs only *existence* of `dyⱼ/dx`, which `exists_hasDerivAt_root`
supplies. Stated for a general `F`; nothing about the dilogarithm enters. And
`hzero` is free for `V`, because `deformed_saddle_iff_curve` says the saddle
condition **is** the curve.

One trap: `F'` is ℂ-linear while the path is ℝ-parameterised, so the composition
needs `HasFDerivAt.restrictScalars ℝ`. Without it the elaborator stalls on
`NormedSpace ℝ ?m`.

### 2. The pinning, with its algebra fully discharged

```lean
exp_logSumA_sub_log_eq_one : exp(Σⱼ log(1 − x·yⱼ) − log x) = 1   -- from Vieta
exp_logSumB_add_log_eq_one : exp(Σⱼ log(1 − yⱼ/x) + log x) = 1   -- from Vieta
branchDiff_eq_zero_of_continuousOn : … continuity + base point ⟹ ≡ 0
```

The `hexp` hypothesis of `eq_zero_of_continuousOn_of_exp_eq_one` is now
**discharged from the Vieta products**. Nothing algebraic is left in the pinning:
what remains is exactly continuity.

### 3. The gluing

```lean
theorem envelope_integrate
    (hcont : ContinuousOn S (Icc 0 b))
    (hderiv : ∀ φ ∈ Ico 0 b, φ ≠ c → HasDerivWithinAt S (2 * φ) (Ici φ) φ) :
    ∀ φ ∈ Icc 0 b, S φ = S 0 + φ ^ 2
```

`constant_of_hasDerivWithinAt_zero_off_point` applied to `φ ↦ S φ − φ²`. At
`b = π` this is **`S(π) − S(0) = π²`** — the transport's conclusion — with the
one exceptional point `c` being `φ₀`, where the discriminant vanishes.

### Where the envelope step now stands

| input | status |
|---|---|
| roots differentiable off the discriminant locus | **proved** (`exists_hasDerivAt_root`) |
| `∂V/∂y = 0` on the curve | **proved** (`deformed_saddle_iff_curve`) |
| the `y′` terms cancel | **proved** (§1) |
| `Σⱼ ∂V/∂x = −2 log x / x` given pinning | **proved** (`sum_dVdx_of_pinned`) |
| `exp(·) = 1` for the pinning | **proved** (§2, from Vieta) |
| `(−2 log x / x)·(i x) = 2φ` | **proved** (`envelope_value`) |
| glue across `φ₀` | **proved** (§3) |
| **`hcont`** | **OPEN** |
| `d/dz Li₂` on the arc | **proved** (`qou-clx8`, closed today) |

**`hcont` is the only open input.** Everything else the envelope step needs is a
theorem. What is *not* done is the final wiring — instantiating §1 at `V` with
its three `Li₂` terms and the `log(−y)²` term, and summing over the three roots.
That is assembly of proved parts, not new mathematics, and it is not written.

Route 26 G6 checks the collapse numerically to **1e-31**, so the wiring has a
target to hit.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — attack options for `hcont`, and one of them in Lean

`QOU/QBeta/FiveTwoBranchByArgument.lean`, sorry-free, no warnings, `lake` green
(2059 jobs). Route 27, 6 gates, exit 0.

### What `hcont` is actually for

It is used for **exactly one thing**: forcing `k = 0` in
`Σⱼ log(1 − x·yⱼ) = log x + 2πi·k`. Nothing else in the envelope step needs it.
That reframing is what opens the options below.

### Option A — argument count (IMPLEMENTED)

Taking imaginary parts, `Σⱼ arg(1 − x·yⱼ) = φ + 2πk`, so `k` is pinned by
**bounds**: if the sum lies in `(−π, 2π)` and `φ ∈ [0,π)`, then `|2πk| < 2π` and
`k = 0`. That is arithmetic — no continuity, no root tracking, no base point.
Lean-proved: `branchInt_eq_zero_of_arg_structure`.

The bounds follow from three facts, measured on the open arc at 40 dps:

| obligation | measured | margin |
|---|---|---|
| every `arg(1 − x·yⱼ) > −π/2` | min `−1.4077` vs `−1.5708` | **10%** |
| at most **one** exceeds `π/2` | 2nd-largest peaks `1.3099` vs `1.5708` | **17%** |
| at least one is `≥ 0` | at most two negative | — |

These are real-algebraic statements on `|x| = 1`, the same shape as `xy_neg`,
which this branch proves by resultant elimination. **They are the new
obligations; they are not proved.**

⚠ **The margins are not generous.** 10% and 17% are much tighter than `xy_neg`'s
were, so the eliminations will be harder. Whether the trade is worth making is a
judgement, not a theorem — the numbers are recorded so it can be made on
evidence.

### Option B — continuity of the root multiset

`Σⱼ log(1 − x·yⱼ)` depends only on the *multiset*, which is continuous even
across `φ₀` where individual branches collide. So the symmetric framing dodges
the branch point. **But Mathlib has nothing on continuity of polynomial roots in
the coefficients** — checked, no `continuous_roots`, no `tendsto_roots`. That
route requires building that infrastructure first: a real and reusable Mathlib
contribution, and a large one.

### Option C — continuous logarithm / winding number

Lift the path directly. Mathlib's winding-number and angle-lifting coverage is
thin; assessed as worse than A.

### Option D — RULED OUT, recorded so it is not retried

The tempting route "`Re(1 − x·yⱼ) > 0` on the arc, hence every `|arg| < π/2`" is
**false**: `max Re(x·yⱼ)` reaches `2.2468` already at `φ/π = 0.9975`. That is why
option A's second obligation has to say *at most one* exceeds `π/2` rather than
*none does*.

### A structural simplification, either way

On the **open** arc the two log-sums are complex **conjugates** — the roots are
closed under conjugation (real cubic on `|x| = 1`) and `1/x = conj x`. So
`k₂ = −k₁`: **there is only one branch integer to pin, not two.** Verified to
1e-40 (G5). The argument breaks at `φ = π`, exactly where `1 − x·y₁` sits on the
cut — the sixth independent appearance of that endpoint.

### Recommendation

Option A, with eyes open about the margins. If either elimination proves
intractable, Option B is the fallback and pays for itself in Mathlib.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 — Option A's obligations are gone: the margins were an artefact

Route 28 (`qbeta_5two_route28_arg_sector_probe.py`, 8 gates) +
`QOU/QBeta/FiveTwoArgSector.lean` (11 theorems, sorry-free, `lake build
QOU.QBeta.FiveTwoArgSector` green, axioms `[propext, Classical.choice,
Quot.sound]`).

**The three obligations above are withdrawn — not because they were proved, but
because they were never the right statement.** They came from confining the
argument sum to the *uniform* window `(−π, 2π)`. But the window only has to
exclude `φ ± 2π`, and it may depend on `φ`. With `φ ∈ [0, π)` the window
`(φ − 2π, φ + 2π)` suffices, and it is loose enough that the individual bounds
become free or elementary:

| input | source | was |
|---|---|---|
| `arg(1 − x·y₁) ∈ (−π/2, 0)`, `y₁` the positive real root | `‖x·y₁‖ = y₁ < 1` ⟹ `Re > 0` | obligation 1, 10% margin |
| `arg(1 − x·y₃) ≥ 0` when `Im(x·y₃) ≤ 0` | `Complex.arg_nonneg_iff` | obligation 3 |
| `arg(1 − x·y₂) ∈ (−π, π]` | **free** | obligation 2, 17% margin |
| when `φ > π/2`, also `arg(1 − x·y₂) ≥ 0` | same as `y₃` | — |

**So the 10% and 17% margins were an artefact of the uniform window, not of the
mathematics.** The judgement call this bean recorded — "whether the trade is
worth making" — did not need to be made.

### What survives, and is now PROVED

One inequality: on the conjugate-pair part of the arc, `s·a < c·b` for the upper
member `y₂ = a + b i` (`sa_lt_cb`). Route 27 measured `max(s·a − c·b) = −0.3365`
and left it open. It follows from two Vieta consequences — `2cR = 1 + 2aR` and
`2a(R−1) = R² − R − 1`, `R = ‖y₂‖²` — by three sign certificates:

* `1 < R` (`one_lt_normSq`), i.e. the real root is `< 1`: otherwise `b² > 0`
  forces `4R(R−1)² > (R²−R−1)²`, impossible on `(0,1]` where the left side is at
  most `16/27` (certificate `(3R−1)²(4−3R) ≥ 0`) and the right at least `1`.
* `a > 0`: `c > a > 0` and `E := 1 + 4aR + 4a²R(R−1) > 0` **termwise**.
* `a < 0 < −c`: `E·(R−1) = R³(R−1)² − 1`, and
  `R³(R−1)² = (R³ − R²)·(R² − R)` is a product of two factors in `(0,1)` — the
  first `< 1` because `c < 0`, the second because `a < 0`.

`sq_gap` is the bridge: `(s·a)² − (c·b)² = a² − c²R`.

On the all-real part (`φ > φ₀`) the inequality is not needed at all: both extra
roots are **negative** (product `1`, sum `2c < 0`), so `Im(x·y) = y·sin φ < 0`
outright. Route 28 G8 confirms `(1 positive, 2 negative)` and `c < 0` at every
such point.

### Option D stays ruled out, and is now explained

`Re(1 − x·yⱼ) > 0` is false near `φ = π` — but that is precisely the all-real
part, where the sign argument replaces it. The two failures do not overlap.

### Adversarial check on the Lean statement itself

Route 28 G6: the hypothesis `π/2 < φ → 0 ≤ a₂` is **load-bearing**. Without it
the best lower bound is `−π/2 + (−π) + 0 = −3π/2`, which clears `φ − 2π` only
while `φ ≤ π/2` — so the weaker statement is false on more than half the arc.

### What is still open

The bridge from "three complex roots satisfying the Vieta relations" to "a real
root in `(0,1)` plus a conjugate pair (or three reals)". That is algebra, not
analysis, and it is stated as hypotheses in `FiveTwoArgSector` rather than
assumed silently. **`hcont`'s consumer is not closed by this file.**

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (later) — the root structure is proved; the pinning is closed

Route 29 (`qbeta_5two_route29_root_structure_probe.py`, 8 gates) +
`QOU/QBeta/FiveTwoRootStructure.lean` (16 theorems, sorry-free, `lake build
QOU.QBeta.FiveTwoRootStructure` green, axioms `[propext, Classical.choice,
Quot.sound]`).

`FiveTwoArgSector` left two hypotheses about the roots. Both are now theorems,
and the cost is **one IVT plus real algebra** — no continuity in `φ`, no root
tracking, no base point.

### The chain

| step | how |
|---|---|
| the curve's cubic **is** `Y³ − 2cY² + (2c+1)Y − 1` on `\|x\| = 1` | `curve_eq_unitCubic`, from `2·Re(x)·x = x² + 1` |
| a real root `t ∈ (0,1)` | `p(0) = −1 < 0 < 1 = p(1)`, IVT. `p(1) = 1` **identically in `c`** — the `2c` terms cancel |
| factor `(Y−t)` out | `Y² + βY + γ`, `β = t−2c`, `γ = t²−2ct+2c+1`, and `t·γ = 1` *is* `p(t) = 0` |
| `β` and `W = t²+t−1` share a sign | `β·t(1−t) = W`, and `t(1−t) > 0` on `(0,1)` |
| `c ≤ 1 ⟹ t > 2/5` | `c ≤ 1` gives `t³−2t²+3t−1 ≥ 0`; that cubic is strictly increasing with value `−7/125` at `2/5` |
| quadratic real ⟹ `W ≥ 0` | `disc ≥ 0` rearranges to `W² ≥ 4t(1−t)²`, which `W < 0` and `t > 2/5` contradict |
| ⟹ **both extra roots negative** | `β > 0`, `γ = 1/t > 0` |
| quadratic complex ⟹ `s·a < c·b` | Route 28's `sa_lt_cb`; `h1` is an identity given `t·γ = 1`, `h2` is `beta_rel` |

`exists_pinning_data` assembles it and returns the factorisation
`p(Y) = (Y−t)(Y−y₂)(Y−y₃)`, so a consumer holding only Vieta data can match its
roots against these.

### Measured

| quantity | value |
|---|---|
| `min t` over `c ≤ 1` | `0.43015970900194673` at `c = 1` — margin `0.0302` above `2/5` |
| branch split | at `φ₀/π = 0.76623`, the **same** point where the full discriminant vanishes (Route 16) |
| `max Im(x·y₃)` on the arc | `−0.01008` (shrinks to `0` at `φ = π`, as it must) |
| `max Im(x·y₂)` where `c < 0` | `−0.00249` |

### The `c ≤ 1` hypothesis is load-bearing (G7, adversarial)

At `c = 5`: `t = 0.09989 < 2/5`, `W = −0.890 < 0`, `disc = +57.97 ≥ 0` — so
`W_nonneg_of_disc_nonneg` is **false** there — and the two other roots are
`8.757` and `1.143`, both **positive**, which flips the sign of `Im(x·y)` and
breaks the pinning. Dropping `c ≤ 1` does not weaken the theorem, it falsifies
it.

### G1 is the gate that mattered

That the real cubic **is** the curve's cubic. Nine defects in this lane were
checks that tested something adjacent to what they claimed; a correct theorem
about the wrong polynomial would have been the tenth. Checked at 701 × 7 points
to `7.4e-40`, and proved in Lean.

### What is left in this bean

The envelope wiring above the pinning: instantiate `hasDerivAt_of_partial_y_eq_zero`
at `V` and sum over the three roots. Assembly of proved parts — Route 26 G6
checks the collapse numerically to `1e-31` — but not written.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (later still) — the three joins, and a claim that was wrong

Route 30 (`qbeta_5two_route30_envelope_wiring_probe.py`, 8 gates) + three Lean
modules, all sorry-free, all `lake build`-verified per module, axioms
`[propext, Classical.choice, Quot.sound]`:

| module | theorems | what it joins |
|---|---|---|
| `FiveTwoBranchPinned` | 4 | `exp(Σⱼ log(1−x·yⱼ) − log x) = 1` ⟹ `Σⱼ arg(1−x·yⱼ) = φ + 2πk`, then `Σⱼ log(1−x·yⱼ) = log x` |
| `FiveTwoEnvelopeWiring` | 8 | the envelope theorem instantiated at the actual `V` |
| `FiveTwoBranchPinnedB` | 9 | `Σⱼ log(1−yⱼ/x) = −log x`, the **second** pinned sum |

### The second pinned sum was invisible until the first was written

`sum_dVdx_of_pinned` takes **two** pinned log-sums; only one had ever been
worked on. Writing the first made the second obvious. This is the argument
against calling a chain of proved lemmas with unwritten joins "assembly".

It is proved by **mirroring** the sector argument, not by Route 27 G5's
conjugation identity (`k₂ = −k₁`) — that would need the root multiset to be
conjugation-closed *as a permutation*. On `|x| = 1`, `(y/x).im = y.im·x.re −
y.re·x.im`, and the same two facts that gave `Im(x·y₃) < 0` and `Im(x·y₂) < 0`
give `Im(y₂/x) > 0` and `Im(y₃/x) > 0`. Nothing new measured or assumed.

### ⚠ A claim this bean almost shipped, and it was FALSE

An earlier draft of `FiveTwoEnvelopeWiring`'s docstring said: *"`∂V/∂y = 0`
reduces to the deformed saddle, which by `deformed_saddle_iff_curve` **is** the
curve. So the envelope hypothesis is free on the curve."*

**It is not free.** Route 30 G2:

| root | `∂V/∂y` |
|---|---|
| the two roots other than the positive real one | `0` (to `1.2e-40`) |
| the positive **real** root `t` | `2πi/t` (to `2.1e-40`) — **not zero** |

The *exponentiated* saddle holds at all three roots (to `2.8e-40`). What fails
at `t` is the **logarithmic** identity: `−t` is a negative real, so it sits on
`log`'s cut, `log(−t) = log t + iπ`, and the `2·log(−y)` term leaves a bare
`2πi`. Exponentiating is necessary, not sufficient — the branch integers have to
line up too. Same family as the `hinv1`/`hlan1` failure and the endpoint
failures: **the sixth time a branch cut has bitten this lane at a real point.**

### The transport survives, and why

`S(φ) = Σⱼ Re Vⱼ` takes real parts, and the leak is `2πi·t′/t` with `t` and `t′`
real — purely imaginary, so `Re` kills it. Measured: `Re(dV/dφ) = Re(∂V/∂x·x′)`
at **all** roots to `4.6e-41`, while the unreduced difference reaches `2.47`.
The Lean statement was weakened to match: `hasDerivAt_re_deformedV_envelope`
takes `Re(∂V/∂y·y′) = 0`, not `∂V/∂y = 0`. The stronger
`hasDerivAt_deformedV_envelope` is still a true theorem — its hypothesis just
fails at one of the three roots, and the docstring now says so.

### The payoff

Route 30 G6: summing over the three roots, `Re Σⱼ ∂V/∂x·(i·x) = 2φ` **exactly**
(`9.2e-41`). That is `dS/dφ`.

### Non-vacuity with teeth

`logSumA_eq_log` has fifteen hypotheses and `logSumB_eq_neg_log` sixteen. G7 and
G8 check that every one holds **simultaneously** at all 399 arc points, and then
that the conclusion does too. A theorem with sixteen hypotheses deserves that.

### What is left

`S(φ)` is not yet defined in Lean as `Σⱼ Re V(x φ, yⱼ φ)` with a differentiable
root labelling, so `envelope_integrate` is not applied to it. That needs
`exists_hasDerivAt_root` threaded through — and it is a join, so it will be
written, not called assembly.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (evening) — `S(φ)` exists, and the non-vacuity gate earned its keep

Route 31 (`qbeta_5two_route31_transport_total_probe.py`, 6 gates) +
`QOU/QBeta/FiveTwoTransport.lean` (10 theorems, sorry-free, `lake build
QOU.QBeta.FiveTwoTransport` green, axioms `[propext, Classical.choice,
Quot.sound]`).

Everything the envelope step needed was proved; what was missing was **the
object it is about**. `S(φ) = Σⱼ Re V(x φ, yⱼ φ)` had never been written as a
Lean function, so `envelope_integrate` had nothing to be applied to. Now:
`arcX`, `envelopeS`, `hasDerivAt_envelopeS` (`S′ = 2φ`), `envelopeS_total`
(`S(π) − S(0) = π²`).

### Measured

| quantity | value |
|---|---|
| `S(φ) − S(0) − φ²` over the arc, incl. across `φ₀` | `4.9e-40` |
| `dS/dφ − 2φ` | `0.0` at working precision |
| `S(π−ε) − S(ε)` against the exact `(π−ε)² − ε²` | `1.8e-40` |

The raw gap from `π²` is `−6.28e-12`, which is **exactly** `−2πε` for the
`ε = 1e-12` endpoint offset — checked against the exact identity rather than a
rounded one, because "close to `π²`" is the kind of claim this lane keeps
getting wrong.

### ⚠ The non-vacuity gate found a fatal hypothesis — twice over

G4 checks all ~20 hypotheses of `hasDerivAt_envelopeS` hold **simultaneously**.
It found `−y ∈ slitPlane` failing at **all 199 points**. Cause: exactly **one**
root is real and positive at every `φ`, so `−y` is a negative real, on `log`'s
cut. A statement carrying that hypothesis is **vacuous on this arc** — true, and
about nothing.

Fixed by removing it from `VSide` and passing the `log(−y)` derivative in, by
whichever of two routes applies:

* `hasDerivAt_log_neg_of_slitPlane` — off the cut, the generic case;
* `hasDerivAt_log_neg_ofReal` — on it, via `log(−t) = log t + iπ`, which is
  perfectly smooth **along a real path** even though the complex derivative does
  not exist.

Both give the same value `Y′/Y`, so `hasDerivAt_deformedV_path` does not care
which supplied it. G4 now checks that one of the two routes covers every root,
and records that exactly `1` root sits on the cut at each `φ`.

This is the second defect in two rounds from the same source: `−t` on `log`'s
cut. Route 30 G2 found it corrupting `∂V/∂y`; Route 31 G4 found it emptying the
hypothesis set. **Both were found by gates that tested what the statement
actually said**, not what it was supposed to mean.

### G6: the envelope theorem, visible

Approaching `φ₀` the two colliding roots separate like `C·√|φ−φ₀|` with
`C = 2.6016257` (stable over five decades), so `dy/dφ` **diverges** like
`0.65040643/√|φ−φ₀|`. Yet the labelled term's derivative stays **bounded** at
`2.7268867` all the way in — because `∂V/∂y = 0` annihilates the divergent `y′`.

That also **withdraws an earlier draft of this gate**, which claimed the
labelled terms *jump* at `φ₀`. They do not: they are continuous and their
derivatives are bounded. The obstruction at `φ₀` is that `y′` fails to exist
*there*, not that anything blows up nearby — which is exactly why one
exceptional point costs nothing.

### What is left

- The root-path labelling is a **hypothesis** of `hasDerivAt_envelopeS`,
  supplied locally by the IFT but not constructed globally in Lean. `S` itself
  needs no labelling (it is symmetric); only term-by-term differentiation does.
- **The sum rule.** `S(π) − S(0) = π²` is the transport's derivative step, not
  the sum rule. Identifying `Σⱼ Re Vⱼ = −3π²/2` with the proved cyclotomic
  `Σₖ(2L+L) = +π²/2` is untouched by any of this.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## 2026-08-08 (late) — the sum rule IS `S(0)`, and the bridge is one `arg`

Route 32 (`qbeta_5two_route32_levelseven_bridge_probe.py`, 9 gates, 50 dps) +
`QOU/QBeta/FiveTwoLevelSevenBridge.lean` (9 theorems, sorry-free, lake green).

### The map

| | |
|---|---|
| `S(0) = −3π²/2` | **this IS the 5₂ sum rule** — residual `1e-30` |
| `S(π) = −π²/2` | and `S(0) = 3·S(π)` exactly |
| at `x = −1` the cubic is the **level-7** one, `y³+2y²−y−1` | and `wₖ = −yⱼ` exactly — `w₁ = 2.24698`, the very value that falsified `hinv1` |
| `Σⱼ Re[2L(−yⱼ) + L(yⱼ)] = +π²/2` | the shape of the proved `extended_sum` |
| the difference | `−π²`, a **log-bilinear** quantity with no dilogarithms |

So the transport is not a step *towards* the sum rule — it is a reformulation
*of* it, moving it from `x = 1` to `x = −1` where the proved cyclotomic identity
lives.

### Why the `−π²` collapses

`corr y = Re[log(−y)² − log(−y)·log(1+y) − ½·log(y)·log(1−y)]`.

* The **log-times-log part vanishes at every root**, because
  `2log|y| = 2log|1+y| + log(1−y)` ⟺ `y² = (1+y)²(1−y)` ⟺ `y³+2y²−y−1 = 0` —
  *the cubic itself* (`sq_eq_of_root`, `log_rel_of_root`).
* The whole `−π²` is the coefficient `−1` at the **unique positive root**, from
  `arg(−t) = π`.

**One argument, at one root.** That is the same `−t`-on-`log`'s-cut that
produced corrections 5 and 6 in this branch. Third appearance — and this time it
is not a defect, it is the answer.

### ⚠ The open link, recorded as a gate (G9)

The numeric bridge uses the **analytic** Rogers `L = Li₂(z) + ½log z log(1−z)`.
Lean's `extended_sum` is stated for the corpus's **piecewise** `extend`. Those
agree by Route 15 **on paper only** — `qou-rstq` item 4 — and that
identification sits *directly* on this bridge. G9 asserts the gap **exists**;
it is the one gate that would fail if this lane ever quietly closed it without
saying so.

### Gap A re-priced (G8)

`|∂p/∂y|` at the positive real root never drops below **1.75** on the arc. The
real root **never collides** — only the other two do, at `φ₀`. So `t(φ)` is
globally differentiable with *no* exceptional point, and `y₂+y₃ = 2c − t`,
`y₂y₃ = 1/t` are too. The obstruction is confined to splitting one quadratic
whose coefficients are smooth.

### On alien calculus

This curve is the GGM deformed 5₂ curve and resurgence is its native frame —
three saddles, complexified actions, integral Stokes constants. It would explain
*why* a sum over all saddles is a clean multiple of `π²` (note `S(0) = 3·S(π)`,
the `3` being the number of saddles). It is **not** an attack route for what
remains: Gap A is IFT bookkeeping and the bridge just collapsed to the cubic
plus one argument. Recorded as a separate lane, and as a source of an
independent check — which this branch's record argues for.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Progress (Round 57)
- Round 57 (`litlfred/qou#8213`, commit `2301811899d7f5b7e6235c29e2d41d3e068ef89b`): Added `prod_x_sub_eq_x_mul_prod_one_sub`, `base_point_x_eq_one_pins_products`, and `root_and_shifts_invertible` in `FiveTwoCyclotomicBloch.lean` plus 80-dps mpmath witness.
