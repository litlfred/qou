import { chapter, section } from "../../schema/builders";

/**
 * Chapter 8: Information-Theoretic Perspectives.
 *
 * Emergent gravity from information geometry, Planck-scale information
 * units, information-theoretic time, Big Bang through an information
 * lens, computation at Planck time lengths, statistical mechanics,
 * and alternative Euler-characteristic scenarios.
 */
export default chapter({
  title: "Information-Theoretic Perspectives",
  label: "chap:info-theory",
  sections: [
    section({
      title: "Emergent Gravity and Information Geometry",
      label: "sec:info-emergent-gravity",
      blocks: [
        "information-theory-intro",
        "regime-table",
        "emergent-gravity-info",
        "planck-info-unit",
      ],
    }),
    section({
      title: "Time and Computation",
      label: "sec:info-time-computation",
      blocks: [
        "info-time-computation-intro",
        "time-info",
        "planck-time",
        "reeb-operations-per-planck",
        "information-theoretic-time",
        "statistical-mechanical-time",
        "statistical-mechanical-time-table-data",
        "big-bang-info",
        "planck-computation",
      ],
    }),
    section({
      title: "Golden Ratio, Julia Sets, and Discrete Dynamics",
      label: "sec:golden-julia-dynamics",
      blocks: [
        "golden-julia-dynamics-intro",
        "golden-ratio-transport",
        "julia-set-reeb",
        "operational-entropy",
        "discrete-planck-step",
        "jet-planck-steps",

        "jet-planck-steps-table1-data",
        "jet-planck-steps-table2-data",
      ],
    }),
section({
      title: "Speed of Light and Mass--Energy Equivalence",
      label: "sec:speed-of-light",
      blocks: [
        "speed-of-light-intro",
        "information-speed-of-light",
        "mass-energy-equivalence",
        "mass-energy-equivalence-proof",
        "photon-threading-mass",
        "gravitational-constant",
        "hausdorff-dimension-recurrence",
        "hausdorff-dimension-recurrence-table3-data",
        "hausdorff-dimension-recurrence-table2-data",
        "hausdorff-dimension-recurrence-table1-data",
        "information-causality",
      ],
    }),
    section({
      title: "Optical Fibres and 1D Quantum Channels",
      label: "sec:optical-fibre-1d-qou",
      blocks: [
        "optical-fibre-intro",
        "one-dim-qou-channel",
        "parallel-fibre-noninteraction",
        "parallel-fibre-noninteraction-proof",
        "fibre-channel-capacity",
        "photon-propagation-1d",
      ],
    }),
    section({
      title: "Computation at Planck Time Lengths",
      label: "sec:planck-scale-computation",
      blocks: [
        "planck-scale-computation-intro",
        "planck-scale-computation",
        "toffoli-transfer-matrix",
        "toffoli-q-and",
        "toffoli-lp-stability",
        "toffoli-lp-stability-table2-data",
        "toffoli-lp-stability-table1-data",
        "q-game-of-life",
        "q-game-of-life-proof",
        "substrate-computation",
        "quantum-computational-universality",
        "skein-turing-machine",
        "reeb-turing-completeness",
      ],
    }),
    section({
      title: "P versus NP as a Boundary Condition",
      label: "sec:p-vs-np-boundary",
      blocks: [
        "p-vs-np-boundary-intro",
        "computational-horizon",
        "p-bandwidth-bound",
        "p-vs-np-boundary",
        "p-vs-np-boundary-table2-data",
        "p-vs-np-boundary-table1-data",
        "p-vs-np-event-horizon",
        "p-vs-np-event-horizon-table2-data",
        "p-vs-np-event-horizon-table1-data",
        "qou-p-neq-np",
      ],
    }),
    section({
      title: "$q$-Heat kernel and spectral analysis",
      label: "sec:q-heat-kernel-analysis",
      blocks: [
        "q-heat-kernel-analysis-intro",
        "q-exponential-taylor",
        "q-gaussian-solves-q-heat",
        "q-heat-kernel-peter-weyl",
        "q-heat-kernel-peter-weyl-proof",
        "q-heat-kernel-peter-weyl-table-data",
        "q-heat-kernel-computational-fallback",
      ],
    }),
    section({
      title: "Statistical Mechanics",
      label: "sec:stat-mech",
      blocks: [
        "stat-mech-intro",
        "quantum-temperature",
        "quantum-temperature-interpretation",
        "quantum-pressure",
        "quantum-pressure-interpretation",
        "quantum-volume",
        "quantum-volume-interpretation",
        "quantum-ideal-gas-law",
        "quantum-ideal-gas-law-interpretation",
        "quantum-ideal-gas-law-interpretation-table-data",
        "boltzmann-constant",
        "gas-constant-derivation",
        "hydrogen-partition-function",
      ],
    }),
    section({
      title: "Phase Transitions and Sublimation",
      label: "sec:phase-transitions",
      blocks: [
        "phase-transitions-intro",
        "phase-transition-boundary",
        // P3 reorder (2026-05-19): composite-crossing-parity moved
        // before phase-transition-interpretation. The former uses
        // prop:shell-structure-eigenvalues + prop:noble-gas-
        // characterization (both in earlier chapters); the latter
        // interprets the parity test. The detangler-watcher flagged
        // phase-transition-interpretation → composite-crossing-parity
        // as an intra-section H1 forward ref; swap makes it a
        // backward ref, no new cascade.
        "composite-crossing-parity",
        "phase-transition-interpretation",
        "crossing-parity-test",
        "crossing-parity-test-table-data",
        "van-der-waals-hopf-channel",
        "hopf-link-symmetric-decomposition",
        "vdw-pskew-isolation",
        "molecular-hbond-phase-transition",
      ],
    }),
    section({
      title: "Incompleteness and the Horizon",
      label: "sec:incompleteness-horizon",
      blocks: [
        "incompleteness-horizon-intro",
        "incompleteness-implies-horizon",
        "incompleteness-horizon",
        "stat-mech-computational-horizon",
        "stat-mech-computational-horizon-table-data",
        "information-paradox-incompleteness",
      ],
    }),
    section({
      title: "Horizons and Aeons",
      label: "sec:horizons-aeons",
      blocks: [
        "horizons-aeons-intro",
        "jet-horizon",
        "big-bang-state",
        "cmb-boundary-datum",
        "cmb-photon-color-content",
        "hawking-radiation",
        "observable-subcategory",
        "aeon",
        "observable-beable-correspondence",
        "horizon-functor",
        "cmb-functor",
        "aeon-boundary-generates-chart",
        "horizon-conformal-invariance",
        "horizon-conformal-invariance-proof",
        "qou-is-ccc",
        "qou-is-ccc-proof",
        "penrose-ccc",
        "penrose-ccc-table-data",
      ],
    }),
    section({
      title: "Quantum Geometry Variants",
      label: "sec:info-geometry-variants",
      blocks: [
        "quantum-brings-intro",
        "other-euler-intro",
      ],
    }),
  ],
});
