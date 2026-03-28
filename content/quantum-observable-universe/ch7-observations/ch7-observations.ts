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
  number: 7,
  title: "Physical Observations",
  label: "chap:observations",
  sections: [
    // ── Central result: overdetermination of q ──────────────────────────
    section({
      title: "The Substrate Consistency Window",
      label: "sec:substrate-consistency",
      blocks: [
        "substrate-consistency-window",
      ],
    }),

    // ── Particle identification conjectures ────────────────────────────
    section({
      title: "Particle Identification Conjectures",
      label: "sec:particle-conjectures",
      blocks: [
        "borromean-quark",
        "higgs-t28",
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
        "hadron-half-life-verification",
        "hadron-half-life-regimes",
        "half-life-shell-worked",
        "half-life-as-q-probe",
        "tritium-decay-knot-equation",
        "nitrogen-14-threading",
        "trace-ratio-observable",
        "shell-threading-conjecture",
        "skein-shell-correction",
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
        "gravity-emergent-data",
        "topological-defects",
        "topological-defects-data",
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
      ],
    }),

    // ── Small-scale observations ──────────────────────────────────────
    section({
      title: "Small-Scale Observations",
      label: "sec:small-scale",
      blocks: [
        "photonic-hall",
        "photonic-hall-data",
        "fine-structure-observation",
        "fine-structure-data",
        "color-confinement-observation",
        "lepton-discrepancies",
        "lepton-anomalies-data",
        "proton-radius-puzzle",
        "proton-radius-data",
        "entropic-gravity",
        "entropic-gravity-data",
        "local-substrate-q",
        "local-substrate-q-proof",
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

    // ── Complexity and interpretation ──────────────────────────────────
    section({
      title: "Complexity and Interpretation",
      label: "sec:complexity-interpretation",
      blocks: [
        "complex-chirality-rotation",
        "trefoil-vortex-chirality-flip",
        "pair-creation-energy",
        "crossing-energy-decomposition",
        "crossing-energy-interpretation",
        "time-reversal-energy-barrier",
        "virtual-particles-exceptional-divisor",
        "cp-violation-evidence",
        "cosmological-chirality-flip",
        "electron-immortality",
      ],
    }),

    // ── Interactive simulations ───────────────────────────────────────
    section({
      title: "Interactive Simulations",
      label: "sec:simulations",
      blocks: [
        "q-double-slit",
        "double-slit-analytical",
        "brings-surface",
        "quantum-brings-surface",
      ],
    }),
  ],
});
