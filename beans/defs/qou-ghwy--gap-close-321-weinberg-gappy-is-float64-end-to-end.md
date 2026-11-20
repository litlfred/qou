---
# qou-ghwy
title: 'GAP: close_321_weinberg_gap.py is float64 end to end (sympy → np.complex128 → eigvals) under a witness declaring compute_dps 70; no precision gate covers the sympy→numpy route'
status: todo
pr: 8211
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-09-03T05:01:07Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-20sx
---

Measured 2026-09-03 (session qou-ggdk). computations/close_321_weinberg_gap.py lines 101, 247-259, 284-285, 309-314, 612-699: exact sympy Hecke matrices cast to np.complex128 and eigen-decomposed; every emitted scalar float(); bare sum() over floats; det_product fields -0.9999999999999998 etc. are the float64 floor of exact ±1. Witness close-321-weinberg-gap.witness.json advertises engine: sympy, precisionMetadata.compute_dps: 70, output_dps: 60 — none true of the numerics; 127 raw-float64 fields (largest in the row); description string 1.0223944 vs computed residual_target 1.022385744453899. mpf_mixed_arithmetic_audit and numpy_mpmath_dtype_leak_audit are green because the producer never imports mpmath — a 27th row for the detector-blindness taxonomy. Verdict path_c_status = inconclusive is unaffected (thresholds 1e-3/1e-2). Fix at the producer: mpmath eigen/determinant at declared dps, mp.nstr serialization; then the witness's precisionMetadata becomes true. Do NOT quote any digit past ~13 from the current witness. Tower status: ORDER-ZERO-ONLY (pure-pattern trace ratio).

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress (2026-11-16, PR #8211)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ElectroweakWeinbergTraceLeptonFiltrationHiggsAndVevScale.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`8ca6e00d291446c4a5427c3266d272e793c16d8e`, `scriptHash: f6006da25e32`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8211`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8211, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
