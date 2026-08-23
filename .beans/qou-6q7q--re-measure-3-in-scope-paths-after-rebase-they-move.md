---
# qou-6q7q
title: 'Re-measure 3 in-scope paths after rebase: they moved on main while the sweep ran'
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:37:53Z
updated_at: 2026-08-23T13:38:20Z
---

## The claim that needs qualifying

PR #5519 says its verdicts are measured **on main**. The branch is behind
main, so that is true of the tree the sweep ran against, not of main today.
Measured rather than assumed: of the **111** in-scope paths (55 producers +
their witnesses), **108 are byte-identical to current `origin/main`** and their
verdicts transfer unchanged. **3 do not:**

| path | kind | moved on main by |
|---|---|---|
| `computations/audits/q0-anchor-consistency-audit.witness.json` | witness | `59b27bfc6d` |
| `computations/probes/binding_qgaussian_ell1_ceiling_measurement.py` | **producer** | `bc96793e5d` |
| `computations/probes/flavor_split_alpha_bond_dilog_probe.py` | **producer** | `bc96793e5d` |

This branch has **zero** commits touching any of the three — all three moved
under it.

## Why the two producers matter more than the count suggests

`bc96793e5d` is *"q0 literals: migrate the 5 unblocked sites"* — it changes
where those producers read q₀ from. That is exactly the class of change that
can move a staleness verdict, so these are not incidental drift: an
`UNCHANGED` measured against the pre-migration producer says nothing about the
migrated one.

## The cheap fix, enabled by the checkpointing

Do **not** rebase mid-sweep — it invalidates the run in flight. After the sweep
completes: rebase, delete just these three producers' entries from
`docs/audits/2026-08-23-q0-muon-staleness-sweep.json`, and re-run with
`--resume`. The other 52 are skipped, so re-measurement costs only what those
producers cost. Selective re-measurement is free precisely because verdicts are
now per-producer records rather than one end-of-run dump.

## Standing hazard

Main moves during a multi-hour sweep. Any verdict file should record the commit
it was measured at, so this comparison is mechanical next time rather than
reconstructed by hand. Related to `qou-cdjd` (the run records nothing about
what it ran against — there, the environment; here, the tree).
