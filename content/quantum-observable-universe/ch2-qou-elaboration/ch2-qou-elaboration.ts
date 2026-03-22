import { chapter, section } from "../../schema/builders";

/**
 * Chapter 2: Elaboration — Categorical and Analytic Foundations.
 *
 * Collects the categorical, algebraic, and analytic details that
 * underpin the definitions of Chapter 1.
 */
export default chapter({
  number: 2,
  title: "Elaboration: Categorical and Analytic Foundations",
  label: "chap:elaboration",
  sections: [
    section({
      title: "Introduction and categorical context",
      label: "sec:elaboration-intro",
      blocks: [
        "ch2-intro",
        "tqft-context",
        "vanishing-explication",
        "levi-generalisation",
        "quantum-gauge-group-category",
        "hopf-structure-diagrams",
        "self-dual-2group",
        "emergence-to-fake-flat",
        "emergence-to-fake-flat-proof",
        "simplicity-from-category",
        "frobenius-simplification",
        "j1e-local-states",
        "dq-squared",
        "dq-squared-proof",
        "q-jacobiator",
        "q-jacobiator-proof",
        "classical-recovery",
        "q-torsion-leaf-minimum",
        "q-harmonic-physical",
        "schrodinger-jet-coaction",
      ],
    }),

    section({
      title: "Lifting: jet prolongation, transport, and torsion",
      label: "sec:lifting",
      blocks: [
        "lifting-intro",
        "categorical-jet-prolongation",
        "categorical-transport",
        "categorical-q-reeb-flow",
        "categorical-q-torsion-leaf",
      ],
    }),
  ],
});
