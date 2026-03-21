import { chapter, section } from "../../schema/builders";

/**
 * Chapter 7: p-Adic Quantum Observable Universe.
 *
 * Categorical reformulation of QOU definitions, quantum groups,
 * p-adic number fields, Witt vector lifting, and finite field realisations.
 */
export default chapter({
  number: 7,
  title: "$\\pp$-Adic Quantum Observable Universe",
  label: "chap:p-adic",
  sections: [
    section({
      title: "Key Results in Categorical Language",
      label: "sec:categorical-reformulation",
      blocks: [
        "categorical-reformulation",
      ],
    }),

    section({
      title: "Universal Enveloping Algebras and Quantum Groups",
      label: "sec:enveloping-algebras",
      blocks: [
        "enveloping-algebras",
      ],
    }),

    section({
      title: "$\\pp$-Adic Number Fields and Universality",
      label: "sec:p-adic-fields",
      blocks: [
        "p-adic-fields",
      ],
    }),

    section({
      title: "$\\mathbb{C}_\\pp$ Quantum Universe",
      label: "sec:cp-que",
      blocks: [
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
      blocks: [
        "jones-polynomials",
      ],
    }),
  ],
});
