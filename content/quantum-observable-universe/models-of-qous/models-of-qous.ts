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
        "models-of-qous-intro",
        "q-yang-mills-levi",
        "yang-mills-mass-gap",
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
        "archimedean-models-intro",
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
        "physicist-translation",
        "categorical-action-vs-chern-simons",
      ],
    }),

    // ── Non-Archimedean models ──────────────────────────────────────
    // R2: Merged four 1-block sections (categorical-reformulation,
    // enveloping-algebras, p-adic-fields, p-adic-realisation) into one.
    section({
      title: "Non-Archimedean models",
      label: "sec:non-archimedean-models",
      blocks: [
        "categorical-reformulation",
        "enveloping-algebras",
        "p-adic-fields",
        "p-adic-realisation",
      ],
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

    // ── Finite-field models and Jones polynomials ───────────────────
    // R3: Merged 1-block sec:jones-polynomials into sec:finite-fields.
    section({
      title: "Finite fields and Jones polynomials",
      label: "sec:finite-fields",
      blocks: [
        "finite-fields-intro",
        "finite-field-realisation",
        "finite-fields-outlook",
        "jones-polynomials",
      ],
    }),

    // ── Mostow confinement and the Archimedean wall (narrative bridge) ─
    // Absorbed from former Ch `encounter` (now dissolved). These blocks
    // narrate the archimedean wall that `sec:archimedean-models` above
    // specifies formally: Mostow confinement, the algebraic↔geometric
    // rigidity pairing, and the literature bridge.
    section({
      title: "Mostow confinement and the Archimedean wall",
      label: "sec:archimedean-encounter",
      blocks: [
        "archimedean-encounter-intro",
        "mostow-confinement",
        "algebraic-geometric-rigidity-pairing",
        "encounter-literature-bridge",
        "outro-models-of-qous",
      ],
    }),

    // ── Fluid dynamics moved to Chapter 10 ──────────────────────────
    // The full development of brane fluid dynamics, q-NS regularity,
    // and the NS obstruction lives in fluid-dynamics/.

    // ═══════════════════════════════════════════════════════════════════
    // PART B lives in descartes-universe/ (same chapter number 5).
    // The pipeline resolves blocks from that directory's own manifest.
    // ═══════════════════════════════════════════════════════════════════
  ],
});
