---
# qou-82mc
title: 'The b3 sign is a convexity property of the aggregator: both known assembly failures are one failure'
status: completed
type: task
priority: normal
created_at: 2026-08-30T09:29:08Z
updated_at: 2026-09-13T10:39:44Z
---

## What it is

`QOU/MassTheory/AggregatorConvexityDichotomy.lean` (8 declarations, sorry-free,
`lean`-direct exit 0, `#print axioms` = `[propext, Classical.choice, Quot.sound]`
on all eight) plus
`computations/probes/aggregator_convexity_divided_difference_probe.py` (6/6, zero
free parameters).

**Claim.** The two assembly failures the corpus has machine-checked are not two
failures. Write a symmetric A-body binding as a function of its total bond
weight, `B(A) = Φ(m_A · g)` with complete-graph bond counts `m_2 = 1`, `m_3 = 3`.
Then the connected 3-body Ursell cumulant

    b₃ = B(3) − 3·B(2) = Φ(3g) − 3·Φ(g)

is a **secant comparison on the ray through the origin, and nothing else**.
Jensen at `0` and `3g` with weights `(2/3, 1/3)`:

* `Φ` concave through the origin ⇒ `b₃ ≤ 0`  (`b3Agg_nonpos_of_concaveOn`)
* `Φ` convex  through the origin ⇒ `b₃ ≥ 0`  (`b3Agg_nonneg_of_convexOn`)

Both known failures are the concave side. The multiplicative/Mayer assembly
(`MayerThreeBodySign`, `Mu3SlotExclusion.thirdDiff_multiplicative`) is strictly
concave and lands at `b₃ < 0`; the bond-functional additive sum
(`PairwiseCumulantVanishing.b3_eq_zero_ofBondFunctional`,
`BodyOrderCumulant.fourthDiff_pairwise`) is affine, the concave boundary, and
lands at `b₃ = 0` exactly. AME2020 requires `b₃ = +1.4262225 > 0`.

So `not_concaveOn_of_b3Agg_pos`: **the measured sign excludes every
concave-through-the-origin aggregator, for every bond weight and every bond
set.** Scope **(b)**, invariant = Jensen, proved in the file.

## The sharpening of the multiplicative case

At a common bond factor `f` the Mayer cumulant factors **exactly**
(`wMult_b3_factor`):

    b₃ = (1 − f³) − 3(1 − f) = −(f − 1)²·(f + 2)

a negated perfect square times a positive factor. Two consequences the threshold
form did not give:

* `wMult_b3_nonpos` needs only `f > −2`, which every bond factor satisfies. The
  earlier `MayerThreeBodySign.b3_neg_of_le` needed the *measured* `f_pn ≤ 2/3`.
  So in the equal-bond case the negative sign is unconditional.
* `wMult_b3_eq_zero_iff`: on `f > −2` it vanishes **only at `f = 1`**, i.e. only
  when the bonds do not couple. There is no tuning of `f` inside this assembly
  that reaches a positive `b₃`; the boundary is the decoupled system.
* the sign is **second order** in the coupling `1 − f`. It is not an artefact of
  where the measured `f_pn` happens to sit.

Probe checks the factorisation at all four measured `f_pn` (D/probe2 0.50823,
D/chi 0.61268804, C/probe2 0.39486, C/chi 0.49932033) plus `f = 1` and `f = 0.9`:
both forms agree to `dps − 10`, all six non-positive.

## The positive orientation — this is the part that is new work, not a negative

The convex branch survives (`b3Agg_sq_pos`: `Φ = x²` gives `b₃ = 6 > 0`), and the
probe measures that **AME's own data sits in it**. Reading `Φ` straight off AME
at bond counts 1, 3, 6 — no model, no fit, no `q₀`, no convention, so the
convention-C/D question and the pin cannot move this:

| A | bonds | Φ (MeV) | Φ/bonds | B/A |
|---|---|---|---|---|
| 2 | 1 | 2.224566 | 2.224566 | 1.112283 |
| 3 | 3 | 8.0999205 | 2.6999735 | 2.6999735 |
| 4 | 6 | 28.295673 | 4.7159455 | 7.07391825 |

First divided differences **2.224566 → 2.93767725 → 6.7319175**, strictly
increasing: `Φ` is **convex** on the measured grid. `Φ(x)/x` strictly
increasing: **strictly superadditive** through the origin.

So the search re-orients. It is not "try a third assembly". It is: **the
aggregator must be strictly convex at small argument** — binding must be
*superadditive* in bond count rather than saturating in it — and, from
`QOU.Mass.CoordinationSaturation` needing `B/A` bounded, **asymptotically
linear**. That class is narrow but non-empty (`x²/(1+x)` is in it). Whether any
Hecke-side quantity produces such a `Φ` is the open question, and it is a much
sharper question than the one this arc started with.

