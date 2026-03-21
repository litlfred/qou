import { chapter, section } from "../../schema/builders";

/**
 * Chapter 3: Path Integrals and Braiding.
 *
 * This chapter develops the braid-group framework and its knot-theoretic
 * consequences within the QOU categorical setting.  The final section
 * derives the Möbius energy functional from the categorical action and
 * establishes the self-avoidance corollary via the R-matrix.
 */
export default chapter({
  number: 3,
  title: "Path Integrals and Braiding",
  label: "chap:path-integrals-braiding",
  sections: [
    section({
      title: "Categorical Möbius Energy and Self-Avoidance",
      label: "sec:categorical-mobius-energy",
      blocks: [
        "mobius-energy-intro",
        "categorical-mobius-energy",
        "self-intersection-obstruction",
        "r-matrix-self-avoidance",
      ],
    }),
  ],
});
