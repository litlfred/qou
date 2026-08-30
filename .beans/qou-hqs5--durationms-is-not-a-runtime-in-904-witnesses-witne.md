---
# qou-hqs5
title: durationMs is not a runtime in ~904 witnesses — WitnessBuilder built after the work with no start_time
status: todo
type: task
created_at: 2026-08-30T20:22:29Z
updated_at: 2026-08-30T20:22:29Z
---


Found 2026-08-30 while working `qou-c7g8`, after `durationMs` misled me into
claiming a six-orders-of-magnitude regression that did not exist.

## The defect

`WitnessBuilder` computes `durationMs = monotonic() - start_time`, where
`start_time` defaults to **its own construction**. A producer that builds it
AFTER doing the work therefore records the time taken to SERIALISE the witness,
not to compute it — and the field is indistinguishable in the witness from a
real runtime.

Concrete case: `computations/hadron_knot_table.py` builds it at line 239, after
the atom loop ends at line 232. Its witness says `durationMs: 53`. I read that
as "19 atoms in 53 ms", concluded the producer had regressed six orders of
magnitude, and wrote it into a commit message before checking. The producer had
not regressed; 53 ms was `json.dumps`.

## Measured population

Static sweep of `computations/` for `WitnessBuilder("name"...)` constructions:

    1641  producers construct one with an explicit name
     258  pass `start_time`                      -> durationMs is a real runtime
     904  no start_time, built in the LAST THIRD -> almost certainly serialisation
     479  no start_time, built earlier           -> may still be roughly right

⚠️ The 904 is a **heuristic**, not proof: it is position-in-file, not control
flow. A producer can construct the builder late but before its real work, or
early inside a function called after it. Confirm per file before editing.

Affected files include dashboard-level producers —
`per_observable_100x_status.py`, `mass_table_ppb.py`, `binding_canonical.py`,
`crystal_basis.py`, `habiro/habiro_exact_taylor_extraction.py`.

## Why it matters beyond tidiness

1. **It actively misleads.** A witness with `durationMs: 53` looks like a
   performance record. Nothing marks it as fake. I am the worked example.
2. **It defeats regression detection.** Any "has this producer got slower?"
   check across the corpus is reading noise for 904 witnesses.
3. **It hides real timeouts.** `qou-c7g8` spent a long time on "is this producer
   hung or slow?" partly because its own witness claimed 53 ms.

## Fix

Capture `_T0 = time.monotonic()` before the work and pass `start_time=_T0`.
Done for `hadron_knot_table.py` in `f400a5c0f` as the worked example.

Do NOT sweep all 904 blindly: fixing this changes `durationMs` in every witness
touched, which is corpus-wide churn. Prefer fixing producers as they are next
regenerated for another reason, or batch them deliberately with the churn
acknowledged. Consider instead making `WitnessBuilder` REFUSE to emit
`durationMs` when no `start_time` was given — a missing field is honest, a wrong
one is not.
