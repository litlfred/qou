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
      ],
    }),
    section({
      title: "Crossing energy and Coulomb charge",
      label: "sec:crossing-energy",
      blocks: [
        "crossing-energy-intro",
        "crossing-energy",
        "crossing-energy-trefoil",
        "commutative-crossing-energy",
        "commutative-crossing-energy-table2-data",
        "commutative-crossing-energy-table1-data",
        "coulomb-charge",
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
        "q-angular-momentum",
        "q-angular-momentum-interpretation",
        "q-energy",
        "noether-theorem-callout",
      ],
    }),
    section({
      title: "Knot-operator energy",
      label: "sec:knot-operator-energy",
      blocks: [
        "atom-isotope-confinement-intro",
        "knot-operator-energy",
        "knot-operator-energy-exists",
        "knot-operator-energy-unique",
        "local-shadow-ordering",
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
