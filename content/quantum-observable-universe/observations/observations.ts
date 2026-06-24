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
        "substrate-consistency-window-table4-data",
        "substrate-consistency-window-table3-data",
        "substrate-consistency-window-table2-data",
        "substrate-consistency-window-table1-data",
        "three-calibration-discipline",
        "three-calibration-discipline-proof",
      ],
    }),

    // ── Particle identification conjectures ────────────────────────────
    section({
      title: "Particle Identification Conjectures",
      label: "sec:particle-conjectures",
      blocks: [
        "particle-conjectures-intro",
        "borromean-quark",
        "borromean-quark-table-data",
        "higgs-t28",
        "s5-equivariant-torus-knots",
        "s5-equivariant-torus-knots-proof",
        "s5-equivariant-torus-knots-table-data",
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
        "substrate-from-leptons-intro",
        // Phase 7 orphan reconnection (2026-05-25):
        "epistemic-status-of-calibrations",
        "skein-mass-relation",
        "skein-mass-relation-proof",
        "knot-volumes-verification",
        "knot-volumes-verification-table2-data",
        "knot-volumes-verification-table1-data",
        "building-block-knots",

        "building-block-knots-table1-data",
        "building-block-knots-table2-data",
        "building-block-knots-table3-data",
        "building-block-knots-table4-data",
        "building-block-knots-table5-data",
        "building-block-knots-table6-data",
        "building-block-knots-table7-data",
      ],
    }),

    // ── Mass predictions vs CODATA ───────────────────────────────────
    // Detangler P17 split (2026-05-22): the 24-block
    // sec:mass-predictions was split into method + per-particle
    // outputs (12 blocks) and specific derivations (12 blocks).
    section({
      title: "Mass predictions: methodology and validation",
      label: "sec:mass-predictions-method",
      blocks: [
        "mass-predictions-intro",
        "stability-cubic-plot",
        "stability-cubic-plot-table-data",
        "neutron-prediction-comparison",
        "neutron-prediction-comparison-table-data",
        "q-stability-ranges",
        "q-stability-ranges-table-data",
        "mass-ratio-predictions",
        "mass-predictions-data",
        "mass-comparison-table",
        "mass-comparison-table-table4-data",
        "mass-comparison-table-table3-data",
        "mass-comparison-table-table2-data",
        "mass-comparison-table-table1-data",
        "atom-mass-full-hecke",
        "atom-mass-full-hecke-table-data",
      ],
    }),
    section({
      title: "Mass predictions vs Feynman amplitudes",
      label: "sec:mass-predictions-method-feynman-qou-comparison",
      blocks: [
        "mass-predictions-method-feynman-qou-comparison-intro",
        "feynman-qou-comparison",
        "feynman-qou-comparison-table2-data",
        "feynman-qou-comparison-table1-data",
        "neutron-proton-mass-splitting",
        "neutron-proton-mass-splitting-proof",
        "photon-channel-wedderburn-chain",
        "mass-formula-validation",

        "mass-formula-validation-table1-data",
        "mass-formula-validation-table2-data",
        "mass-formula-validation-table3-data",
        "mass-formula-validation-table4-data",
        "mass-formula-validation-table5-data",
        "mass-formula-validation-table6-data",
        "mass-formula-validation-table7-data",
        "mass-formula-validation-table8-data",
        "mass-formula-validation-table9-data",
      ],
    }),
    section({
      title: "Mass predictions: per-particle derivations",
      label: "sec:mass-predictions-derivations",
      blocks: [
        "mass-predictions-derivations-intro",
        "nucleon-borromean-topology",
        "nucleon-borromean-topology-proof",
        "pair-skein-mass-formula",
        "pair-skein-mass-formula-proof",
        "flavor-split-substrate",
        "flavor-split-substrate-proof",
        "dressed-quark-numerology-at-q0",
        // Phase 7 orphan reconnection (2026-05-25):
        "m-tau-knot-prediction",
      ],
    }),
    section({
      title: "Terminal resolution and the $W$-boson discrepancy",
      label: "sec:mass-predictions-derivations-terminal-resolution-proof",
      blocks: [
        "mass-predictions-derivations-terminal-resolution-proof-intro",
        "terminal-resolution-proof",
        "terminal-resolution-cz",
        "w-boson-mass-discrepancy",

        "w-boson-mass-discrepancy-table1-data",
        "w-boson-mass-discrepancy-table2-data",
        "w-boson-mass-discrepancy-table3-data",
        "w-boson-mass-discrepancy-table4-data",
        "w-boson-mass-discrepancy-table5-data",
        "w-boson-mass-discrepancy-table6-data",
        "w-boson-mass-discrepancy-table7-data",
      ],
    }),

    // ── Beta decay: half-lives and nuclear data ─────────────────────────
    // Detangler P18 split (2026-05-22): the 25-block
    // sec:beta-decay-observations was split into the categorical
    // β-decay mechanism (Q-value + half-life + tritium worked
    // example) and the magic-shell consequences (trace ratio,
    // double-magic LR-fusion, magic-numbers-from-q, Strutinsky).
    section({
      title:
        "Beta decay as $\\operatorname{Im}\\mathfrak{V}$: $Q$-values, half-life, and tritium",
      label: "sec:beta-decay-mechanism",
      blocks: [
        "beta-decay-observations-intro",
        "qvalue-observation",
        "qvalue-observation-table-data",
        "hadron-half-life-verification",

        "hadron-half-life-verification-table1-data",
        "hadron-half-life-verification-table2-data",
        "hadron-half-life-verification-table3-data",
        "hadron-half-life-verification-table4-data",
        "hadron-half-life-verification-table5-data",
        "hadron-half-life-verification-table6-data",
      ],
    }),
    section({
      title: "Half-life regimes and the $N_V$ tower",
      label: "sec:beta-decay-mechanism-hadron-half-life",
      blocks: [
        "beta-decay-mechanism-hadron-half-life-intro",
        "hadron-half-life-verification-table7-data",
        "hadron-half-life-regimes",
        "n-v-bring-action",
        "n-v-tower-depth-ninety",
        "n-v-leading-order-derivation",
        "half-life-shell-worked",
        "half-life-shell-worked-table-data",
        "half-life-as-q-probe",
        "finiteness-bound-interpretation",
        "tritium-decay-knot-equation",
        "tritium-qvalue-audit",
      ],
    }),
    section({
      title:
        "Beta decay: magic-shell structure and complex-volume consequences",
      label: "sec:beta-decay-magic-shells",
      blocks: [
        "beta-decay-magic-shells-intro",
        "nitrogen-14-threading",
        "trace-ratio-observable",
        "trace-ratio-observable-proof",
        "trace-ratio-interpretation",
        // Detangler R3 (2026-05-23): 6-row verification-nuclei
        // trace-ratio table extracted from
        // trace-ratio-interpretation.md.
        "trace-ratio-interpretation-table-data",
        "diagrammatic-double-magic-lr-fusion",
        "double-magic-Ca40-diagram",
        "double-magic-Ca40-diagram-table-data",
        "double-magic-delta-i-bound",
      ],
    }),
    section({
      title: "Magic numbers and the $k=12$ barrier",
      label: "sec:beta-decay-magic-shells-k12-barrier-bypass",
      blocks: [
        "beta-decay-magic-shells-k12-barrier-bypass-intro",
        "double-magic-delta-i-bound-table2-data",
        "double-magic-delta-i-bound-table1-data",
        "magic-numbers-from-q",
        "k12-barrier-bypass",
        "non-magic-Li6-diagram",
        "shell-threading-conjecture",
        "single-magic-O18-diagram",
        "bw-mass-decomposition-dictionary",
        // Detangler R3 (2026-05-23): 7-row BW-to-Schur-Weyl
        // dictionary extracted from bw-mass-decomposition-dictionary.md.
        "bw-mass-decomposition-dictionary-table-data",
        "strutinsky-from-graded-trace",
      ],
    }),

    // ── Large-scale observations ──────────────────────────────────────
    section({
      title: "Large-Scale Observations",
      label: "sec:large-scale",
      blocks: [
        "large-scale-intro",
        "cmb-q-torsion",
        "cmb-torsion-data",
        "gravity-emergent",
        "gravity-spectral-prefactor",
        "gravity-spectral-prefactor-proof",
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
        "nuclear-stability-observations-intro",
        "valley-table",
        // Detangler R3 (2026-05-23): 7-row representative-isotopes
        // table extracted from valley-table.md.
        "valley-table-data",
        "golden-ratio-degeneration",
        "hydrogen-knot-structure",

        "hydrogen-knot-structure-table1-data",
        "hydrogen-knot-structure-table2-data",
        "hydrogen-knot-structure-table3-data",
        "sdp-regime-switch",
        "sdp-regime-switch-table-data",
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
        "strangelet-crossing-energy-proof",
        "strangelet-witten-stability",

        // — Phase diagram: deconfinement, CFL, equation of state
        "deconfinement-golden-threshold",
        "hopf-diquark",
        "borromean-hopf-energy-crossover",
        "borromean-hopf-energy-crossover-proof",
        "borromean-hopf-energy-crossover-factor-250",
        "color-superconductivity-borromean",
        "eos-borromean-cfl",
        "eos-borromean-cfl-proof",
        "eos-borromean-cfl-table-data",

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
        "precision-tests-intro",
        "photonic-hall",
        "photonic-hall-data",
        "fine-structure-observation",
        "fine-structure-observation-table2-data",
        "fine-structure-observation-table1-data",
        "fine-structure-data",
        "color-confinement-observation",
        "color-confinement-observation-table-data",
        "confinement-curvature-rank",
        "physics-names-knot-operations",
        "physics-names-knot-operations-table-data",
        "lepton-discrepancies",
        "lepton-anomalies-data",
      ],
    }),

    // ── Proton radius and gravity ─────────────────────────────────────
    section({
      title: "Proton Radius and Gravity Tests",
      label: "sec:proton-gravity-tests",
      blocks: [
        "proton-gravity-tests-intro",
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
        "crystal-resonance-intro",
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
        "breit-wheeler-pair-creation-intro",
        "pair-creation-energy",
        "breit-wheeler-observation",
      ],
    }),

    // ── Complexity and interpretation ──────────────────────────────────
    section({
      title: "Complexity and Interpretation",
      label: "sec:complexity-interpretation",
      blocks: [
        "complexity-interpretation-intro",
        "fermion-boson-chart-localization",
        "complex-chirality-rotation",
        "trefoil-vortex-chirality-flip",
        "crossing-energy-decomposition",
        "crossing-energy-interpretation",
        "time-reversal-energy-barrier",
        "virtual-particles-exceptional-divisor",
        "vacuum-polarization-virtual-pairs",
        // Detangler R3 (2026-05-23): 6-row QFT-to-QOU dictionary
        // extracted from vacuum-polarization-virtual-pairs.md.
        "vacuum-polarization-virtual-pairs-table-data",
        "cp-violation-evidence",
        "cp-violation-spectral-form",
        "cosmological-chirality-flip",
        "electron-immortality",
      ],
    }),

    // ── Non-comm probability framework (broadly useful, resolves #649) ─
    section({
      title:
        "Non-Commutative Probability, the q-CLT, and the Archimedean Macroscopic Limit",
      label: "sec:non-comm-probability-q-clt",
      blocks: [
        "non-comm-probability-intro",
        "algebraic-gns-embedding",
        "algebraic-gns-embedding-proof",
        "algebraic-gns-embedding-cfs-consequence",
        "non-commutative-probability-dictionary",
        "non-commutative-probability-dictionary-table-data",
        "q-plancherel-asymptotic-skeleton",
        "centered-hecke-variance-positive",
        "centered-hecke-variance-positive-table-data",
        "centered-hecke-variance-positive-proof",
        "archimedean-macroscopic-washout",
        "brane-tower-q-laplacian-decay",
        "brane-tower-q-laplacian-decay-proof",
        "cfs-comparison-summary",
      ],
    }),

    // ── Transcendence falsifiability signatures ──────────────────────
    section({
      title: "Transcendence Falsifiability Signatures",
      label: "sec:transcendence-signatures",
      blocks: [
        "transcendence-signatures-intro",
        "observables-algebraic-independence",
      ],
    }),

    // ── Interactive simulations ───────────────────────────────────────
    section({
      title: "Interactive Simulations",
      label: "sec:simulations",
      blocks: [
        "simulations-intro",
        "q-double-slit",
        "double-slit-analytical",
        "brings-surface-simulator",
        "quantum-brings-surface",
        "beta-decay-simulator",
        "beta-decay-simulator-table-data",
        "outro-observations",
      ],
    }),
  ],
});
