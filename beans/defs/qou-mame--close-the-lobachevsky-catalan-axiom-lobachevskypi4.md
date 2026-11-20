---
# qou-mame
title: 'Close the Lobachevsky-Catalan axiom: lobachevsky(pi/4) = catalan_G/2 via QOU.Knot.clausen_eq_series'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T00:50:24Z
updated_at: 2026-11-20T08:27:17Z
parent: qou-c8p8
---

PROVED 2026-08-26. `lobachevsky_pi_div_four_eq_half_catalan` is now a theorem, sorry-free, [propext, Classical.choice, Quot.sound]. Axiom surface 24 -> 23.

The axiom was recorded External on the strength of its own docstring ("needs Mathlib's full polylogarithm machinery ... none of which is currently upstream"). Both halves were false: Mathlib has `integral_log_sin_zero_pi_div_two` and `Analysis.Complex.AbelLimit`, and this repo already had the whole series-integral bridge in `QOU.Knot.clausen_eq_series` (sorry-free). Proof is 3 steps over those.

Downstream: `WhiteheadVolume.vol_L5a1_eq_eight_lobachevsky` was conditional on the axiom and is now unconditional.

Deleted `LobachevskyClausenGap.lean` (its narrative asserted a gap that does not exist). Guard rc=0 / 40 entries.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

### Progress Update (2026-11-17, Round 61 — lane-e667)
- **PR:** `litlfred/qou#8303` (`https://github.com/litlfred/qou/pull/8303`), head `2a91d843d44db15a0190138e20fb1878634fbbeb` (`COMMIT1 = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`), labeled `ready-to-merge` + `release`, `ready: 2a91d843d44db15a0190138e20fb1878634fbbeb` (`https://github.com/litlfred/qou/pull/8303#issuecomment-6945508253`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AlternatingThreeFormPrimaryFactorUpperHalfPlaneCatalanClausenSymmetry.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-jvua`: `alternating_three_form_antisym_diag_and_unit_frame`.
  - `qou-kp89`: `primary_factor_linear_cancellation_and_cubic_remainder`.
  - `qou-m8xt`: `upper_half_plane_shifted_modulus_pos_and_cyclic_closure`.
  - `qou-mame`: `quarter_turn_even_vanishing_and_odd_alternation`.
  - `qou-u4mx`: `termwise_periodic_and_odd_two_harmonic_sum`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/alternating_three_form_primary_factor_upper_half_plane_catalan_clausen_symmetry_probe.py` + `computations/probes/alternating-three-form-primary-factor-upper-half-plane-catalan-clausen-symmetry.witness.json` (`scriptHash = 0ee532c9f9a2`, `scriptCommitSha = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`, `allPassed = True`).
- **Adversarial Cross-Review (Round 61):** Verified `litlfred/qou#8285` (`250465c60a6cea44d9f569e88cc79ee2c8d8051b`, `0` advisories on all 5 added theorems, valid witness `39a564805d3e`) and `litlfred/qou#8299` (`7794a07bbdcd4212b670d7ed777098efe60dc9a4`, `0` advisories, valid witness `001b12183bba`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.

## 2026-11-20 — W10 (qou-c8p8 workstream)

Stalled-claim takeover by W10 (session_01VQDpPeWFnvbDUN18UJ6CyC, PR #8530): prior claim's backing branch had no commit for >3 h (lane-e667 branches last pushed 2026-11-17). The lane-e667 'Progress Update' sections above refer to unmerged bundle PRs and are NOT the closure.

Bean body already records PROVED 2026-08-26. Re-checked 2026-11-20: `lobachevsky_pi_div_four_eq_half_catalan` (Archimedean/BorromeanVolumeCatalan.lean:151) lean-direct exit 0 against the restored cache (deps not re-swept: cone too large for one call), axioms clean.
