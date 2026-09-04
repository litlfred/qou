---
# qou-pqmw
title: Add disclosure — 78 bare projections currently exempt (tracked, triage pending)
status: todo
type: task
priority: low
tags:
    - vacuity
    - issue-2472
created_at: 2026-08-10T01:47:54Z
updated_at: 2026-09-04T20:55:30Z
parent: qou-5p7n
---

**78 declarations** that project a class field verbatim with no disclosure and no citation, currently **exempt** (mostly under the type-matched carve-out, tracked with triage pending).

Criterion (1) — *disclosure*. Lowest priority of the four disclosure classes because the scanner already tracks them and they do not fail the gate; but the exemption's stated justification does not hold for any of them, so each needs either the disclosure sentence or ordinary self-assuming triage.

Sub-clusters worth doing together: `Instanton.lean` (4), `QHookBound.lean` (4), `core-levi-form.lean` (3), `HadronicMass.lean` (3), `categorical-jet.lean` (2), `SkewSYT.lean` (2), `MassTowerOpenProblemsClasses.lean` (2), `TrefoilCanonicalMassUnit.lean` (1 here + 2 in the non-exempt bean).

- `content/quantum-observable-universe/braids-and-knots/knot-eigenbasis-complete.lean:303` — `knot_eigenbasis_density`
- `content/quantum-observable-universe/brings-surface/levi-form-defect.lean:51` — `matter_locus_nonempty`
- `content/quantum-observable-universe/brings-surface/mi-sw-abelianisation.lean:48` — `mi_sw_nonneg`
- `content/quantum-observable-universe/climax-volume-mass/mobius-energy-proof.lean:105` — `MobiusEnergy`
- `content/quantum-observable-universe/climax-volume-mass/non-self-intersection-proof.lean:81` — `NonSelfIntersection.exclusionRadius_eq`
- `content/quantum-observable-universe/climax-volume-mass/non-self-intersection.lean:67` — `noncocomm_iff_quantum`
- `content/quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.lean:98` — `acoustic_horizon_regularity`
- `content/quantum-observable-universe/fluid-dynamics/core-levi-form.lean:164` — `core_levi_cond_aspect_bound`
- `content/quantum-observable-universe/fluid-dynamics/core-levi-form.lean:172` — `core_levi_cond_bound`
- `content/quantum-observable-universe/fluid-dynamics/core-levi-form.lean:106` — `core_levi_form`
- `content/quantum-observable-universe/fluid-dynamics/discrete-vortex-spectrum.lean:91` — `discrete_vortex_spectrum`
- `content/quantum-observable-universe/fluid-dynamics/helicity-conservation.lean:78` — `helicity_cwf_relation`
- `content/quantum-observable-universe/fluid-dynamics/root-of-unity-truncation.lean:73` — `root_of_unity_truncation_conditional`
- `content/quantum-observable-universe/fluid-dynamics/vorticity-lower-bound.lean:75` — `vorticity_lower_bound_conditional`
- `content/quantum-observable-universe/knots-particles-confinement/magic-shell-coupling-kappa.lean:82` — `kappa_closed_form_is_categorical`
- `content/quantum-observable-universe/lean/QOU/Archimedean/BranchingConvergence.lean:352` — `branching_convergence`
- `content/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeTranscendence.lean:699` — `tower_noncollapse_implies_independence`
- `content/quantum-observable-universe/lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean:171` — `brane_tower_finite`
- `content/quantum-observable-universe/lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean:71` — `term7_structural`
- `content/quantum-observable-universe/lean/QOU/Archimedean/OrderingIndependence.lean:113` — `skein_multiset_invariance_axiom`
- `content/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:795` — `convergence_rate`
- `content/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:599` — `qFact_ratio_bound`
- `content/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:406` — `qInt_ratio_bound_small`
- `content/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:709` — `wedderburn_weight_perturbation`
- `content/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean:1037` — `convergence_bound`
- `content/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean:1092` — `knot_invariant_convergence`
- `content/quantum-observable-universe/lean/QOU/Archimedean/TMCorrespondence.lean:317` — `matrixChain_eq_buildChains_axiom`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum.lean:94` — `gb_residue_spectral_sum`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/GradedTraceResidueSplit.lean:91` — `graded_trace_residue_split`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean:106` — `phi_q_tower_algebraic_stratification`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/QRogersPentagonArchimedean.lean:203` — `rogers_correction_leading_h_order`
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean:877` — `a4_betti_magnitude_closure`
- `content/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals.lean:210` — `amplitude_finite_sum`
- `content/quantum-observable-universe/lean/QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean:122` — `dressed_mass_from_substrate_split`
- `content/quantum-observable-universe/lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean:70` — `discrete_vortex_spectrum`
- `content/quantum-observable-universe/lean/QOU/FluidDynamics/ns_obstruction_tower.lean:46` — `ns_obstruction_tower`
- `content/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean:69` — `q_bkm_criterion`
- `content/quantum-observable-universe/lean/QOU/FluidDynamics/root_of_unity_truncation.lean:69` — `root_of_unity_truncation`
- `content/quantum-observable-universe/lean/QOU/Habiro/FlowSolution.lean:70` — `habiro_flow_solutions_realise_synthesis`
- `content/quantum-observable-universe/lean/QOU/HadronicMass.lean:470` — `neutron_pair_skein_approx`
- `content/quantum-observable-universe/lean/QOU/HadronicMass.lean:443` — `proton_pair_skein_approx`
- `content/quantum-observable-universe/lean/QOU/HadronicMass.lean:611` — `skein_mass_relation_holds`
- `content/quantum-observable-universe/lean/QOU/Information/p_bandwidth_bound.lean:95` — `p_bandwidth_bound`
- `content/quantum-observable-universe/lean/QOU/Infra/Polylogarithm.lean:157` — `beta3_via_class`
- `content/quantum-observable-universe/lean/QOU/Interactions/ConfinementSDP.lean:200` — `sdp_lp_projection`
- `content/quantum-observable-universe/lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:168` — `trefoil_topological_mass_eq_codata`
- `content/quantum-observable-universe/lean/QOU/Knot/FigureEightVolume.lean:116` — `saddle_eq_volume`
- `content/quantum-observable-universe/lean/QOU/MobiusEnergy.lean:148` — `MobiusEnergy`
- `content/quantum-observable-universe/lean/QOU/MotivesArchimedean.lean:163` — `factors_def`
- `content/quantum-observable-universe/lean/QOU/PAdicQuantumGroups.lean:170` — `padic_frobenius_relation_preserved`
- `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/GaugeTheory.lean:61` — `fiber_adjoint_involution_sq`
- `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:231` — `categorical_dq_squared_nonvanishing`
- `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:133` — `categorical_irreducible`
- `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:279` — `categorical_jet_prolongation`
- `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:259` — `kernelIncl_exact`
- `content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean:63` — `cat_eigenspace_decomposition`
- `content/quantum-observable-universe/lean/QOU/Torsion/JetProlongation.lean:61` — `jet_prolongation_C`
- `content/quantum-observable-universe/lean/QOU/Torsion/TopologicalMass.lean:88` — `topological_mass_decomposition`
- `content/quantum-observable-universe/lifting-and-descent/descent-lemma.lean:42` — `descent_surjective`
- `content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.lean:275` — `rho_eq_qdim_via_canonical_knot`
- `content/quantum-observable-universe/mass-theory/crystal-basis-resolves-mass-tower-open-problems.lean:10` — `crystal_basis_reduction`
- `content/quantum-observable-universe/mass-theory/descended-level-zero.lean:20` — `descended_level_zero`
- `content/quantum-observable-universe/mass-theory/he4-channel-active-set.lean:154` — `he4_strong_duality_value`
- `content/quantum-observable-universe/mass-theory/mass-side-kernel-formalize-first-gates.lean:95` — `mass_anchor_stable_forward`
- `content/quantum-observable-universe/mass-theory/mass-side-kernel-formalize-first-gates.lean:177` — `mass_direction_sanity_forward`
- `content/quantum-observable-universe/mass-theory/q-beta-direction-sanity-gate.lean:86` — `qbeta_direction_sanity_magnitude_match`
- `content/quantum-observable-universe/mass-theory/q-beta-q-eq-one-shadow-gate.lean:86` — `qbeta_q_eq_one_shadow_anchors`
- `content/quantum-observable-universe/mass-theory/q-beta-radius-of-convergence-gate.lean:102` — `qbeta_g_simple_pole_at_u_substrate`
- `content/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.lean:71` — `shared_denominator_cusp_holonomy`
- `content/quantum-observable-universe/models-of-qous/main-commutative-diagram.lean:78` — `diagram_commutes`
- `content/quantum-observable-universe/molecular-construction/h2s-angle-s3-braid-holonomy.lean:39` — `opening_eq_holonomy_of_conj`
- `content/quantum-observable-universe/nuclear-interactions/cpt-d6-d7-d8-closure.lean:66` — `cpt_closure`
- `content/quantum-observable-universe/nuclear-interactions/q-beta-spectral-bridge.lean:294` — `q_beta_spectral_conditional`
- `content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.lean:133` — `nu_selfConjugate`
- `content/quantum-observable-universe/quantum-observable-universes/contact-affine-chart.lean:66` — `ContactAffineChart.affineCoord_welldefined`
- `content/quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.lean:53` — `volume_form_is_nondegen`
- `content/quantum-observable-universe/quantum-universes/categorical-jet.lean:55` — `CategoricalJet.kernelIncl_exact`
- `content/quantum-observable-universe/quantum-universes/categorical-jet.lean:83` — `categorical_jet_prolongation`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`


