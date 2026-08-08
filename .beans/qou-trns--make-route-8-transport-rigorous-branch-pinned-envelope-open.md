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
updated_at: 2026-08-07T21:15:00Z
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
