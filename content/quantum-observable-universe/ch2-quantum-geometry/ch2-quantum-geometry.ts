import { chapter, section } from "../../schema/builders";

/**
 * Chapter 2: Quantum Geometry.
 *
 * Elaboration of the categorical and analytic foundations introduced
 * in Chapter 1.  TQFT context, Hopf structure, quantum flatness,
 * the q-jacobiator, classical recovery, and the categorical lifting
 * of jet prolongation, transport, and torsion.
 *
 * Extracted from the former "elaboration" sections of Ch. 1 to keep
 * that chapter focused on the core QOU axioms.
 */
export default chapter({
  number: 2,
  title: "Quantum Geometry",
  label: "chap:quantum-geometry",
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
        "quantum-flatness",
        "emergence-to-quantum-flat",
        "emergence-to-quantum-flat-proof",
        "simplicity-from-category",
        "frobenius-simplification",
        "j1e-local-states",
      ],
    }),

    section({
      title: "Non-vanishing of $d_q^2$ and the $q$-jacobiator",
      label: "sec:dq-squared-elaboration",
      blocks: [
        "dq-squared",
        "dq-squared-proof",
        "q-jacobiator",
        "q-jacobiator-proof",
        "classical-recovery",
      ],
    }),

    section({
      title: "Physical elaborations",
      label: "sec:physical-elaborations",
      blocks: [
        "q-torsion-leaf-minimum",
        "q-harmonic-physical",
        "linearisation-convention",
        "schrodinger-jet-coaction",
      ],
    }),

    section({
      title: "Lifting: jet prolongation, transport, and torsion",
      label: "sec:lifting",
      blocks: [
        "lifting-intro",
        "categorical-jet-prolongation",
        "categorical-jet-prolongation-proof",
        "categorical-transport",
        "categorical-q-reeb-flow",
        "categorical-q-torsion-leaf",
      ],
    }),
  ],
});
