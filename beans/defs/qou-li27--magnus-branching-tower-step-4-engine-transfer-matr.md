---
# qou-li27
title: Magnus branching-tower step-4 engine (transfer-matrix contraction on mpfr)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T17:41:57Z
updated_at: 2026-11-17T11:58:00Z
parent: qou-v2om
---

Tower steps 1-3 validated + merged (#6183): branching H_n->H_{n-1} faithful, bond p(3(A-1)) sub-exp, germ/link locality O(1), sigma_g & A_g single-level-local MPOs. Step 4 = the doubled-Bratteli weighted-trace contraction Sigma_lambda y_lambda tr(rho_lambda Omega2_lambda) over the shape-bond, gated vs flat-sparse A=3/A=4. Build on gmpy2.mpfr (#6273, 3.8x) and bake in S_Z x S_N / S3 block symmetries (identical nucleon tensors computed once). This is what reaches A>>4.

## Round 89 Progress (`litlfred/qou#8334`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/QuantumIntegerRatioAndLevelTwoStokesBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/quantum_integer_ratio_and_level_two_stokes_brick_probe.py` & `computations/probes/quantum-integer-ratio-and-level-two-stokes-brick.witness.json` (`scriptCommitSha = 4d6630423af48b31069a83d2407a32bd592eec79`, HEAD `c9d68807b57ef2cf531ca6340ce9802c12bf8d5d`, `allPassed = true`).
