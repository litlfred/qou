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
        "main-commutative-diagram",
        "main-commutative-diagram-proof",
      ],
    }),

    // ── Headline conjectures ──────────────────────────────────────────
    // R4 YM-split: `conj:yang-mills-mass-gap` was competing with
    // `prop:main-commutative-diagram` for 'the main result' framing in
    // sec:physical-interpretation.  Split into its own subsection paired
    // with the GR-substrate-geometry interpretation that motivates it.
    section({
      title: "Headline conjectures",
      label: "sec:headline-conjectures",
      blocks: [
        "headline-conjectures-intro",
        "yang-mills-mass-gap",
        "yang-mills-mass-gap-table-data",
        "gr-substrate-geometry",
      ],
    }),

    // ── Archimedean witnesses (R1: split from the former Archimedean specialisations section) ───
    // The catalogue of archimedean realisations — explicit examples,
    // not bridge/wall material.  After Rec 2 (4 Descartes-coded blocks
    // moved out), this section holds: the intro + 6 explicit witnesses
    // + cosmological-limits (kept here per audit minor pattern as a
    // separate physical-limits cluster).
    section({
      title: "Archimedean witnesses",
      label: "sec:archimedean-witnesses",
      blocks: [
        "archimedean-models-intro",
        "calabi-yau",
        "ale",
        "instanton",
        "irreducible-connection",
        "self-dual-curvature",
        "reeb-decomposition",
        "cosmological-limits",
      ],
    }),

    // ── Categorical-differential bridge (R1: split from the former Archimedean specialisations section) ──
    // The "bridge" sub-section: how the categorical machinery (Levi
    // substrate, Webster inner product, Heisenberg commutator, spatial-
    // realisation functor, categorical-archimedean bridge) connects to
    // differential-geometric witnesses on the archimedean side.
    section({
      title: "Categorical-differential bridge",
      label: "sec:categorical-differential-bridge",
      blocks: [
        "categorical-differential-bridge-intro",
        "c-substrate-via-levi",
        "webster-inner-product",
        "heisenberg-commutator-prop",
        "heisenberg-commutator",
        "observation-archimedean",
        "spatial-realization-functor",
        "categorical-archimedean-bridge",
        "categorical-archimedean-bridge-proof",
        "physicist-translation",
        "categorical-action-vs-chern-simons",
      ],
    }),

    // ── Non-Archimedean models ──────────────────────────────────────
    // R3 (Rec 3): Removed 3 TODO-outline prose blocks
    // (categorical-reformulation, p-adic-fields, finite-fields-outlook
    // — the last in sec:finite-fields below).  `enveloping-algebras`
    // retained because 3 sibling chapters (kronheimer-mrowka, reducible-
    // reps, first-order-taylor) cross-reference sec:enveloping-algebras.
    section({
      title: "Non-Archimedean models",
      label: "sec:non-archimedean-models",
      blocks: [
        "non-archimedean-models-intro",
        "enveloping-algebras",
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
    // R3 (Rec 3): Removed `finite-fields-outlook` (sec:finite-fields)
    // — was a TODO bullet outline redundant with finite-fields-intro.
    section({
      title: "Finite fields and Jones polynomials",
      label: "sec:finite-fields",
      blocks: [
        "finite-fields-intro",
        "finite-field-realisation",
        "jones-polynomials",
      ],
    }),

    // ── Mostow confinement and the Archimedean wall (narrative bridge) ─
    // Absorbed from former Ch `encounter` (now dissolved). These blocks
    // narrate the archimedean wall that the Archimedean-witnesses + bridge sections above
    // specifies formally: Mostow confinement, the algebraic↔geometric
    // rigidity pairing, and the literature bridge.
    section({
      title: "Mostow confinement and the Archimedean wall",
      label: "sec:archimedean-encounter",
      blocks: [
        "archimedean-encounter-intro",
        "outro-models-of-qous",
      ],
    }),

    // ── Fluid dynamics moved to Chapter 10 ──────────────────────────
    // The full development of brane fluid dynamics, q-NS regularity,
    // and the NS obstruction lives in fluid-dynamics/.

    // ═══════════════════════════════════════════════════════════════════
    // PART B lives in archimedean-universe/ (same chapter number 5).
    // The pipeline resolves blocks from that directory's own manifest.
    // ═══════════════════════════════════════════════════════════════════
  ],
});
