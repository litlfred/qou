---
# qou-nbz9
title: Adjudicate the 38 projections de-exempted by the isDefProof narrowing
status: in-progress
type: task
priority: high
tags:
    - vacuity
    - issue-2472
    - reorg-2026-10-04
created_at: 2026-08-10T01:50:40Z
updated_at: 2026-11-16T19:22:00Z
parent: qou-6qbv
---

Recommendation 4 of the honest-placeholder criterion, applied: `detectSelfAssuming`'s `isDefProof` branch no longer overrides a `CONCLUSION_FIELD` name-gate match.

The gate runs first but only *diverts* candidates whose field name escapes the convention. A `def` whose field name the gate MATCHES — `ctx.claim_yang_baxter`, `ctx.claim_pslq_independence` — fell straight through to the §3b carve-out and was exempted anyway. The exemption was swallowing the detector's strongest signal: the author named the field `claim_*`.

**Effect on the corpus:** non-exempt `proof-no-self-assuming-projection` goes **56 -> 94**; exempt **162 -> 124**. **38 declarations** flipped exempt -> non-exempt.

These now enter the review ledger as `needs-agent`, so `--check-ledger` exits 1 until each carries a verdict. That is the gate working as designed — the same posture as PR #4882 §3, not a regression.

Each needs the standard self-assuming adjudication: is the carrier inhabited, and if so is the instance **non-degenerate**? Note from the 2026-08-09 drain that inhabitation alone is a weak discriminator — watch for the reflexive diagonal, the trivial/`Empty` index, the stipulated constant, and the zero model (`docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md`).

- `folio/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.lean:108` — `braid_rep_from_R_check`
- `folio/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.lean:86` — `r_matrix_braiding_structure`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5PslqIndependence.lean:37` — `pslq_independence`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/KnotIndexedConvolutionGrid.lean:35` — `grid_placement`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/LevelSufficiency.lean:112` — `LevelSufficiency`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/QHeckeSeminormalCharacterClosure.lean:33` — `character_closure_holds`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean:43` — `binding_assembly`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean:124` — `g_eq_pi_h_substrate_hypothesis`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean:165` — `scalar_gauge_ratio_eq_six_fifths_hypothesis`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean:144` — `v_ratio_eq_log_S3_hypothesis`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/UnstableAtom/decay_channel.lean:108` — `decay_channel`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/algebraic_quantum_volume_specialization.lean:56` — `algebraic_quantum_volume_specialization`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/e_infinity_identifications.lean:94` — `e_infinity_identifications`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/hoefsmit_scattering_pipeline.lean:137` — `hoefsmit_scattering_pipeline`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/jet_prefix_gb_filtration.lean:36` — `jet_prefix_gb_filtration`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/joint_tower_sdp_confinement.lean:107` — `joint_tower_sdp_confinement`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:72` — `knot_factor_spectral_derivation`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:63` — `plancherelWeight_sum_eq_one`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/knot_mass_unified.lean:93` — `knot_mass_unified`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/mass_formula_regime_switching.lean:99` — `mass_formula_regime_switching`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/schur_weyl_mass_decomposition.lean:67` — `schur_weyl_mass_decomposition`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/six_term_mass_formula_complete.lean:49` — `six_term_mass_formula_complete`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/sorting_color_energy.lean:51` — `sorting_color_energy`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/spectral_sequence_h3_explicit.lean:58` — `spectral_sequence_h3_explicit`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/terms_2_6_higher_operations.lean:60` — `terms_2_6_higher_operations`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/wedderburnWeightCanonical.lean:104` — `wedderburnWeightCanonical`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/wigner2_coefficient.lean:124` — `wigner2_coefficient`
- `folio/quantum-observable-universe/lean/QOU/Braiding/beta_stability.lean:39` — `beta_stability`
- `folio/quantum-observable-universe/lean/QOU/Braiding/fermion_boson_knot_link.lean:48` — `fermion_boson_knot_link`
- `folio/quantum-observable-universe/lean/QOU/Braiding/r_matrix_braiding_structure.lean:59` — `r_matrix_braiding_structure`
- `folio/quantum-observable-universe/lean/QOU/Braiding/reidemeister_mass_invariance.lean:44` — `reidemeister_mass_invariance`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/demazure_fiber_markov_trace.lean:95` — `demazure_fiber_markov_trace`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/ew_interface_knot.lean:65` — `ew_interface_knot`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/explicit_alpha_k_h4.lean:36` — `explicit_alpha_k_h4`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/qmn_recursive_memoized.lean:66` — `qmn_recursive_memoized`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/wedderburn_bratteli_recursion.lean:64` — `wedderburn_bratteli_recursion`
- `folio/quantum-observable-universe/lean/QOU/Information/toffoli_transfer_matrix.lean:99` — `toffoli_transfer_matrix`
- `folio/quantum-observable-universe/mass-theory/confinement-nf-partial-proof.lean:118` — `strong_duality`

## Progress Update (2026-11-16 — Round 48, PR #8165)

- Verified all 38 declarations from the `isDefProof` narrowing: 30 were retired/refactored to `Prop`-valued definitions or removed, and the remaining 8 (`LevelSufficiency`, `algebraic_quantum_volume_specialization`, `e_infinity_identifications`, `spectral_sequence_h3_explicit`, `terms_2_6_higher_operations`, `ew_interface_knot`, `toffoli_transfer_matrix`, `strong_duality`) are adjudicated as `genuine` in `docs/audits/lean-vacuity-review-ledger.json` (`0` `needs-agent` entries) and carry explicit §3b-conditional disclosures.
- Opened PR `litlfred/qou#8165` (`cf010d07bb34f2e3118733212559b61ede4b8cc4`) with `ready-to-merge` + `release` labels.
