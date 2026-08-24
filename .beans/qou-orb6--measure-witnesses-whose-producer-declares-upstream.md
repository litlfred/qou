---
# qou-orb6
title: 'MEASURE: witnesses whose producer declares upstreams but that record no edge are invisible to witness_dependency_drift'
status: todo
type: task
priority: normal
created_at: 2026-08-24T16:15:24Z
updated_at: 2026-08-24T16:16:10Z
---

## Not a new class — a RECURRENCE of the one `producer_upstream_edge_gap_audit`
## retracted to, with the cost measured

That audit's RETRACTION (2026-08-23) narrowed its finding to: *"the previously
committed witness was generated a month BEFORE its producer learned to record
edges, so that witness had no edge and the drift detector could not walk to
it ... narrower and self-closing."*

Correct about the mechanism. **"Self-closing" says nothing about how long, or
how wrong, before it closes** — and this is the measurement of that.

### The worked instance (PR #5671, bean `qou-nmza`)

`averaged-block-swap-binding.witness.json`, committed state before the fix:

    computedAt                 2026-06-11T02:21:28
    upstream_witness_hashes    ABSENT
    data.atom_traces.id        0.055358425349822354

Its producer DOES declare the edge (`add_upstream(HERE /
"binding-canonical.witness.json")`), but the committed witness predates that
instrumentation, so `witness_dependency_drift` could not walk to it. Meanwhile
`binding-canonical` was recomputed 2026-08-22 under convention D to
`0.16097414544240738…`.

**Result: 2.5 months at rel 0.6561 — 65.6 % wrong — while carrying
`id_trace_matches_binding_canonical` at tolerance 1e-9 marked PASSED.**
Post-re-run the same assertion holds at 2.96e-31.

That compounding is the point: the missing edge hides the staleness, and the
frozen assertion actively asserts the opposite. Documented as a mechanism in
`witness_failed_assertion_audit.py` (§"A second way a PASSING assertion lies").

## Measurement — and its LIMITS, which are not yet bounded

Name-based mapping (producer that calls `add_upstream`/`record_upstream` ->
its `WitnessBuilder("<stem>")`), over the tracked tree:

    witnesses whose producer declares upstreams : 165
      edge recorded (drift detector can walk)   : 113
      NO edge recorded -> invisible to drift    :  52   (32 %)

    by witness computedAt:  2026-05: 8   06: 24   07: 2   08: 18

**DO NOT QUOTE 52 AS A FINDING.** At least one confirmed false positive:
`path-b-evacuation.witness.json` was attributed to
`tools/qou-substrate/python/qou_substrate/witness.py` — the WitnessBuilder
LIBRARY, whose line 1094 contains `WitnessBuilder("path-b-evacuation", …)`.
A name-based map cannot tell a producer from an example inside the library.
The false-positive rate is unbounded because I stopped here.

## The part that is NOT explained, and matters most

18 of the 52 have `computedAt` in 2026-08 — **after** the 2026-08-08
`record_upstream` port, several on 2026-08-23/24. "Self-closing" does not
cover those. Three were spot-checked and their producers genuinely do declare:

    delta_lambda_categorical_verification.py  record_upstream:80, add_upstream_records:248
    binding_block_multiplicative.py           record_upstream:142, add_upstream_records:312
    l2_row_independence_probe.py              record_upstream:86

yet e.g. `delta-lambda-categorical-verification.witness.json` has NO
`upstream_witness_hashes` under any spelling (checked `upstream`, `upstreams`,
`provenance` too). So either `_UPSTREAM_RECORDS` is empty on the path taken,
or the `record_upstream` call sites are in branches not executed. **Resolve
this before drawing any conclusion from the 52** — if declared-but-unwritten
is the common case, the fix is in the producers' control flow, not a
regeneration wave, and the two framings imply completely different work.

## Next steps, in order

1. Explain the 18 post-port cases. That determines everything else.
2. Rebuild the mapping AST-side (a `WitnessBuilder(...)` in the module that
   also has the `add_upstream` call), not by name, and exclude
   `qou_substrate/witness.py` itself.
3. Only then decide between "regenerate the pre-port backlog" and "fix
   producer control flow".

## Coordination

This axis is owned by `computations/audits/producer_upstream_edge_gap_audit.py`
and `computations/witness_upstream_declaration_audit.py`. **Do not build a
third detector** — extend one of those. This bean exists to carry the measured
cost (65.6 %, 2.5 months) that the existing retraction's "self-closing" framing
leaves out, plus the unresolved post-port count.