Note this is *coherent with*, not in tension with, saturation: real `B/A` rises
steeply to `A = 4` (1.11 → 2.70 → 7.07) and only then flattens toward ~8.8 at
⁵⁶Fe. Convex-at-small-argument and asymptotically-linear is exactly that shape.

## Three things this does NOT establish, recorded before anyone quotes it

1. **Three interior points cannot distinguish convex from convex-then-concave**,
   and saturation *requires* the latter eventually. "Convex" here is a local
   statement about the light nuclei, not an asymptotic claim.
2. **`b₄ > 0` is not evidence for convexity.** `√·` is concave and yields
   `b₄ = √6 − 4√3 + 6 > 0`. `b₃` is the discriminator of this family; `b₄` is
   not, and a `b₄` agreement must not be read as evidence about the aggregator.
   Asserted in the probe so it cannot be quietly forgotten.
3. **`b3Agg_linear_eq_zero` is a numerical agreement with
   `b3_eq_zero_ofBondFunctional`, not a reduction of it.** Different route, same
   value. Stated that way in the docstring.

## Normalisation trap caught en route — do not repeat it

I nearly compared the corpus `μ₃`/`μ₄` signs against Ursell `b₃`/`b₄` as if they
were the same family. **They are not.** Checked with exact arithmetic:

    mu3 = B(3H)/B(2H) − [3]_q = 3.8128 − 3.3420 = +0.4708
    b3 in the same units    = b3/B(2H)          = +0.6411
    difference = ([3]_q − 3) + (3H alone vs isospin average) = +0.1703

Two different baselines (`[3]_q = 3.3420` vs `3`) and two different numerators
(³H alone vs the isospin average). So `μ₄ = −4.591` being negative while
`b₄ = +9.243387` is positive is **not a discrepancy** — it is two
normalisations. Same trap class as the `c₃` 3.47 % / 3.35 % case in AGENTS.md.
Nothing was published on the conflation.

## Bond count caveat

`m_A = C(A,2)` is used only on `A ≤ 4`, where the complete graph is 3-regular and
therefore coincides with bounded degree 3, so
`QOU.Mass.CoordinationSaturation` — which refutes `m = C(A,2)` as a *law* — does
not bite on this grid. It would beyond `A = 4`. Do not extend the grid naively.

## Follow-ups

* Identify a candidate `Φ` from Hecke-side quantities that is convex at small
  argument and asymptotically linear, then test it against `b₃`, `b₄` *and*
  saturation together. Only the conjunction is informative.
* Extend the convexity measurement past `A = 4` with a *derived* bond set rather
  than `C(A,2)`, which is the only way to see where the convex→concave turn is.
* Related open beans: `qou-brng` (linking-vs-self-energy amplitude assignment),
  `qou-e5jf`, `qou-9yqb`, `qou-edt7`.


## 🛑 TITLE IS NOW MISLEADING 2026-09-13 — convexity is SUFFICIENT but STRICTLY UNNECESSARY

This bean is `completed` and titled *"The b3 sign is a convexity property of the
aggregator"*. A reader landing on that title takes convexity for the invariant.
It is not.

`QOU/MassTheory/B3AggSecantCharacterisation.lean` (on `main`, merge
`3cb26d4b9f8`) proves the **iff** that convexity was approximating: with
`s x = Φ x / x` the origin-secant slope,

    b3Agg Φ g = 3g·(s(3g) − s(g))      exactly
    0 ≤ b3Agg Φ g  ↔  s(g) ≤ s(3g)     an IFF, not an implication

and `convexOn_sufficient_not_necessary` exhibits `Φ = x³ − x²` — **not**
`ConvexOn ℝ (Ici 0)` (concave near the origin, `Φ'' = 6x − 2 < 0` for `x < 1/3`)
— with `b3Agg Φ 1 = 18 > 0`.

**A search for `b₃ > 0` restricted to convex aggregators searches a strict
subset.** Global convexity is a condition at every pair of points; `b₃ > 0`
requires only that ONE secant slope not drop across ONE fixed scale ratio.

And because it is an **iff**, choosing `Φ` to make `b₃ > 0` is the assumption
rewritten, not evidence for it — selection against the target under §NO FITTING.
The non-circular reformulation is the scaling route: `Φ(3g) = c·Φ(g) ⟹
b₃ = (c−3)Φ(g)`, so for a p-homogeneous law `b₃ > 0 ↔ p > 1`, i.e. **"is the
assembly superlinear in the bond count?"** rather than "why should the aggregator
curve upward?"

Live carrier: `qou-2ss0`. Left `completed` — only the title misleads.
