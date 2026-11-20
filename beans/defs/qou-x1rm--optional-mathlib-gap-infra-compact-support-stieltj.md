---
# qou-x1rm
title: 'Optional Mathlib-gap infra: compact-support => StieltjesDeterminate via Stone-Weierstrass (Jackson determinacy leg)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T15:13:34Z
updated_at: 2026-11-20T19:56:42Z
parent: qou-c8p8
---

## Round 62 Progress (`lane-e667`)
- Formalized `qou-nuxb`, `qou-vvk7`, `qou-wdgz`, `qou-x1rm`, `qou-yc05` in `QOU.Foundations.EllipticOppositeEdgeCancellationYoungBranchingPoleLoopMomentDeterminacySdpDuality` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = ef58a15bca3db38dea59fe221f7e9999b200df2d`, `COMMIT2 = 818496040b6469592e089027f50b2165ec02bf1f`, `scriptHash = cf9a4ea15ba1`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8310 (`ready-to-merge`, `release`, `ready: 818496040b6469592e089027f50b2165ec02bf1f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — DONE (PR #8678)

`QOU/MathlibExt/StieltjesCompactDeterminacy.lean`, sorry-free, standard axioms. `stieltjesDeterminate_of_moment_bound`: `M k ≤ C·R^k` ⇒ `StieltjesDeterminate M` (Markov puts mass on [0,R]; Weierstrass + `ext_of_forall_integral_eq_of_IsFiniteMeasure`). Measure form `eq_of_hasStieltjesMoments_of_Ioi_null`. NOT covered: k! moments (Carleman); `CarlemanDeterminacyStieltjes` / `FrechetShohatStieltjes` remain uninstantiated.
