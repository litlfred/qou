---
# qou-q7lf
title: 'hadron_knot_table crashes: mpmath dtype=object reaches scipy.sparse (qou-5qwb class)'
status: todo
type: task
created_at: 2026-08-23T08:10:16Z
updated_at: 2026-08-23T08:10:16Z
---

Found while sampling the convention-C witness backlog (`qou-z11r`, PR #5510).
`computations/hadron_knot_table.py` does not run to completion on main.

## Two failures, in order

1. `ModuleNotFoundError: No module named 'scipy'` -- environment only. Per
   AGENTS.md ("if this container is simply missing a library, install it and
   re-run rather than committing the weaker record") I installed scipy 1.17.1
   rather than accepting it. That revealed the real one:

2. ```
   File ".../scipy/sparse/_sputils.py", line 56, in upcast
     raise TypeError(f'no supported conversion for types: {args!r}')
   TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))
   ```
   via `hecke_core_legacy._build_ysn_matrices` -> `csr_matrix`.

## Why this is the qou-5qwb class, not a scipy problem

`dtype('O')` is numpy's object dtype, which is what an **mpmath value** becomes
when it lands in an ndarray. This is the same promotion that cost a 4000x
slowdown in `hoefsmit_numpy` (`qou-5qwb`) and that makes flipping
`q_parameter.Q` to `mpf` unsafe -- documented in #5453 §3. Here it does not
merely deoptimise; scipy.sparse refuses the mixed float64/object pair outright,
so the producer aborts and writes nothing.

So an `mpf` is reaching `_build_ysn_matrices` where a float is expected. The
fix is at that boundary -- carry the value as float into the sparse
constructor, or keep the YSN build entirely in mpmath and off scipy.sparse --
not by widening anything.

## Consequence for the C->D triage

`hadron-knot-table.witness.json` carries z_C and CANNOT be re-run to find out
whether that is stale output or a live C producer, so it stays unclassified in
`qou-z11r`. Any other producer in that 58 whose YSN path goes through
`hecke_core_legacy` is likely blocked the same way -- worth checking before
budgeting the sweep, since a "just re-run the producer" plan silently does not
apply to them.

Not fixed in #5510: out of that PR's scope (its subject is the q0 pin on
`atom_per_generator_volumes_mpfr` and the per-interface probe naming).
