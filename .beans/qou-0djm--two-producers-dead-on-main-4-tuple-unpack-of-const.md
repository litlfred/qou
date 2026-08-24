---
# qou-0djm
title: 'Two producers dead on main: 4-tuple unpack of _constants(), which returns 3'
status: todo
type: task
created_at: 2026-08-24T11:29:04Z
updated_at: 2026-08-24T11:29:04Z
---

Found while sweeping the 19 `_ame_table()` consumers (qou-ex8k). PRE-EXISTING
on main, unrelated to that change.

    computations/delta_lambda_shape_probe.py:80
        me, q0, E0, g8 = _constants()
    computations/probe_collective_binding_residual.py:79
        me, q0, alpha, g8 = _constants()

Both import `_constants` from mass_binding_dashboard, which ends

    return float(mex), float(q0x), float(e0x)        # me, q0, E0

Three values. Both crash on the FIRST line of main() with
`ValueError: not enough values to unpack (expected 4, got 3)`.

`_constants()` has returned three values at every commit going back to at
least 2026-08-08 (checked twelve commits of mass_binding_dashboard.py), so
these two have been dead for over two weeks. Their committed witnesses are
frozen at whatever the last working version produced, and no drain or
regeneration can touch them.

WATCH OUT -- a near-identical line is NOT a defect:
    computations/binding_single_pipeline_comparison.py:242
        me, q0, E0, g8 = _constants()
That file defines its OWN `_constants()` at line 118 returning four values.
It runs clean (rc=0) and writes its witness. I only established that by
running it; a grep for the unpack pattern flags all three identically.

WHAT THE FIX NEEDS TO DECIDE
Whether the fourth value (`g8` / `alpha`) was ever real. Both callers name it
differently -- `E0, g8` vs `alpha, g8` -- which suggests they were written
against different APIs, or against the local 4-tuple version in
binding_single_pipeline_comparison and then had the import swapped. Resolving
that is a judgement about what these probes are meant to compute, not a
mechanical repair, which is why it is a bean and not a patch.
