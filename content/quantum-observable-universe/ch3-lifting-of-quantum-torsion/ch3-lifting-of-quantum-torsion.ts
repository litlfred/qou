import { chapter, section } from "../../schema/builders";

/**
 * Lifting and Descent.
 *
 * Covers jet prolongation, the recursive brane tower, Yekutieli lifting,
 * the main QOU theorem, cosimplicial structure, descent, mass decomposition,
 * and the quantum dilogarithm.
 *
 * Hadron, proton/neutron, bundle, and topological-mass blocks moved to
 * ch4-path-integrals-and-braiding and ch11-experimental-evidence during
 * chapter restructuring (2026-03).
 */
export default chapter({
  number: 3,
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
        "jet-prolongation-proof",
        "prolongation-categorical",
        "recursive-brane-tower",
        "brane-tower-levels",
      ],
    }),

    // ── Categorical lifting (from ch2 elaboration) ─────────────────────
    section({
      title: "Categorical Lifting: Transport and Torsion",
      label: "sec:lifting",
      blocks: [
        "lifting-intro",
        "categorical-jet-prolongation",
        "categorical-jet-prolongation-proof",
        "categorical-transport",
        "categorical-q-reeb-flow",
        "categorical-q-torsion-leaf",
      ],
    }),

    // ── Descent primitives (only need jet + brane tower) ───────────────
    section({
      title: "Descent Preliminaries",
      label: "ssec:descent-prelim",
      blocks: [
        "descent-lemma",
        "descent-lemma-proof",
        "descent-involution",
      ],
    }),

    // ── Yekutieli lifting (needed by cosimplicial + descent) ───────────
    section({
      title: "Yekutieli Lifting and Quantum Characteristic Classes",
      label: "sec:yekutieli-lifting",
      blocks: [
        "yekutieli-lifting-condition",
        "quantum-characteristic-classes",
        "yekutieli-lifting",
        "yekutieli-lifting-proof",
        "qu-to-qou",
        "fermionic-twisted-sectors",
      ],
    }),

    // ── Algebraic infrastructure ───────────────────────────────────────
    section({
      title: "Direct Limit Algebra",
      label: "sec:direct-limit",
      blocks: [
        "direct-limit-algebra",
        "direct-limit-lusztig",
        "jet-shell",
        "stack-like-structure",
        "vacuum-state",
        "vacuum-state-proof",
        "global-gluing",
        "global-gluing-proof",
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
        "descent",
        "descent-eigenspaces",
        "descent-eigenspaces-proof",
        "brane-boundary",
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
        "cosimplicial-crossed-groupoid-proof",
        "jet-as-descent",
        "descent-condition",
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
        "topological-mass-proof",
        "quantum-dilogarithm",
        "quantum-dilogarithm-proof",
      ],
    }),
  ],
});
