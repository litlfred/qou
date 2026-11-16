---
# qou-adgd
title: 'GAP: ArchimedeanLimit on [-1,0), x=1 and x>1 (LiTwo is a tsum, so the class needs Re Li2 there)'
status: in-progress
pr: 8212
type: task
created_at: 2026-11-15T18:12:20Z
updated_at: 2026-11-15T18:12:20Z
parent: qou-r9ih
---

Issue #7942, PR #7946. ArchimedeanLimit is proved on (0,1) on main (DilogPartAConvergence.archimedeanLimit_Ioo). PR #7946 proves it FALSE for x < -1 (ArchimedeanLimitDomain.not_archimedeanLimit_of_lt_neg_one), because LiTwo is a tsum and is 0 when |x|>1 (not summable), while the q-product limit is not 0. Open: [-1,0) (the series converges; needs the alternating/Abel exchange), x=1 (zeta(2) boundary), and x>1 (statement must be restated with Re Li2 or an analytic continuation, not the tsum). No alpha_em Lean theorem takes ArchimedeanLimit as a hypothesis; it appears only in docstrings.


## Progress Update (2026-11-16T21:42:42Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/extended-bloch-flattening-and-gaussian-cell.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8212 (`6f86defb7b9ef2d83e38ac9d5dd375a7109fbabd`); keeping `status: in-progress` until PR merges.
