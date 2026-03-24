import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6: The Descartes Universe.
 *
 * Opens with the Descartes condition and theorem (moved from the former
 * "Universes" chapter), followed by the topological mass ansatz, skein
 * decomposition, and experimental evidence at large and small scales.
 */
export default chapter({
  number: 6,
  title: "The Descartes Universe",
  label: "chap:descartes-universe",
  sections: [
    // ── Descartes theory (moved from ch6-descartes-universe) ──

    section({
      title: "The Descartes condition",
      label: "sec:descartes-condition",
      blocks: [
        "descent-to-zero",
        "descartes-condition",
        "descartes-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
      ],
    }),

    section({
      title: "Leptons and chirality",
      label: "sec:descartes-leptons-chirality",
      blocks: [
        "descartes-leptons",
        "descartes-chirality",
        "light-cone-affine",
      ],
    }),

    section({
      title: "Trefoil subgroups and Bring's curve",
      label: "sec:trefoil-brings",
      blocks: [
        "chirality-trefoil",
        "brings-curve",
      ],
    }),

    section({
      title: "Colour-sector coordinates on the exceptional fibre",
      label: "sec:colour-sector-coords",
      blocks: [
        "exceptional-divisor",
        "chiral-sector-coords",
      ],
    }),

    section({
      title: "Categorical braid structure",
      label: "sec:descartes-braid",
      blocks: [
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "skein-archimedean-shadow",
      ],
    }),

    section({
      title: "The Descartes theorem",
      label: "sec:descartes-theorem",
      blocks: [
        "descartes",
        "descartes-proof",
        "universality-general",
        "descartes-yekutieli",
        "observation-brings",
      ],
    }),

    // ── Mass conjecture and ansatz ──

    section({
      title: "Topological mass ansatz",
      label: "sec:topological-mass-ansatz",
      blocks: [
        "topological-mass-formula",
        "hyperbolic-volumes-prose",
      ],
    }),

    // ── Experimental evidence ──

    section({
      title: "Skein Decomposition and Hadronic Mass",
      label: "sec:skein-hadronic-mass",
      blocks: [
        "skein-decomposition",
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
