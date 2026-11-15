---
# qou-q4mj
title: 'raw-float64 REGRESSED on main: onepb-status-dashboard 5 -> 6 fields, from the set_compute_dps fix'
status: completed
type: task
priority: high
created_at: 2026-08-29T08:50:59Z
updated_at: 2026-08-29T10:25:55Z
---

Found 2026-08-29 while running scripts/precision-gates.sh as the pre-commit
preflight on branch claude/tower-gap-lean-and-infra-2026-08-29 (PR #5978). NOT
that branch's defect; recorded here because it is live on main and the ratchet
is now red on it.

WHAT. computations/witness_raw_float64_audit.py reports

    REGRESSED (count increased) : 1
    computations/onepb-status-dashboard.witness.json   5 -> 6

Reproducible: re-running the audit from a clean tree gives the same. The
committed computations/witness-raw-float64-audit.witness.json still said
`regressed: 0`, i.e. it was stale and was masking this. Refreshed in c50e5ae465
on the branch above, so the count is now visible.

CAUSE, checked rather than assumed. Commit 629e257818, "onepb dashboard:
set_compute_dps() -- mpmath was defaulting to dps=15", authored 2026-08-29
06:50 UTC by another session and already merged; `git merge-base
--is-ancestor 629e257818 origin/main` confirms it is on main. Its own message
says it was fixing a float64 reduction by adding `import mpmath as mp`, and that
this introduced a subtler problem. The regenerated dashboard witness carries one
more raw float64 field than the previous one. `onepb-status-dashboard.witness.json`
is clean in the working tree, so the extra float is in the COMMITTED file.

Same event, other counters that moved in the audit:
    total_fields                127,045 -> 127,046   (+1, this field)
    lp_dual_carved_out_fields       427 -> 394       (-33, that file leaving the map)

FIX AT THE PRODUCER. Per AGENTS.md, "Never make a red run green by widening a
baseline" -- do NOT add the file to raw-float64-baseline.json and do NOT
--rebaseline. The single new float64 field needs finding in the dashboard
producer and carrying as mpmath.mpf, serialized via _precision.fmt. It is one
field, so this should be small.

NOT A FINDING about the causing commit's own subject: raising dps from the
mpmath default of 15 was correct and is not in question. This is a leftover
serialization site the dps fix exposed.


CLOSED 2026-08-29. Fixed on main. Re-running computations/witness_raw_float64_audit.py
against the merged tree at origin/main f8612ad245..dbdf919a15 reports
REGRESSED (count increased): 0, and onepb-status-dashboard.witness.json no longer
appears in the regression list. Not fixed by this branch -- this bean existed to
make sure the red was owned rather than baselined away, and it was owned.
