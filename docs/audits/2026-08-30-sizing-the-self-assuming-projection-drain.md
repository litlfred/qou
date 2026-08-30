# Sizing the self-assuming-projection drain: 12 sampled, 0 legitimate, ~102 independent fixes

**Date:** 2026-08-30 · **Bean:** `qou-z9ws` (arc parent `qou-rq9n`, ledger `qou-s3zd`)

---

## The question

`proof-no-self-assuming-projection` is the largest block of adjudicated-`genuine`
verdicts in the vacuity review ledger — **112 of 191**. Before committing to a
drain, two things needed measuring:

1. **How many are really defects?** The category flags a theorem whose conclusion
   is character-identical to a field it projects. That is *sometimes* the
   legitimate Mathlib accessor idiom, so some fraction of the 112 could be
   mis-adjudicated.
2. **Is it one pattern or many?** 112 instances of a single systemic shape is a
   different job from 112 independent ones.

## Method

**Sample:** 12 of 112, deterministic and evenly spaced across the sorted
population (indices `0, 9, 18, 28, 37, 46, 56, 65, 74, 84, 93, 102`), so it is
reproducible and not cherry-picked.

**Discriminator:** the one the ledger itself uses —

> *"A projection like this is the legitimate Mathlib accessor idiom ONLY when
> something builds the bundle."*

So for each sampled declaration: find the structure/class it projects from, and
search the corpus for any `instance` / `def` / `abbrev` / `example` that produces
one.

## Result 1 — the ratio: 0 of 12 legitimate

| sampled declaration | bundle | inhabited? |
|---|---|---|
| `knot_eigenbasis_density` | `KnotEigenbasisData` | no |
| `tower_noncollapse_implies_independence` | `YekutieliLiftingCondition`, `TowerNoncollapseImpliesIndependence` | no |
| `knot_operator_selection` | `KnotOperatorSelectionContext` | no |
| `phi_q_tower_algebraic_stratification` | `PhiQTowerAlgebraicStratification` | no |
| `hoefsmit_scattering_pipeline` | `HoefsmitScatteringPipelineContext` | no |
| `sorting_color_energy` | `SortingColorEnergyContext` | no |
| `demazure_fiber_markov_trace` | `DemazureFiberMarkovTraceContext` | no |
| `markovTrace_branching` | `MarkovIdentificationContext` | no |
| `nucleon_ordering_factorization` | `NucleonOrderingFactorizationContext` | no |
| `atomic_nf_witness` | `AtomicNfWitnessContext` | no |
| `descent_surjective` | `DescentLemma` | no |
| `qbeta_direction_sanity_magnitude_match` | `DirectionSanityGateClass` | no |

**Every sampled bundle is uninhabited**, so by the ledger's own rule none is the
accessor idiom, and all twelve adjudications stand. The prior agent's `genuine`
verdicts were right on this sample.

**State the uncertainty honestly.** 0 of 12 does not mean 0 of 112. By the rule
of three, an observed zero in n=12 is consistent with a true legitimate rate up
to roughly **25 %** at 95 % confidence. What the sample rules out is the
possibility that the category is *mostly* noise; it does not rule out a dozen or
two legitimate cases among the rest.

### Two automated detectors disagreed, and both were wrong

Worth recording, because the ratio would have been wrong if either had been
trusted. Two independently-written producer searches disagreed on 2 of the 12,
in opposite directions:

- One reported `DemazureFiberMarkovTraceContext` **inhabited** at
  `demazure_fiber_markov_trace.lean:95`. That line is the flagged declaration
  itself — `def … [ctx : DemazureFiberMarkovTraceContext] : … := ⟨ctx.claim_i…,
  ctx.claim_ii…, ctx.claim_iii…⟩` — matched because `Foo :=` appeared on it.
- The other reported `DirectionSanityGateClass` **inhabited** at
  `q-beta-direction-sanity-gate.lean:99`. That is
  `theorem direction_sanity_gate_reject … : ¬ DirectionSanityGateClass m` — a
  *refutation*, matched by a "bundle appears in the conclusion" rule.

Both were resolved by reading the source. A producer search that cannot tell a
constructor from a consumer or from a negation is not evidence, and this
category is exactly where that distinction lives.

## Result 2 — the sizing: ~102 independent fixes

Measured over all 112, not the sample:

| quantity | value |
|---|---|
| distinct bundle types | **102** |
| bundles appearing exactly once | **95** |
| most-repeated bundle | `RMatrixBraidingContext`, **3** |
| bodies that visibly project a field | 90 |
| bodies with no visible projection | 21 |
| projections onto a `claim*`-named field | 66 |

**The naming is systemic; the content is not.** Two-thirds of the projections
land on fields called `claim_i…`, `claim_ii…`, `claim_iii…` — the §3b-cond item-5
shape, where a context class carries the block's own conclusion and the
"theorem" hands it back. But those fields belong to **102 different context
classes, 95 of which occur once**. There is no shared structure to fix once.

## What this means for the drain

The disposition recorded on these entries is *"construct a witness instance and
prove the property there, or drop the pseudo-theorem and project the field at
use sites"*. Neither is mechanical:

- **Constructing a witness** means supplying the mathematics the context class
  was standing in for. For many of these — `KnotOperatorSelectionContext`,
  `HoefsmitScatteringPipelineContext`, `NucleonOrderingFactorizationContext` —
  that *is* the open research, not a formalisation chore.
- **Dropping the pseudo-theorem** is cheap per case but changes what each
  content block claims, so it is an authorial decision each time.

**So this is a week-shaped job, not a session-shaped one**, and the binding
constraint is not typing but per-case mathematical judgement across ~102
unrelated contexts.

### The cheaper decomposition, if it is wanted

The 21 bodies with **no visible projection** are a different sub-shape and were
not characterised here — they may be a smaller, more uniform group and are worth
measuring before the 90. Likewise the 7 bundles that appear more than once
(`RMatrixBraidingContext` ×3, and six ×2) are the only places one fix covers
more than one defect.

## Reproducing

Both measurements are pure reads over the committed ledger and the `.lean`
sources; no producer was run and nothing was regenerated. The sample indices are
fixed above so the same twelve come back.
