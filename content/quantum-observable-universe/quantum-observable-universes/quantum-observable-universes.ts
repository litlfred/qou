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
        "qou-definition-intro",
        "quantum-observable-universe",
        "quantum-observable-universe-exists",
        "qou-exists-axiom-1",
        "qou-exists-axiom-1-proof",
        "qou-exists-axiom-2",
        "qou-exists-axiom-2-proof",
        "qou-exists-axiom-3",
        "qou-exists-axiom-3-proof",
        "qou-exists-axiom-4",
        "qou-exists-axiom-4-proof",
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
        "emergence-intro",
      ],
      // Over-weight split (P4): 21-block emergence section into 3
      // reading-order sub-arcs. Order preserved; parent keeps the intro.
      subsections: [
        section({
          title: "Volume from rigidity",
          label: "sec:emergence-volume-rigidity",
          blocks: [
            "frobenius-su2",
            "dagger-su2",
            "volume-from-rigidity",
            "volume-from-rigidity-proof",
            "su2-volume-from-rigidity",
            "su2-emergence",
            "su2-emergence-volume-determinant",
            "su2-emergence-volume-determinant-proof",
            "su2-emergence-dagger-unitarity",
            "su2-emergence-dagger-unitarity-proof",
            "su2-emergence-proof",
          ],
        }),
        section({
          title: "Spin labels",
          label: "sec:emergence-spin-labels",
          blocks: [
            "su2-emergence-example",
            "spin-labels",
            "spin-labels-proof",
            "spin-labels-su2",
            "spin-half-representation",
          ],
        }),
        section({
          title: "The $G$-action on the substrate",
          label: "sec:emergence-g-action",
          blocks: [
            // Phase 7 orphan reconnection (2026-05-25):
            "g-action-on-substrate",
            "g-action-on-substrate-table1-data",
            "g-action-on-substrate-table2-data",
            "g-action-on-substrate-table3-data",
          ],
        }),
      ],
    }),

    // ── Maximal torus and weight decomposition ────────────────────────
    section({
      title: "Maximal torus and weight decomposition",
      label: "sec:weight-decomposition",
      blocks: [
        "weight-decomposition-intro",
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
        "vectors-hadrons-intro",
        "adjoint-trace",
        "pawlowski-leitner-basis",
        "pawlowski-leitner-inner-product",
      ],
    }),

    // ── Differential structures ───────────────────────────────────────
    // Detangler P1 split (2026-05-23): the 20-block
    // sec:differential-structures was split into the categorical
    // Reeb construction + fibre-adjoint involution machinery.
    section({
      title: "Differential structures: categorical Reeb",
      label: "sec:differential-structures-reeb",
      blocks: [
        "differential-structures-intro",
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
      ],
    }),
    section({
      title: "Differential structures: fibre-adjoint involution",
      label: "sec:differential-structures-fiber-adjoint",
      blocks: [
        "differential-structures-fiber-adjoint-intro",
        "fibre-functor-atlas",
        "fibre-functor-atlas-proof",
        "substrate-radial-coordinate",
        "substrate-radial-coordinate-proof",
        "fiber-adjoint-involution",
        "fai-projector-coadjoint-orbit",
        "fai-projector-coadjoint-orbit-proof",
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
        "substrate-parameter-intro",
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
        // Brane geometry primitives relocated from braids-and-knots/
        // per the PR #823 fit-section-chapter audit. These supply
        // the state-bundle fibre + U(1)-equivariant machinery that
        // later chapters (vertex operators, gauge structure) build on.
        "exceptional-divisor",
        // Re-homed from particle-interactions (cross-chapter forward-ref
        // fix): a QOU-axioms definition (commutative specialisation) that
        // u1-equivariant-reduction below depends on.
        "commutative-qou",
        "u1-equivariant-reduction",
        "u1-equivariant-reduction-proof",
      ],
    }),

    // ── Heisenberg commutator ────────────────────────────────────────
    // Relocated from models-of-qous/sec:categorical-differential-bridge
    // per Phase 3 of chapter-restructure-2026-05-25. The Heisenberg
    // commutator emerges from QOU's fibre structure (uses
    // def:quantum-planck-constant defined in this chapter); it's a
    // QOU-level result, not a "model" of QOUs.
    section({
      title: "Heisenberg commutator",
      label: "sec:heisenberg-commutator",
      blocks: [
        "intro-heisenberg-commutator",
        "heisenberg-commutator-prop",
        "heisenberg-commutator",
      ],
    }),

    // ── Algebraic substrate and the Reeb derivation ──────────────────
    // Absorbed from former `algebraic-substrate / sec:algebraic-substrate-reeb`
    // (now dissolved). These 12 blocks deepen the substrate parameter
    // into the Frobenius--Hopf substrate, Reeb derivation, and Brings
    // coordinate ring — content that is genuinely foundational and
    // referenced from braids, fluid, info-theory, QOU itself.
    section({
      title: "The algebraic substrate and the Reeb derivation",
      label: "sec:algebraic-substrate-reeb",
      blocks: [
        "algebraic-substrate-intro",
        "substrate-preamble",
        "frobenius-hopf-substrate",
        "substrate-parameter-planck",
        "categorical-reeb-derivation",
        "reeb-flow-bridge",
        "reeb-contact-universal-computer",
        "brings-coordinate-ring",
        "magic-numbers-bring",
        "rigid-dualizing-complex",
        "rigid-dualizing-brings",
        "substrate-self-duality",
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
        // Phase 7 orphan reconnection (2026-05-25):
        "affine-light-cone-figure",
      ],
    }),

    // ── Categorical action ────────────────────────────────────────────
    section({
      title: "Categorical Dirac operator",
      label: "sec:categorical-dirac-operator",
      blocks: [
        "categorical-dirac-operator-intro",
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
        "categorical-lagrangian-intro",
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
        "categorical-action-intro",
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
        "variational-equations-intro",
        "variational-equations",
        "variational-equations-proof",
        "wavefront-propagation",
        "photon-wavefront-example",
      ],
    }),

    // ── Particles ─────────────────────────────────────────────────────
    section({
      title: "Particle types and observation",
      label: "sec:particles",
      blocks: [
        "particles-intro",
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
        "germ-commutator-q-curvature",
        "q-harmonic-flow",
        "observation-fermion-action",
      ],
    }),

    // ── Geometric interpretations ─────────────────────────────────────
    section({
      title: "Geometric interpretations",
      label: "sec:geometric-interpretations",
      blocks: [
        "geometric-interpretations-intro",
        "vector-calculus-bridge",
        "q-laplacian-interpretation",
        "q-codifferential-formula-prop",
        "q-codifferential-formula",
        "q-laplacian-expansion",
        "q-laplacian-spectral-tower",
        "hodge-laplacian-relation",
        "categorical-lichnerowicz",
        "categorical-lichnerowicz-proof",
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
        "instanton-intro",
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
        "dq-squared-intro",
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
        "q-deformed-operators-intro",
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
    // ── q-Harmonic analysis (P4 split 2026-05-19): the 38-block
    //    sec:q-harmonic-analysis is split into three topical sub-
    //    sections matching the three transform families. The existing
    //    sec:q-harmonic-analysis-intro stays at the top of A and
    //    previews all three sub-sections as an umbrella narrative.
    section({
      title: "Linear $q$-transforms: heat, Laplace, Fourier",
      label: "sec:q-linear-transforms",
      blocks: [
        "q-harmonic-analysis-intro",
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
      ],
    }),

    // ── q-Resolvent and categorical Wick rotation ────────────────────
    section({
      title: "$q$-Resolvent and categorical Wick rotation",
      label: "sec:q-resolvent-wick",
      blocks: [
        "intro-q-resolvent-wick",
        "q-resolvent",
        "q-resolvent-exists",
        "q-resolvent-exists-proof",
        "q-resolvent-unique",
        "q-resolvent-unique-proof",
        "laplace-fourier-wick-rotation",
      ],
    }),

    // ── q-Exponential, logarithm, and dilogarithm ────────────────────
    // Detangler P2 split (2026-05-23): the 19-block
    // sec:q-special-functions was split into exp+log + dilog.
    section({
      title: "$q$-Exponential and $q$-logarithm",
      label: "sec:q-special-functions-exp-log",
      blocks: [
        "intro-q-special-functions",
        "q-exponential",
        "q-exponential-exists",
        "q-exponential-exists-proof",
        "q-exponential-unique",
        "q-exponential-unique-proof",
        "q-exp-finite-field-obstruction",
        "q-exp-p-adic",
        "q-exp-p-adic-table-data",
        "q-logarithm",
        "q-logarithm-exists",
        "q-logarithm-exists-proof",
        "q-logarithm-unique",
        "q-logarithm-unique-proof",
      ],
    }),
    section({
      title: "$q$-Dilogarithm",
      label: "sec:q-special-functions-dilog",
      blocks: [
        "q-special-functions-dilog-intro",
        "q-dilogarithm",
        "q-dilogarithm-exists",
        "q-dilogarithm-exists-proof",
        "q-dilogarithm-unique",
        "q-dilogarithm-unique-proof",
        // Generating-functions-as-Reeb-flow-solutions synthesis (Commit 3).
        "generating-functions-solve-reeb-flow",
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
        "braiding-conventions-intro",
        "braiding-unit-circle-convention",
        "sqrt-q-ribbon-structure",
        "sign-as-spin-structure",
        "i-as-braiding-orientation",
        "affine-chart-origin-of-i-and-q",
        "reeb-u1-chart-swap",
        "reeb-u1-chart-swap-proof",
        "categorical-coordinate-ring",
        "categorical-coordinate-ring-proof",
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
        "dq-squared-elaboration-intro",
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
        "physical-elaborations-intro",
        "q-torsion-leaf-minimum",
        "q-harmonic-physical",
        "linearisation-convention",
        "schrodinger-jet-coaction",
        "outro-quantum-observable-universes",
      ],
    }),

    // ── Orbital space from normal bundle ──────────────────────────────
    // NOTE (R1): sec:orbital-space and sec:fivefold-symmetry moved to
    // archimedean-universe (§5/§6) because their blocks forward-reference
    // Reidemeister invariance (braids-and-knots) and shell/skein content
    // (archimedean-universe). They belong in the Descartes chapter.
  ],
});
