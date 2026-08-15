---
# qou-0vn0
title: raw-float64 ratchet cannot distinguish a CLEAN witness from an EMPTY one
status: todo
type: task
created_at: 2026-08-15T03:15:07Z
updated_at: 2026-08-15T03:15:07Z
---


## Observed 2026-08-15, nearly landed

While draining the raw-float64 reds (PR #5070) a long-compute producer
(`rho_k_co_casimir_extended.py`, ~45 min) was re-run. Mid-run, its witness
showed **0 raw floats** and `witness_raw_float64_audit.py` duly reported

    NEW dirty witnesses : 0      REGRESSED : 0

i.e. a clean sweep. The file was **gutted**: the script writes the witness
early and fills it in at the end, so the on-disk state was

    durationMs  2552837 -> 519
    2272 deletions, 36 insertions

Committing that would have destroyed a 42-minute witness *and* reported
success for doing so. Caught only because the duration looked wrong.

## The hole

The ratchet counts raw float64 fields. An **empty** witness has none, so it
scores identically to a perfectly-serialized one. The gate cannot tell
"cleaned" from "deleted", which is the same defect shape as a check that
passes by examining nothing.

This is not hypothetical beyond the near-miss: any truncation, failed write,
or interrupted long-compute produces a file that the ratchet calls clean.

## Sketch

Cheapest useful guard: compare against the committed witness rather than
scoring in isolation. Flag when a witness's **field count drops sharply**
(say > 50 %) while its raw-float count also drops — that is the signature of
deletion rather than serialization. A genuine drain converts floats to
strings and keeps the field count roughly constant; #5070's four probes went
29/19/17/12 -> 0 raw floats with field counts *unchanged*, so they would pass
the guard cleanly.

Secondary: have `WitnessBuilder` write atomically (temp file + rename) so a
partial state is never observable on disk. That fixes the cause rather than
detecting it, and would also protect every other witness consumer.

Related: `qou-irzg` (the ratchet's scan root excludes `docs/audits/scripts/`).
Both are coverage/soundness gaps in the same gate.
