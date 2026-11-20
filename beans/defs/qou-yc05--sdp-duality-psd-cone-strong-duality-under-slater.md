---
# qou-yc05
title: 'SDP duality: PSD cone strong duality under Slater'
status: in-progress
type: task
priority: normal
tags:
    - mathlib
    - reorg-2026-10-04
created_at: 2026-08-24T06:35:58Z
updated_at: 2026-11-20T21:27:24Z
parent: qou-c8p8
---

Build theorem: SDP strong duality for PSD cone. Mathlib has Hahn-Banach but not PSD cone duality. Route: Boyd-Vandenberghe Thm 5.5 — PSD cone is proper → Slater condition → strong duality. Harder than LP (~500 lines). Consumers: ConfinementSDP.strong_duality, confinement-sdp.strong_duality.

## Round 62 Progress (`lane-e667`)
- Formalized `qou-nuxb`, `qou-vvk7`, `qou-wdgz`, `qou-x1rm`, `qou-yc05` in `QOU.Foundations.EllipticOppositeEdgeCancellationYoungBranchingPoleLoopMomentDeterminacySdpDuality` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = ef58a15bca3db38dea59fe221f7e9999b200df2d`, `COMMIT2 = 818496040b6469592e089027f50b2165ec02bf1f`, `scriptHash = cf9a4ea15ba1`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8310 (`ready-to-merge`, `release`, `ready: 818496040b6469592e089027f50b2165ec02bf1f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — dual-Slater direction PROVED (PR #8678); bean stays open

`QOU/Mathlib/SDPStrongDuality.lean`, sorry-free, standard axioms: PSD self-duality, closedness/convexity, compact sublevels; `strong_duality_of_dual_slater` (primal feasible + dual strictly feasible ⇒ primal optimum attained, zero gap) and `no_duality_gap`. Symmetric data. STILL OPEN: primal-Slater direction (dual attainment); discharging `ConfinementSDP.strong_duality` (LP-style data field) and `MathlibExt/SDP.HasStrongDuality` (primal-Slater, over a CommRing).

## 2026-11-20 (later) — primal-Slater direction PROVED (PR #8678)

`strong_duality_of_primal_slater` (needs linearly independent constraints), `exists_optimal_pair` (both Slater ⇒ optimal pair + complementary slackness). `MathlibExt/SDP.HasStrongDuality` is FALSE as stated: `not_forall_hasStrongDuality` (1×1 cost −1, no constraints). `hasStrongDuality_of_slater` proves it for ℝ under symmetric data + independent constraints + dual Slater. STILL OPEN: dropping linear independence; wiring `ConfinementSDP.strong_duality` (LP-style data field).

## 2026-11-20 (later still) — linear independence removed (PR #8678)

Primed versions `strong_duality_of_primal_slater'`, `exists_optimal_pair'`, `hasStrongDuality_of_slater'` need no surjectivity. STILL OPEN: non-symmetric data; wiring `ConfinementSDP.strong_duality` (its field is LP-style data, not this SDP form).
