import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Unital Gröbner Bases
 *
 * Single-chapter paper covering definitions, division algorithm,
 * the main decomposition theorem, Buchberger's theorem over R,
 * and PBW as a corollary.
 */
export default chapter({
  title: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings",
  label: "chap:ugb",
  sections: [
    section({
      title: "Introduction",
      label: "sec:ugb-introduction",
      blocks: [
        "introduction",
        "motivating-examples",
      ],
    }),

    section({
      title: "Monomials, orderings, and admissible systems",
      label: "sec:ugb-definitions",
      blocks: [
        "monomial-basis",
        "admissible-system",
        "remainder-module",
      ],
    }),

    section({
      title: "Division algorithm and Gröbner bases",
      label: "sec:ugb-division",
      blocks: [
        "division-algorithm",
        "groebner-basis",
      ],
    }),

    section({
      title: "Main results",
      label: "sec:ugb-main-results",
      blocks: [
        "generator-choice-lemma",
        "generator-choice-lemma-proof",
        "main-theorem",
        "main-theorem-proof",
        "s-polynomial-decomposition",
        "s-polynomial-decomposition-proof",
        "buchberger",
        "buchberger-proof",
        "pbw-corollary",
        "pbw-corollary-proof",
      ],
    }),
  ],
});
