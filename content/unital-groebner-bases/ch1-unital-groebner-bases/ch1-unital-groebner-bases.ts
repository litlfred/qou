import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Unital Gröbner Bases.
 *
 * Core definitions, the division algorithm, and the main theorem proof.
 */
export default chapter({
  number: 1,
  title: "Unital Gröbner Bases",
  label: "chap:ugb-definitions",
  sections: [
    section({
      title: "Notation and basic definitions",
      label: "sec:ugb-notation",
      blocks: [
        "monomial-basis",
        "leading-terms",
        "admissible-system",
      ],
    }),
    section({
      title: "Gröbner bases and the division algorithm",
      label: "sec:ugb-division",
      blocks: [
        "remainder-modules",
        "division-algorithm",
        "unital-groebner-basis",
      ],
    }),
    section({
      title: "Proof of the main theorem",
      label: "sec:ugb-main-proof",
      blocks: [
        "lemma-generator-choice",
        "ugb-main-theorem-proof",
      ],
    }),
  ],
});
