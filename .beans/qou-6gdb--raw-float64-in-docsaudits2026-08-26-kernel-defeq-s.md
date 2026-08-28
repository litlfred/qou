---
# qou-6gdb
title: raw-float64 in docs/audits/2026-08-26-kernel-defeq-sample.witness.json (2 coverage pcts) — takes the audits-tree ratchet red; not my domain
status: todo
type: task
priority: normal
created_at: 2026-08-28T15:50:41Z
updated_at: 2026-08-28T15:51:25Z
---

## What and where

`docs/audits/2026-08-26-kernel-defeq-sample.witness.json` carries two raw
float64 fields:

    /coverage/coverage_of_tree_pct           = 2.3
    /coverage/coverage_of_olean_reachable_pct = 2.5

This is the single NEW-dirty entry taking the **audits-tree raw-float64**
gate red (`witnesses carrying raw float64: 33`, baseline 32). Surfaced by
running `scripts/precision-gates.sh --changed` as the mandated preflight on
an unrelated PR.

## Ownership, and why I did not fix it

Landed with the `qou-0avp` olean-coverage arc (`cdbdc84af` /
`f991249ee`), 2026-08-26. Not my domain -- the HOMFLY branch that found it
touches nothing in that cone. Fixing it means editing that producer, and
**the witness does not record `scriptFile`**, so the producer would have to
be identified first (a second, smaller defect worth fixing at the same time).

## Assessment, stated plainly

Benign in effect: both values are coverage *percentages* -- ratios of olean
counts reported to one decimal -- not physics quantities, and nothing
downstream re-derives them. But the gate is a **ratchet**, and the discipline
is explicit that a baseline drains and never grows. So this should be fixed
at the producer (`mpmath.mpf` from the source, serialize with
`_precision.fmt`), NOT baselined.

Cheap, once the producer is located.
