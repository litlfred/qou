---
# qou-yh08
title: 'Sub-canonical dps: 952 sites set precision below OUTPUT_DPS=60 after the 2026-05-31 bump'
status: todo
type: task
created_at: 2026-08-23T07:58:25Z
updated_at: 2026-08-23T07:58:25Z
---

`qou_substrate.precision` was bumped on 2026-05-31 (PR #1595) from 50->60 output
and 65->70 compute. Most call sites never followed.

A scan of the tree finds **952** explicit `mp.dps = N` / `workdps(N)` sites below
the canonical `OUTPUT_DPS = 60`:

    dps=50 : 610   (the old output value)
    dps=40 : 213
    dps=30 :  92
    other  :  37

against 447 sites at or above canonical, and only 145 files importing
`COMPUTE_DPS` / `OUTPUT_DPS` at all.

## Not the never-raises-dps defect

`never_raises_dps_audit.py` (blocking, `precision-gates.sh:60`) is green and
draining — 10 runnable producers left of a 46-file / 206-construction baseline,
36 files drained, 0 new, 0 regressed. Those sites never raise dps at all.

**These sites DO raise dps** — to a value that stopped being canonical. No
existing ratchet covers "raises dps, but below canonical". The three dps
ratchets (`import-time dps`, `never-raises-dps`, `float64-padding`) and
`module_const_precision_audit.py` all pass while these 952 stand.

## Why this is filed, not fixed

Raising precision changes every value the affected producers emit, so it needs a
witness-regeneration plan, and whether a given 50 is deliberate is an owner call.
Bulk-editing 952 sites blind would be the "widen a baseline to make a red run
green" move that `precision-gates.sh` explicitly warns against.

## Suggested shape

A ratchet in the same style as the others — count sites below `OUTPUT_DPS`,
baseline at today's 952, drain never grow — so the number is visible and cannot
regress while the decision is pending.

Found while fixing a hardcoded `60` in `tower_term_li2q` (bean qou-2tuv), which
was itself the wrong constant: 60 is the *serialization* precision; compute
wants `COMPUTE_DPS` = 70.
