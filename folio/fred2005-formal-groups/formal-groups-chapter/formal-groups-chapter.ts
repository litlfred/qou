import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Formal Groups and the Lifting Theorem
 *
 * Covers the integration of skewed-Poisson structures, Gröbner–Shirshov
 * deformation, strong multiplicativity, Witt vector lift, and unit-root
 * F-crystal equivalence.
 */
export default chapter({
  title: "Formal Groups and the Lifting Theorem",
  label: "chap:formal-groups",
  sections: [
    section({
      title: "Commutative formal group",
      label: "sec:commutative-formal-group",
      blocks: [
        "commutative-formal-group",
      ],
    }),

    section({
      title: "Skewed-Poisson structure",
      label: "sec:skewed-poisson",
      blocks: [
        "skewed-poisson-structure",
      ],
    }),

    section({
      title: "Integration theorem",
      label: "sec:integration-theorem",
      blocks: [
        "non-commutative-formal-group",
        "skew-poisson-integrates",
        "reduction-mod-p",
      ],
    }),

    section({
      title: "Gröbner–Shirshov deformation",
      label: "sec:gs-deformation",
      blocks: [
        "grobner-shirshov-basis",
        "grobner-shirshov-basis-exists",
      ],
    }),

    section({
      title: "Strong multiplicativity",
      label: "sec:strong-multiplicativity",
      blocks: [
        "strong-multiplicativity",
      ],
    }),

    section({
      title: "Witt vector lift",
      label: "sec:witt-vector-lift",
      blocks: [
        "witt-vector-lift",
        "witt-vector-lift-exists",
      ],
    }),

    section({
      title: "Unit-root F-crystal",
      label: "sec:unit-root-f-crystal",
      blocks: [
        "unit-root-f-crystal",
        "unit-root-iff-integrable",
      ],
    }),
  ],
});
