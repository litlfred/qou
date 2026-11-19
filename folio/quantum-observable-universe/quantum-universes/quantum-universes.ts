import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Quantum Universes.
 *
 * The QU axioms: a braided monoidal category (rigidity is imposed only
 * in Chapter 2, on a quantum observable universe) with a
 * Frobenius--Hopf object, a fibre functor, and a differential
 * calculus.  Chapter 2 adds observability, measurability, and the
 * volume constraint to obtain the Quantum Observable Universe (QOU).
 *
 * Structures available on a QU alone: Frobenius pairing, higher forms,
 * involutive/dagger structure, Tannaka--Krein, connections, jets,
 * and the Hodge star.
 */
export default chapter({
  title: "Quantum Universes",
  label: "chap:qu",
  sections: [
    section({
      title: "Introduction",
      label: "sec:qou-intro",
      blocks: [
        "quantum-universes-intro",
        "scheme-notation",
      ],
    }),

    section({
      title: "Preliminary: rigid monoidal categories",
      label: "sec:rigid-monoidal",
      blocks: [
        "rigid-monoidal-intro",
        "snake-identity",
        "rigid-monoidal-category",
        "monoidal-justification",
        "rigid-monoidal-vect",
      ],
    }),

    section({
      title: "The Quantum Universe",
      label: "sec:quantum-universe",
      blocks: [
        "quantum-universe-intro",
        "frobenius-hopf-substrate",
        "quantum-universe",
        // Light-touch physical motivation for each axiom, and the
        // foreshadow of ch:knots-particles-confinement §1 (the braiding's
        // hexagons are what make "an interaction" order-independent).
        // Kept out of the definition itself so the definition stays tight.
        "quantum-universe-axiom-motivation",
        "quantum-universe-exists",
        "quantum-universe-exists-proof",
        "tau-notation",
        "frobenius-pairing",
        "frobenius-pairing-exists",
        "frobenius-pairing-exists-proof",
      ],
    }),
    section({
      title: "Uniqueness and the $\\mathrm{SU}(2)$ realisation",
      label: "sec:quantum-universe-frobenius-pairing-unique",
      blocks: [
        "quantum-universe-frobenius-pairing-unique-intro",
        "frobenius-pairing-unique",
        "frobenius-pairing-unique-proof",
        "frobenius-geometric-role",
        "quantum-universe-su2",
        "quantum-universe-su2-table1-data",
        "frobenius-pairing-su2",
        "higher-forms",
        "higher-forms-su2",
        "fundamental-object-explication",
        "fundamental-object",
        "tannaka-dual",
        "simple-objects-V",
        "unit-simplicity",
        "hochschild-homology",
        "grothendieck-group-of-a-qou",
        "chern-character",
        "su2-characters-and-quantum-dimension",
      ],
    }),

    section({
      title: "Consequences of the QU axioms",
      label: "sec:qu-consequences",
      blocks: [
        "qu-consequences-intro",
        "frobenius-relation",
        "frobenius-relation-proof",
        "frobenius-relation-su2",
        "involutive-structure",
        "positive-definite-dagger",
        "positive-definite-dagger-proof",
        "positive-dagger-su2",
        "dagger-notation",
        "tannaka-krein-overview",
        "axiom-independence",
      ],
    }),

    section({
      title: "Structures on a Quantum Universe",
      label: "sec:qu-structures",
      blocks: [
        "qu-structures-intro",
        "categorical-connection",
        "categorical-connection-exists",
        "categorical-connection-exists-proof",
        "categorical-connection-unique",
        "categorical-connection-unique-proof",
        "categorical-connection-su2",
        "categorical-jet",
        "categorical-hodge-star",
        "categorical-hodge-star-exists",
        "categorical-hodge-star-exists-proof",
        "categorical-hodge-star-unique",
        "categorical-hodge-star-unique-proof",
        "hodge-su2",
        "poisson-object",
        "poisson-hkr-connection",
        "outro-quantum-universes",
      ],
    }),
  ],
});
