import { chapter, section } from "../../schema/builders";

/**
 * Chapter 7: Physical Observations.
 *
 * CODATA/PDG comparisons, experimental predictions, and proposed
 * experiments.  All setup (knot→particle mapping, mass formulas,
 * skein decomposition) lives in Ch. 6 (The Descartes Universe);
 * this chapter is purely observational data and predictions.
 */
export default chapter({
  title: "Physical Observations",
  label: "chap:observations",
  sections: [
    // ── Central result: overdetermination of q ──────────────────────────
    section({
      title: "The Substrate Consistency Window",
      label: "sec:substrate-consistency",
      blocks: [
        "observations-intro",
        "substrate-consistency-window",
        "three-calibration-discipline",
      ],
    }),

    // ── Particle identification conjectures ────────────────────────────
    section({
      title: "Particle Identification Conjectures",
      label: "sec:particle-conjectures",
      blocks: [
        "borromean-quark",
        "higgs-t28",
        "s5-equivariant-torus-knots",
        "symmetry-preserving-leptons",
      ],
    }),

    // ── Double-slit experiment ────────────────────────────────────────
    section({
      title: "Double-slit experiment",
      label: "sec:double-slit-experiment",
      blocks: [
        "double-slit-intro",
        "double-slit-q-phase",
        "double-slit-massive-pattern",
        "double-slit-two-modes",
        "q-deformed-double-slit",
      ],
    }),

    // ── Substrate parameter from lepton masses ────────────────────────
    section({
      title: "Substrate Parameter from Lepton Masses",
      label: "sec:substrate-from-leptons",
      blocks: [
        "skein-mass-relation",
        "skein-mass-relation-proof",
        "knot-volumes-verification",
        "building-block-knots",
      ],
    }),

    // ── Mass predictions vs CODATA ───────────────────────────────────
    section({
      title: "Mass Predictions and CODATA Comparison",
      label: "sec:mass-predictions",
      blocks: [
        "stability-cubic-plot",
        "neutron-prediction-comparison",
        "q-stability-ranges",
        "mass-ratio-predictions",
        "mass-predictions-data",
        "mass-comparison-table",
        "atom-mass-full-hecke",
        "feynman-qou-comparison",
        "neutron-proton-mass-splitting",
        "photon-channel-wedderburn-chain",
        "mass-formula-validation",
        "nucleon-borromean-topology",
        "nucleon-borromean-topology-proof",
        "pair-skein-mass-formula",
        "pair-skein-mass-formula-proof",
        "nucleon-mass-splitting",
        "nucleon-mass-splitting-proof",
        "deuteron-binding-energy",
        "deuteron-binding-energy-proof",
        "terminal-resolution-proof",
        "terminal-resolution-cz",
        "w-boson-mass-discrepancy",
      ],
    }),

    // ── Beta decay: half-lives and nuclear data ─────────────────────────
    section({
      title: "Beta Decay",
      label: "sec:beta-decay-observations",
      blocks: [
        "qvalue-observation",
        "hadron-half-life-verification",
        "hadron-half-life-regimes",
        "n-v-bring-action",
        "n-v-tower-depth-ninety",
        "n-v-leading-order-derivation",
        "half-life-shell-worked",
        "half-life-as-q-probe",
        "finiteness-bound-interpretation",
        "tritium-decay-knot-equation",
        "tritium-qvalue-audit",
        "nitrogen-14-threading",
        "trace-ratio-observable",
        "trace-ratio-interpretation",
        "diagrammatic-double-magic-lr-fusion",
        "double-magic-Ca40-diagram",
        "double-magic-delta-i-bound",
        "k12-barrier-bypass",
        "magic-numbers-from-q",
        "non-magic-Li6-diagram",
        "shell-threading-conjecture",
        "single-magic-O18-diagram",
        "bw-mass-decomposition-dictionary",
        "strutinsky-from-graded-trace",
      ],
    }),

    // ── Large-scale observations ──────────────────────────────────────
    section({
      title: "Large-Scale Observations",
      label: "sec:large-scale",
      blocks: [
        "cmb-q-torsion",
        "cmb-torsion-data",
        "gravity-emergent",
        "gravity-spectral-prefactor",
        "g-q-closed-form",
        "gravity-emergent-data",
        "topological-defects",
        "topological-defects-data",
        "ns-blowup-physical-evidence",
      ],
    }),

    // ── Nuclear stability and the valley ────────────────────────────────
    section({
      title: "Nuclear Stability",
      label: "sec:nuclear-stability-observations",
      blocks: [
        "valley-table",
        "golden-ratio-degeneration",
        "hydrogen-knot-structure",
        "sdp-regime-switch",
      ],
    }),

    // ── Strangelet stability ─────────────────────────────────────────────
    // Three subsections: (1) why strange matter binds harder,
    // (2) what happens at extreme density, (3) how to observe it.
    section({
      title: "Strangelet Stability and Deconfinement",
      label: "sec:strangelet-stability",
      blocks: [
        "strangelet-intro",

        // — Why strange matter binds harder (and why it's not the ground state)
        "strangelet-crossing-energy",
        "strangelet-witten-stability",

        // — Phase diagram: deconfinement, CFL, equation of state
        "deconfinement-golden-threshold",
        "hopf-diquark",
        "borromean-hopf-energy-crossover",
        "color-superconductivity-borromean",
        "eos-borromean-cfl",

        // — Observable signatures
        "cfl-neutron-star-observables",
        "strangelet-merger-signature",
        "strangelet-double-beta",
      ],
    }),

    // ── Precision tests ─────────────────────────────────────────────
    // (P8 split: 21-block sec:small-scale → 3 focused sections)
    section({
      title: "Precision Tests",
      label: "sec:precision-tests",
      blocks: [
        "photonic-hall",
        "photonic-hall-data",
        "fine-structure-observation",
        "fine-structure-data",
        "color-confinement-observation",
        "confinement-curvature-rank",
        "physics-names-knot-operations",
        "lepton-discrepancies",
        "lepton-anomalies-data",
      ],
    }),

    // ── Proton radius and gravity ─────────────────────────────────────
    section({
      title: "Proton Radius and Gravity Tests",
      label: "sec:proton-gravity-tests",
      blocks: [
        "proton-radius-puzzle",
        "proton-radius-data",
        "entropic-gravity",
        "entropic-gravity-data",
        "local-substrate-q",
        "local-substrate-q-proof",
      ],
    }),

    // ── Crystal resonance experiments ─────────────────────────────────
    section({
      title: "Crystal Resonance Experiments",
      label: "sec:crystal-resonance",
      blocks: [
        "crystal-probe-q",
        "substrate-telescope",
        "magnetic-friction",
        "crystal-resonance-data",
        "lattice-layout",
        "crystal-resonance-planned",
        "crystal-resonance-experiments",
        "bec-vortex-data",
      ],
    }),

    // ── Breit–Wheeler pair creation ────────────────────────────────────
    section({
      title: "Breit--Wheeler Pair Creation",
      label: "sec:breit-wheeler-pair-creation",
      blocks: [
        "breit-wheeler-observation",
        "pair-creation-energy",
      ],
    }),

    // ── Complexity and interpretation ──────────────────────────────────
    section({
      title: "Complexity and Interpretation",
      label: "sec:complexity-interpretation",
      blocks: [
        "fermion-boson-chart-localization",
        "complex-chirality-rotation",
        "trefoil-vortex-chirality-flip",
        "crossing-energy-decomposition",
        "crossing-energy-interpretation",
        "time-reversal-energy-barrier",
        "virtual-particles-exceptional-divisor",
        "vacuum-polarization-virtual-pairs",
        "cp-violation-evidence",
        "cp-violation-spectral-form",
        "cosmological-chirality-flip",
        "electron-immortality",
      ],
    }),

    // ── Causal Fermion Systems comparison ──────────────────────────────
    section({
      title:
        "Causal Fermion Systems and the Algebraic Causal-Action Structure",
      label: "sec:causal-fermion-systems",
      blocks: [
        "causal-fermion-systems-intro",
        "algebraic-causal-action-structure",
        "algebraic-causal-action-structure-proof",
        "cfs-algebraic-mirror",
        "algebraic-gns-embedding",
        "algebraic-gns-embedding-proof",
        "q-plancherel-asymptotic-skeleton",
        "cfs-as-traceful-projection-of-qou",
        "mu-arch-continuum-limit",
        "cfs-as-archimedean-shadow",
      ],
    }),

    // ── Transcendence falsifiability signatures ──────────────────────
    section({
      title: "Transcendence Falsifiability Signatures",
      label: "sec:transcendence-signatures",
      blocks: [
        "observables-algebraic-independence",
        "observables-algebraic-dependence",
      ],
    }),

    // ── Interactive simulations ───────────────────────────────────────
    section({
      title: "Interactive Simulations",
      label: "sec:simulations",
      blocks: [
        "q-double-slit",
        "double-slit-analytical",
        "brings-surface-simulator",
        "quantum-brings-surface",
        "beta-decay-simulator",
      ],
    }),
  ],
});
