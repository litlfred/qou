---
# qou-epy2
title: 'L4-5: Gaussian sum -> integral cell comparison'
status: in-progress
pr: 8212
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:36:11Z
updated_at: 2026-10-04T15:21:06Z
parent: qou-r9ih
---

RE-SCOPED 2026-08-19 -- this brick is a Gaussian sum/integral CELL COMPARISON,
which is exactly what QOU/MathlibExt/GaussianSumBound (integral_exp_neg_mul_sq_le,
sum_exp_neg_mul_sq_le) and CorrectedTrapezoid / CompositeEulerMaclaurin already
provide generically.  Grep before writing.  Audit:
docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md


## Progress Update (2026-11-16T21:42:42Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/extended-bloch-flattening-and-gaussian-cell.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8212 (`6f86defb7b9ef2d83e38ac9d5dd375a7109fbabd`); keeping `status: in-progress` until PR merges.
