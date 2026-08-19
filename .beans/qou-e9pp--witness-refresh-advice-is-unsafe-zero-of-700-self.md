---
# qou-e9pp
title: 'Witness-refresh advice is unsafe: ZERO of ~700 self-stale witnesses are safe to re-run'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T13:15:18Z
updated_at: 2026-08-19T13:15:50Z
---


## What was measured

`computations/witness_staleness_triage.py` (PR #5002) normalises both producer
versions through `ast.unparse` and reports which self-stale drifts can move a
number. Three runs, 1564 commits of `main` apart, corpus 2898 -> 2985:

    2026-08-11   substantive 242   rewritten 329   unresolvable 107   cosmetic 0
    2026-08-19   substantive 239   rewritten 329   unresolvable 106   cosmetic 0
    2026-08-19   substantive 256   rewritten 338   unresolvable 103   cosmetic 0

`cosmetic` (= safe to refresh) is 0 every time. Source-identical is necessary
but not sufficient; the two extra gates are environment match and whether the
producer emits provenance at all.

## Status: the measurement is done; two follow-ups are NOT

1. **`rewritten` is ~48% of the backlog and has no branch-side fix.** The
   recorded `commitSha` resolves to nothing because rebase-merge rewrites it.
   `main` spent 13 commits in one 8-day window hand-patching the field, which
   buys only the interval until the next merge. A durable fix has to run
   post-merge on `main`, or the field has to stop being treated as decidable.
   Not attempted here.
2. **The `substantive` queue (256) is untriaged.** This script says which drifts
   *can* move a number; it does not say which *did*. That needs the runner
   (`witness_producer_executes_audit.py`, already on `main` via #4960 -- its
   ENV_MISSING / DIFFERS buckets are the run-time complement to this script's
   static env gate), and it needs a container with `scipy` / `pyhecke_native` /
   `clarabel` present, which this one does not have.

## Do not

Do not drain `substantive` by re-running producers in an under-provisioned
container. Measured cost: `binding_canonical.py` without `pyhecke_native` moves
`tr_M_atom` 0.388 -> 0.575 (48%) with no crash and no warning.
