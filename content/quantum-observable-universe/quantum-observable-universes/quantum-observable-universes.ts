import { chapter, section } from "../../schema/builders";

/**
 * Chapter 2: Quantum Observable Universes.
 *
 * Opens with the Quantum Observable Universe (QOU) axioms — adding
 * observability, measurability, and the volume constraint to the QU
 * of Chapter 1.  This unlocks SU(2) emergence, the Reeb vector field,
 * weight decompositions, substrate deformation, the categorical action,
 * particles, instantons, and q-deformed operators.
 *
 * The elaboration material (TQFT context, q-jacobiator, physical
 * elaborations, categorical lifting) follows the core development.
 */
export default chapter({
  title: "Quantum Observable Universes",
  label: "chap:qou",
  sections: [
    // ── The QOU axiom ─────────────────────────────────────────────────
    section({
      title: "The Quantum Observable Universe",
      label: "sec:qou-definition",
      blocks: [
        "quantum-observable-universe",
        "quantum-observable-universe-exists",
        "quantum-observable-universe-exists-proof",
        "braiding-induced-ordering",
        "frobenius-integration",
        "yekutieli-stokes-remark",
        "fibre-functor-rigidity",
        "qou-su2",
        "base-field-independence",
      ],
    }),

    // ── Emergence from observability ──────────────────────────────────
    section({
      title: "Emergence from observability",
      label: "sec:emergence",
      blocks: [
        "frobenius-su2",
        "dagger-su2",
        "volume-from-rigidity",
        "volume-from-rigidity-proof",
        "su2-volume-from-rigidity",
        "su2-emergence",
        "su2-emergence-proof",
        "su2-emergence-example",
        "spin-labels",
        "spin-labels-proof",
        "spin-labels-su2",
        "spin-half-representation",
      ],
    }),

    // ── Maximal torus and weight decomposition ────────────────────────
    section({
      title: "Maximal torus and weight decomposition",
      label: "sec:weight-decomposition",
      blocks: [
        "maximal-torus",
        "maximal-torus-su2",
        "weight-decomposition",
        "weight-decomposition-exists",
        "weight-decomposition-exists-proof",
        "weight-decomposition-su2",
        "reeb-physical",
      ],
    }),

    // ── Vectors, hadrons, PawLei basis ────────────────────────────────
    section({
      title: "Vectors, hadrons, and the PawLei basis",
      label: "sec:vectors-hadrons",
      blocks: [
        "adjoint-trace",
        "pawlowski-leitner-basis",
        "pawlowski-leitner-inner-product",
      ],
    }),

    // ── Differential structures ───────────────────────────────────────
    section({
      title: "Differential structures and gauge actions",
      label: "sec:differential-structures",
      blocks: [
        "categorical-reeb",
        "categorical-reeb-exists",
        "categorical-reeb-exists-proof",
        "categorical-reeb-unique",
        "categorical-reeb-unique-proof",
        "reeb-su2",
        "categorical-reeb-brings",
        "projective-line-object",
        "projective-line-su2",
        "contact-affine-chart",
        "fibre-functor-atlas",
        "substrate-radial-coordinate",
        "substrate-radial-coordinate-proof",
        "fiber-adjoint-involution",
        "fiber-adjoint-involution-proof",
        "fiber-adjoint-su2",
        "connection-su2",
      ],
    }),

    // ── Substrate parameter ───────────────────────────────────────────
    section({
      title: "Substrate parameter and deformation",
      label: "sec:substrate-parameter",
      blocks: [
        "quantum-universe-explication",
        "braiding-eigenvalue-extraction",
        "spectral-chart-correspondence",
        "tannaka-krein-reconstruction",
        "substrate-parameter",
        "substrate-parameter-exists",
        "substrate-parameter-exists-proof",
        "substrate-parameter-unique",
        "substrate-parameter-unique-proof",
        "substrate-parameter-su2",
        "substrate-parameter-brings",
        "quantum-gauge-group",
        "quantum-planck-constant",
        "planck-limits",
        "q-hodge-star",
      ],
    }),

    // ── Quick examples of QOU realisations ────────────────────────────
    section({
      title: "Examples of quantum observable universes",
      label: "sec:qou-examples",
      blocks: [
        "archimedean-intro",
        "c-quantum-universe",
        "notation-special-cases",
        "c-quantum-observable-universe",
        "archimedean-realisations",
      ],
    }),

    // ── Categorical action ────────────────────────────────────────────
    section({
      title: "Categorical Dirac operator",
      label: "sec:categorical-dirac-operator",
      blocks: [
        "categorical-dirac-operator",
        "categorical-dirac-operator-exists",
        "categorical-dirac-operator-exists-proof",
        "categorical-dirac-operator-unique",
        "categorical-dirac-operator-unique-proof",
      ],
    }),

    section({
      title: "Categorical Lagrangian",
      label: "sec:categorical-lagrangian",
      blocks: [
        "categorical-lagrangian",
        "categorical-lagrangian-exists",
        "categorical-lagrangian-exists-proof",
        "categorical-lagrangian-unique",
        "categorical-lagrangian-unique-proof",
      ],
    }),

    section({
      title: "Categorical action",
      label: "sec:categorical-action",
      blocks: [
        "categorical-action",
        "categorical-action-exists",
        "categorical-action-exists-proof",
        "categorical-action-unique",
        "categorical-action-unique-proof",
        "categorical-action-notation",
        "categorical-action-notation-su2",
        "qou-canonical-action",
      ],
    }),

    section({
      title: "Variational equations and wavefronts",
      label: "sec:variational-equations",
      blocks: [
        "variational-equations",
        "variational-equations-proof",
        "wavefront-propagation",
        "photon-wavefront-example",
      ],
    }),

    // ── Particles ─────────────────────────────────────────────────────
    section({
      title: "Particles, fermions, bosons, and observation",
      label: "sec:particles",
      blocks: [
        "categorical-q-ext-deriv",
        "categorical-q-ext-deriv-exists",
        "categorical-q-ext-deriv-exists-proof",
        "categorical-q-ext-deriv-unique",
        "categorical-q-ext-deriv-unique-proof",
        "q-harmonic-form",
        "fermion-boson-decomposition",
        "categorical-point",
        "categorical-point-explication",
        "observation",
        "observation-physical-roles",
        "observation-energy",
        "observation-energy-proof",
        "two-observer-parallelogram",
        "observation-fermion-action",
      ],
    }),

    // ── Geometric interpretations ─────────────────────────────────────
    section({
      title: "Geometric interpretations",
      label: "sec:geometric-interpretations",
      blocks: [
        "vector-calculus-bridge",
        "q-laplacian-interpretation",
        "q-codifferential-formula-prop",
        "q-codifferential-formula",
        "q-laplacian-expansion",
        "hodge-laplacian-relation",
        "q-harmonic-particle",
        "brings-geometric-connection",
        "complex-substrate-interpretation",
      ],
    }),

    // ── Instanton and self-duality ────────────────────────────────────
    section({
      title: "Categorical instanton and self-duality",
      label: "sec:instanton",
      blocks: [
        "categorical-instanton",
        "categorical-instanton-exists",
        "categorical-instanton-exists-proof",
        "categorical-instanton-unique",
        "categorical-instanton-unique-proof",
        "instanton-on-shell",
        "categorical-irreducible",
        "categorical-irreducible-proof",
        "categorical-self-duality",
        "categorical-self-duality-proof",
        "self-dual-ses",
        "hopf-non-cocommutativity",
      ],
    }),

    // ── Non-vanishing of d_q^2 ────────────────────────────────────────
    section({
      title: "Non-vanishing of $d_q^2$ and jet prolongation",
      label: "sec:dq-squared",
      blocks: [
        "categorical-dq-squared",
        "categorical-dq-squared-proof",
        "categorical-q-lie-bracket",
        "categorical-q-connection",
        "categorical-q-connection-exists",
        "categorical-q-connection-exists-proof",
        "categorical-q-connection-unique",
        "categorical-q-connection-unique-proof",
      ],
    }),

    // ── q-Deformed operators ──────────────────────────────────────────
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
        "quantum-torsion-motivation",
      ],
    }),

    // ── q-Harmonic analysis: heat equation, Laplace, Fourier ─────────
    section({
      title: "$q$-Harmonic analysis: heat equation, Laplace, Fourier",
      label: "sec:q-harmonic-analysis",
      blocks: [
        "q-heat-equation",
        "q-heat-equation-exists",
        "q-heat-equation-exists-proof",
        "q-heat-equation-unique",
        "q-heat-equation-unique-proof",
        "categorical-laplace-transform",
        "categorical-laplace-transform-exists",
        "categorical-laplace-transform-exists-proof",
        "categorical-laplace-transform-unique",
        "categorical-laplace-transform-unique-proof",
        "categorical-fourier-transform",
        "categorical-fourier-transform-exists",
        "categorical-fourier-transform-exists-proof",
        "categorical-fourier-transform-unique",
        "categorical-fourier-transform-unique-proof",
        "q-resolvent",
        "q-resolvent-exists",
        "q-resolvent-exists-proof",
        "q-resolvent-unique",
        "q-resolvent-unique-proof",
        "laplace-fourier-wick-rotation",
        "q-exponential",
        "q-exponential-exists",
        "q-exponential-exists-proof",
        "q-exponential-unique",
        "q-exponential-unique-proof",
        "q-exp-finite-field-obstruction",
        "q-exp-p-adic",
        "q-logarithm",
        "q-logarithm-exists",
        "q-logarithm-exists-proof",
        "q-logarithm-unique",
        "q-logarithm-unique-proof",
        "q-dilogarithm",
        "q-dilogarithm-exists",
        "q-dilogarithm-exists-proof",
        "q-dilogarithm-unique",
        "q-dilogarithm-unique-proof",
      ],
    }),

    // ── Braiding conventions: eigenvalue labelling, ribbon, orientation ─
    // Held out of the core definition sections (sec:qou-definition,
    // sec:substrate-parameter) so the convention/elaboration content does
    // not pollute the QU/QOU axiomatic statements.
    section({
      title: "Braiding conventions: eigenvalue labelling, ribbon, orientation",
      label: "sec:braiding-conventions",
      blocks: [
        "braiding-unit-circle-convention",
        "sqrt-q-ribbon-structure",
        "sign-as-spin-structure",
        "i-as-braiding-orientation",
        "affine-chart-origin-of-i-and-q",
        "categorical-coordinate-ring",
      ],
    }),

    // ── Elaboration: categorical and analytic foundations ──────────────
    section({
      title: "Elaboration: categorical context",
      label: "sec:elaboration-intro",
      blocks: [
        "intro",
        "tqft-context",
        "vanishing-explication",
        "levi-generalisation",
        "quantum-gauge-group-category",
        "hopf-structure-diagrams",
        "self-dual-2group",
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

    // ── Orbital space from normal bundle ──────────────────────────────
    // NOTE (R1): sec:orbital-space and sec:fivefold-symmetry moved to
    // descartes-universe (§5/§6) because their blocks forward-reference
    // Reidemeister invariance (braids-and-knots) and shell/skein content
    // (descartes-universe). They belong in the Descartes chapter.
  ],
});
