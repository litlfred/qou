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
        "time-info",
        "planck-time",
        "reeb-operations-per-planck",
        "information-theoretic-time",
        "statistical-mechanical-time",
        "big-bang-info",
        "planck-computation",
      ],
    }),
    section({
      title: "Golden Ratio, Julia Sets, and Discrete Dynamics",
      label: "sec:golden-julia-dynamics",
      blocks: [
        "golden-ratio-transport",
        "julia-set-reeb",
        "operational-entropy",
        "discrete-planck-step",
        "jet-planck-steps",
      ],
    }),
section({
      title: "Speed of Light and Mass--Energy Equivalence",
      label: "sec:speed-of-light",
      blocks: [
        "information-speed-of-light",
        "mass-energy-equivalence",
        "photon-threading-mass",
        "gravitational-constant",
        "hausdorff-dimension-recurrence",
        "information-causality",
      ],
    }),
    section({
      title: "Computation at Planck Time Lengths",
      label: "sec:planck-scale-computation",
      blocks: [
        "planck-scale-computation",
        "toffoli-transfer-matrix",
        "toffoli-q-and",
        "toffoli-lp-stability",
        "q-game-of-life",
        "substrate-computation",
        "quantum-computational-universality",
        "skein-turing-machine",
      ],
    }),
    section({
      title: "P versus NP as a Boundary Condition",
      label: "sec:p-vs-np-boundary",
      blocks: [
        "computational-horizon",
        "skein-resolution-obstruction",
        "p-bandwidth-bound",
        "p-vs-np-boundary",
        "p-vs-np-event-horizon",
        "qou-p-neq-np",
      ],
    }),
    section({
      title: "$q$-Heat kernel and spectral analysis",
      label: "sec:q-heat-kernel-analysis",
      blocks: [
        "q-exponential-taylor",
        "q-gaussian-solves-q-heat",
        "q-heat-kernel-peter-weyl",
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
        "boltzmann-constant",
        "gas-constant-derivation",
        "hydrogen-partition-function",
      ],
    }),
    section({
      title: "Phase Transitions and Sublimation",
      label: "sec:phase-transitions",
      blocks: [
        "phase-transition-boundary",
        "phase-transition-interpretation",
        "composite-crossing-parity",
        "crossing-parity-test",
      ],
    }),
    section({
      title: "Incompleteness and the Horizon",
      label: "sec:incompleteness-horizon",
      blocks: [
        "incompleteness-implies-horizon",
        "incompleteness-horizon",
        "stat-mech-computational-horizon",
        "information-paradox-incompleteness",
      ],
    }),
    section({
      title: "Horizons and Aeons",
      label: "sec:horizons-aeons",
      blocks: [
        "jet-horizon",
        "big-bang-state",
        "cmb-boundary-datum",
        "cmb-photon-color-content",
        "hawking-radiation",
        "observable-subcategory",
        "aeon",
        "horizon-functor",
        "cmb-functor",
        "aeon-boundary-generates-chart",
        "horizon-conformal-invariance",
        "qou-is-ccc",
        "penrose-ccc",
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
