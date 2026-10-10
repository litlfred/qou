---
# qou-ghwy
title: 'GAP: close_321_weinberg_gap.py is float64 end to end (sympy → np.complex128 → eigvals) under a witness declaring compute_dps 70; no precision gate covers the sympy→numpy route'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-09-03T05:01:07Z
updated_at: 2026-10-10T07:16:01Z
parent: qou-8lxd
---

Measured 2026-09-03 (session qou-ggdk). computations/close_321_weinberg_gap.py lines 101, 247-259, 284-285, 309-314, 612-699: exact sympy Hecke matrices cast to np.complex128 and eigen-decomposed; every emitted scalar float(); bare sum() over floats; det_product fields -0.9999999999999998 etc. are the float64 floor of exact ±1. Witness close-321-weinberg-gap.witness.json advertises engine: sympy, precisionMetadata.compute_dps: 70, output_dps: 60 — none true of the numerics; 127 raw-float64 fields (largest in the row); description string 1.0223944 vs computed residual_target 1.022385744453899. mpf_mixed_arithmetic_audit and numpy_mpmath_dtype_leak_audit are green because the producer never imports mpmath — a 27th row for the detector-blindness taxonomy. Verdict path_c_status = inconclusive is unaffected (thresholds 1e-3/1e-2). Fix at the producer: mpmath eigen/determinant at declared dps, mp.nstr serialization; then the witness's precisionMetadata becomes true. Do NOT quote any digit past ~13 from the current witness. Tower status: ORDER-ZERO-ONLY (pure-pattern trace ratio).
