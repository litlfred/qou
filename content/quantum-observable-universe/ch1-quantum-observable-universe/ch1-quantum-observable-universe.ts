import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Quantum Universes.
 *
 * Pure QU axioms — rigid monoidal category with a Frobenius--Hopf
 * object.  No observability (fibre functor) assumed here; that is
 * introduced in Chapter 2 (Quantum Observable Universes).
 *
 * Structures available on a QU alone: Frobenius pairing, higher forms,
 * involutive/dagger structure, Tannaka--Krein, abstract hadrons,
 * connections, jets, and the Hodge star.
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
        "involutive-structure",
        "positive-definite-dagger",
        "tannaka-krein-overview",
      ],
    }),

    section({
      title: "Structures on a Quantum Universe",
      label: "sec:qu-structures",
      blocks: [
        "categorical-connection",
        "categorical-jet",
        "categorical-hodge-star",
        "hodge-su2",
      ],
    }),
  ],
});
