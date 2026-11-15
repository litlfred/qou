---
# qou-qvg6
title: 'BUG: precommit-precision-warn writes a strictly-worse ratchet witness in a bare container'
status: completed
type: task
priority: normal
created_at: 2026-08-26T19:42:03Z
updated_at: 2026-08-26T20:02:20Z
---

## What happened

Committing an unrelated PR (`qou-0avp`, tools only — **no** `computations/`
script and **no** producer touched) left
`computations/witness-raw-float64-audit.witness.json` modified in the working
tree. The `PreToolUse` hook
[`scripts/precommit-precision-warn.sh`](../scripts/precommit-precision-warn.sh)
fires on any commit touching a witness — my PR added
`docs/audits/2026-08-26-borrowed-name-audit.witness.json`, which matches — and
runs `python3 computations/witness_raw_float64_audit.py --strict` (line 71).
That producer **writes its witness** as an ordinary side effect of running.

## Why the written numbers were WRONG, not merely churn

    dirty_witnesses                     1277 -> 1279   (+2)
    drained_files                        893 ->  884   (-9)
    ephemeral_duration_carved_out_fields  42 ->    0
    ephemeral_duration_field_names    5 names -> []

`_ephemeral_timing_fields()` imports `_EPHEMERAL_META_FIELDS` from
`qou_substrate.witness`. **`qou_substrate` is not importable in a bare
container** (confirmed: `ModuleNotFoundError`; it is not on PyPI — AGENTS.md
records all four in-tree packages as unpublished). The producer's `except`
branch then returns `frozenset()`, and its comment says exactly why:

> Never let provenance-import failure silently widen the gate: an empty set
> carves out nothing, so the audit stays STRICTER, not looser.

**That fail-safe is correct and should not be changed.** Failing strict is the
right direction for a gate. The defect is downstream: the strict-degraded
result is then *written to a tracked file*.

## Why this is worth fixing rather than shrugging at

1. **It only misfires in a bare container — which AGENTS.md calls the
   DEFAULT** (*"a bare container is the default here — mpmath/numpy/scipy are
   routinely absent on a fresh clone"*). Where `qou_substrate` imports, the
   rewrite is byte-identical and the tree never goes dirty. So the failure is
   invisible exactly to whoever has a working environment.
2. **The direction is the dangerous one.** It makes `dirty_witnesses` GROW and
   `drained_files` SHRINK. AGENTS.md: *"baselines drain, never grow."* An agent
   with a commit-everything reflex — or one obeying a stop-hook that says
   "there are uncommitted changes, please commit and push" — pushes a fake
   9-file drain reversal into the ratchet other agents read as live.
3. **A warn-only hook should not mutate tracked files at all.** AGENTS.md
   documents three deliberate properties of this hook (warns never blocks; runs
   the ratchet only, not the 3-minute family; is not a substitute for the
   preflight). "Leaves the tree dirty" is not among them and reads as
   unintended.

## Options (not chosen here — this bean is the report)

- Run the audit in a **read-only / `--no-write`** mode from the hook, so it can
  report NEW-dirty without emitting the witness. Needs such a flag to exist.
- Have the producer **refuse to write** when the provenance import failed,
  rather than writing strict-degraded numbers — i.e. extend the existing
  fail-safe from "compute stricter" to "compute stricter, do not persist".
- Have the hook `git checkout --` the witness afterwards. Cheapest, but hides
  the underlying write and would clobber a genuine concurrent edit.

Second option looks right, since it fixes every caller rather than one hook,
but it is a change to a precision producer and wants the owner's eye.

## What I did

Reverted the file; committed nothing. My PR #5856 is tools-only and this file
is not its content.



## FIXED 2026-08-26 — option 2 (producer refuses to persist)

`computations/witness_raw_float64_audit.py` now records
`EPHEMERAL_PROVENANCE_OK` and, when the import failed, prints a loud stderr
notice naming cause and remedy and returns **without writing the witness**.
The exit code is computed by the same expression as the write path, so the
**gate is unchanged** — and the empty-carve-out fail-safe itself is
deliberately untouched, because failing strict is right for a gate.

Verified both directions: without `qou_substrate` the tree stays clean and
the gate still runs; with `pip install -e tools/qou-substrate` the witness is
written with the carve-out restored (42 fields, drained_files 893).

Separately committed a legitimate drain the correct run revealed:
`dirty_witnesses 1277 -> 1275`, `total_fields 211732 -> 211712`.
