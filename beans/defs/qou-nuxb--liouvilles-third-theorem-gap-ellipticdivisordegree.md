---
# qou-nuxb
title: Liouville's third theorem gap (EllipticDivisorDegree.lean)
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-12T10:23:09Z
updated_at: 2026-11-20T16:19:39Z
parent: qou-c8p8
---

## Round 62 Progress (`lane-e667`)
- Formalized `qou-nuxb`, `qou-vvk7`, `qou-wdgz`, `qou-x1rm`, `qou-yc05` in `QOU.Foundations.EllipticOppositeEdgeCancellationYoungBranchingPoleLoopMomentDeterminacySdpDuality` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = ef58a15bca3db38dea59fe221f7e9999b200df2d`, `COMMIT2 = 818496040b6469592e089027f50b2165ec02bf1f`, `scriptHash = cf9a4ea15ba1`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8310 (`ready-to-merge`, `release`, `ready: 818496040b6469592e089027f50b2165ec02bf1f`).
- Keeping bean at `status: in-progress` pending merge and verification.


## 2026-11-20 — PROVED (W10, PR #8604)

Liouville third theorem `QOU.Mathlib.EllipticDivisorDegree.elliptic_divisor_degree_zero` is proved sorry-free in `QOU/Mathlib/LiouvilleThird.lean` (annulus route: exp pull-back, ℤ-order annulus argument principle, winding identity, lattice-reduction bijection). Axioms [propext, Classical.choice, Quot.sound]; library sweep 6 ok / 0 RED. Known mathematics (not a conjecture). Nonconstancy hypothesis dropped as unused.
