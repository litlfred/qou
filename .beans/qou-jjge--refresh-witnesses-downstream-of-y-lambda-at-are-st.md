---
# qou-jjge
title: 'REFRESH: witnesses downstream of y_lambda_at are stale in their last ~20 digits after the 30->50 cap raise'
status: todo
type: task
priority: normal
created_at: 2026-08-24T12:50:17Z
updated_at: 2026-08-24T12:50:52Z
---

Opened by PR #5641, which raised the `y_lambda_at` output cap from 30 to 50
digits (`computations/wedderburn_jones_markov.py`, bean `qou-840k` item 4).

## What is stale

Every committed witness whose value passes through `y_lambda_at` — ~155
consumers. The staleness is confined to digits ~31-50; digits 1-30 are
unchanged, so nothing is WRONG, it is under-precise and now knowably so.

MEASURED effect on the Markov normalisation `Σ y_λ f^λ = 1` at the proton q₀:

    n   capped at 30   after
    4   1.0e-30        2.673e-51
    5   5.0e-31        1.069e-50
    6   1.0e-31        1.336e-51

## Why this was NOT done in #5641

A two-token precision fix must not carry a ~155-producer regeneration as a
side effect. Prior lesson in this corpus, the hard way: a sweep run "with no
side effects" rewrote 29 witnesses and turned the raw-float64 ratchet red —
**a producer IS its side effect here**, and producers write SIBLING witnesses
beyond the one being targeted.

## Doing it properly

1. Enumerate the true consumer set from the import cone of `y_lambda_at`,
   not by grepping the name (module-alias reads are invisible to a name grep).
2. Baseline each witness from **git** (`git show origin/main:<witness>`),
   never from the working tree the sweep is mutating — that contamination
   produced two false MOVED verdicts in a previous measurement pass.
3. Mask volatile provenance (`timestamp`, `elapsed_seconds`, `measured_at`,
   `start_time_monotonic`, the `/invocation/*` block) or you measure the
   harness, not the mathematics.
4. Record WHICH fields moved, so a mask gap is re-classifiable from the
   checkpoint instead of costing another full sweep.
5. Restore the whole `computations/` tree between producers.
6. Expect ~16% of producers not to complete at all (14 crash / 10 timeout at
   240s on the last full measurement) — those are their own backlog, not
   part of this refresh.

## Related

- `qou-840k` — the parent float64-excision bean; items 3, 5, 6 still open.
  Item 3 (rewire `global_wedderburn_sum_q_hecke_seminormal` onto
  `_build_seminormal_matrices_mpf`) is the next-largest precision win and
  carries precise edit notes there.
- `qou-840k` item 6 names the corpus sites claiming "1e-50" for tr_M. Those
  claims were FALSE while the cap read 30 and are TRUE as of #5641, so that
  item's premise has inverted — the sites may now be correct as written.
  Re-check before editing them.
