---
# qou-7e1t
title: 'low_isotope_mass_table clobbers its own canonical upstream: default re-runs it at target-dps 11 over a committed 60-dps table'
status: todo
type: bug
priority: normal
created_at: 2026-08-22T15:29:23Z
updated_at: 2026-08-22T15:30:45Z
---

## What

`computations/low_isotope_mass_table.py` describes itself as a "thin
projection" of `canonical-mass-table-extended.witness.json`. It is not
only that: **by default it re-runs the canonical producer first**, as a
subprocess, with its own arguments —

    if not args.no_rerun_canonical:
        run_canonical(args.method, args.target_dps)

    parser.add_argument("--target-dps", type=int, default=11)
    parser.add_argument("--method", ... default "auto")

— and those defaults are NARROWER than the committed canonical artifact.
Measured by running it with defaults over the committed table:

| field | committed canonical | after the wrapper's default run |
|---|---|---|
| `parameters.target_dps` | **60** | **11** |
| `parameters.method` | `branching` | `auto` |
| `parameters.dps` | 0 | 50 |
| rows | 7 | 9 (`p`, `n` now compute) |

So running the LOW-ISOTOPE wrapper silently rewrites the CANONICAL
upstream table, dropping its target precision from 60 dps to 11. The
canonical witness is a different, coarser computation afterwards, and
nothing in the wrapper's output says a canonical artifact was replaced.

## Why it bites

This is the mechanism behind a narrowing I hit and reverted earlier in
this arc without identifying the cause (recorded then as "ran the extended
producer with the low-isotope atom list", 7 rows -> 5, 60 -> 11 dps). It is
not the atom list; it is the wrapper's own `--target-dps 11` default
reaching a producer whose committed output is 60.

Note the row count moves the OTHER way (7 -> 9): `--method auto` routes
`p`/`n` through the direct H_3 path, while the committed `branching` table
records them as ERROR rows. So the clobbered table is simultaneously
*wider* in coverage and *coarser* in precision than the committed one —
which is exactly why the damage is easy to miss by eyeballing a row count.

## Second, separate defect: the projection's upstream is stale

The committed `low-isotope-mass-table.witness.json` records

    derived_from.scriptHash:  b6c20f1b6e02
    derived_from.computedAt:  2026-08-15T21:36:25Z

while the canonical witness actually in the tree is `dfcd6d57966b`,
computed 2026-08-22. The projection describes a canonical witness that is
7 days old and no longer present. To its credit `derived_from` makes this
*detectable* — but nothing enforces it, and the two witnesses disagree on
their face: the projection carries `method: auto, target_dps: 11, 5 atoms`
against a committed canonical of `method: branching, target_dps: 60,
7 rows`. They cannot both describe the same computation.

Regenerating honestly with `--no-rerun-canonical` against the CURRENT
canonical yields **3 atoms**, not 5, because the current canonical has no
`p`/`n` rows. So the wrapper's two modes give materially different
witnesses, and the destructive one is the default.

## Lineage

`qou-5h7z` (completed) documented an earlier staleness in this same file —
pre-convention-D `tr_M` values and collapsed ctypes — and explicitly
declined to commit its regeneration. That bean's C->D deltas
(`2H 0.38828647 -> 0.57509096`) are the FIRST of three steps for the
deuteron; the colour-blind -> colour-weighted move landed on PR #5427 is
the third (`0.575090872 -> 0.575172244`). Different axis, same file.

## What was and was not done on PR #5427

**Done:** the anchor gap. `builder.save()` was called bare, so the emitted
witness carried `q0Anchor: null` / `q0Value: null` — it could not say which
layer its numbers belonged to, which is the enabling condition for the
cross-layer comparison retracted in `qou-4e5k`. It now inherits both from
the witness it projects (inherited, not read from `q_parameter`: this
producer computes nothing, and reading the live pin would declare the pin
this PROCESS imports rather than the pin the NUMBERS were computed at).

**Not done — deliberately:** the witness is not regenerated. Regenerating
correctly narrows it 5 -> 3 atoms, which is a visible loss that is really a
symptom of this bean, not of the anchor fix; and regenerating with defaults
would clobber the canonical table. The source fix is inert until someone
regenerates, which is the same posture used for the producer fixes earlier
in that PR.

## Next honest step

Decide what the wrapper should be. Candidates, roughly increasing cost:

1. **Make `--no-rerun-canonical` the default** and require an explicit flag
   to re-run. A projection should not have a destructive default.
2. **Refuse to re-run at settings coarser than the existing artifact** —
   compare `target_dps` and abort rather than downgrade.
3. **Reconcile method.** Decide whether the canonical table should be
   `auto` (covers `p`/`n`) or `branching` (errors on them), and make both
   producers agree, so a projection cannot be wider than its source.
