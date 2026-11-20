---
# qou-wdgz
title: Parallelogram bare pole integral
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs:mathlib
created_at: 2026-08-24T06:44:05Z
updated_at: 2026-11-20T20:28:21Z
parent: qou-c8p8
---

Prove parallelogramIntegral_inv_sub_eq_two_pi_i. Winding.

## Round 62 Progress (`lane-e667`)
- Formalized `qou-nuxb`, `qou-vvk7`, `qou-wdgz`, `qou-x1rm`, `qou-yc05` in `QOU.Foundations.EllipticOppositeEdgeCancellationYoungBranchingPoleLoopMomentDeterminacySdpDuality` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = ef58a15bca3db38dea59fe221f7e9999b200df2d`, `COMMIT2 = 818496040b6469592e089027f50b2165ec02bf1f`, `scriptHash = cf9a4ea15ba1`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8310 (`ready-to-merge`, `release`, `ready: 818496040b6469592e089027f50b2165ec02bf1f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — DONE (PR #8651)

`parallelogramIntegral_inv_sub_eq_two_pi_i` is now a theorem (was `axiom`), same statement, sorry-free, standard axioms. Edge integrals = log(u+1) − log u by FTC on a half-plane; exp of the sum telescopes to 1 so sum = 2πi·n; each edge angle ∈ (0,π) ⇒ n = 1. No consumers of the module.
