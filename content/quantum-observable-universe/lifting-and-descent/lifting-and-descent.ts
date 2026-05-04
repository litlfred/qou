import { chapter, section } from "../../schema/builders";

/**
 * Lifting and Descent.
 *
 * Covers jet prolongation, the recursive brane tower, Yekutieli lifting,
 * the main QOU theorem, cosimplicial structure, descent, mass decomposition,
 * and the quantum dilogarithm.
 *
 * Hadron, proton/neutron, bundle, and topological-mass blocks moved to
 * braids-and-knots and q-geometric-langlands during
 * chapter restructuring (2026-03).
 */
export default chapter({
  title: "Lifting and Descent",
  label: "chap:torsion",
  sections: [
    // ── Foundations ─────────────────────────────────────────────────────
    // (Recursive Brane Tower merged here — only 2 blocks)
    section({
      title: "Jet Prolongation and the Recursive Brane Tower",
      label: "sec:jet-prolongation",
      blocks: [
        "jet-prolongation",
        "jet-prolongation-su2",
        "jet-prolongation-categorical-jet",
        "jet-prolongation-categorical-jet-proof",
        "jet-prolongation-proof",
        "prolongation-categorical",
        "recursive-brane-tower",
        "recursive-brane-tower-su2",
        "brane-tower-levels",
        "arc-space",
      ],
    }),

    // ── Categorical lifting ─────────────────────────────────────────────
    section({
      title: "Categorical Lifting: Transport and Torsion",
      label: "sec:lifting",
      blocks: [
        "lifting-intro",
        "categorical-jet-prolongation",
        "categorical-jet-prolongation-proof",
        "categorical-q-reeb-flow",
        "reeb-primes-as-orbits",
      ],
    }),

    // ── Descent primitives (only need jet + brane tower) ───────────────
    section({
      title: "Descent Preliminaries",
      label: "ssec:descent-prelim",
      blocks: [
        "descent-lemma",
        "descent-lemma-su2",
        "descent-lemma-proof",
        "descent-involution",
        "descent-involution-su2",
      ],
    }),

    // ── Yekutieli lifting (needed by cosimplicial + descent) ───────────
    section({
      title: "Categorical Lifting and Quantum Characteristic Classes",
      label: "sec:yekutieli-lifting",
      blocks: [
        "yekutieli-lifting-condition",
        "yekutieli-lifting-condition-su2",
        "quantum-characteristic-classes",
        "quantum-characteristic-classes-exists",
        "quantum-characteristic-classes-exists-proof",
        "quantum-characteristic-classes-unique",
        "quantum-characteristic-classes-unique-proof",
        "quantum-characteristic-classes-su2",
        "yekutieli-lifting",
        "yekutieli-lifting-su2",
        "yekutieli-lifting-proof",
        "qu-to-qou",
        "qu-to-qou-su2",
        "fermionic-twisted-sectors",
        "kummer-filtration-obstruction",
        "kummer-tower",
        "hochschild-kummer-connection",
        "motivic-galois-character",
        "qou-motivic-galois-instance",
        "motivic-perpetual-obstruction",
      ],
    }),

    // ── Algebraic infrastructure ───────────────────────────────────────
    section({
      title: "Direct Limit Algebra",
      label: "sec:direct-limit",
      blocks: [
        "direct-limit-algebra",
        "direct-limit-algebra-su2",
        "direct-limit-lusztig",
        "jet-shell",
        "stack-like-structure",
        "vacuum-state",
        "vacuum-state-proof",
        "vacuum-state-su2",
        "global-gluing",
        "global-gluing-proof",
        "ordering-jet-compatibility",
      ],
    }),

    section({
      title: "Mass in the Brane Tower",
      label: "sec:mass-brane",
      blocks: [
        "mass-noncommutative-drag",
        "euler-char-stability",
        "euler-char-stability-proof",
        "mass-identity",
        "mass-identity-exists",
        "mass-identity-exists-proof",
        "mass-identity-unique",
        "mass-identity-unique-proof",
        "mass-identity-su2",
        "homological-shell-condensation",
      ],
    }),

    section({
      title: "Betti Numbers and Harmonic Basis",
      label: "sec:betti-harmonic",
      blocks: [
        "betti-numbers-brane",
        "q-harmonic-basis-brane",
        "weight-space-decomposition-brane",
        "algebraic-filter-classification",
        "algebraic-filter",
        "distributional-connection",
      ],
    }),

    // ── Descent (must precede cosimplicial groupoid) ───────────────────
    section({
      title: "Descent",
      label: "ssec:descent",
      blocks: [
        "descent-intro",
        "descent-eigenspaces",
        "descent-eigenspaces-su2",
        "descent-eigenspaces-proof",
        "brane-boundary",
        "brane-boundary-su2",
        "brane-boundary-structure",
        "descent-reduction-zero",
        "descent-physical-zero",
        "descent-reduction",
        "descent-physical",
        "descent-fixed-point",
      ],
    }),

    // ── Cosimplicial structure (now all deps are upstream) ─────────────
    // (Yekutieli Categorical Mapping merged here — only 1 block)
    section({
      title: "Cosimplicial Crossed Groupoid Structure",
      label: "ssec:cosimplicial-crossed-groupoid",
      blocks: [
        "cosimplicial-intro",
        "yekutieli-triple",
        "cosimplicial-crossed-groupoid",
        "ccg-cosimplicial-identities",
        "ccg-cosimplicial-identities-proof",
        "ccg-crossed-module-structure",
        "ccg-crossed-module-structure-proof",
        "cosimplicial-crossed-groupoid-proof",
        "jet-as-descent",
        "descent-condition",
        "descent-cocycle-deviation",
        "descent-cocycle-deviation-proof",
        "descent-condition-proof",
        "weak-equiv-invariance",
        "weak-equiv-invariance-proof",
        "yekutieli-mapping-table",
      ],
    }),

    // ── Localized knots (trimmed — hadrons/particles moved out) ────────
    section({
      title: "Localized Knots",
      label: "sec:localized-knots",
      blocks: [
        "localized-knot-intro",
        "localized-knot",
      ],
    }),

    // ── Archimedean specialisations ──────────────────────────────────
    section({
      title: "Archimedean Specialisations",
      label: "sec:archimedean-lifting",
      blocks: [
        "jet-prolongation-C",
        "jet-prolongation-C-proof",
        "yekutieli-archimedean-band",
        "qu-to-qou-proof",
        "mass-identity-C",
        "mass-identity-C-proof",
        "mass-geometric-drag",
        "euler-char-stability-C",
        "brane-boundary-structure-proof",
        "quantum-dilogarithm",
        "quantum-dilogarithm-proof",
        "topological-mass-conjecture",
        "topological-mass-eigenspace-decomp",
        "topological-mass-eigenspace-decomp-proof",
        "topological-mass-holonomy",
        "topological-mass-holonomy-proof",
        "topological-mass-transient-localisation",
        "topological-mass-transient-localisation-proof",
        "topological-mass-dilogarithm",
        "topological-mass-dilogarithm-proof",
        "topological-mass-proof",
        "topological-mass-su2",
      ],
    }),
  ],
});
