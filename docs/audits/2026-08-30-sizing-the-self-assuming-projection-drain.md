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

> **🛑 THE FIRST BULLET BELOW IS WRONG, AND ALL THREE OF ITS OWN EXAMPLES
> REFUTE IT (measured 2026-08-30, same day; see
> [`2026-08-30-the-remainder-is-vacuous-not-open.md`](2026-08-30-the-remainder-is-vacuous-not-open.md)).**
> `KnotOperatorSelectionContext`, `HoefsmitScatteringPipelineContext` and
> `NucleonOrderingFactorizationContext` are each **inhabited by `Unit` and
> zero, with no hypotheses** — machine-checked, along with 22 others of the 79
> classes. Constructing a witness for such a class is not the open research; it
> is a one-liner, and it is *the defect* rather than progress, because a class
> inhabited that cheaply constrains nothing and the `[C]`-conditional
> declaration downstream is conditional on nothing.
>
> The bullet is kept rather than deleted because the *shape* of the argument is
> still right — a genuinely contentful class would cost exactly what it says.
> What was missing is that nobody had asked which of these are contentful, and
> the answer for at least a quarter of them is "none of it". Read the second
> bullet as the live one.

The disposition recorded on these entries is *"construct a witness instance and
prove the property there, or drop the pseudo-theorem and project the field at
use sites"*. Neither is mechanical:

- ~~**Constructing a witness** means supplying the mathematics the context class
  was standing in for. For many of these — `KnotOperatorSelectionContext`,
  `HoefsmitScatteringPipelineContext`, `NucleonOrderingFactorizationContext` —
  that *is* the open research, not a formalisation chore.~~ **Refuted above.**
- **Dropping the pseudo-theorem** is cheap per case but changes what each
  content block claims, so it is an authorial decision each time.

~~**So this is a week-shaped job, not a session-shaped one**, and the binding
constraint is not typing but per-case mathematical judgement across ~102
unrelated contexts.~~

**Revised 2026-08-30.** The week-shaped verdict rested on the refuted bullet.
With at least 25 of the 79 classes machine-proved vacuous, that fraction of the
job is not mathematical judgement at all — those context classes want
*re-encoding* (constrain a parameter, per the q-NS remedy) or the pseudo-theorem
wants dropping, and neither needs a derivation. The remaining ~54 are
unmeasured, not established as hard: `unproven` and `skipped` are statements
about the prober, not about them.

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

---

# Follow-up: both "cheaper decompositions" measured — one was mine misreading my own regex

Added 2026-08-30, same day, after working the two leads this document
recommended.

## 🛑 RETRACTION — the "21 bodies with no visible projection" is not a sub-shape

This document reported *"21 bodies with no visible projection … a different
sub-shape … possibly smaller and more uniform"* and recommended measuring it
first. **That number is an artifact of my own regex.**

The body scan looked for a projection under a hard-coded list of instance
names — `ctx|inst|h|hC|c|s|dl|kec|hi|self`. Re-run against *any*
`identifier.field`, **19 of the 21 do project**; they simply bind the instance
as `d`, `hZ`, `hT`, `dc`, `hyp`, `i`, `fac`, `jgcs`, `fct`, `hArg`, `hStrong`,
`v`, `pq`, `fai`, `jp`, `lpd`, `hK` or `chart`.

So there is **no distinct sub-shape and no cheaper decomposition here.** The
21 collapse into the ordinary population, and the recommendation to measure
them first is withdrawn. Same failure mode as the two producer detectors above:
a name-keyed pattern reporting absence where it had only failed to look.

## The 2 that are genuinely different

**`structurallyValidBinding_necessary`** — a pure tautology, not a projection:

    theorem structurallyValidBinding_necessary (h_invalid : ¬P) : ¬P := h_invalid

`id` under a name promising a necessity result. **Fixed** — removed, with the
module header corrected. Three things made this determinate rather than
authorial:

- the file sets its own precedent one declaration earlier: `withinLengthBound`
  records that *"the previous `(h : ¬P) : ¬P := h` was a self-assuming
  tautology"* and replaces it with a named decidable predicate;
- the predicate already has a canonical name — `BraidWord.structurallyValidBinding`
  in `mass-theory/conj-canonical-knot-id-sdp.lean:156`, ~20 use sites, body
  identical — so defining a local copy would have been the worse fix;
- nothing consumed it. The header's only related entry named
  `structurallyValidBinding_necessary_for_canonical`, **which does not exist
  and never did**; that entry is corrected too.

The necessity claim the header describes is still unwritten and stays
authorial: it needs the algebra-evaluation map the header lists as an open
port, which is why its sibling `evenPower_necessary_for_blockPosSemidef` is an
honest `axiom`.

**`whitehead_volume_conjecture`** — *not* mine to fix and not a hidden defect.
Its docstring is accurate: the genuine unconditional proof exists downstream as
`QOU.Knot.WhiteheadSaddle.whitehead_vc_innerSum_half` (verified present at
`WhiteheadSaddleClausen.lean:731` — namespace and filename differ, which is
correct, not a dead reference), this base file is Mathlib-only and cannot
import it, and bean `qou-1gkf` tracks the port. An honestly-documented
state-and-queue.

## The 7 repeated bundles: 15 declarations, all genuine

| bundle | defects | inhabited? |
|---|---|---|
| `RMatrixBraidingContext` | 3 | no |
| `CoreLeviContext` | 2 | no |
| `HasFiniteLPDuality` | 2 | no |
| `KnotFactorSpectralContext` | 2 | no |
| `DressedMassSubstrateSplit` | 2 | no |
| `AtomicLPStabilityContext` | 2 | no |
| `BarEvenKernel` | 2 | no |

All seven uninhabited, so all 15 are genuine. **Hand-verified total is now 27
of 112, still 0 legitimate** — which tightens the rule-of-three bound on the
legitimate rate from ~25 % to roughly **11 %**.

These are the only places one fix covers more than one defect, and the saving
is small: 15 declarations across 7 bundles, i.e. 8 fewer independent fixes out
of 112. It does not change the week-shaped verdict.

## New finding: a same-namespace duplicate

`RMatrixBraidingContext` and `r_matrix_braiding_structure` are each declared
**twice in namespace `QOU.Braiding`**, in two files:

- `braids-and-knots/r-matrix-braiding-structure.lean` (153 lines) — the
  content-block sibling, a **strict superset**: adds `Rcheck1`, `Rcheck2`,
  `claim_braid_relation` and `braid_rep_from_R_check`;
- `lean/QOU/Braiding/r_matrix_braiding_structure.lean` (65 lines) — the subset.

The duplication is deliberate: the sibling's header says it mirrors *"the
build-graph copy under `QOU/Braiding/r_matrix_braiding_structure.lean`"`.
**But that copy is in no build graph** — nothing imports it, and `QOU.lean`
imports six other `QOU.Braiding.*` modules and not this one (`grep -c` = 0).
So the stated rationale for keeping the mirror does not hold.

Left for an author: either drop the unimported subset, or add it to the
umbrella and make the sibling reference rather than restate it. Not done here —
it changes what `prop:r-matrix-braiding-structure` resolves to under the §0a
sibling-first rule, which is a content decision.
