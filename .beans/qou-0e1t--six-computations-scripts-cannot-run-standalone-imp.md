---
# qou-0e1t
title: 'Six computations/ scripts cannot run standalone: import _path_bridge precedes the sys.path bootstrap that resolves it'
status: completed
type: task
priority: normal
created_at: 2026-08-29T01:24:53Z
updated_at: 2026-08-29T01:25:32Z
---

## What was broken

`_path_bridge` lives in `computations/`. A script in a cluster subdirectory has
`sys.path[0]` set to its OWN directory, so `import _path_bridge` resolves only
if something already put `computations/` on the path. Six scripts import it
BEFORE that bootstrap (one had it two lines later; one had no `sys.path` setup
at all), so they raise `ModuleNotFoundError` and cannot be run.

    computations/deltalambda/carrier_table_convention_d_rederivation.py
    computations/meson/meson_braid_syllable_bound_probe.py
    computations/probes/np_splitting_residual_probe.py
    computations/qbeta/qbeta_d_frame_trace_baseline_probe.py
    computations/qbeta/qbeta_epsnpq_functional_mismatch_probe.py
    computations/qbeta/qbeta_ladder_convention_fee_probe.py

Plus `qbeta_delta_element_fork_pricing_probe.py` on the cds1 branch, which is
where this was found (fixed there, PR #5897).

**Why it went unnoticed: the failure is silent in normal agent use.** A caller
that has already set `PYTHONPATH`, or that imports rather than executes, masks
it completely. The fork-pricing probe's recorded "15/15" was obtained exactly
that way.

`qbeta_d_frame_trace_baseline_probe.py` matters most: its
`gap_over_ladder_ratio = 92.1058` is what the fork-pricing probe calibrates
against, and it could not be re-run to check.

## The committed witnesses were never wrong

All five that emit one reproduce with **no numeric value moved** — only
`environment` fields (mpmath 1.3.0 -> 1.4.1, added scipy/clarabel/numpy/sympy).
So this is a *runnability* defect, not a correctness one. Witnesses restored
rather than committed, keeping the diff to six one-hunk source changes.

## 28 -> 6: the count was wrong first, and by the usual mechanism

The first scan matched only `sys.path.insert(` and reported **28**. Sampling
three by hand: all three ran fine — they bootstrap with `sys.path[:0] = [...]`,
a spelling the regex did not know. **22 false positives from one missing
spelling**, the detector-blindness class in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`. True count 6, each
confirmed by EXECUTING it.

## Guard added

`computations/audits/path_bridge_bootstrap_audit.py` — patterns only to
*narrow to candidates*, then **runs each one** and judges on whether the
interpreter really raises. Strips `PYTHONPATH` first, since that inheritance is
the masking bug itself. Self-tested: revert one file -> exit 1 naming it;
restore -> exit 0. It is not reporting clean vacuously.
