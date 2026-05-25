import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6 — q-Hyperbolic, Volume, and the Mass Endomorphism (CLIMAX).
 *
 * The first-half climax of the paper. Develops the geometric realisation
 * of braid words as Reeb-bundle complements, the q-hyperbolic structure
 * on those complements, the volume invariant $\mathrm{Vol}(K)$, the
 * tangle-energy decomposition (Möbius energy, crossing energy, q-energy
 * with rotation/translation/action terms), and the mass endomorphism
 * statement $\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot c_q^{-2}$ via
 * non-abelian Stokes integration.
 *
 * Phase 4 chunk 1 (2026-05-25): 41 blocks moved from braids-and-knots
 * across 4 sections (Möbius energy, crossing energy, Lagrange/q-kinematics,
 * exceptional divisor + Reeb bundle). Subsequent chunks will add
 * vertex-factorisation, transfer-matrix-mass, and the Kashaev
 * archimedean-realization sections to complete the climax.
 *
 * Story-arc placement: Part II "Structural Mechanics" Ch 6 — the
 * geometric step of the Cat → Alg → Geom → Arch → Phys arc. Receives
 * the algebraic data from Ch 5 (Hecke); hands off to Ch 7 (Bring's
 * surface) and onward to Mass — Theory (Ch 10) and Mass — Application
 * (Ch 11).
 */
export default chapter({
  title: "q-Hyperbolic Structures, Volume, and the Mass Endomorphism",
  label: "chap:climax-volume-mass",
  sections: [
    section({
      title: "Categorical Möbius energy and self-avoidance",
      label: "sec:mobius-energy",
      blocks: [
        "mobius-energy-intro",
        "mobius-energy",
        "mobius-energy-frobenius-kernel",
        "mobius-energy-frobenius-kernel-proof",
        "mobius-energy-proof",
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
        "skein-crossing-asymmetry-prop",
        "skein-crossing-asymmetry",
        "skein-bar-antisymmetry",
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
      title: "Exceptional Divisor, Reeb Bundle, and Vertex Operators",
      label: "sec:exceptional-divisor-reeb",
      blocks: [
        "exceptional-divisor-reeb-intro",
        "reeb-bundle",
        "reeb-exceptional-divisor",
        "vertex-operator",
        "vertex-operator-dictionary",
        "vertex-operator-dictionary-table-data",
        "q-reeb-flow-on-coral-coords",
        "six-canonical-knot-operators",
        "six-canonical-knot-operators-table-data",
        "garside-as-compound-flow",
        "garside-flow-explicit-closed-form",
        "ramified-disc-fusion",
        "reeb-bundle-complement-equals-volume",
        "torus-knot-zero-volume-via-reeb",
        "hyperbolic-knot-positive-volume-via-reeb",
      ],
    }),
  ],
});
