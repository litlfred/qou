import { chapter, section } from "../../schema/builders";

/**
 * Chapter 7: Observations and Experimental Evidence.
 *
 * All content below the Archimedean wall: the topological mass formula
 * (Archimedean specialisation of thm:topological-mass), double-slit
 * experiment, skein decomposition of hadronic mass, and large-/small-scale
 * observational predictions.  Builds on Descartes definitions from Ch. 5.
 */
export default chapter({
  number: 7,
  title: "Observations and Experimental Evidence",
  label: "chap:observations",
  sections: [
    // ── Archimedean mass formula (the wall) ───────────────────────────
    section({
      title: "Topological mass formula",
      label: "sec:topological-mass-ansatz",
      blocks: [
        "topological-mass-formula",
        "hyperbolic-volumes-prose",
        "knot-volumes-verification",
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

    // ── Skein decomposition and hadronic mass ─────────────────────────
    section({
      title: "Skein Decomposition and Hadronic Mass",
      label: "sec:skein-hadronic-mass",
      blocks: [
        "ch11-intro",
        "skein-decomposition",
        "skein-mass-relation",
        "skein-mass-relation-proof",
        "terminal-resolution",
        "terminal-resolution-proof",
        "terminal-resolution-cz",
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

    // ── Small-scale observations ──────────────────────────────────────
    section({
      title: "Small-Scale Observations",
      label: "sec:small-scale",
      blocks: [
        "mass-ratio-predictions",
        "mass-predictions-data",
        "mass-from-generators",
        "knot-formula-table",
        "mass-comparison-table",
        "photonic-hall",
        "photonic-hall-data",
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
