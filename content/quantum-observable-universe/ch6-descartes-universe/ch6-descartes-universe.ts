import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6: Quantum Universes.
 *
 * Collects the various realisations of the QOU axioms beyond the
 * Descartes universe: p-adic, finite-field, Witt-vector, and
 * Jones polynomial settings, plus fluid-dynamic and information-
 * theoretic perspectives on the brane.
 */
export default chapter({
  number: 6,
  title: "Quantum Universes",
  label: "chap:quantum-universes",
  sections: [
    section({
      title: "Key Results in Categorical Language",
      label: "sec:categorical-reformulation",
      blocks: ["categorical-reformulation"],
    }),
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
    section({
      title: "Quotient to Finite Fields",
      label: "sec:finite-fields",
      blocks: [
        "finite-field-realisation",
        "finite-fields-outlook",
      ],
    }),
    section({
      title: "Jones Polynomials",
      label: "sec:jones-polynomials",
      blocks: ["jones-polynomials"],
    }),

    // ── Fluid dynamics (moved from ch4) ──────────────────────────────
    section({
      title: "Fluid Dynamics of the Brane",
      label: "sec:brane-fluid",
      blocks: [
        "brane-fluid",
        "geodesic-vortices",
        "braid-fluid",
        "planck-reynolds",
      ],
    }),

    // ── Information theory (moved from ch4) ──────────────────────────
    section({
      title: "Information-Theoretic Perspectives",
      label: "sec:info-theory",
      blocks: [
        "emergent-gravity-info",
        "planck-info-unit",
        "time-info",
        "big-bang-info",
        "planck-computation",
      ],
    }),
  ],
});
