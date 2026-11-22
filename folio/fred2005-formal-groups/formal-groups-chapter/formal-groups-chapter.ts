import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Non-commutative formal groups in positive characteristic
 *
 * Follows F. Leitner, arXiv:math/0602138: formal groups and their
 * distribution algebras, Poisson structures on splays, strong
 * multiplicativity, the Gröbner presentation of Dist(G), and the
 * integration theorem (Thm. 3.7). The paper works over a field of
 * characteristic p; the earlier Witt-vector, Z_p-lift and unit-root
 * F-crystal sections had no source in it and were removed 2026-11-21.
 */
export default chapter({
  title: "Non-commutative Formal Groups in Positive Characteristic",
  label: "chap:formal-groups",
  sections: [
    section({
      title: "Formal groups and distribution algebras",
      label: "sec:commutative-formal-group",
      blocks: [
        "commutative-formal-group",
        "non-commutative-formal-group",
      ],
    }),

    section({
      title: "Poisson structures on splays",
      label: "sec:skewed-poisson",
      blocks: [
        "skewed-poisson-structure",
        "strong-multiplicativity",
        "strong-multiplicativity-poisson-lie",
      ],
    }),

    section({
      title: "Gröbner presentation of the distribution algebra",
      label: "sec:gs-deformation",
      blocks: [
        "grobner-shirshov-basis",
        "grobner-shirshov-basis-exists",
      ],
    }),

    section({
      title: "Integration theorem",
      label: "sec:integration-theorem",
      blocks: [
        "skew-poisson-integrates",
      ],
    }),
  ],
});
