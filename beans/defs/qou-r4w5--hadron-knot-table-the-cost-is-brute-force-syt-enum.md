---
# qou-r4w5
title: 'hadron_knot_table: the cost is brute-force SYT enumeration in hecke_core_legacy._count_syts_by_12_relation, and chi_lambda(sigma_1) has a closed form'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T06:51:25Z
updated_at: 2026-10-04T15:20:42Z
parent: qou-5vkl
---

Measured 2026-08-29 (PR #5962, item 6 of the q0 drain backlog). The backlog
said: do not sink a session into this producer; if you can cheaply establish
*why* it is slow, that is worth more than a completed run.

## Method — a stack sampler, not a profiler

`faulthandler.dump_traceback_later(25, repeat=True, exit=False)` over a 200 s
bounded run. Needs no completion, no instrumentation, and costs nothing. Worth
reusing on any producer AGENTS.md describes as "runs, does not finish".

*(First attempt failed on `sys.path` — `runpy.run_path` does not reproduce the
script's own sys.path setup, so `_path_bridge` was missing. It looked exactly
like a producer defect. Third instance this corpus has recorded of an
environment fault impersonating a finding; check the harness before the
subject.)*

## The result

Three A=1 atoms clear in ~25 s. Deuterium — the first bound atom — then runs
indefinitely, and **every sample sits inside
`hecke_core_legacy.unified_iterative_correction`**, reached from
`binding_energy:2334` <- `hadron_knot_table.compute_atom:180`:

| sample | innermost frame | route |
|---|---|---|
| 1 | `_count_syts_by_12_relation.fill` at **recursion depth 16** | `partition_character_sigma1:389` <- `_partition_table:436` <- `_ensure_ysn_attached:1167` <- `__iter__:488` <- `unified_iterative_correction:1364` |
| 2 | `_matmul_dim:1102` | `unified_iterative_correction:1506` |

## Why `fill` is the interesting one

`_count_syts_by_12_relation` **enumerates every standard Young tableau** of a
shape, one cell per recursion level, purely to bucket them by whether 1 and 2
share a row, a column, or neither. Depth 16 means shapes of >= 16 cells, and the
work is `Sum_lambda f^lambda` — the involution number, ~4.6e7 at n = 16.

And it is **arithmetic-free**: pure Python lists and integers. No mpf, no numpy.

**The closed form is already in the docstring** two lines above the call:

    chi_lambda(sigma_1) = q*n_row + (-q^-1)*n_col + h*n_mix_pairs

The three counts are what the enumeration computes by brute force. `n_row` and
`n_col` are classical hook-length quantities; nothing here requires listing the
tableaux.

## What is NOT claimed

That `fill` dominates the total. Three samples over 200 s of ONE atom is
evidence about where this atom spends its first minutes, not a profile, and
sample 2 landed in a dense matmul instead. Nothing here measures what a closed
form or a memo would buy. Someone should profile one bound atom properly before
optimising.

## Two corrections to the surrounding record

1. **It confirms and sharpens AGENTS.md.** That document names
   `unified_iterative_correction` reached via `binding_energy` as the site;
   these samples name the two calls inside it.
2. **No `scipy.sparse` anywhere in any stack.** The sparse dtype-object
   boundary bean `qou-q7lf` reported is not what this producer is doing — which
   matches AGENTS.md's own note that `qou-q7lf` is stale and the sparse site was
   fixed in `da645cf0f32` / `46dcfc62a57`.
