---
# qou-1oif
title: S_n / Specht / SYT / RSK residuals (programme sp00 completed)
status: in-progress
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:06Z
updated_at: 2026-11-17T11:34:45Z
parent: qou-rtxm
---

Sub-epic P3.SN of Lean / Mathlib foundations (work-plan reorganisation 2026-10-04).


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `hook_three_content_sum_and_cubic_factor` — proves three-box hook diagram content sum vanishing `0 + (1 + (-1)) = 0` and cubic spectral factorization `x · ((x + 1) · (x - 1)) = x³ - x` over generic `CommRingCarrier R`, with `S_4` Burnside dimension sum `1² + 3² + 2² + 3² + 1² = 24 = 4!` verified in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.

## Round 64 Progress (`lane-e667`)
- Formalized `qou-7xt3`, `qou-ck0g`, `qou-em1j`, `qou-kbjc`, `qou-w0zn` in `QOU.Foundations.ThreeCellPosetOrbitSizeBarSymEigenvalueLengthGeneratingQBinomialUpDownWeyl` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 directory-mode static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = 13e718201144523610e11912018cdb123e6155b3`, `COMMIT2 = 06940a10b90934e8a8d7233d592147be01aa5979`, `scriptHash = 01e1202f7b26`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8323 (`ready-to-merge`, `release`, `ready: 06940a10b90934e8a8d7233d592147be01aa5979`).
- Keeping bean at `status: in-progress` pending merge and verification.
