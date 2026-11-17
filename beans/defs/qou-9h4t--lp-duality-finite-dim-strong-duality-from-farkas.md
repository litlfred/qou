---
# qou-9h4t
title: 'LP duality: finite-dim strong duality from Farkas'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - mathlib
created_at: 2026-08-24T06:35:58Z
updated_at: 2026-11-17T10:08:09Z
parent: qou-c8p8
---

Build theorem: finite-dim LP strong duality. Mathlib has Farkas (ProperCone.hyperplane_separation) but not LP duality. Route: positive orthant is a proper cone → instantiate Farkas → derive primal=dual under Slater. ~300 lines. Consumers: 6 class fields (shell_filling, lp_dual_stability, confinement_frobenius, operator_selection_lp, confinement-nf-partial-proof).

### Progress Update (2026-11-17, Round 59 — lane-e667)
- **PR:** `litlfred/qou#8291` (`https://github.com/litlfred/qou/pull/8291`), head `97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`COMMIT1 = 9f95671d31537da41246588ea9801b300607f995`), labeled `ready-to-merge` + `release`, `ready: 97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`https://github.com/litlfred/qou/pull/8291#issuecomment-6944908884`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/HyperbolicScalingDescartesCubicFarkasDuality.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-322e`: `chordal_step_symmetry_diagonal_and_concatenation` over `CommRingCarrier R`.
  - `qou-4tsl`: `alternating_two_wedge_antisym_and_three_wedge_vanishing` and `alternating_two_wedge_ring_antisym_and_diag` over `Int` and `CommRingCarrier R`.
  - `qou-5gai`: `dilation_cube_jacobian_density_cancellation` over `CommRingCarrier R`.
  - `qou-7y3g`: `classical_av4_cubic_factorization_and_complex_roots` over `Int`.
  - `qou-9h4t`: `primal_dual_slack_gap_and_complementary_slackness` over `Int`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/hyperbolic_scaling_descartes_cubic_farkas_duality_probe.py` + `computations/probes/hyperbolic-scaling-descartes-cubic-farkas-duality.witness.json` (`scriptHash = 9b07010b5e8c`, `scriptCommitSha = 9f95671d31537da41246588ea9801b300607f995`, `allPassed = True`).
- **Adversarial Cross-Review (Round 59):** Verified `litlfred/qou#8276` (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`, `0` advisories) and remediated `3 major, 2 advisory` borrowed-name findings on sibling PR `litlfred/qou#8261`, pushing `77aeb5c622eb2876245d1628c2f107b5f85999f8` and posting `ready: 77aeb5c622eb2876245d1628c2f107b5f85999f8` (`https://github.com/litlfred/qou/pull/8261#issuecomment-6942739479`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
