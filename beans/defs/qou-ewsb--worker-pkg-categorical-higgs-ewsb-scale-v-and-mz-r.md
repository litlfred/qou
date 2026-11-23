---
# qou-ewsb
title: 'SM/Eightfold Worker Pkg 3 (Q-Gap-9): Categorical Higgs Mechanism, EWSB Scale v_EW & m_H, and UV-to-M_Z RG Thresholds (sin^2 theta_W, alpha_s)'
status: in-progress
type: feature
priority: high
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-23T23:28:45Z
parent: qou-sm8w
---

## Scope & Linked Legacy Beans (`qou-ukqh`, `qou-z3x8`, `qou-zd6l`, `qou-5iaz`, `qou-0whz`)

1. **Instantiate `CategoricalHiggsMechanism` & Reconcile `W` Carrier (`qou-ukqh`, `qou-0whz`):** Formalize the longitudinal-mode Goldstone-linking map on `F = V_2 oplus W_3^*` breaking `su(2)_L oplus u(1)_Y -> u(1)_EM`, and reconcile `T(2,4)` (`W` propagator) vs `T(3,5)` (4-fermion weak vertex).
2. **Pin `v_EW` and `m_H / M_W / M_Z` from Sweedler `(q_0^2-1)^8` + Toroidal Habiro/Schur Invariants (`qou-z3x8`):** Combine `#9204`'s proved `(q_0^2 - 1)^8 = 8.408e-6` scaling (`G_F m_p^2 = 1.027e-5`) with toroidal Schur/Jones evaluations on `T(2,4), T(2,6), T(2,8)` at 80 dps (`PREREGISTRATION.md` first).
3. **Categorical UV-to-`M_Z` & `Lambda_QCD` Threshold Ratio (`qou-zd6l`, `qou-5iaz`):** Using the proved 1-loop slopes `(b_3, b_2, b_1) = (7, 19/6, -41/10)` and `sin^2 theta_W^{UV} = 3/8`, test whether the categorical UV-to-EWSB ratio `ln(mu_UV / M_Z)` derived from `(q_0^2 - 1)^{-4}` simultaneously runs `sin^2 theta_W -> 0.23122` and pins `alpha_s(M_Z) ~ 0.1179` from `m_p / Lambda_QCD` without free parameters.

## Additional Lean Targets from Analyst 10 Audit
- Reconcile `ElectroweakBringSchwingerBridge.lean` (`v_EW` at `-29.37 ppb`, `m_Z/m_W` at `+174.7 ppm`, `m_H = 124.26 GeV` at `-0.67%`) with `ElectroweakVevGaps.su2_coupling_not_selfConsistent` by testing whether `#9204`'s Sweedler weak-jet Frobenius norm `(q_0^2 - 1)^8` (`(q_0^2 - 1)^{-4} = 344.87` vs `v/m_p = 262.42`) supplies the self-consistent `alpha_v` without importing `alpha_2`; fix `catalanG` rational literal in `HiggsCategoricalMassFormula.lean:96` (`qou-3nva`) and sync `sm-params-higgs.md`.


## 2026-11-23 Worker 23 Delivery (PR #9227, Issue #9226, Branch `claude/sm8w-ewsb-vew-mh-mz-rg-20261123`)
- **Pre-Registration**: `computations/probes/sm8w_ewsb_vew_mh_mz_rg/PREREGISTRATION.md` committed first (`bdfaf539356`).
- **Lean 4 (`0 sorry`, standard axioms only, wired into `QOU.lean`)**:
  - Remediated `QOU.BraidKnot.catalanG` decimal literal in `HiggsCategoricalMassFormula.lean` to exact `QOU.Archimedean.Catalan_constant = Cl_2 (Real.pi / 2)` + certified rational bracket `(87/100, 96/100)` (`qou-3nva`).
  - Added `QOU/StandardModel/ElectroweakSweedlerScaleAndRGThresholds.lean` proving Sweedler `(q^2-1)^k` ↔ `(G_F, v_EW)` bridges, `EwVevGaps` loop compatibility (`0 < (q^2-1)^4 < 1/256 < 1/30`) vs tree non-coincidence (`ewDressedTreeComplexity q < 287 < 300 < (q^2-1)^{-4}`), `su(2)_L + u(1)_Y -> u(1)_EM` Goldstone rank `3`, Higgs potential stability (`lambda_H > 0, m_H^2 = 2 lambda_H v^2`), representation-derived 1-loop `(41/10, -19/6, -7)` & 2-loop `b_{ij}` matrix, and `sin^2 theta_W^0 = 3/8` Georgi-Quinn-Weinberg / coupling-triangle RG theorems.
- **80-dps Probe & Stamped Witness**: `computations/probes/sm8w_ewsb_vew_mh_mz_rg/sm8w_ewsb_vew_mh_mz_rg_probe.{py,witness.json}` (`5/5` assertions passed, `scriptCommitSha = 9f5084e881b`, synced `sm-params-higgs.{md,ts}`). Held `in-progress` per reviewer-separated closure discipline pending owner merge of #9227.
