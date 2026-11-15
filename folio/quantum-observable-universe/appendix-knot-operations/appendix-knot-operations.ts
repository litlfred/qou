import { chapter, section } from "../../schema/builders";

/**
 * Appendix: Knot Operation Actions Dictionary.
 *
 * Complete reference for Hecke algebra operations in H₃(q):
 * particle NFs, multiplication table, composite operations,
 * and the gluon model comparison.
 */
export default chapter({
  tabLabel: "K",
  title: "Knot Operation Actions Dictionary",
  label: "app:knot-operations",
  sections: [
    section({
      title: "Hecke algebra operations",
      label: "sec:hecke-operations",
      blocks: [
        "hecke-operations",
        "hecke-operations-table2-data",
        "hecke-operations-table1-data",
        // Atomization (batch-085): Borromean gluon-content / color-singlet
        // interpretation split out of rem:hecke-operations into its own remark.
        "borromean-gluon-content",
      ],
    }),
    section({
      title: "Knot operator action on basis pairs",
      label: "sec:knot-operator-basis-table",
      blocks: [
        "knot-operator-basis-table-intro",
        "knot-operator-basis-table",

        "knot-operator-basis-table-table1-data",
        "knot-operator-basis-table-table2-data",
        "knot-operator-basis-table-table3-data",
        "knot-operator-basis-table-table4-data",
      ],
    }),
    section({
      title: "Hadron-level knot decomposition table",
      label: "sec:hadron-level-knot-table",
      blocks: [
        "hadron-level-knot-table",
        // Detangler R3 (2026-05-23): 15-row hadron-level knot
        // decomposition data extracted from the remark.
        "hadron-level-knot-table-data",
      ],
    }),
  ],
});
