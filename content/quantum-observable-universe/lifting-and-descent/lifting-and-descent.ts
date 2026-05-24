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
        "qu-to-qou",
        "qu-to-qou-su2",
      ],
    }),
    section({
      title: "Yekutieli lifting: Kummer-motivic enrichment",
      label: "sec:yekutieli-lifting-kummer-motivic",
      blocks: [
        "yekutieli-lifting-kummer-motivic-intro",
        "fermionic-twisted-sectors",
        "kummer-filtration-obstruction",
        "kummer-tower",
        "hochschild-kummer-connection",
        // def:motivic-substrate — substrate of the classical-limit
        // functor; lives here alongside motivic-galois-character +
        // qou-motivic-galois-instance (its consumers). Detangler
        // P34 (2026-05-22).
        "motivic-substrate",
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
        "ordering-jet-compatibility",
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
        // New H2 to prop:graded-trace-residue-split +
        // thm:knot-mass-formula-unified @ braids-and-knots
        // (accepted §5).
        "gb-spectral-sequence",
        "gb-spectral-sequence-table-data",
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
        "betti-harmonic-intro",
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
        "mass-identity-C",
        "mass-identity-C-proof",
        "mass-geometric-drag",
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
        // thm:topological-mass — the theorem statement, moved here
        // from braids-and-knots/sec:categorical-mass-foundations
        // per detangler P30 (2026-05-22).
        "topological-mass",
        "topological-mass-conjecture",
      ],
    }),
    section({
      title: "Archimedean specialisations: topological-mass variants",
      label: "sec:archimedean-lifting-topological-mass-variants",
      blocks: [
        "archimedean-lifting-topological-mass-variants-intro",
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
        "outro-lifting-and-descent",
      ],
    }),
  ],
});
