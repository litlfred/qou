import { chapter, section } from "../../schema/builders";

/**
 * Chapter 5: Universality.
 *
 * Categorical reformulations, quantum groups, p-adic and finite-field
 * realisations, Witt-vector lifting, and Jones polynomials.
 * (Descartes-specific content moved to ch11-experimental-evidence.)
 */
export default chapter({
  number: 5,
  title: "Universality",
  label: "chap:universality",
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
  ],
});
