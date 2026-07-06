import os
import re

# We will scan content/quantum-observable-universe/ to find all .md files.
md_files = []
for root, dirs, files in os.walk("/Users/litlfred/space_cats/qou/content/quantum-observable-universe/"):
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(root, f))

# Let's list some of the candidates
candidates = [
    "variational_equations.lean",
    "q_gl_obstruction_calc.lean",
    "orbital_fourier_decomposition.lean",
    "qou_canonical_action.lean",
    "MassEndomorphism/PhiQConvergence.lean",
    "Interactions/QIntegerMassFormula.lean",
    "Archimedean/skein_finiteness_bound.lean",
    "Archimedean/torus_knot_shell_binding.lean",
    "Archimedean/shell_structure_eigenvalues.lean",
    "Archimedean/HyperbolicVolumeIndependence.lean",
    "Archimedean/EmCouplingBringZeroMode.lean",
    "Archimedean/skein_polynomial_transfer_matrix.lean",
    "Archimedean/em_coupling_projection.lean",
    "Archimedean/parity_violation_skein.lean",
    "Archimedean/skew_poisson_integration.lean",
    "Archimedean/reidemeister_action_table.lean",
    "QuantumBloch/pentagon_uv_commutation.lean",
    "ParticleInteractions/tritium_qvalue_symbolic.lean",
    "ParticleInteractions/demand_stability.lean",
    "ParticleInteractions/atomic_nf_witness.lean",
    "ParticleInteractions/parity_regime_selection.lean",
    "ParticleInteractions/four_term_pair_nucleon.lean",
    "ParticleInteractions/confinement_frobenius_reciprocity.lean",
    "ParticleInteractions/operator_selection_lp.lean",
    "ParticleInteractions/ground_state_ordering.lean",
    "ParticleInteractions/mass_categorical_descent.lean",
    "ParticleInteractions/transfer_matrix_identities.lean",
    "ParticleInteractions/frobenius_positivity_filter.lean",
    "ParticleInteractions/lp_dual_stability.lean",
    "ParticleInteractions/PerNucleonChannelDecomposition.lean",
    "ParticleInteractions/positron_correction.lean",
    "ParticleInteractions/SpectatorNormalization.lean",
    "QuantumObservableUniverse/fibre_functor_atlas.lean",
    "QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean",
    "Substrate/ProtonMassSubstrateIdentity.lean",
    "FluidDynamics/quantum_peter_weyl.lean",
    "FluidDynamics/core_levi_form.lean",
    "FluidDynamics/q_turbulence_spectrum.lean",
    "FluidDynamics/root_of_unity_truncation.lean",
    "FluidDynamics/helicity_conservation.lean",
    "FluidDynamics/kelvin_dispersion_derivation.lean",
    "FluidDynamics/q_ns_wellposedness.lean",
    "FluidDynamics/vorticity_lower_bound.lean",
    "FluidDynamics/acoustic_horizon_conditions.lean",
    "HyperellipticQuintic/minimal_z5_classification.lean",
    "BaryonWeight/beta4_hook.lean",
    "Molecular/shell_filling_rule.lean",
    "LiftingDescent/JetProlongation.lean",
    "LiftingDescent/jp_categorical_jet.lean",
    "LiftingDescent/tm_eigenspace_decomp.lean",
    "LiftingDescent/tm_descended_is_holonomy.lean",
    "LiftingDescent/tm_dilogarithm_evaluation.lean",
    "LiftingDescent/tm_transient_localisation.lean",
    "BraidKnot/SymmetricCrystalPairProduction.lean",
    "BraidKnot/HeckeAnyonicSubstrate.lean",
    "BraidKnot/GSReductionOrder.lean",
    "BraidKnot/KazhdanLusztigClassicalLimit.lean",
    "BraidKnot/CemeteryGroupEmergence.lean",
    "BraidKnot/ConfinementGradingCorrespondence.lean",
    "BraidKnot/RootOfUnityMTCTruncation.lean",
    "ArchimedeanUniverse/mi_sw_cartan_reduction.lean",
    "ArchimedeanUniverse/heisenberg_commutator.lean",
    "FrobeniusHopfData/frobeniusForm.lean",
    "Brings/coral_elliptic.lean",
    "Brings/brings_is_qou.lean",
    "Observations/brane_tower_q_laplacian_decay.lean",
    "Observations/QPlancherelAsymptoticSkeleton.lean",
    "Observations/SDPRegimeSwitch.lean",
    "Observations/strangelet_crossing_energy.lean",
    "Observations/centered_hecke_variance_positive.lean",
    "Observations/hecke_satisfies_blitvic_hypothesis.lean",
    "Observations/substrate_consistency_window.lean",
    "FeynmanPathIntegrals/markov_identification.lean",
    "AppendixSurreals/BigbangHeatdeath.lean",
    "Descent/descended_level_zero.lean",
    "Interactions/BorromeanUnique.lean",
    "ParticleInteractions/deuterium_derived_binding.lean",
    "BraidKnot/JucysMurphyCentralElementsQOU.lean"
]

base_dir = "/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/"

# For each candidate, find if its filename (without extension) is mentioned in any .md file
# or if there is a .md file with a similar name.
for cand in candidates:
    cand_name = os.path.basename(cand)
    name_no_ext = os.path.splitext(cand_name)[0]
    
    matches = []
    # Search mentions in .md files
    for md_path in md_files:
        rel_md = os.path.relpath(md_path, "/Users/litlfred/space_cats/qou/content/quantum-observable-universe/")
        # Read the first few lines / check if mentions name_no_ext
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
            if name_no_ext in content:
                matches.append((rel_md, "content_mention"))
            elif name_no_ext.replace("_", "-") in rel_md or name_no_ext.lower() in rel_md.lower():
                matches.append((rel_md, "filename_match"))
        except Exception as e:
            pass
            
    if matches:
        print(f"Candidate: {cand}")
        for match, reason in matches:
            print(f"  -> {match} ({reason})")
