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
        "spin-labels",
        "spin-labels-proof",
        "spin-labels-su2",
        "categorical-reeb",
        "categorical-reeb-exists",
        "categorical-reeb-exists-proof",
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
        "tannaka-krein-reconstruction",
        "substrate-parameter",
        "substrate-parameter-exists",
        "substrate-parameter-exists-proof",
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
      title: "Categorical action and variational equations",
      label: "sec:categorical-action",
      blocks: [
        "categorical-dirac-operator",
        "categorical-lagrangian",
        "categorical-action",
        "categorical-action-notation",
        "categorical-action-notation-su2",
        "qou-canonical-action",
        "physicist-translation",
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
        "categorical-laplace-transform",
        "categorical-fourier-transform",
        "q-resolvent",
        "laplace-fourier-wick-rotation",
        "q-exponential",
        "q-exponential-exists",
        "q-exponential-unique",
        "q-exp-finite-field-obstruction",
        "q-exp-p-adic",
        "q-logarithm",
        "q-dilogarithm",
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
