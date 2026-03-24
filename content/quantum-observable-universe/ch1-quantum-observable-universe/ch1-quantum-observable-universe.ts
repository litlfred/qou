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
        "snake-identity",
        "rigid-monoidal-vect",
      ],
    }),

    section({
      title: "Core definitions",
      label: "sec:core-definitions",
      blocks: [
        "quantum-universe",
        "tau-notation",
        "frobenius-pairing",
        "frobenius-geometric-role",
        "quantum-universe-su2",
        "higher-forms",
        "higher-forms-su2",
        "fundamental-object-explication",
        "unit-simplicity",
        "quantum-observable-universe",
        "frobenius-integration",
        "yekutieli-stokes-remark",
        "qou-su2",
        "base-field-independence",
        "maximal-torus",
        "maximal-torus-su2",
        "weight-decomposition",
        "weight-decomposition-exists",
        "weight-decomposition-exists-proof",
        "reeb-physical",
      ],
    }),

    section({
      title: "Consequences of the axioms",
      label: "sec:axiom-consequences",
      blocks: [
        "frobenius-relation",
        "frobenius-relation-proof",
        "frobenius-su2",
        "involutive-structure",
        "positive-definite-dagger",
        "dagger-su2",
        "volume-from-rigidity",
        "volume-from-rigidity-proof",
        "su2-volume-from-rigidity",
        "tannaka-krein-overview",
        "su2-emergence",
        "su2-emergence-proof",
        "su2-emergence-example",
      ],
    }),

    section({
      title: "Differential structures and gauge actions",
      label: "sec:differential-structures",
      blocks: [
        "spin-labels",
        "spin-labels-proof",
        "spin-labels-su2",
        "categorical-reeb",
        "categorical-reeb-exists",
        "categorical-reeb-exists-proof",
        "reeb-su2",
        "projective-line-object",
        "projective-line-su2",
        "contact-affine-chart",
        "substrate-radial-coordinate",
        "substrate-radial-coordinate-proof",
        "fiber-adjoint-involution",
        "fiber-adjoint-involution-proof",
        "fiber-adjoint-su2",
        "categorical-connection",
        "connection-su2",
        "categorical-jet",
        "categorical-hodge-star",
        "hodge-su2",
      ],
    }),

    section({
      title: "Spatial realization and the categorical--geometric bridge",
      label: "sec:spatial-realization",
      blocks: [
        "spatial-realization-functor",
        "categorical-archimedean-bridge",
        "categorical-archimedean-bridge-proof",
      ],
    }),

    section({
      title: "Substrate parameter and deformation",
      label: "sec:substrate-parameter",
      blocks: [
        "quantum-universe-explication",
        "substrate-parameter",
        "substrate-parameter-exists",
        "substrate-parameter-exists-proof",
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
        "variational-equations-proof",
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
        "categorical-point-explication",
        "observation",
        "two-observer-parallelogram",
      ],
    }),

    section({
      title: "Geometric interpretations",
      label: "sec:geometric-interpretations",
      blocks: [
        "vector-calculus-bridge",
        "q-laplacian-interpretation",
        "q-codifferential-formula",
        "q-laplacian-expansion",
        "hodge-laplacian-relation",
        "q-harmonic-particle",
        "brings-geometric-connection",
      ],
    }),

    section({
      title: "Categorical instanton and self-duality",
      label: "sec:instanton",
      blocks: [
        "categorical-instanton",
        "categorical-irreducible",
        "categorical-irreducible-proof",
        "categorical-self-duality",
        "categorical-self-duality-proof",
        "self-dual-ses",
        "hopf-non-cocommutativity",
      ],
    }),

    section({
      title: "Non-vanishing of $d_q^2$ and jet prolongation",
      label: "sec:dq-squared",
      blocks: [
        "categorical-dq-squared",
        "categorical-dq-squared-proof",
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
        "webster-inner-product",
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
        "main-commutative-diagram-proof",
      ],
    }),

    // ── Elaboration: categorical and analytic foundations (formerly Ch. 2) ─

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
        "dq-squared",
        "dq-squared-proof",
        "q-jacobiator",
        "q-jacobiator-proof",
        "classical-recovery",
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
