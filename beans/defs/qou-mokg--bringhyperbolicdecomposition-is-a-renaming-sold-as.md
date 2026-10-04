---
# qou-mokg
title: BringHyperbolicDecomposition is a renaming sold as a decomposition — identical field to BringZeroModeBlochClass, and its docstring promises three things the field does not encode
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:22:51Z
updated_at: 2026-10-04T15:16:45Z
parent: qou-r9ih
---

MEASURED 2026-09-04 during the qou-08zf Lean gap assessment.

`predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.lean:150` proves
`BringZeroModeBlochClass` from `BringHyperbolicDecomposition` by

    bring_zero_mode_realised := hD.bw_sum_realised

The two classes carry the IDENTICAL field, so the "conditional theorem" is a
pure projection -- §3b-cond rule 5's degenerate shape.

NOT LAUNDERED, and the distinction matters: it is a `theorem`, not an
`instance`, so nothing auto-fires and no downstream conditional is silently
discharged. This is a naming/exposition defect, not a soundness one.

Two things to fix:

1. The docstring promises a knot MULTI-SET, MULTIPLICITIES and a NORMALISATION
   that the single field does not encode -- the `proof-claims-unencoded`
   criterion (severity major) in the vacuity audit.
2. It describes the field as `exists z, z = 2/(3*pi)` -- the CLOSED pre-Phase-2
   loophole form, not the live one. So the docstring documents a state the
   corpus moved past.

Either encode what the docstring promises, or say plainly that the class is a
named alias for the one field it carries and let the theorem read as the
projection it is.
