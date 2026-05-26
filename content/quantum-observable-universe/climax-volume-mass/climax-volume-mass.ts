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
      title: "Vertex factorisation: exceptional divisor + Markov trace",
      label: "sec:vertex-factorisation-markov",
      blocks: [
        "vertex-factorisation-intro",
        "vertex-is-exceptional-divisor",
        "vertex-is-exceptional-divisor-proof",
        "six-operators-via-vertex-factorisation",
        "six-operators-via-vertex-factorisation-table-data",
        "breit-wheeler-vertex",
        "breit-wheeler-vertex-literature",
        "markov-trace-product",
        "markov-trace-product-interpretation",
        "hecke-markov-transition",
        "hecke-markov-interpretation",
        "hecke-markov-interpretation-table-data",
        "markov-lambda-knot-operations",
        "markov-chain-fluctuations",
      ],
    }),
    section({
      title: "Vertex factorisation: Feynman identifications",
      label: "sec:vertex-factorisation-feynman",
      blocks: [
        "vertex-factorisation-feynman-intro",
        "feynman-eigenbasis-decomposition",
        "feynman-eigenbasis-decomposition-proof",
        "feynman-trace-collapse",
        "feynman-trace-collapse-proof",
        "feynman-markov-identification",
        "feynman-markov-identification-proof",
        "feynman-categorical-trace",
        "feynman-categorical-trace-proof",
        "feynman-qou-dictionary",
        "feynman-qou-dictionary-table-data",
        "feynman-classical-limit",
        "feynman-classical-limit-interpretation",
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
      ],
    }),
    section({
      title: "Kashiwara-Jones interpretations and quantum-dilogarithm",
      label: "sec:kashiwara-jones-quantum-dilog",
      blocks: [
        "intro-kashiwara-jones-quantum-dilog",
        "kashiwara-jones-alternation-interpretation",
        "hopf-jones-c3-categorical",
        "kashiwara-jones-c4-categorical",
        "canonical-braid-interface-composition",
        "canonical-braid-interface-composition-table3-data",
        "canonical-braid-interface-composition-table2-data",
        "canonical-braid-interface-composition-table1-data",
        "prop-rigid-monoidal-structural-gap-invariance",
        "qz-bicompletion",
        "quantum-dilogarithm-stratified",
        "quantum-dilogarithm-stratified-proof",
        "q-pochhammer-partial-product",
        "phi-q-categorical-truncation",
        "phi-q-categorical-truncation-proof",
      ],
    }),
    section({
      title: "Archimedean realization and Kashaev volume",
      label: "sec:archimedean-realization-kashaev",
      blocks: [
        "intro-archimedean-realization-kashaev",
        "archimedean-realization-functor",
        "archimedean-image-table",
        "archimedean-image-table-table2-data",
        "archimedean-image-table-table1-data",
        "pre-tau-vs-post-tau",
        "vol-through-tau",
        "vol-as-motivic-period",
        "kashaev-volume-density",
        "kashaev-as-archimedean-realization",
        "phi-q-piece",
        "phi-q-tower-algebraic-stratification",
        "kashaev-volume-conjecture",
        "figure-8-archimedean-illustration",
        "gb-depth-period-correspondence",
        "vc-as-depth-2-instance",
        "bring-figure-eight-depth-2-witness",
      ],
    }),
    section({
      title: "Reconnected orphan blocks (Phase 7)",
      label: "sec:climax-volume-mass-orphan-reconnect",
      blocks: [
        "categorical-linking-operation",
        "crossed-module-euler-characteristic",
        "dim-master-pentagon",
        "geometric-invariant-piecewise",
        "hopf-link-non-magic",
        "kashaev-density-equals-sdp-multiplicity",
        "p-from-braid-mirror",
        "pachner-pentagon-borromean",
        "poincare-lefschetz-borromean",
        "q-rogers-pentagon-archimedean",
        "volume-perturbation-formula",
      ],
    }),
  ],
});
