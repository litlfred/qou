import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Unital Gröbner Bases
 *
 * Definitions, division algorithm, the main decomposition theorem, and — from
 * the original single-chapter draft this directory also carries — Buchberger's
 * theorem over R and PBW as a corollary.
 *
 * The 2004 import laid down three chapter directories but wired only this one,
 * which is a self-complete monolith. Wiring all three (owner ruling, bean
 * `qou-3yel`) brings in a parallel treatment of several blocks; those live in
 * this directory and are now listed beside the block each one restates. The
 * overlap is real and left visible on purpose — deciding which treatment the
 * paper keeps is an editorial call, not a manifest repair.
 */
export default chapter({
  title: "Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings",
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
        "leading-term-data",
        // Second-generation counterpart, placed beside the block it restates.
        "leading-terms",
        "admissible-system",
        "remainder-module",
        "remainder-modules",
      ],
    }),

    section({
      title: "Division algorithm and Gröbner--Shirshov bases",
      label: "sec:ugb-division",
      blocks: [
        "division-algorithm",
        "groebner-basis",
        "unital",
        // Required by ch0 `thm:ugb-main` and by all three ch2 blocks.
        "unital-groebner-basis",
        "s-polynomial",
      ],
    }),

    section({
      title: "Main results",
      label: "sec:ugb-main-results",
      blocks: [
        "generator-choice-lemma",
        "generator-choice-lemma-proof",
        "lemma-generator-choice",
        "main-theorem",
        "main-theorem-proof",
        // Proves `thm:ugb-main`, stated in the introduction chapter.
        "ugb-main-theorem-proof",
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
