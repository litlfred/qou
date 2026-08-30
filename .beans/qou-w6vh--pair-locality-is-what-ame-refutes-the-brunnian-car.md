---
# qou-w6vh
title: 'Pair-locality is what AME refutes: the Brunnian carrier is load-bearing, not incidental'
status: completed
type: task
priority: normal
created_at: 2026-08-30T12:47:18Z
updated_at: 2026-08-30T12:48:17Z
---

## What this is

A bridge between two results that landed on `main` the same day from **different
sessions**, which had not been put together.

* `QOU.Mass.SelfMutualPartition.binding_eq_neg_mutualEnergy` (`qou-brng`, #6145) —
  binding `= −(mutual energy) = −Σ over inter-component crossings`.
* `QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise` (`qou-bhzt`, #6101) —
  a pairwise-additive binding has `b₃ = 0` identically.

**Every crossing joins exactly two components**, so the first sum groups by
unordered pair with no extra hypothesis at all. That puts it one hypothesis away
from the second — namely whether a pair's weight is the *same* in every assembly
containing it. Call that **pair-locality**. If it held, R2 would be refuted on
contact, because AME2020 measures `b₃ = +1.4262225`, not zero.

`QOU/Mass/CrossingModelPairLocality.lean` — 8 declarations, sorry-free,
`lean`-direct exit 0. Notably `brunnian_not_pairLocal` and `pairLocal_of_constant`
depend on **no axioms at all**; the rest on `[propext, Quot.sound]` only (no
`Classical.choice`).

| declaration | content |
|---|---|
| `isPairwise_of_pairLocal` | assembly-independent pair weights ⇒ pairwise-additive |
| `b3_eq_zero_of_pairLocal` | hence `b₃ = 0` identically |
| `b4_eq_zero_of_pairLocal` | and `b₄ = 0` |
| `not_pairLocal_of_b3_ne_zero` | **a nonzero measured `b₃` refutes pair-locality** |
| `brunnian_not_pairLocal` | a Brunnian carrier is exactly that violation |
| `b3_eq_neg_tripleMutual_of_brunnian` | with pair terms gone, `b₃` **is** the triple channel |
| `tripleMutual_neg_of_b3_pos` | so `b₃ > 0` forces an **attractive** triple channel |
| `pairLocal_of_constant` | non-vacuity |

## The consequence worth keeping

**The Brunnian property of the carrier is load-bearing, not a curiosity.** A
Brunnian link is precisely a maximal failure of pair-locality: every 2-sublink is
trivial, so the pair weight measured in isolation is zero, while the assembled
link is not. The corpus already establishes that the ³He/⁴He carrier `L6a4` is
Brunnian (`QOU.Mass.BrunnianBindingChannel`, #6125) — and this says that is
exactly what saves `binding = −(mutual)` from an immediate `b₃ = 0` refutation.

Read the other way: **if the carrier were not Brunnian (or otherwise
assembly-dependent), R2 together with the AME cumulant would be inconsistent.**

## A direct hit on an existing structure

`QOU.Mass.CoordinationBinding.BondExtensiveBinding` gives `binding = ε · bondCount`
with `bondCount = C(A,2)`. That is pair-local by inspection, so `b₂ = ε`,
`b₃ = 3ε − 3ε = 0` — **refuted by AME**. This is a *second, independent* exclusion
of the uniform-ε complete-graph reading: `QOU.Mass.CoordinationSaturation` already
excluded it because `B/A = ε(A−1)/2` is unbounded, and that argument is about large
`A` while this one bites at `A = 3`. The coordination-*count* idea survives; the
uniform-ε-per-bond reading of it does not.

## The measurement

`computations/probes/pair_locality_shortfall_probe.py` — 6/6, mpmath end to end,
zero free parameters, consumes no framework quantity.

A pair-local assembly has `b₃ = b₄ = 0` **forced**, so its entire binding is
`C(A,2)·b₂`:

| A | pair-local ceiling | AME | shortfall | irreducible |
|---|---|---|---|---|
| 2 | 2.224566 | 2.224566 | 0 | 0 % |
| 3 | 6.673698 | 8.0999205 | 1.4262225 | **17.61 %** |
| 4 | 13.347396 | 28.295673 | 14.948277 | **52.83 %** |

**More than half of ⁴He's binding is irreducibly many-body** — a factor 2.12 above
the pair-local ceiling, and no bond functional whatsoever changes that, because the
exclusion is of the *assembly*, not of the function it applies.

⁴He by body order: pairs 13.347 MeV (47.2 %), triples 5.705 (20.2 %), quad 9.243
(32.7 %).

**Derived prediction, zero-fit.** With a Brunnian carrier the pair terms vanish, so
`b₃` *is* the triple channel exactly — no contamination, no free constant. The
measured `b₃ > 0` therefore pins the three-body mutual energy to **attractive,
1.4262225 MeV per triple**. That is a target the Brunnian count channel of
`BrunnianBindingChannel` can be checked against.

**Corpus cross-check (independent reproduction, not a new result).** `b₃/b₂ =
0.6411` and `b₄/b₂ = 4.1551` against the 0.64 and 4.16 recorded in
`deltalambda-kappa-interface-residual-simplex.witness.json` from the 2026-06-23
audit — agreeing to 0.18 % and 0.12 %.

## What this does NOT do

* **It does not close `qou-brng`.** The bean's stated open item is the *mass*-side
  identification — the substrate mass observable with the crossing self-energy at
  full Markov-trace granularity (`self` closing to the q-dim self-trace `lw`, and
  the archimedean dressing `m = m_e·Vol·lw/ℏ_q²`). Nothing here touches it.
* **It does progress `#6125` sub-question 2, in the negative direction.** That
  question asks why the surviving count channel enters as a *bare integer* while
  the self channel keeps the full q-dim trace. The answer is now partly
  constrained: it **cannot** enter as a bare integer *per pair*, because that is
  pair-local and gives `b₃ = 0`. Whatever the count is, it depends on the cluster.
* **"Irreducibly many-body" is about the assembly, not the force.** A genuine
  two-body force can produce non-pairwise *binding* through the assembly — which is
  exactly what a Brunnian carrier does. Do not quote 52.8 % as "half the nuclear
  force is three-body".
* **`b₂` is not Brunnian.** The deuteron carrier is a clasp (Hopf/trefoil,
  `Vol = 0`) per the 2026-08-29 owner ruling, so the hierarchy is mixed: pairs
  through clasps, higher orders through Brunnian channels. The Lean's Brunnian
  theorems apply to the higher orders only.
* **Three body orders is three data points.** The growth of the irreducible
  fraction with `A` is *consistent with* a Brunnian hierarchy; it does not
  establish one, and `A > 4` is untested here.
* **The ℏ_q² saturation question is untouched** (`qou-brng` R3, separately measured
  numerology-suspect by #6145). Not revisited, not forced.

## Checked before claiming

Ran the corpus-grep. The genericity check I first intended — whether the
`μ₃ > 0`, `μ₄ < 0` sign flip is an artefact of the subtracted baseline — is
**already closed**: `QOU.MassTheory.Mu3BaselineFragility.mu3_positive_all_baselines`
and `mu4_negative_all_baselines`, with the companion probe measuring a 1.73×
baseline-class spread that the signs survive. I would have re-derived a closed
result; recorded so the next agent does not.

Also confirmed en route, exactly: `μ_k` inverts `M(A) = ρ_strong(A) − ρ_grad(A)`
with `ρ_grad = [A]_q!/[2]_q!` (`M(2) = 0`, `M(3) = 0.470769`, `M(4) = −2.707972`),
which is the **same** binomial inversion as the Ursell `b_k` applied to a
*different sequence*. So `μ₄ = −4.591 < 0` against `b₄ = +9.243 > 0` is two
normalisations, not a discrepancy — the same separation recorded in `qou-82mc`,
now with the exact producer identified.

## Related

`qou-brng`, `qou-bhzt`, `qou-82mc` (the convexity dichotomy — this supplies the
mechanism for the superadditivity it demands), `qou-zy94`, `qou-edt7`.