## 1 of 78 drained (2026-09-04) — `q_beta_spectral_conditional`

`nuclear-interactions/q-beta-spectral-bridge.lean` — the disclosure sentence
this bean prescribes is now on the declaration.  Status left `todo`: 77 remain.

The old docstring was worse than absent — it *defended* the projection:
"Derived from the class field `forms_agree` — not a `sorry`-projection of an
unrelated conclusion."  As `docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md`
sets out, that answers the wrong objection: the §3b-cond item-5 complaint is not
that the conclusion is UNRELATED to the field but that it is IDENTICAL to it.
That audit already adjudicated this declaration `genuine` in the review ledger.

Recorded on the declaration: the class is honest (content-bearing, uninhabited
— the correct §3b-tax open state); only the wrapper is the defect, and it is a
DISCLOSURE defect, not a mathematical one.  The file's real content
(`q_beta_spectral_bridge`, three identities) is unconditional and is what
should be cited.

NOT done, deliberately: closing the wrapper properly needs the class to relate
`Q_beta_A`/`Q_beta_B` to the file's `(h, z)` forms so that agreement DERIVES
something (exact agreement would force `z = 1` via the ratio identity).  That
changes what the block claims — authorial, left open.

Verified: `lean`-direct **exit 0** with a COMPLETE sentinel written after the
process exited (not read from a possibly-truncated log), 0 error lines; the one
warning is a pre-existing unused `hzh` at line 87.
