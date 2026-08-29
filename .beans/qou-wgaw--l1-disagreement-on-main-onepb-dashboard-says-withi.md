---
# qou-wgaw
title: 'L1 disagreement on main: onepb dashboard says within_1ppb True, cross-check says False 6/6'
status: todo
type: task
priority: normal
created_at: 2026-08-29T04:23:18Z
updated_at: 2026-08-29T04:23:43Z
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
