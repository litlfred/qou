import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Quantum Observable Universe.
 *
 * Sections can be inline or referenced by name.
 * Referenced sections resolve to `<name>/<name>.ts` in this directory.
 * Blocks within sections are atomic knowledge units (root-name .ts + .md pairs).
 */
export default chapter({
  number: 1,
  title: "Quantum Observable Universe",
  label: "chap:qou",
  sections: [
    section({
      title: "Introduction",
      label: "sec:qou-intro",
      blocks: [
        "ch1-intro",
      ],
    }),

    section({
      title: "Preliminary: rigid monoidal categories",
      label: "sec:rigid-monoidal",
      blocks: [
        "rigid-monoidal-category",
        "rigid-monoidal-vect",
      ],
    }),

    section({
      title: "Core definitions",
      label: "sec:core-definitions",
      blocks: [
        "quantum-universe",
        "quantum-universe-su2",
        "higher-forms",
        "higher-forms-su2",
        "quantum-observable-universe",
        "qou-su2",
        "base-field-independence",
      ],
    }),

    section({
      title: "Consequences of the axioms",
      label: "sec:axiom-consequences",
      blocks: [
        "frobenius-relation",
        "frobenius-su2",
        "involutive-structure",
        "positive-definite-dagger",
        "dagger-su2",
        "volume-from-rigidity",
        "su2-volume-from-rigidity",
        "tannaka-krein-overview",
        "su2-emergence",
        "su2-emergence-example",
      ],
    }),

    section({
      title: "Differential structures and gauge actions",
      label: "sec:differential-structures",
      blocks: [
        "spin-labels",
        "spin-labels-su2",
        "maximal-torus",
        "maximal-torus-su2",
        "weight-decomposition",
        "reeb-physical",
        "categorical-reeb",
        "reeb-su2",
        "projective-line-object",
        "projective-line-su2",
        "fiber-adjoint-involution",
        "fiber-adjoint-su2",
        "categorical-connection",
        "connection-su2",
        "categorical-jet",
        "categorical-hodge-star",
        "hodge-su2",
      ],
    }),

    section({
      title: "Substrate parameter and deformation",
      label: "sec:substrate-parameter",
      blocks: [
        "quantum-universe-explication",
        "substrate-parameter",
        "quantum-gauge-group",
        "quantum-planck-constant",
        "planck-limits",
        "q-hodge-star",
      ],
    }),

    section({
      title: "Categorical action and variational equations",
      label: "sec:categorical-action",
      blocks: [
        "categorical-action-notation",
        "categorical-action-notation-su2",
        "categorical-action",
        "variational-equations",
      ],
    }),

    section({
      title: "Particles, fermions, bosons, and observation",
      label: "sec:particles",
      blocks: [
        "categorical-q-ext-deriv",
        "q-harmonic-form",
        "fermion-boson-decomposition",
        "categorical-point",
        "observation",
        "two-observer-parallelogram",
      ],
    }),

    section({
      title: "Categorical instanton and self-duality",
      label: "sec:instanton",
      blocks: [
        "categorical-instanton",
        "categorical-irreducible",
        "categorical-self-duality",
        "self-dual-ses",
        "hopf-non-cocommutativity",
      ],
    }),

    section({
      title: "Non-vanishing of $d_q^2$ and jet prolongation",
      label: "sec:dq-squared",
      blocks: [
        "categorical-dq-squared",
        "categorical-q-lie-bracket",
        "categorical-q-connection",
      ],
    }),

    section({
      title: "Archimedean quantum universe",
      label: "sec:archimedean-qou",
      blocks: [
        "archimedean-intro",
        "c-quantum-universe",
        "notation-special-cases",
        "c-quantum-observable-universe",
        "archimedean-realisations",
        "calabi-yau",
        "ale",
        "brings-surface",
        "cosmological-limits",
        "instanton",
        "irreducible-connection",
        "self-dual-curvature",
        "c-substrate-via-levi",
        "heisenberg-commutator",
        "reeb-decomposition",
        "observation-archimedean",
      ],
    }),

    section({
      title: "$q$-Deformed operators",
      label: "sec:q-deformed-operators",
      blocks: [
        "q-ext-deriv",
        "q-lie-bracket",
        "q-connection",
        "q-reeb-vector-field",
        "q-reeb-flow",
        "q-torsion-leaf",
        "q-torsion-existence",
      ],
    }),

    section({
      title: "Physical interpretation and main result",
      label: "sec:physical-interpretation",
      blocks: [
        "q-yang-mills-levi",
        "gr-substrate-geometry",
        "main-commutative-diagram",
      ],
    }),
  ],
});
