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
        "planck-time-interpretation",
        "information-theoretic-time",
        "reeb-operations-per-planck",
        "reeb-operations-per-planck-proof",
        "reeb-operations-per-planck-physical",
        "information-theoretic-time-properties",
        "information-theoretic-time-julia-microscopic",
        "information-theoretic-time-arrow",
        "statistical-mechanical-time",
        "statistical-mechanical-time-table-data",
        "big-bang-info",
        "planck-computation",
        // Ledger §5 orphan integration (2026-07-12): interpretive remark
        // on computational time, categorical dynamics, and the proposed
        // four-domain Planck-step dictionary.
        "computational-spacetime-observer",
        // Decision 7: the hbar_q / Reeb-coefficient result and its two
        // qualifications — the finite-q gradient/Reeb mixing, and the
        // share-versus-total reading of the two Planck lengths.
        "reeb-coefficient-is-hbar-q",
        "connes-distance-not-reeb-step-count",
        "planck-length-share-vs-total",
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
        "operational-entropy-properties",
        "discrete-planck-step",
        "planck-step-arithmetic-realisations",
        "golden-threshold-time-marker",
        "jet-planck-steps",
        "jet-planck-steps-table1-data",
        "jet-planck-steps-table2-data",
        "jet-planck-particle-spectrum",
        "jet-planck-encodability-vs-scattering",

      ],
    }),
section({
      title: "Speed of Light and Mass--Energy Equivalence",
      label: "sec:speed-of-light",
      blocks: [
        "speed-of-light-intro",
        "information-speed-of-light",
        "information-bandwidth",
        "speed-of-light-regimes-lieb-robinson",
        "mass-energy-equivalence",
        "mass-energy-equivalence-proof",
        "mass-energy-equivalence-interpretation",
        "mass-energy-electron-check",
        "mass-energy-pair-creation",
        "photon-threading-mass",
        "photon-threading-mass-interpretation",
        "gravitational-constant",
        "gravitational-constant-properties",
        "operational-entropy-self-consistency",
        "julia-hausdorff-dimension-prediction",
        "hausdorff-dimension-recurrence",
        "hausdorff-dimension-recurrence-table3-data",
        "hausdorff-dimension-recurrence-table2-data",
        "hausdorff-dimension-recurrence-table1-data",
        "hausdorff-dimension-classical-comparison",
        "information-causality",
        "information-causality-table-data",
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
        "dsr-planck-scale-phenomenology",
        "dispersion-suppression-scale",
        "regime-table",
      ],
    }),
    section({
      title: "Computation at Planck Time Lengths",
      label: "sec:planck-scale-computation",
      blocks: [
        "planck-scale-computation-intro",
        "planck-scale-computation",
        "toffoli-transfer-matrix",
        "toffoli-transfer-matrix-proof",
        "toffoli-transfer-matrix-interpretation",
        "toffoli-q-and",
        "toffoli-lp-stability",
        "toffoli-lp-stability-proof",
        "toffoli-lp-stability-table2-data",
        "toffoli-lp-stability-table1-data",
        "q-game-of-life",
        "q-game-of-life-proof",
        "q-game-of-life-interpretation",
        "substrate-computation",
        "reeb-turing-completeness-classical",
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
        "p-bandwidth-bound-proof",
        "p-bandwidth-interpretation",
        "polynomial-observable-subcategory",
        "computational-boundary",
        "p-vs-np-boundary",
        "p-vs-np-boundary-table2-data",
        "p-vs-np-boundary-table1-data",
        "p-vs-np-boundary-interpretation",
        "p-vs-np-event-horizon",
        "p-vs-np-event-horizon-table2-data",
        "p-vs-np-event-horizon-table1-data",
        "qou-p-neq-np",
        // Skein-observation bridge (2026-07-25): the trichotomy remark —
        // q-Collatz halting, P vs NP, and q-NS regularity as one length-
        // filtration question on the Skein substrate (interprets the
        // computational horizon; formalized in QOU.Information.
        // SkeinObservationSystem).
        "skein-filtration-trichotomy",
        "geometry-of-incompleteness",
      ],
    }),
    section({
      title: "$q$-Heat kernel and spectral analysis",
      label: "sec:q-heat-kernel-analysis",
      blocks: [
        "q-heat-kernel-analysis-intro",
        "q-exponential-taylor",
        "q-exponential-taylor-proof",
        "q-gaussian-solves-q-heat",
        "q-gaussian-solves-q-heat-proof",
        "q-gaussian-solves-q-heat-interpretation",
        "q-heat-kernel-peter-weyl",
        "q-heat-kernel-peter-weyl-proof",
        "q-heat-kernel-peter-weyl-table-data",
        "q-heat-kernel-peter-weyl-interpretation",
        "q-heat-kernel-computational-fallback",
      ],
    }),
    section({
      title: "Statistical Mechanics",
      label: "sec:stat-mech",
      blocks: [
        "stat-mech-intro",
        "quantum-entropy",
        "quantum-temperature",
        "quantum-temperature-interpretation",
        "quantum-pressure",
        "quantum-pressure-interpretation",
        "quantum-volume",
        "quantum-volume-interpretation",
        "quantum-ideal-gas-law",
        "quantum-ideal-gas-law-proof",
        "quantum-ideal-gas-law-interpretation",
        "quantum-ideal-gas-law-interpretation-table-data",
        "boltzmann-constant",
        "boltzmann-constant-motivation",
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
        "composite-crossing-sublimation-criteria",
        "phase-transition-interpretation",
        "crossing-parity-test",
        "crossing-parity-test-table-data",
        "van-der-waals-hopf-channel",
        "hopf-link-symmetric-decomposition",
        "hopf-link-symmetric-decomposition-van-der-waals-reading",
        "vdw-pskew-isolation",
        "vdw-pskew-isolation-interpretation",
        "molecular-hbond-phase-transition",
      ],
    }),
    section({
      title: "Incompleteness and the Horizon",
      label: "sec:incompleteness-horizon",
      blocks: [
        "incompleteness-horizon-intro",
        "incompleteness-implies-horizon",
        "incompleteness-implies-horizon-proof",
        "incompleteness-horizon-nontriviality",
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
        "big-bang-state-jet-horizon",
        "cmb-boundary-datum",
        "cmb-photon-color-content",
        "hawking-radiation",
        "incompleteness-horizon",
        "observable-subcategory",
        "aeon",
        "aeon-boundary",
        "aeon-adjacency",
        "observable-beable-correspondence",
        "horizon-functor",
        "cmb-functor",
        "aeon-boundary-generates-chart",
        "horizon-conformal-invariance",
        "horizon-conformal-invariance-proof",
        "horizon-conformal-invariance-interpretation",
        "qou-is-ccc",
        "qou-is-ccc-proof",
        "penrose-ccc",
        "penrose-ccc-table-data",
      ],
    }),
    section({
      title: "Connections to the Swampland Program",
      label: "sec:swampland-connections",
      blocks: [
        "swampland-connections-intro",
        "swampland-no-global-symmetry",
        "swampland-distance-conjecture",
        "swampland-island-of-consistency",
        "swampland-emergent-coupling",
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
