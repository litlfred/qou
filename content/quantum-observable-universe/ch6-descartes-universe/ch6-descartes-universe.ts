import { chapter, section } from "../../schema/builders";

/**
 * Chapter 5: Models of QOU.
 *
 * Concrete realisations of the QOU axioms: the Archimedean model
 * (main commutative diagram, Calabi--Yau, ALE, Bring's surface,
 * instantons), p-adic and finite-field models, Witt-vector lifting,
 * Jones polynomials, and fluid-dynamic perspectives.
 */
export default chapter({
  number: 5,
  title: "Models of QOU",
  label: "chap:models-qou",
  sections: [
    // ── Physical interpretation and main result (from ch1 §16) ────────
    section({
      title: "Physical interpretation and the main result",
      label: "sec:physical-interpretation",
      blocks: [
        "q-yang-mills-levi",
        "gr-substrate-geometry",
        "main-commutative-diagram",
        "main-commutative-diagram-proof",
      ],
    }),

    // ── Archimedean realisations (from ch1 §17) ──────────────────────
    section({
      title: "Archimedean specialisations",
      label: "sec:archimedean-models",
      blocks: [
        "calabi-yau",
        "ale",
        "brings-surface",
        "cosmological-limits",
        "instanton",
        "irreducible-connection",
        "seiberg-witten",
        "primordial-vortex",
        "geometric-drag",
        "self-dual-curvature",
        "c-substrate-via-levi",
        "webster-inner-product",
        "heisenberg-commutator",
        "reeb-decomposition",
        "observation-archimedean",
        "spatial-realization-functor",
        "categorical-archimedean-bridge",
        "categorical-archimedean-bridge-proof",
      ],
    }),

    // ── Categorical reformulation ─────────────────────────────────────
    section({
      title: "Key Results in Categorical Language",
      label: "sec:categorical-reformulation",
      blocks: ["categorical-reformulation"],
    }),

    // ── Non-Archimedean models ────────────────────────────────────────
    section({
      title: "Universal Enveloping Algebras and Quantum Groups",
      label: "sec:enveloping-algebras",
      blocks: ["enveloping-algebras"],
    }),
    section({
      title: "$\\pp$-Adic Number Fields and Universality",
      label: "sec:p-adic-fields",
      blocks: ["p-adic-fields"],
    }),
    section({
      title: "$\\mathbb{C}_\\pp$ Quantum Universe",
      label: "sec:cp-que",
      blocks: ["p-adic-realisation"],
    }),
    section({
      title: "Lifting via Formal Groups and Witt Vectors",
      label: "sec:witt-vector-lifting",
      blocks: [
        "witt-vector-lifting-intro",
        "witt-vector-lift",
        "skew-poisson-integration",
        "skew-poisson-integration-proof",
        "witt-lift-qou",
      ],
    }),

    // ── Finite-field models ───────────────────────────────────────────
    section({
      title: "Quotient to Finite Fields",
      label: "sec:finite-fields",
      blocks: [
        "finite-field-realisation",
        "finite-fields-outlook",
      ],
    }),

    // ── Jones polynomials ─────────────────────────────────────────────
    section({
      title: "Jones Polynomials",
      label: "sec:jones-polynomials",
      blocks: ["jones-polynomials"],
    }),

    // ── Fluid dynamics ────────────────────────────────────────────────
    section({
      title: "Fluid Dynamics of the Brane",
      label: "sec:brane-fluid",
      blocks: [
        "brane-fluid",
        "geodesic-vortices",
        "braid-fluid",
        "planck-reynolds",
        "vortex-intensity-modes",
        "discrete-vortex-spectrum",
      ],
    }),

  ],
});
