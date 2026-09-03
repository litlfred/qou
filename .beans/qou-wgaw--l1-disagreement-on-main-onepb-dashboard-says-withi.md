---
# qou-wgaw
title: 'L1 disagreement on main: onepb dashboard says within_1ppb True, cross-check says False 6/6'
status: todo
type: task
priority: normal
created_at: 2026-08-29T04:23:18Z
updated_at: 2026-08-29T06:37:14Z
---

Measured on origin/main, read-only, 2026-08-29.

Two committed witnesses disagree about whether the trace cross-check is within
1 ppb:

  computations/onepb-status-dashboard.witness.json
    data/summary/markov_trace_consistency/all_within_1ppb = TRUE

  computations/cross-check-trM-1ppb.witness.json   (q0Anchor: muon)
    within_1ppb = FALSE on 6 of 6 entries
    within_peel_tolerance = FALSE as well

This matters because AGENTS.md sends agents to the FIRST of these for L1
status ('Where to check status: L1: computations/onepb-status-dashboard.
witness.json') and documents the L1 leg as MET. The dedicated cross-check
producer disagrees.

NOT YET ESTABLISHED, and this is the honest limit of the finding:

  - Whether the two fields measure the SAME quantity. The dashboard's field
    sits under markov_trace_consistency and may be a method-vs-method
    agreement check, while cross-check-trM-1ppb is per-atom against a peel
    reference. They could both be correct about different things.
  - Which one is stale. cross-check-trM-1ppb is muon-stamped and refuses a
    proton run by design ('L1 cross-check must run under the MUON q0 pin'),
    so it is NOT simply an unmigrated witness.
  - Whether the drain on PR #5950 changes either. Both readings above are
    from origin/main, taken BEFORE that branch merges.

Separately: both fields are named '1ppb' while AGENTS.md states the L1 target
was upgraded from 1 ppb to 1 ppQ (1e-15) on 2026-05-26. So the field names are
stale against the stated goal regardless of which verdict is right, and a
reader checking 'is L1 met' against a field named for the superseded threshold
is not measuring the current target either way.

Surfaced by the qou-3f7a drain agent, which reported all_atoms_within_1ppQ was
already False on main; the above is an independent re-measurement that
confirms a disagreement exists but scopes it differently from that report.


---

## SETTLED 2026-08-29 (PR #5962) — same quantity, and the dashboard is wrong TWICE

This bean's stated open question was *whether the two fields measure the same
quantity*. They do, and it is not a close call.

`onepb_status_dashboard.py:143-172` reads
`cross-check-trM-1ppb.witness.json` and reduces over its own `data.deltas`.
It is not a method-vs-method check standing beside the per-atom one — it is a
**projection of the very witness that reports False**. One source, one of the
two readings wrong.

### Defect 1 — a key-miss, and this is the one that matters

    "max_rel_delta": max((float(d.get("rel_delta", 0)) for d in ...), default=0.0)

**No delta entry has ever carried `rel_delta`.** Measured, the keys present are
`rel_delta_max`, `peel_rel_delta`, `exact_method_rel_delta`,
`pairwise_rel_deltas`. So `.get(..., 0)` returned 0 for all six atoms and
`max_rel_delta` was `0.0` **by key-miss, not by measurement**.

That field feeds the **gating** assertion `markov_trace_max_rel_delta`
(expected 0.0, tolerance 1e-9). So the L1 Markov-trace gate **could not fail**,
whatever the cross-check found. AGENTS.md sends agents to this witness for L1
status.

True value from the key that exists: **2.90663e-7** (helium-4) — 290x the
gate's own tolerance, on 6 of 6 atoms.

Staleness drains on a re-run; a key-miss does not. This one would have survived
every future regeneration.

### Defect 2 — staleness

`all_within_1ppb` and `any_diverge` are passed straight through and were simply
stale: dashboard computed 2026-07-20, cross-check 2026-08-29. Replaying the
reduction on today's source yields False for both.

### Result

    max_rel_delta    0.0   -> 2.90663064970691e-7
    any_diverge      False -> True
    all_within_1ppb  True  -> False
    allPassed        True  -> False

Tolerance UNCHANGED at 1e-9. No baseline widened.

### On the naming — the bean was right and it is now actionable

Both fields are named `1ppb` while L1's target has been **1 ppQ (1e-15)** since
2026-05-26. The fix was mechanical because the source witness **already carries
`within_1ppQ`** (False on all 6). Added `all_within_1ppQ` plus an
`l1_target_note` saying which to quote; `*_1ppb` kept for consumer
compatibility. Also recorded `max_rel_delta_source_key` so a future key rename
surfaces as a changed field instead of silently reading 0.0 again.

### Method note

The decisive step was not reading the code — it was **replaying the dashboard's
exact reduction against today's source witness**. That separates "stale" from
"structurally wrong" in one command, and the two defects here are one of each.
