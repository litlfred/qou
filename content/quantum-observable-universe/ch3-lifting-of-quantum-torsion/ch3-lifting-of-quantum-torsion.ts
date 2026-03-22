import { chapter, section } from "../../schema/builders";

/**
 * Lifting and Descent.
 *
 * Covers jet prolongation, the recursive brane tower, Yekutieli lifting,
 * the main QOU theorem, cosimplicial structure, descent, mass decomposition,
 * and the quantum dilogarithm.
 */
export default chapter({
  number: 3,
  title: "Lifting and Descent",
  label: "chap:torsion",
  sections: [
    section({
      title: "Jet Prolongation",
      label: "sec:jet-prolongation",
      blocks: [
        "jet-prolongation",
        "jet-prolongation-proof",
        "jet-prolongation-C",
        "jet-prolongation-C-proof",
        "prolongation-categorical",
      ],
    }),

    section({
      title: "Recursive Brane Tower",
      label: "sec:recursive-brane-tower",
      blocks: [
        "recursive-brane-tower",
        "brane-tower-levels",
      ],
    }),

    section({
      title: "Yekutieli Lifting and Quantum Characteristic Classes",
      label: "sec:yekutieli-lifting",
      blocks: [
        "yekutieli-lifting-condition",
        "quantum-characteristic-classes",
        "yekutieli-archimedean-band",
        "yekutieli-lifting",
        "yekutieli-lifting-proof",
        "qu-to-qou",
        "qu-to-qou-proof",
        "fermionic-twisted-sectors",
      ],
    }),

    section({
      title: "Betti Numbers and Harmonic Basis",
      label: "sec:betti-harmonic",
      blocks: [
        "betti-numbers-brane",
        "q-harmonic-basis-brane",
        "weight-space-decomposition-brane",
        "algebraic-filter",
        "distributional-connection",
      ],
    }),

    section({
      title: "Direct Limit Algebra",
      label: "sec:direct-limit",
      blocks: [
        "direct-limit-algebra",
        "direct-limit-lusztig",
        "jet-shell",
        "stack-like-structure",
        "global-gluing",
        "global-gluing-proof",
        "vacuum-state",
        "vacuum-state-proof",
      ],
    }),

    section({
      title: "Mass in the Brane Tower",
      label: "sec:mass-brane",
      blocks: [
        "mass-geometric-drag",
        "mass-noncommutative-drag",
        "euler-char-stability",
        "euler-char-stability-proof",
        "mass-identity",
        "mass-identity-C",
      ],
    }),

    section({
      title: "Yekutieli Categorical Mapping",
      label: "sec:yekutieli-mapping",
      blocks: [
        "yekutieli-mapping-table",
      ],
    }),

    section({
      title: "Cosimplicial Crossed Groupoid Structure",
      label: "ssec:cosimplicial-crossed-groupoid",
      blocks: [
        "cosimplicial-intro",
        "yekutieli-triple",
        "cosimplicial-crossed-groupoid",
        "cosimplicial-crossed-groupoid-proof",
        "jet-as-descent",
        "descent-condition",
        "descent-condition-proof",
        "weak-equiv-invariance",
        "weak-equiv-invariance-proof",
      ],
    }),

    section({
      title: "Descent",
      label: "ssec:descent",
      blocks: [
        "descent-intro",
        "descent",
        "descent-lemma",
        "descent-lemma-proof",
        "descent-involution",
        "descent-eigenspaces",
        "descent-eigenspaces-proof",
        "brane-boundary",
        "brane-boundary-structure",
        "brane-boundary-structure-proof",
        "descent-reduction",
        "descent-physical",
        "descent-reduction-zero",
        "descent-physical-zero",
        "descent-fixed-point",
      ],
    }),

    section({
      title: "Localized Knots, Hadrons, and Bundle Initial Conditions",
      label: "sec:localized-knots-bundles",
      blocks: [
        "localized-knot-intro",
        "localized-knot",
        "hadron",
        "localized-hadron",
        "bundle-initial-conditions",
        "bundle-isotopy-equivalence",
        "knot-particle-dictionary",
        "torsion-knot-flow",
        "bundle-category",
      ],
    }),

    section({
      title: "Topological Decomposition of Mass",
      label: "sec:topological-mass",
      blocks: [
        "topological-mass",
        "topological-mass-proof",
        "quantum-dilogarithm",
        "qdlog-julia",
        "julia-s1-photon-scatter",
      ],
    }),
  ],
});
