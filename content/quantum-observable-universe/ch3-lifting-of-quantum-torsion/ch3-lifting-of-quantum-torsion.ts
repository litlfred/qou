import { chapter, section } from "../../schema/builders";

/**
 * Chapter 3: Lifting of Quantum Torsion.
 *
 * Covers jet prolongation, the recursive brane tower, Yekutieli lifting,
 * the main QOU theorem, cosimplicial structure, descent, mass decomposition,
 * and the quantum dilogarithm.
 */
export default chapter({
  number: 3,
  title: "Lifting of Quantum Torsion",
  label: "chap:torsion",
  sections: [
    section({
      title: "Jet Prolongation",
      label: "sec:jet-prolongation",
      blocks: [
        "jet-prolongation",
        "jet-prolongation-C",
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
        "qu-to-qou",
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
        "vacuum-state",
      ],
    }),

    section({
      title: "Mass in the Brane Tower",
      label: "sec:mass-brane",
      blocks: [
        "mass-geometric-drag",
        "mass-noncommutative-drag",
        "euler-char-stability",
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
        "jet-as-descent",
        "descent-condition",
        "weak-equiv-invariance",
      ],
    }),

    section({
      title: "Descent",
      label: "ssec:descent",
      blocks: [
        "descent-intro",
        "descent",
        "descent-lemma",
        "descent-involution",
        "descent-eigenspaces",
        "brane-boundary",
        "brane-boundary-structure",
        "descent-reduction",
        "descent-physical",
        "descent-reduction-zero",
        "descent-physical-zero",
        "descent-fixed-point",
      ],
    }),

    section({
      title: "Topological Decomposition of Mass",
      label: "sec:topological-mass",
      blocks: [
        "topological-mass",
        "quantum-dilogarithm",
        "qdlog-julia",
        "julia-s1-photon-scatter",
      ],
    }),
  ],
});
