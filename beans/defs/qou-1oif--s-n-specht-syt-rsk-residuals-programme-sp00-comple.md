---
# qou-1oif
title: S_n / Specht / SYT / RSK residuals (programme sp00 completed)
status: in-progress
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:06Z
updated_at: 2026-11-17T12:24:25Z
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

## Progress 2026-11-17 (Round 65 — PR #8331)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/CumulativeSwapCentralityTabloidTransitionCellProductFactorialCurlTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/cumulative-swap-centrality-tabloid-transition-cell-product-factorial-curl-trace.witness.json` (`scriptHash = 9e4c62bb8c28`, `scriptCommitSha = 4331c3d6858037c7a16d08f2202e77af0fee8a52`, `HEAD = 69f8f329d2048eae2ceddcc8d14985dd544d587f`).
- PR: https://github.com/litlfred/qou/pull/8331 (`ready: 69f8f329d2048eae2ceddcc8d14985dd544d587f`).

## Progress 2026-11-17 (Round 66 — PR #8340)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json` (`scriptHash = 0309390e769d`, `scriptCommitSha = c43b700db42337a2547c8ff1e2a1665156dd27ea`, `HEAD = d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
- PR: https://github.com/litlfred/qou/pull/8340 (`ready: d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
