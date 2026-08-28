---
# qou-4un2
title: 'q0 migration DROPS witness provenance: 17 of 122 lost scriptFile/commitSha, and the audit is blind to it by construction'
status: todo
type: bug
priority: normal
created_at: 2026-08-28T14:08:26Z
updated_at: 2026-08-28T14:09:00Z
---

## Measured 2026-08-28, on origin/main at cdbdc84af1

The `migrate(q0) batch*` sweep (bean `qou-1c4y`, still **in-progress**) regenerates
witnesses through producers that do not emit provenance. Those producers write a
witness WITHOUT the top-level fields, so the regeneration DELETES them.

Method: for each of the 9 `migrate(q0) batch*` commits, diff every modified
`*.witness.json` between `sha~1` and `sha`, and record keys present before and
absent after.

    9 migration batch commits
    122 witness files modified
    17 lost at least one provenance field
    per-field: scriptFile 17, commitSha 17, engine 16, auditOnly 15

Worked case — `sublemma-2-1-alpha-shift-extract.witness.json`:

    c3a7e16856  present: auditOnly, commitSha, engine, scriptFile
    3563e08910  present: NONE          <- migrate(q0) batch 4
    253e2ffaf5  present: NONE          <- still gone on main today

I found this on 2026-08-23 while regression-testing #5517: a fresh run of that
producer dropped exactly those four fields, so I DECLINED to commit the
regeneration. The migration sweep committed it five days later.

## Why no gate caught it

`computations/witness_provenance_attribution_audit.py`, line 12, in its own words:

  > "no `scriptFile` at all are invisible to the method, because there is
  >  nothing to [attribute]"

The gate reports "N witnesses carry a scriptFile claim" — a count over the
witnesses that HAVE one. Deleting the field removes the witness from the
denominator rather than failing anything. A provenance regression is therefore
structurally unobservable to the check meant to police provenance: the metric
is a numerator with no fixed denominator.

## Scope caveat — do NOT quote the aggregate as the loss

Witnesses lacking `scriptFile` went 463 -> 505 across the same window, but the
corpus grew 3060 -> 3170 in it, so most of that +42 is new witnesses that never
had the field. **17 is the defensible number** (per-file before/after); 42 is not.

## Second, separate defect this exposes

These are AGENTS.md "bare producers": the provenance on disk was added
downstream, so re-running one destroys it. That is already recorded as a hazard
in the idle-pass witness policy. What is new here is that a *bulk sweep* is now
executing that hazard at scale, unattended, and `qou-1c4y` has more batches to
run.

## Next honest step (ordered)

1. **Stop the bleed.** Make the migration refuse to write a witness that would
   drop a provenance key present in the committed version. Cheap, and it is the
   only step that must land before the next batch.
2. **Fix the gate.** Make `witness_provenance_attribution_audit` ratchet the
   COUNT of provenance-less witnesses rather than only auditing those that have
   it, so a deletion is a red rather than a smaller denominator.
3. **Restore the 17.** Their prior values are in git; a restore is a JSON merge,
   not a producer re-run (re-running is what deleted them).
4. **Fix the bare producers** so a future re-run emits provenance itself.

Steps 1 and 2 are small and independent of the science. Step 3 is mechanical.
Step 4 is per-producer and is the real fix.
