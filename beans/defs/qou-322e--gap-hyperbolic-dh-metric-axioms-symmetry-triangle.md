---
# qou-322e
title: 'GAP: hyperbolic dH metric axioms — symmetry, triangle, separation'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T11:11:36Z
updated_at: 2026-11-20T08:27:17Z
parent: qou-c8p8
---

Origin: PR #5211 (T2 hyperbolic metric backfill). QOU/Archimedean/HyperbolicMetric.lean derives dH = ⨅ path lengths and proves dH_self sorry-free, but the three remaining pseudometric axioms are open: dH_comm (path-reversal reflection CoV on the Icc-restricted lintegral), dH_triangle (path concatenation + reparametrisation-invariance CoV), separation dH x y = 0 → x = y (needs FTC/absolute-continuity lower bound; Cantor-path obstruction to a naive bound). Not needed for the isometry engine or the geodesic classification. Kept as a bean (not a sorry) per AGENTS.md rule 13.

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

## 2026-11-20 — W10 (qou-c8p8 workstream)

Stalled-claim takeover by W10 (session_01VQDpPeWFnvbDUN18UJ6CyC, PR #8530): prior claim's backing branch had no commit for >3 h (lane-e667 branches last pushed 2026-11-17). The lane-e667 'Progress Update' sections above refer to unmerged bundle PRs and are NOT the closure.

Subject proved on main: `dH_comm` (HyperbolicMetric.lean:231), `dH_triangle` (:630), `dH_eq_zero_eq` (HyperbolicMetricSeparation.lean:324). Re-checked 2026-11-20, axioms clean. PR #8530 fixes the stale 'separation remains open' docstring.
