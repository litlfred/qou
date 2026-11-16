---
# qou-bmyx
title: 'ArgPrinciple: argument-principle scaffold for PI-3 (zero-counting via contour/residues) — the least-Analysis-blocked of the three walls'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T11:53:39Z
updated_at: 2026-11-16T19:05:00Z
parent: qou-rtxm
---


---
**Progress 2026-07-20 (reduction):** residue_logDeriv_eq_order reduced from a full sorry to ONE residual sorry (the global closed-disc factorization). 3 new sorry-free analytic bricks: logDeriv_zpow_sub_mul_split, inv_two_pi_I_mul_integral_nat_sub_center_inv, circleIntegral_logDeriv_eq_zero_of_analyticOnNhd. Residue-computation tail (split + integrate + cancel) is sorry-free. lean-direct exit 0 (3 intended sorries). Commit 63b97ba4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-20 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Full Sorry-Free Verification & Cleared-Denominator LogDeriv Order Split (PR #8157)
- Verified that `QOU.Mathlib.ArgumentPrinciple` (`residue_logDeriv_eq_order`, `argument_principle`, `entire_zero_count`) is 100% sorry-free on `main` via `MeromorphicOn.extract_zeros_poles`, and added the generic-ring cleared-denominator Leibniz logarithmic-derivative order decomposition `logDeriv_factor_cleared_identity` in `folio/quantum-observable-universe/lean/QOU/Foundations/FrobeniusHopfMarkovBridge.lean` (wired into `QOU.lean`, 0 `sorry`, generic `CommRingOps R` per §7c).
- PR: https://github.com/litlfred/qou/pull/8157 (commit `16f8c01498462170d1ad98f5b5426233d3feea7d`). Status kept `in-progress`.
