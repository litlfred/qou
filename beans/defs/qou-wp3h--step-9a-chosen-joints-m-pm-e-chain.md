---
# qou-wp3h
title: Step-9a chosen joints (m_p/m_e chain)
status: in-progress
type: epic
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:58Z
updated_at: 2026-11-23T23:38:35Z
parent: qou-10v9
---

Sub-epic P1.9A of PROGRAM: L2 at 1 ppQ (mass and binding accuracy) (work-plan reorganisation 2026-10-04).

## Progress Update (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`, PR #8143)

- Executed Option 1 across all 5 child beans under PR `litlfred/qou#8143` (commit `7df80d1c2e228518b2ca15ec1d314be46da8e524`):
  - `qou-ev3a`: Proved the reverse direction (converse) of D2 at $v = n - 1$ for all three depth-1 carrier shapes in `QOU/BraidsAndKnots/HookArmLeg.lean` (`depth1_three_shapes_achieve_hookLen_eq_sum_sub_one`, `0` `sorry`).
  - `qou-zbcj` & `qou-tw5z`: Added `QOU/Torsion/MultiplicativeIntegralCurvature.lean` (`0` `sorry`, wired into `QOU/Torsion.lean` and `QOU.lean`) and 50+ dps `mpmath` probe `computations/probes/yekutieli_multiplicative_integral_curvature_probe.py` + `yekutieli-multiplicative-integral-curvature.witness.json` (registered in `computations/q0_anchor_manifest.json`).
  - `qou-kx92` & `qou-qkbp`: Verified landed `main` commits (`62d3235885`, `a2842b21ac`, `0912f1aa53`, `709b8cc166`, `b9c56a4a59`, `534794e799`) and recorded audit notes.
- All beans kept at `status: in-progress` per owner rule.

