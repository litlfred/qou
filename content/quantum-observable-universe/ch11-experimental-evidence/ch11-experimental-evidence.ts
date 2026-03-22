import { chapter, section } from "../../schema/builders";

export default chapter({
  number: 9,
  title: "Experimental Evidence",
  label: "chap:experimental",
  sections: [
    section({
      title: "Skein Decomposition and Hadronic Mass",
      label: "sec:skein-hadronic-mass",
      blocks: [
        "skein-decomposition",
        "hyperbolic-volumes-prose",
        "skein-mass-relation",
        "skein-mass-relation-proof",
        "terminal-resolution",
        "terminal-resolution-proof",
        "ch11-intro",
      ],
    }),

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

    section({
      title: "Small-Scale Observations",
      label: "sec:small-scale",
      blocks: [
        "mass-ratio-predictions",
        "mass-predictions-data",
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
  ],
});
