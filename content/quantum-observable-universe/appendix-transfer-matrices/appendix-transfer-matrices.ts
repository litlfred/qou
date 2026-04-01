import { chapter, section } from "../../schema/builders";

/**
 * Appendix B: Transfer Matrices.
 *
 * Self-contained reference for every transfer matrix in the paper,
 * including trivial cases.  Designed so the reader can use the
 * matrices without having read the body of the paper.
 */
export default chapter({
  tabLabel: "M",
  title: "Transfer Matrices",
  label: "app:transfer-matrices",
  sections: [
    section({
      title: "Notation and conventions",
      label: "sec:tm-notation",
      blocks: [
        "tm-notation",
      ],
    }),
    section({
      title: "The general transfer matrix",
      label: "sec:tm-general-form",
      blocks: [
        "tm-general-form",
      ],
    }),
    section({
      title: "Transfer matrices of knot pairs",
      label: "sec:tm-knot-pairs",
      blocks: [
        "tm-knot-pairs",
      ],
    }),
    section({
      title: "Interaction and decay matrices",
      label: "sec:tm-interactions",
      blocks: [
        "tm-interactions",
      ],
    }),
    section({
      title: "Worked examples",
      label: "sec:tm-worked-examples",
      blocks: [
        "tm-worked-examples",
      ],
    }),
  ],
});
