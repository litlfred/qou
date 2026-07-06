# Vacuity-candidate triage — 162 pre-existing flags (2026-06-26)

Triage of the 162 non-exempt candidates from the *pre-existing* `lean-vacuity-axiom-audit.ts` detectors (not the conjecture-discipline checks added in #2853/#2865). Method: heuristic first pass over every decl body + shadow/derivation signals, then per-candidate review (sub-agents on ranges 19-37/76-113; direct review on the rest after the agent API throttled), against the AGENTS.md §3b discriminator.

**Totals:** 162 candidates — **95 genuine** (real vacuity defects), 67 legit (false positives), 0 needs-build.


## By category

| category | genuine | legit | needs_build |
|---|--:|--:|--:|
| self-assuming-projection | 53 | 2 | 0 |
| trivial-true | 36 | 36 | 0 |
| decide-masking | 0 | 17 | 0 |
| false-premise | 0 | 12 | 0 |
| placeholder-stub | 6 | 0 | 0 |

## GENUINE — real fake-proof defects (need fixing)

Each asserts/derives nothing meaningful. Fix = state the real proposition (cited `sorry` if not yet provable), derive the conclusion from genuine sub-hypotheses (not a verbatim projection), or demote to `conjecture`. Fixes require a `lake build` to verify (CI).

| file | decl | category | reason |
|---|---|---|---|
| braids-and-knots/pentagon-uv-commutation-woronowicz.lean:149 | `q_commutation_grade_one_half` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| braids-and-knots/pentagon-uv-commutation-woronowicz.lean:274 | `pentagon_ascension_under_woronowicz` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| information-theory/q-gaussian-solves-q-heat.lean:59 | `qGaussian_variance` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/Archimedean/PauliWitness/witness_12C.lean:64 | `witness_12C` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/PauliWitness/witness_4He.lean:56 | `witness_4He` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/PauliWitness/witness_8Be.lean:61 | `witness_8Be` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/archimedean_braid_structure.lean:78 | `descartes_braid_structure` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/archimedean_hartree_derivation.lean:72 | `archimedean_hartree_derivation` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/beta_decay_transfer_matrix.lean:128 | `beta_decay_transfer_matrix` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/borromean_hopf_energy_crossover.lean:132 | `borromean_hopf_energy_crossover` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/eos_borromean_cfl.lean:165 | `eos_borromean_cfl` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/genus_filtration_ideal.lean:111 | `genus_filtration_ideal` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/genus_maximal_descent.lean:55 | `genus_maximal_descent` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/gram_weighted_qvalue.lean:139 | `gram_weighted_qvalue` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/knot_operator_selection.lean:85 | `knot_operator_selection` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/shell_structure_eigenvalues.lean:174 | `shell_structure_eigenvalues` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/skein_finiteness_bound.lean:130 | `skein_finiteness_bound` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Archimedean/torus_knot_shell_binding.lean:123 | `torus_knot_shell_binding` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ArchimedeanUniverse/brings_euler_characteristic.lean:51 | `brings_euler_characteristic` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ArchimedeanUniverse/brings_riemann_hurwitz.lean:53 | `brings_riemann_hurwitz` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ArchimedeanUniverse/heisenberg_commutator.lean:63 | `heisenberg_commutator` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ArchimedeanUniverse/mi_sw_cartan_reduction.lean:49 | `mi_sw_cartan_reduction` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/BaryonWeight/beta4_hook.lean:67 | `beta4_hook` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/BraidKnot/BraneTowerNStar.lean:202 | `betaDecayRecoveryTarget_1ppb_remains_conjectural` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:239 | `wedderburn_decomposition_generic` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/Li2qUniqueness.lean:64 | `briggs_klein_is_neg_li2q` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/Li2qUniqueness.lean:104 | `li2q_unique_from_ftc` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean:363 | `qbeta_inductive_categorical_closure_conjecture` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/QSchurWeightsGeneral.lean:54 | `contentSum_add_cell` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/QSchurWeightsGeneral.lean:74 | `qSchur_weight_by_induction` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/QSchurWeightsGeneral.lean:85 | `qSchur_normalisation` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/SixTermPerDerivationWeights.lean:57 | `binding_assembly_subpercent` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidKnot/ThreeCalibrationInputs.lean:59 | `three_calibration_inputs` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidsAndKnots/UnitModulusEigenvalue.lean:66 | `borromean_trace_21_eq_neg_two` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/BraidsAndKnots/UnitModulusEigenvalue.lean:90 | `all_positive_trace_positive` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/Brings/brings_is_qou.lean:67 | `brings_is_qou` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Brings/color_elliptic.lean:48 | `color_elliptic` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/CategoricalReeb/ofWeightDecomposition.lean:60 | `ofWeightDecomposition` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/CommutativeQOU/u1EquivariantReduction.lean:79 | `u1EquivariantReduction` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Descent/descended_level_zero.lean:45 | `descended_level_zero` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Encounter/MostowRigidity.lean:153 | `mass_rigidity_of_mostow` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Experimental/local_substrate_q.lean:44 | `local_substrate_q` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Experimental/terminal_resolution.lean:48 | `terminal_resolution` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/FeynmanPathIntegrals/markov_identification.lean:63 | `markov_identification` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/FrobeniusHopfData/frobeniusForm.lean:71 | `frobeniusForm` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/HadronicMass/nucleon_borromean_topology.lean:56 | `nucleon_borromean_topology` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Hecke/Hoefsmit.lean:217 | `hoefsmit_distinguishes_word_sensitivity` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/HyperellipticQuintic/minimal_z5_classification.lean:86 | `minimal_z5_classification` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Interactions/UniversalILP.lean:49 | `UniversalILP` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Interactions/inductiveGBReduction.lean:83 | `inductiveGBReduction` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/LightningPath.lean:76 | `lightning_path_synthesis` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/Machinery/LambdaScaleAbsorbed.lean:73 | `no_separate_lambda_scale` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/MassComputationChainRoadmap.lean:142 | `additive_wedderburn_recurrence_matches_std_rep_trace` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:168 | `typed_crossings_encoding_unique` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:188 | `phi_q_converges_absolutely` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:218 | `n_star_existence_conjecture` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:241 | `wedderburn_weights_H3` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:294 | `per_nucleon_shift_additive` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:304 | `per_nucleon_shift_at_A1` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:327 | `frobenius_co_casimir_universal_high_n` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassComputationChainRoadmap.lean:353 | `wenzl_bridge_atomic_tr_M` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/MassDerivation.lean:73 | `topological_mass_formula` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/MathlibExt.lean:134 | `List.prod_eq_of_perm` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/Molecular/benzene_threading_emergence.lean:1 | — | placeholder-stub | unfilled placeholder / conclusion bundled from impl_* fields |
| lean/QOU/Molecular/ch4_lp_dual_binding.lean:1 | — | placeholder-stub | unfilled placeholder / conclusion bundled from impl_* fields |
| lean/QOU/Molecular/co2_lp_dual_binding.lean:1 | — | placeholder-stub | unfilled placeholder / conclusion bundled from impl_* fields |
| lean/QOU/Molecular/co_lp_dual_binding.lean:1 | — | placeholder-stub | unfilled placeholder / conclusion bundled from impl_* fields |
| lean/QOU/Molecular/h2_lp_dual_binding.lean:1 | — | placeholder-stub | unfilled placeholder / conclusion bundled from impl_* fields |
| lean/QOU/ParticleInteractions/SpectatorNormalization.lean:52 | `SpectatorNormalization` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/atomic_nf_witness.lean:105 | `atomic_nf_witness` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean:84 | `confinement_frobenius_reciprocity` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/deuterium_derived_binding.lean:131 | `deuterium_derived_binding` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean:57 | `four_term_pair_nucleon` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/ground_state_ordering.lean:64 | `ground_state_ordering` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/lp_dual_stability.lean:93 | `lp_dual_stability` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/mass_categorical_descent.lean:62 | `mass_categorical_descent` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/neutron_qvalue_symbolic.lean:1 | — | placeholder-stub | unfilled placeholder / conclusion bundled from impl_* fields |
| lean/QOU/ParticleInteractions/operator_selection_lp.lean:103 | `operator_selection_lp` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/parity_regime_selection.lean:78 | `parity_regime_selection` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/ParticleInteractions/transfer_matrix_identities.lean:58 | `transfer_matrix_identities` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/PhotonThreading.lean:91 | `crossing_energy_gauge_invariant` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| lean/QOU/QuantumObservableUniverse/exists_axiom_1_frobenius.lean:45 | `exists_axiom_1_frobenius` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/QuantumObservableUniverse/exists_axiom_3_chern.lean:47 | `exists_axiom_3_chern` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/orbital_fourier_decomposition.lean:121 | `orbital_fourier_decomposition` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/qou_canonical_action.lean:105 | `qou_canonical_action` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| lean/QOU/variational_equations.lean:107 | `variational_equations` | self-assuming-projection | body is a bare projection `:= ctx.claim_*` returning the conclusion field verbatim |
| mass-theory/atom-knot-mass-derivation-proof.lean:24 | `categorical_leg_to_markov_trace` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| mass-theory/atom-knot-mass-derivation-proof.lean:36 | `archimedean_realization_to_mev` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| mass-theory/atom-knot-mass-derivation-proof.lean:45 | `post_archimedean_naming_borrowed` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| mass-theory/atom-knot-mass-derivation-proof.lean:63 | `atom_knot_mass_derivation_proof` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| mass-theory/eigenvalue-product-expansion.lean:33 | `geometric_sum_is_qint` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| mass-theory/markov-trace-product.lean:274 | `degree_bound` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| mass-theory/vertex-is-exceptional-divisor.lean:33 | `vertex_is_exceptional_divisor` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| predicted-spectra/breit-wheeler-pair-production.lean:25 | `breit_wheeler_pair_production` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |
| quantum-observable-universes/qou-canonical-action.lean:79 | `qou_canonical_action_unique_up_to_scalar` | trivial-true | conclusion is `True := trivial` / `X=X:=rfl` — asserts nothing (def-disguised-true) |

## needs_build (compile to confirm)

| file | decl | category |
|---|---|---|
