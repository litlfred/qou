---
# qou-9h4t
title: 'LP duality: finite-dim strong duality from Farkas'
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
    - mathlib
created_at: 2026-08-24T06:35:58Z
updated_at: 2026-11-20T14:43:42Z
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

## 2026-11-20 — W10 (qou-c8p8 workstream)

Stalled-claim takeover by W10 (session_01VQDpPeWFnvbDUN18UJ6CyC, PR #8530): prior claim's backing branch had no commit for >3 h (lane-e667 branches last pushed 2026-11-17). The lane-e667 'Progress Update' sections above refer to unmerged bundle PRs and are NOT the closure.

Subject is proved on main (via qou-kl8z): `QOU.Optimization.lp_strong_duality_uncond` (MatrixFarkasInstance.lean), Farkas from `QOU.Mathlib.isClosed_coneSpan` / `farkas_alternative_real`. Re-checked 2026-11-20: lean-library-sweep --only-exact 4/4 ok; `#print axioms` = [propext, Classical.choice, Quot.sound]. The 6 consumer `strong_duality` fields are NOT discharged and cannot be by this theorem: each carrier stores objective values as free reals with no feasibility/optimality data. PR #8530 corrects the four library docstrings that said the infrastructure is missing; discharging the fields needs a carrier retype (owner ask on #8526). Two mass-theory content blocks carry the same stale sentence; left for W1.


## 2026-11-20 — owner ruling implemented (PR #8579)

ShellFillingRuleContext.strong_duality DISCHARGED: claim (iii) is now derived from lp_strong_duality_uncond via the explicit ElectronAssignmentLP. The other three library carriers stay honest assumptions per the ruling.
