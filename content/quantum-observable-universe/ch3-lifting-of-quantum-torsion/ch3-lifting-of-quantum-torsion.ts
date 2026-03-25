import { chapter, section } from "../../schema/builders";

/**
 * Lifting and Descent.
 *
 * Covers jet prolongation, the recursive brane tower, Yekutieli lifting,
 * the main QOU theorem, cosimplicial structure, descent, mass decomposition,
 * and the quantum dilogarithm.
 *
 * Section ordering optimised to minimise dependency-graph backward edges
 * (19 → 4 after section reorder + block-level fixes).  The key insight:
 * Descent machinery must precede Cosimplicial Crossed Groupoid, which
 * references lem:descent, def:descent-involution, and prop:descent-eigenspaces.
 */
export default chapter({
  number: 2,
  title: "Lifting and Descent",
  label: "chap:torsion",
  sections: [
    // ── Foundations ─────────────────────────────────────────────────────
    section({
      title: "Jet Prolongation",
      label: "sec:jet-prolongation",
      blocks: [
        "jet-prolongation",
        "jet-prolongation-proof",
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
    // vacuum-state placed before global-gluing (global-gluing uses it)
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
        "algebraic-filter",
        "distributional-connection",
      ],
    }),

    // ── Descent (must precede cosimplicial groupoid) ───────────────────
    // descent-reduction-zero placed before descent-reduction (which uses it)
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
        "descent-reduction-zero",
        "descent-physical-zero",
        "descent-reduction",
        "descent-physical",
        "descent-fixed-point",
      ],
    }),

    // ── Cosimplicial structure (now all deps are upstream) ─────────────
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
      title: "Yekutieli Categorical Mapping",
      label: "sec:yekutieli-mapping",
      blocks: [
        "yekutieli-mapping-table",
      ],
    }),

    section({
      title: "Localized Knots, Hadrons, and Bundle Initial Conditions",
      label: "sec:localized-knots-bundles",
      blocks: [
        "localized-knot-intro",
        "localized-knot",
        "hadron",
        "hadron-operations",
        "knot-factorization",
        "localized-hadron",
        "hadron-fibre-embedding",
        "skein-generation",
        "skein-generation-proof",
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
        "topological-mass-categorical-proof",
        "qdlog-julia",
        "julia-s1-photon-scatter",
      ],
    }),

    // ── Archimedean specialisations ──────────────────────────────────
    // All results below require the archimedean realisation (manifolds,
    // gauge theory, Killing forms, Stokes theorem, etc.).  The categorical
    // statements they specialise remain in the sections above.

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
