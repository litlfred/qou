import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Quantum Universes.
 *
 * The QU axioms: a rigid symmetric monoidal category with a
 * Frobenius--Hopf object, a fibre functor, and a differential
 * calculus.  Chapter 2 adds observability, measurability, and the
 * volume constraint to obtain the Quantum Observable Universe (QOU).
 *
 * Structures available on a QU alone: Frobenius pairing, higher forms,
 * involutive/dagger structure, Tannaka--Krein, connections, jets,
 * and the Hodge star.
 */
export default chapter({
  number: 1,
  title: "Quantum Universes",
  label: "chap:qu",
  sections: [
    section({
      title: "Introduction",
      label: "sec:qou-intro",
      blocks: [
        "ch1-intro",
        "scheme-notation",
      ],
    }),

    section({
      title: "Preliminary: rigid monoidal categories",
      label: "sec:rigid-monoidal",
      blocks: [
        "no-quasi-zeros",
        "snake-identity",
        "rigid-monoidal-category",
        "rigid-monoidal-vect",
      ],
    }),

    section({
      title: "The Quantum Universe",
      label: "sec:quantum-universe",
      blocks: [
        "quantum-universe",
        "tau-notation",
        "frobenius-pairing",
        "frobenius-geometric-role",
        "quantum-universe-su2",
        "higher-forms",
        "higher-forms-su2",
        "fundamental-object-explication",
        "simple-objects-V",
        "unit-simplicity",
      ],
    }),

    section({
      title: "Consequences of the QU axioms",
      label: "sec:qu-consequences",
      blocks: [
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
        "categorical-connection",
        "categorical-connection-su2",
        "categorical-jet",
        "categorical-hodge-star",
        "hodge-su2",
      ],
    }),
  ],
});
