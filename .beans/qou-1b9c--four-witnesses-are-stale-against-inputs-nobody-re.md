---
# qou-1b9c
title: four witnesses are stale against inputs nobody re-ran — found only because agents happened to execute them
status: todo
type: task
priority: normal
created_at: 2026-08-30T10:42:01Z
updated_at: 2026-08-30T10:42:28Z
---


## How these were found — which is the point

Three drain agents ran every producer in their slices to establish a baseline.
That incidentally executed producers **none of them edited**, and eight
witnesses came back different. Nobody was looking for this; it fell out of
running things.

Reverted, because they belong to no change in this branch and committing them
would land unreviewed numeric movement under commit messages about something
else. But the movement is real, and reverting only restores the honest-stale
state (`qou-a31p`: a stale witness advertises that it needs re-running; a
silently-updated one does not).

## The four with genuine payload movement

**`qbeta/qbeta-habiro-cross-pair-quick-dp`** — 87 non-provenance fields
changed. The sharpest is a *conclusion-level* flip:

    data.n_minus_p.per_m[0].delta   : 0     -> -6
    data.n_minus_p.per_m[0].is_zero : True  -> False

A quantity recorded as identically zero is not zero. This is the same family
as `qou-saop`, where a verdict reversed under a green witness, and it is on a
sibling of that very probe.

**`probes/qbeta-habiro-phi8-squared-from-z-squared-probe`** — the factored
expressions move materially:

    64*u**42*(u**4 + 1)**3*(u**1…   ->  192*u**46*(u**4 + 1)**3*(u**…
    64*(u**4 + 1)**2*(1993*u**20…   ->  768*(u**4 + 1)**2*(29068579*…

Different leading coefficient, different degree, different inner polynomial.

**`q-dirac-linking-weight-h4-50dps`** — `precisionMetadata` moves
`compute_dps 50 -> 70`, `output_dps 40 -> 60`, `truncation_bound 1e-40 ->
1e-60`. The committed witness advertises a precision the producer no longer
computes at.

**`computations/witness-raw-float64-audit`** — an audit output, so its drift
is expected; noted only so the list is complete.

The other four (`meson-habiro-c2-off-integer-pivot`, `ocneanu-12-route-reexam`,
`probes/meson-gmor-derivation-probe`, `yekutieli-half-h2-observable-hunt`)
differ in the `environment` block alone.

## Why no gate sees them

Same two reasons as `qou-2364` and `qou-saop`, now with a third instance each:

* the producers are **unchanged**, so `witness_staleness_triage.py` — which
  keys on `scriptHash` drift — is looking at the wrong axis;
* nothing re-runs producers to compare against their committed witnesses, and
  where the input edge is undeclared (`qou-5k8x`: 220 of 391 producers)
  `witness_dependency_drift.py` has nothing to reason over either.

So the only thing that surfaced these was **executing them**, which no gate
does.

## What to decide

Whether a periodic "re-run and diff" sweep is worth its cost. It is the one
check that would have caught `qou-2364`, `qou-saop` and all four of these, and
none of the existing gates can. The obvious objection is runtime — the corpus
has ~700 witness-emitting producers and several take >10 min — so a sampled or
staleness-ordered sweep is the realistic form.
