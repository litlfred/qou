---
# qou-5k8x
title: witnesses that read upstreams with bare json.load have no drift edge — and pad float64 to 50 digits
status: in-progress
pr: 8186
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:26:32Z
updated_at: 2026-10-04T15:14:27Z
parent: qou-9nnz
---


## The mechanism behind qou-2364

`qou-2364` found a witness recording a number no state of the repository
produces, and the cause turned out to be that its **upstream inputs** were
regenerated while it was not. The obvious follow-up question is why no gate
saw it. This is why.

`computations/qbeta/qbeta_markov_trace_steps_4_5.py` reads its upstream with a
bare `json.load` and never calls `record_upstream` / `add_upstream`:

    $ grep -cE "record_upstream|add_upstream" qbeta_markov_trace_steps_4_5.py
    0

so its witness carries no `upstream_witness_hashes` and no `upstreamRecords`.
`witness_dependency_drift.py` reasons over recorded edges, and there is no
edge here to reason over. The dependency simply does not exist as far as any
tool is concerned, while being entirely real at runtime.

That is the general shape: **a producer can consume a witness without
declaring it, and the drift detector is then correct-but-blind.** The existing
`witness_staleness_triage.py` catches producers whose own `scriptHash` moved —
a different axis, and one that misses this case exactly, because here the
producer is unchanged and only its input moved.

## Second defect in the same read: float64 padded to 50 digits

The value arrives as a JSON float64 and is widened with
`sp.Float(<json float>, 50)`. The witness then records

    S_at_q0 = 0.18689366772151219664443999590730527415871620178223

which is 17 real digits followed by 33 digits of whatever the binary64 happens
to expand to. Any downstream comparison at more than ~1e-16 is comparing
padding. The corpus has a raw-float64 axis for precisely this and it does not
fire here, because the value is a *string* by the time it lands.

## Scope

Not one file. The question worth answering is how many producers read a
witness without declaring it — `grep -l "json.load"` over `computations/`
against the set that calls `record_upstream` would size it. Both halves are
mechanical to detect; neither is currently detected.

Found while draining `qou-26f2`: the tautology in this file was
`computed=str(S_at_q0), expected=str(S_at_q0)`, which is what made a value
loaded verbatim from an unrecorded upstream look like a verified computation.

## RESOLVED 2026-08-30 — with an important correction to this bean's framing

**This is not a new discovery, and the bean should not have implied it was.**
`qou_substrate.witness.record_upstream` exists precisely for it, and its
docstring already contains the survey:

> A survey of this corpus found that 290 of 330 producers that consume a
> witness read it **before** constructing their builder — the prevailing shape
> is "read the inputs at the top, build the witness at the bottom". That
> ordering, not oversight, is why `add_upstream` adoption sat at 5.7%: the API
> asked for a structure most producers do not have.

So the gap was known, diagnosed correctly, and a tool was built to close it
without a restructure. What this bean adds is the **current number** and the
**consequence**, not the problem.

## Current adoption, measured

Over `computations/` (live, `_deprecated` and tests excluded), counting only
producers that BOTH read a witness and emit one — the population that actually
has an edge to declare:

    producers that read a witness and emit one : 391
      declare the dependency edge              : 171
      SILENT                                   : 220  (56%)

Adoption has moved from 5.7% to ~44% since that survey. 220 producers still
consume a witness without declaring it, and for each of those
`witness_dependency_drift.py` is correct and blind simultaneously.

## The consequence, which is the part worth keeping

This is the mechanism behind `qou-2364`. That witness recorded a number no
state of the repository produces, because its **inputs** were regenerated while
it was not — and no gate saw it. `witness_staleness_triage.py` catches
producers whose own `scriptHash` moved, which is a different axis and misses
this case exactly, since there the producer was unchanged. The only tool that
could have caught it reasons over recorded edges, and there was no edge.

## Fixed in `qbeta_markov_trace_steps_4_5.py`

Both reads now go through `record_upstream`, and the builder gets
`add_upstream_records`. Verified: **2 edges recorded with sha256**, where
before there were none.

Second defect in the same read, also fixed: `tau_M_at_q0` arrives as a JSON
binary64 and was widened with `sp.Float(x, 50)`, so the witness recorded

    0.18689366772151219664443999590730527415871620178223

— ~17 digits of value followed by ~33 of binary-representation artefact, which
no upstream field can back because the producer records no higher-precision
form. Now `sp.Float(repr(x))`, giving the shortest decimal that round-trips
the double:

    0.1868936677215122

with a `S_at_q0_precision` note in the witness saying why it is not widened.
The raw-float64 axis never fired on the old value because it was a *string* by
the time it landed.

## Left open

The other 219. Both halves are mechanically detectable — "emits a witness and
reads one but never calls `record_upstream`" is the query above — so this is a
sweep someone can run, not a search. Whether it should be a gate is the
question worth deciding: it would go red on 56% of the relevant corpus today.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 51 Progress
- [x] PR https://github.com/litlfred/qou/pull/8186 (`fb4f6926d3f96fd99209ef3cb58128ff0ce2701b`): replaced bare `json.load(open(...))` in `computations/qbeta/qbeta_markov_trace_steps_4_5.py` with `record_upstream` + `wb.add_upstream_records`, removed false-precision `sp.Float(..., 50)` padding on `tau_M_at_q0`, and regenerated `qbeta-markov-trace-steps-4-5.witness.json`.
