---
# qou-z9ws
title: 'SIZED: the 112 self-assuming projections are ~102 independent defects, not one systemic pattern'
status: completed
type: task
priority: normal
created_at: 2026-08-30T13:41:46Z
updated_at: 2026-08-30T13:43:04Z
---

Full measurement: docs/audits/2026-08-30-sizing-the-self-assuming-projection-drain.md

## Ratio — 0 of 12 legitimate

Sampled 12 of the 112 `genuine` `proof-no-self-assuming-projection` entries,
deterministic and evenly spaced (indices 0,9,18,28,37,46,56,65,74,84,93,102).
Applied the ledger's own discriminator: a projection is the legitimate Mathlib
accessor idiom ONLY when something builds the bundle.

**Every sampled bundle is uninhabited.** All 12 adjudications stand; the prior
agent was right on this sample.

Uncertainty stated rather than hidden: 0/12 is consistent with a true legitimate
rate up to ~25% (rule of three, 95%). The sample rules out the category being
mostly noise; it does not rule out a dozen or two legitimate cases in the rest.

## Two detectors disagreed on 2 of 12, and BOTH were wrong

- one called `DemazureFiberMarkovTraceContext` inhabited at
  demazure_fiber_markov_trace.lean:95 -- that line is the FLAGGED DECLARATION,
  `def ... [ctx : ...] : ... := ⟨ctx.claim_i..., ctx.claim_ii..., ...⟩`, matched
  because `Foo :=` appeared on it;
- the other called `DirectionSanityGateClass` inhabited at
  q-beta-direction-sanity-gate.lean:99 -- that is
  `theorem ... : ¬ DirectionSanityGateClass m`, a REFUTATION, matched by a
  "bundle in the conclusion" rule.

Resolved by reading the source. A producer search that cannot separate a
constructor from a consumer or a negation is not evidence, and this category is
precisely where that distinction lives.

## Sizing — ~102 independent fixes, not one pattern

Measured over all 112:

  distinct bundle types            102
  bundles appearing exactly once    95
  most-repeated bundle               3   (RMatrixBraidingContext)
  bodies projecting a field         90
  bodies with no visible projection 21
  projections onto `claim*` fields  66

The NAMING is systemic -- two-thirds land on `claim_i/ii/iii`-style fields, the
§3b-cond item-5 shape -- but those fields belong to 102 different context
classes, 95 of them singletons. There is no shared structure to fix once.

## Verdict: week-shaped, not session-shaped

The recorded disposition is "construct a witness instance and prove the property
there, or drop the pseudo-theorem". Constructing a witness means supplying the
mathematics the context class stood in for, and for several
(KnotOperatorSelectionContext, HoefsmitScatteringPipelineContext,
NucleonOrderingFactorizationContext) that IS the open research. Dropping is
cheap per case but changes what the block claims, so it is authorial each time.
The binding constraint is per-case judgement across ~102 unrelated contexts.

## Cheaper decompositions, if wanted

- The 21 bodies with NO visible projection are a different sub-shape, not
  characterised here; possibly smaller and more uniform. Measure before the 90.
- The 7 bundles occurring more than once are the only places one fix covers more
  than one defect.
