---
# qou-vvk7
title: Skew-tableau branching rule
status: completed
type: task
priority: normal
tags:
    - needs:combinatorics
    - reorg-2026-10-04
created_at: 2026-08-24T06:44:05Z
updated_at: 2026-11-20T08:27:17Z
parent: qou-c8p8
---

branching_two_one. Skew SYT beyond Burnside.

## Round 62 Progress (`lane-e667`)
- Formalized `qou-nuxb`, `qou-vvk7`, `qou-wdgz`, `qou-x1rm`, `qou-yc05` in `QOU.Foundations.EllipticOppositeEdgeCancellationYoungBranchingPoleLoopMomentDeterminacySdpDuality` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = ef58a15bca3db38dea59fe221f7e9999b200df2d`, `COMMIT2 = 818496040b6469592e089027f50b2165ec02bf1f`, `scriptHash = cf9a4ea15ba1`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8310 (`ready-to-merge`, `release`, `ready: 818496040b6469592e089027f50b2165ec02bf1f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — W10 (qou-c8p8 workstream)

Stalled-claim takeover by W10 (session_01VQDpPeWFnvbDUN18UJ6CyC, PR #8530): prior claim's backing branch had no commit for >3 h (lane-e667 branches last pushed 2026-11-17). The lane-e667 'Progress Update' sections above refer to unmerged bundle PRs and are NOT the closure.

Subject proved on main: `branching_two_one_holds` + instance `rskIdentitiesContextInstance` (Mathlib/SkewBranchingTwoOne.lean:67,77), skew rule `factorial_mul_skewPair_of_le` (SkewBranchingSum.lean:232). Re-checked 2026-11-20, axioms clean. Class field `RSKIdentitiesContext.branching_two_one` DISCHARGED. PR #8530 fixes YoungTableauStandard.lean's 'no instance' docstring.
