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
        "jet-prolongation-intro",
        "jet-prolongation",
        "jet-prolongation-su2",
        "jet-prolongation-categorical-jet",
        "jet-prolongation-categorical-jet-proof",
        "jet-prolongation-proof",
        "prolongation-categorical",
        "recursive-brane-tower",
        "brane-tower-terminology",
        "recursive-brane-tower-su2",
        "brane-tower-levels",
        "arc-space",
        "arc-space-brane-tower",
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
        "sdescent-prelim-intro",
        "descent-lemma",
        "descent-lemma-su2",
        "descent-lemma-proof",
        "descent-involution",
        "descent-involution-su2",
      ],
    }),

    // ── Yekutieli lifting (needed by cosimplicial + descent) ───────────
    // Detangler P3 split (2026-05-23): 22-block sec:yekutieli-lifting
    // split into construction (lifting + QCC) and kummer-motivic
    // (Kummer filtration + motivic substrate / Galois).
    section({
      title: "Categorical lifting and quantum characteristic classes",
      label: "sec:yekutieli-lifting-construction",
      blocks: [
        "yekutieli-lifting-intro",
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
        "yekutieli-setting-explicit",
        "qu-to-qou",
        "qu-to-qou-su2",
        "jet-tower-splitting-bring",
      ],
    }),
    section({
      title: "Kummer filtration and motivic Galois enrichment",
      label: "sec:yekutieli-lifting-kummer-motivic",
      blocks: [
        "yekutieli-lifting-kummer-motivic-intro",
        "kummer-filtration-obstruction",
        "kummer-tower",
        "motivic-substrate",
        "motivic-substrate-canonicity",
        "hochschild-kummer-connection",
        "hkr-theorem",
        "s1-action-and-loop-space",
        // def:motivic-substrate — substrate of the classical-limit
        // functor; lives here alongside motivic-galois-character +
        // qou-motivic-galois-instance (its consumers). Detangler
        // P34 (2026-05-22).
        "motivic-galois-character",
        "motivic-perpetual-obstruction",
        "kummer-tower-motivic-galois",
      ],
    }),

    // ── Algebraic infrastructure ───────────────────────────────────────
    section({
      title: "Direct Limit Algebra",
      label: "sec:direct-limit",
      blocks: [
        "direct-limit-intro",
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
        "global-gluing-interpretation",
        "ordering-jet-compatibility",
        "ordering-jet-compatibility-proof",
      ],
    }),

    section({
      title: "Mass in the Brane Tower",
      label: "sec:mass-brane",
      blocks: [
        "mass-brane-intro",
        // prop:gb-spectral-sequence moved here from
        // braids-and-knots/sec:spectral-sequence-chirality-confinement
        // per detangler P29 (2026-05-22). 12 H1 fwd-refs cleared.
        // mass-identity, mass-noncommutative-drag, topological-mass
        // and their proof trees moved to mass-theory (2026-05-27)
        // per mass-endomorphism restructuring.
        "euler-char-stability",
        "euler-char-stability-proof",
      ],
    }),

    section({
      title: "Betti Numbers and Harmonic Basis",
      label: "sec:betti-harmonic",
      blocks: [
        "betti-harmonic-intro",
        "betti-numbers-brane",
        "q-harmonic-basis-brane",
        "weight-space-decomposition-brane",
        "algebraic-filter-classification",
        "algebraic-filter-physical",
        "algebraic-filter",
        "fermionic-twisted-sectors",
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
        "descent-reduction",
        "descent-reduction-two",
        "descent-reduction-three",
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
        "ccg-crossed-module-structure",
        "ccg-crossed-module-structure-proof",
        "cosimplicial-crossed-groupoid-proof",
        "jet-as-descent",
        "descent-condition",
        "descent-cocycle-deviation",
        "descent-cocycle-deviation-proof",
        "descent-condition-proof",
        "p3-blowup-yekutieli-intro",
        "p3-blowup-yekutieli",
        "blowup-cohomological-address",
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
    // Detangler P4 split (2026-05-23): 25-block sec:archimedean-lifting
    // split 3-way into foundations + topological-mass-formula +
    // topological-mass-variants.
    section({
      title: "Archimedean specialisations: foundations",
      label: "sec:archimedean-lifting-foundations",
      blocks: [
        "archimedean-lifting-intro",
        "jet-prolongation-C",
        "jet-prolongation-C-proof",
        "yekutieli-archimedean-band",
        "qu-to-qou-proof",
        // mass-identity-C, mass-identity-C-proof, mass-geometric-drag
        // moved to mass-theory (2026-05-27).
        "euler-char-stability-C",
        "brane-boundary-structure-proof",
      ],
    }),
    section({
      title: "Archimedean specialisations: topological-mass formula",
      label: "sec:archimedean-lifting-topological-mass-formula",
      blocks: [
        "archimedean-lifting-topological-mass-formula-intro",
        "quantum-dilogarithm",
        "quantum-dilogarithm-proof",
        // topological-mass + topological-mass-conjecture moved to
        // mass-theory (2026-05-27).
      ],
    }),
    section({
      title: "Archimedean specialisations: topological-mass variants",
      label: "sec:archimedean-lifting-topological-mass-variants",
      blocks: [
        // topological-mass variants (eigenspace, holonomy, transient,
        // dilogarithm, proof, su2) moved to mass-theory (2026-05-27).
        "archimedean-lifting-topological-mass-variants-intro",
        "outro-lifting-and-descent",
      ],
    }),
  ],
});
