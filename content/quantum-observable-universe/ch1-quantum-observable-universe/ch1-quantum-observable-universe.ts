import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Quantum Observable Universe.
 *
 * Pure categorical development of the QOU axioms.  The Archimedean
 * realisation is asserted briefly as an example (§9) but the detailed
 * Archimedean content is pushed to the end (§17) so the reader does
 * not assume an Archimedean setting.
 *
 * The elaboration material (formerly Ch. 2) has been extracted into
 * a separate "Quantum Geometry" chapter.
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
        "snake-identity",
        "rigid-monoidal-category",
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
        "simple-objects-V",
        "unit-simplicity",
        "quantum-observable-universe",
        "frobenius-integration",
        "yekutieli-stokes-remark",
        "fibre-functor-rigidity",
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
        "spin-half-representation",
      ],
    }),

    section({
      title: "Vectors, hadrons, and the PawLei basis",
      label: "sec:vectors-hadrons",
      blocks: [
        "categorical-hadron",
        "adjoint-trace",
        "pawlowski-leitner-basis",
        "pawlowski-leitner-inner-product",
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

    // ── Quick Archimedean assertion (just the existence examples) ─────
    // Kept here so downstream chapters can reference ex:c-quantum-universe
    // and ex:c-quantum-observable-universe without an Archimedean chapter.
    section({
      title: "Examples of quantum universes",
      label: "sec:qou-examples",
      blocks: [
        "archimedean-intro",
        "c-quantum-universe",
        "notation-special-cases",
        "c-quantum-observable-universe",
        "archimedean-realisations",
      ],
    }),

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
        "instanton-on-shell",
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

    // ── q-Deformed operators (categorical, not Archimedean) ───────────
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

    // ── Physical interpretation (categorical main result) ─────────────
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

    // ── Archimedean detail (pushed to end) ────────────────────────────
    // The reader should not assume Archimedean until here.  Everything
    // above is valid over any base field.
    section({
      title: "Archimedean specialisations",
      label: "sec:archimedean-qou",
      blocks: [
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
  ],
});
