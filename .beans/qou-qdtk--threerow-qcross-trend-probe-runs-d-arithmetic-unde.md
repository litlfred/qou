---
# qou-qdtk
title: threerow_qcross_trend_probe runs D arithmetic under a C narrative and prints 2.0 is not an integer
status: completed
type: task
priority: normal
created_at: 2026-08-25T11:50:30Z
updated_at: 2026-08-25T21:13:59Z
---

CONFIRMED 2026-08-25, measured. Audit:
docs/audits/2026-08-25-ylambda-threerow-frame-audit.md
Tool: computations/audits/ylambda_threerow_frame_audit.py

THE DEFECT. The probe's docstring, its `_D_wenzl`, its `U_STAR` and its
line-223 symbolic identity all describe convention **C**:

    Q^r = u^3/D(u),  D(u) = -u^6-u^4+u^3+u^2+1,  u* = 1.13068544546204,
    r(q0) = 2.5995

Its code calls `_wenzl_constants`, which on main returns convention **D**.
Measured side by side at q0:

    Q^r from the corpus (LIVE)             1.517953249818345896  = Q^2 => r = 2.0
    Q^r = u^3/D(u)  (the probe's own text) 1.720251751213844854       => r = 2.5995

WHAT IT PRINTS AS A RESULT.

  * `r(1.45) = 2.0  <- COMPLEX => OFF-BRANCH` -- prints 2.0 and labels it
    complex. Under D, Q^r = Q^2 is entire: no pole, so q* does not exist and
    the "real-level branch" is all of q > 0.
  * The level-integer ladder q_k (r(q_k) = k) prints r = 2.0 at EVERY rung,
    q_2 through q_10.
  * `r(q0) = 2.0 not in Z` -- FALSE as printed. Under C, r = 2.5995 not in Z
    was the real claim; under D it inverts.
  * Its headline object G_n(q) = sum_{ell(lambda)>=3} y_lambda * Delta_lambda
    is identically zero (max|y| on that stratum: 3.34e-43 at n=9, floor
    2.21e-34). The measured crossing list is IDENTICAL for every n from 3 to
    21 -- an n-dependent object does not give an n-independent answer; a
    bisect-on-sign-change over round-off does.

SCOPE: (a), about THIS PROBE. It does not refute the general-r mathematics the
probe describes -- the Q^r = u^3/D(u) family is a legitimate object -- it says
the probe is NOT COMPUTING IT. Two honest dispositions, and it cannot stay as
it is:

  1. Correct the narrative to D. The object becomes trivially zero and the
     probe's question dissolves; say so and retire it.
  2. Re-pin the arithmetic to the general-r family explicitly, and register the
     probe as an off-canon comparison in the trace-convention registry.

Whoever takes it should also re-read #4829 and the UNIT-2 sibling
(threerow_crossing_a_dependence_probe), since this probe issues a CORRECTION to
UNIT-2 about crossings "above q*" -- and q* does not exist under D, so that
correction is C-frame too.

NOT the same as qou-58w3 (he4-two-row-dominance pinning a C-era 866/1000) --
that is a separate instance of the same class, already open.
