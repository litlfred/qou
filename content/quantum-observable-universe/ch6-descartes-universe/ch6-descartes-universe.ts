import { chapter, section } from "../../schema/builders";

/**
 * Chapter 5: Models of QOUs.
 *
 * Concrete realisations of the QOU axioms.  First half: general models
 * (Archimedean, p-adic, finite-field, Witt-vector, Jones, fluid).
 * Second half: the Descartes universe — the specific realisation with
 * χ(A) = −6 and Bring's surface as fibre geometry.
 *
 * Merged from former Ch 5 (Models of QOU) + Ch 6 (The Descartes Universe).
 */
export default chapter({
  number: 5,
  title: "Models of QOUs",
  label: "chap:models-qou",
  sections: [
    // ═══════════════════════════════════════════════════════════════════
    // PART A: GENERAL MODELS
    // ═══════════════════════════════════════════════════════════════════

    // ── Physical interpretation and main result ─────────────────────
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

    // ── Archimedean realisations ────────────────────────────────────
    section({
      title: "Archimedean specialisations",
      label: "sec:archimedean-models",
      blocks: [
        "calabi-yau",
        "ale",
        "brings-surface-unit-circle",
        "cosmological-limits",
        "instanton",
        "irreducible-connection",
        "seiberg-witten",
        "primordial-vortex",
        "geometric-drag",
        "self-dual-curvature",
        "c-substrate-via-levi",
        "webster-inner-product",
        "heisenberg-commutator-prop",
        "heisenberg-commutator",
        "reeb-decomposition",
        "observation-archimedean",
        "spatial-realization-functor",
        "categorical-archimedean-bridge",
        "categorical-archimedean-bridge-proof",
      ],
    }),

    // ── Categorical reformulation ───────────────────────────────────
    section({
      title: "Key Results in Categorical Language",
      label: "sec:categorical-reformulation",
      blocks: ["categorical-reformulation"],
    }),

    // ── Non-Archimedean models ──────────────────────────────────────
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

    // ── Finite-field models ─────────────────────────────────────────
    section({
      title: "Quotient to Finite Fields",
      label: "sec:finite-fields",
      blocks: [
        "finite-field-realisation",
        "finite-fields-outlook",
      ],
    }),

    // ── Jones polynomials ───────────────────────────────────────────
    section({
      title: "Jones Polynomials",
      label: "sec:jones-polynomials",
      blocks: ["jones-polynomials"],
    }),

    // ── Fluid dynamics ──────────────────────────────────────────────
    section({
      title: "Fluid Dynamics of the Brane",
      label: "sec:brane-fluid",
      blocks: [
        "brane-fluid",
        "madelung-fluid",
        "hamilton-jacobi-phase",
        "q-navier-stokes",
        "geodesic-vortices",
        "braid-fluid",
        "planck-reynolds",
        "vortex-intensity-modes",
        "discrete-vortex-spectrum",
        "helicity-conservation",
        "q-turbulence-spectrum",
        "vortex-reconnection",
        "berry-vortex-moduli",
      ],
    }),

    // ═══════════════════════════════════════════════════════════════════
    // PART B lives in ch5-brings-surface/ (same chapter number 5).
    // The pipeline resolves blocks from that directory's own manifest.
    // ═══════════════════════════════════════════════════════════════════
  ],
});