## Progress Update (2026-11-16 — Round 48: PR #8160)
- **PR:** [`litlfred/qou#8160`](https://github.com/litlfred/qou/pull/8160) (`c0fb591249c67f13f6a77b40075589852babb011`)
- Completed Lean formalization and impact analysis for `8gzz`, `qou-0w42`, `qou-tknh`, `qou-bhrx`, and `qou-loqn` (`0` `sorry`, `0` self-assuming audit hits).

## Progress Update (2026-11-16 — Round 49: PR #8143 fix + PR #8164)
- **PR #8143 fix:** Stamped `scriptCommitSha: "7df80d1c2e228518b2ca15ec1d314be46da8e524"` in `computations/probes/yekutieli-multiplicative-integral-curvature.witness.json` (`4340428cced694b249ca48316cbb5096751b5f64`).
- **PR #8164:** Opened [`litlfred/qou#8164`](https://github.com/litlfred/qou/pull/8164) (`47da262e4f487a8f51de58f3577a63d5b17e6d6a`) for `qou-ch8w`, `qou-quv8`, `qou-yczy`, `qou-h5aw`, and `qou-n4u6` (`0` `sorry`, `0` self-assuming audit hits, 50+ dps witness `na-stokes-bar-parity-local-bond.witness.json`).
- **Batch 5 (2026-11-16, PR #8171, head `1c72739193707fef67fbebe3aa153f994c73933e`)**: Addressed `qou-nbx7`, `qou-mrel`, `qou-n04i`, `qou-ncgk`, and `qou-3fqa` across `ProtonBorromeanAssembly.lean`, `YekutieliIntegration.lean`, and 50+ dps probe `delta_split_mrel_four_phi_resummation_probe.py` + witness `delta-split-mrel-four-phi-resummation.witness.json` (all kept `in-progress`).



## Claim reset 2026-11-22
In-progress only through an untouched batch PR / no live branch (applicability review, thread "Coordinate the L2 1-ppQ derivation plan"; plan doc /mnt/project-files/l2-1ppq-coordination/). Reset to todo under the stalled-claim policy; nothing in the work was judged. Re-claim if you pick it up.

Claimed by claude/w7-chen-mult-integral-masstrace-20261123 (Worker 17, 2026-11-23)

EOS (2026-11-23, Worker 17, branch claude/w7-chen-mult-integral-masstrace-20261123, issue #9214):
- Lean 4 module folio/quantum-observable-universe/lean/QOU/Torsion/ChenMultiplicativeIntegralBridge.lean (commit 15db38d0253, 0 sorry, 0 custom axioms — [propext, Classical.choice, Quot.sound] only, zero empirical constants):
  (1) Ordered matrix product path-concatenation multiplicativity (orderedProd_append, eulerStepProd_append), gauge covariance & closed-loop trace invariance (orderedProdFin_gauge_covariant, trace_gaugeTransform_closed_loop), and units/weighted associator conjugation trace invariance (trace_eq_of_units_intertwine, weighted_trace_eq_of_commuting_intertwine).
  (2) Algebraic Chen iterated-integral tensor-coalgebra shuffle homomorphism & group-like signature stability over generic [CommAlgebra Q R] (shuffleEval_chenSigMul, shuffleEval_wordProd, isShuffleGroupLike_segmentSig, IsShuffleGroupLike.chenSigMul, isShuffleGroupLike_piecewiseLinear).
  (3) Picard contraction, linear ODE fundamental-solution uniqueness, and discrete Gronwall O(1/N) error bound + convergence of N-step Euler ordered matrix products (norm_picardOp_sub_le, IsLinearFundSol.eqOn, eulerOrderedProd_error_bound, tendsto_eulerOrderedProd_isFundSol).
  (4) Concrete non-vacuous Matrix (Fin (d+2)) (Fin (d+2)) R Frobenius-Hopf substrate instantiation of MassTraceIdentity: regular trace d * Tr(M) vs counit trace Tr(M) (matFrobHopf_frobeniusMass_eq_trace, matFrobHopf_leftTrace_eq_dim_mul_trace), inner commutator connection nablaEndo = adEndo K satisfying Leibniz and non-vanishing on KZ Casimir kzOmega01 (adEndo_leibniz, adEndo_kzOmega01_ne_zero), block-diagonal Reeb/matter decoupling (evalTraceLin_cross_zero, substrateLagrangian_normalised), and non-abelian 3x3 Borromean two-term instantiation matching twoTermCandidateBorromean (substrate_borromean_two_term_instantiation).
  (5) Explicit 2-row/hook Hecke & KZ monodromy bridge on B_3 ([2,1], dim 2) and B_4 ([2,2], dim 2; [3,1], dim 3), proving exact KZ half-turn fundamental solution, local quadratic Hecke relation, real/complex monodromy-to-Hecke trace equality, and Convention-D 2-row generator synthesis (kzHalfTurnFundReal_isFundSol, kzLocalMonodromyReal_hecke_quad, kzMonodromy_trace_eq_hecke_real, kzMonodromy_trace_eq_hecke_complex, conventionD_twoRow_generator_synthesis).
- Pre-registered 80-dps probe & witness computations/probes/w7_chen_multiplicative_integral/ (PREREGISTRATION.md cbd41d51fb5, probe 15db38d0253, witness 5978c1eb262, workDps=80, outputDps=50, q0Anchor=proton, 59/59 assertions passed, 0 float64): path-concatenation < 2.5e-80, Chen shuffle/deconcatenation < 6e-82, Gronwall O(1/N) bound + Richardson O(1/N) scaling verified, continuous KZ Yang-Baxter & far-commutativity < 4.5e-80, Klein-four V_4 symmetry P_KZ^{[2,2]}(sigma_0)=P_KZ^{[2,2]}(sigma_2) to 2.11e-81 vs [3,1] diff 3.0332, Drinfeld associator Phi_KZ conjugacy < 2.4e-80 with leading zeta(2) commutator norm (1/2)eta_0^2 = 0.0054284 verified to 3.44e-5, and |Tr(P_KZ(w)) - Tr(rho_Hecke(w))| < 1.6e-80 across all 21 knot/link sector-word pairs (3_1, 4_1, T(3,5), Borromean, T(4,3) + Markov stabilizations).

Ready PR opened: https://github.com/litlfred/qou/pull/9228 (head 5978c1eb262, Refs #9214).
