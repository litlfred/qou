---
# qou-5k8x
title: witnesses that read upstreams with bare json.load have no drift edge — and pad float64 to 50 digits
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:26:32Z
updated_at: 2026-08-30T09:27:03Z
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
