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

        "tm-notation-table1-data",
        "tm-notation-table2-data",
        "tm-notation-table3-data",
        "tm-notation-table4-data",
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

        "tm-knot-pairs-table1-data",
        "tm-knot-pairs-table2-data",
        "tm-knot-pairs-table3-data",
        "tm-knot-pairs-table4-data",
      ],
    }),
    section({
      title: "Interaction and decay matrices",
      label: "sec:tm-interactions",
      blocks: [
        "tm-interactions",
        "tm-interaction-completeness",
        "tm-interaction-completeness-table-data",
      ],
    }),
    section({
      title: "Worked examples (light nuclei)",
      label: "sec:tm-worked-examples",
      blocks: [
        "tm-worked-examples",
      ],
    }),
    section({
      title: "Inductive construction ($A \\to A+1$)",
      label: "sec:tm-inductive-construction",
      blocks: [
        "tm-inductive-construction",
      ],
    }),
    section({
      title: "Heavy-atom worked examples",
      label: "sec:tm-heavy-atom-examples",
      blocks: [
        "tm-heavy-atom-examples",

        "tm-heavy-atom-examples-table1-data",
        "tm-heavy-atom-examples-table2-data",
        "tm-heavy-atom-examples-table3-data",
        "tm-heavy-atom-examples-table4-data",
        "tm-heavy-atom-examples-table5-data",
        "tm-heavy-atom-examples-table6-data",
        "tm-heavy-atom-examples-table7-data",
        "tm-heavy-atom-examples-table8-data",
      ],
    }),
  ],
});
