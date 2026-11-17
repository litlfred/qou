---
# qou-5mxd
title: Port far-commutativity ([A_a,A_b]=0 for |a-b|>=2) from the sparse He4 Magnus probe to the dense deuteron/triton probes
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:07:55Z
updated_at: 2026-11-17T08:04:32Z
parent: qou-v2om
---

## VERIFIED 2026-09-08: triton 14/14, the maximal overlap

unpatched 14, patched 19, overlapping 14 (max possible 14) -> ALL IDENTICAL on
dim / y_lambda / tr_rho_Omega2 / tr_Omega2_ctrl. Control (perturbed row) caught,
so the comparison is live. 5 further patched partitions have no baseline.
Still unmeasured: any speedup at H9 (none found at H6), and the 30/30 witness.

## Implementation & Witness Progress (PR #8269)
- Branch: `qou-10v9-07ts-324i-49vn-4pdh-5mxd` (`7a961cf268c0cf36c3f70fd39f92645c16c9a30a`), PR: `litlfred/qou#8269`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/chi_rust_nondeterminism_override_blindness_chi_cache_staleness_qmp_digit_cap_and_magnus_far_commutativity_probe.py` -> `computations/probes/chi-rust-nondeterminism-override-blindness-chi-cache-staleness-qmp-digit-cap-and-magnus-far-commutativity.witness.json` (`allPassed: true`, `scriptCommitSha: e7b85e53d7a8855337daf870617a2e9a6b0acc11`)
