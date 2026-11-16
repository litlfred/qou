---
# qou-tw5z
title: Compute the surface-ordering curvature/area (commutator) term of the na-Stokes multiplicative integral; verify it equals -pi^2/3. Upgrades MQ2/MQ3 from open to derived (anomaly = non-abelian curvature, not regulator artifact).
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-26T12:23:36Z
updated_at: 2026-11-16T18:02:18Z
parent: qou-wp3h
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`, PR #8143)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Torsion/MultiplicativeIntegralCurvature.lean` (`0` `sorry`, PR `litlfred/qou#8143`, commit `7df80d1c2e228518b2ca15ec1d314be46da8e524`):
  - `surfaceOrderingShift_eq_neg_pi_sq_div_three`: `-(Real.pi ^ 2 / 6) - (Real.pi ^ 2 / 6) = -Real.pi ^ 2 / 3`.
  - `hasSum_neg_two_zeta_two` & `tsum_neg_two_zeta_two_eq_surfaceOrderingShift`: proves `HasSum (fun n : ℕ => -2 * (1 / (n : ℝ) ^ 2)) (-Real.pi ^ 2 / 3)` and `∑' n : ℕ, -2 * (1 / (n : ℝ) ^ 2) = -Real.pi ^ 2 / 3` (`-2 * ζ(2)`).
  - `iterated_partB_shift_eq_neg_pi_sq_div_three` & `naStokes_partB_shift_eq_surfaceOrderingShift`: proves that under `[NaStokesPartBOrdering x]`, `physicalPartB - LiTwo x = surfaceOrderingShift = -Real.pi ^ 2 / 3`.
- Verified to 50+ dps in `computations/probes/yekutieli_multiplicative_integral_curvature_probe.py` (`computations/probes/yekutieli-multiplicative-integral-curvature.witness.json`): `-2 * zeta(2) = -3.289868133696452872944830333292050378437899802413596875471116458740015 = -pi^2 / 3`, shifting the commuting iterated Part B value `-pi^2 / 6` to `-pi^2 / 2`.
- Kept at `status: in-progress` pending PR #8143 merge and owner verification.
