import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6: Universes.
 *
 * The Descartes condition, its implications for genus-4 base curves,
 * chirality, colour sectors, braid-group structure, and the Descartes
 * theorem; followed by p-adic, finite-field, and Witt-vector realisations.
 */
export default chapter({
  number: 5,
  title: "Universes",
  label: "chap:universes",
  sections: [
    section({
      title: "The Descartes condition",
      label: "sec:descartes-condition",
      blocks: [
        "descartes-condition",
        "descartes-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
      ],
    }),

    section({
      title: "Leptons and chirality",
      label: "sec:descartes-leptons-chirality",
      blocks: [
        "descartes-leptons",
        "descartes-chirality",
        "light-cone-affine",
      ],
    }),

    section({
      title: "Trefoil subgroups and Bring's curve",
      label: "sec:trefoil-brings",
      blocks: [
        "chirality-trefoil",
        "brings-curve",
      ],
    }),

    section({
      title: "Colour-sector coordinates on the exceptional fibre",
      label: "sec:colour-sector-coords",
      blocks: [
        "exceptional-divisor",
        "chiral-sector-coords",
      ],
    }),

    section({
      title: "Categorical braid structure",
      label: "sec:descartes-braid",
      blocks: [
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "skein-archimedean-shadow",
      ],
    }),

    section({
      title: "The Descartes theorem",
      label: "sec:descartes-theorem",
      blocks: [
        "descartes",
        "descartes-proof",
        "universality-general",
        "descartes-yekutieli",
        "observation-brings",
      ],
    }),

    // ── p-Adic and non-Archimedean realisations (formerly Ch. 7) ─

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
