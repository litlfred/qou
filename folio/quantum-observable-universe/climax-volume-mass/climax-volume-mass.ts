import { chapter, section } from "../../schema/builders";

/**
 * q-Hyperbolic Geometry.
 *
 * Geometric realisation of braid words as knot complements: Mobius
 * energy (self-avoidance), crossing energy (Coulomb charge), Lagrange
 * resolvents (q-deformed kinematics), knot-operator energy, and
 * braiding relations (spectral filter).
 *
 * The mass-derivation sections (vertex factorisation, Feynman
 * identification, Kashiwara-Jones, quantum dilogarithm, archimedean
 * realization) moved to the Mass chapter (2026-05-27) where they
 * belong as the geometric face of the mass endomorphism.
 */
export default chapter({
  title: "q-Hyperbolic Geometry",
  label: "chap:climax-volume-mass",
  sections: [
    section({
      title: "Categorical Mobius energy and self-avoidance",
      label: "sec:mobius-energy",
      blocks: [
        "mobius-energy-intro",
        "mobius-energy",
        "mobius-energy-frobenius-kernel",
        "mobius-energy-frobenius-kernel-proof",
        "mobius-energy-proof",
        "jones-mobius-diagonal",
        "jones-mobius-diagonal-proof",
        "non-self-intersection",
        "nsi-q-deformed-kernel",
        "nsi-q-deformed-kernel-proof",
        "non-self-intersection-proof",
        "non-self-intersection-interpretation",
      ],
    }),
    section({
      title: "Crossing energy, skein asymmetry, and the Coulomb–strong ratio",
      label: "sec:crossing-energy",
      blocks: [
        // def:crossing-energy and def:coulomb-charge relocated to
        // knots-particles-confinement §7 (2026-08-09, decision 5). They move
        // as ONE unit — coulomb-charge.ts carries `uses: ["def:crossing-energy"]`
        // and coulomb-charge.md defines the Coulomb charge as a decomposition
        // OF the crossing energy — so splitting them across the chapter
        // boundary would have created a fresh forward edge. The blocks below
        // still develop both quantities; only the two definitions moved, so
        // this section's title now names material it consumes rather than
        // establishes. Title revisit deferred (no section renames this round).
        "crossing-energy-intro",
        "crossing-energy-categorical-origin",
        "crossing-energy-trefoil",
        "commutative-crossing-energy",
        "branch-phase-mass-tower-witness",
        "categorical-coordinate-ring-dedup",
        "commutative-crossing-energy-table2-data",
        "commutative-crossing-energy-table1-data",
        "coulomb-strong-ratio-q-rational",
        "coulomb-strong-ratio-q-rational-proof",
        "skein-crossing-asymmetry-prop",
        "skein-crossing-asymmetry",
        "skein-bar-antisymmetry",
        "skein-bar-antisymmetry-proof",
      ],
    }),
    section({
      title: "Lagrange Resolvents and $q$-Deformed Kinematics",
      label: "sec:lagrange-q-kinematics",
      blocks: [
        "lagrange-q-kinematics-intro",
        "lagrange-resolvents",
        "q-momentum",
        "q-momentum-building-block-values",
        "q-momentum-properties",
        "q-angular-momentum",
        "q-angular-momentum-interpretation",
        "q-energy",
        "q-energy-terms-and-limits",
        "noether-theorem-callout",
      ],
    }),
    section({
      title: "Knot-operator energy",
      label: "sec:knot-operator-energy",
      blocks: [
        "atom-isotope-confinement-intro",
        "knot-operator-energy",
        "knot-operator-energy-vanishing",
        "knot-operator-energy-consumers",
        "knot-operator-energy-exists",
        "knot-operator-energy-unique",
        "local-shadow-ordering",
        "shadow-price-continuity",
        "phase-boundary-variety",
        "confinement-local-constancy",
        "shadow-ordering-compute-shortcut",
        // Re-homed orphans: the per-component selection rule lw(c) — its
        // c=1 (muon/knot) and c=3 (proton/Borromean 3-link) exact anchors,
        // and the c=2 prediction proved from them.
        "selection-rule-anchors-c1-c3",
        "selection-rule-c2-prediction",
      ],
    }),
    section({
      title: "Braiding Relations and the Spectral Filter",
      label: "sec:braiding-relations",
      blocks: [
        "braiding-relations-intro",
        "skein-archimedean-shadow",
        "vertex-algebra-relations",
        "vertex-algebra-relations-table1-data",
        "vertex-algebra-relations-table2-data",
        "vertex-algebra-relations-table3-data",
        "vertex-algebra-jet-relations",
        "vertex-algebra-jet-relations-table1-data",
        "vertex-algebra-jet-relations-table2-data",
        "vertex-algebra-jet-relations-table3-data",
        "t211-ideal-annihilation",
        "outro-climax-volume-mass",
      ],
    }),
  ],
});
