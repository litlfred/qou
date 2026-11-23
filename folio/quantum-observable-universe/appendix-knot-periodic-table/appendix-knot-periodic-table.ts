import { chapter, section } from "../../schema/builders";

/**
 * Appendix A: Knot-Periodic Table.
 *
 * Knot diagrams of light atoms showing sub-Hopf link structure,
 * followed by the complete table of all 92 naturally occurring
 * elements with QOU predicted masses and AME2020 binding energies.
 */
export default chapter({
  tabLabel: "T",
  title: "Knot-Periodic Table of the Elements",
  label: "app:knot-periodic-table",
  sections: [
    section({
      title: "Knot diagrams of light atoms",
      label: "sec:knot-atom-diagrams",
      blocks: [
        "knot-atom-diagrams",
        "knot-atom-diagrams-sim",
      ],
    }),
    section({
      title: "Knot formulas for all elements",
      label: "sec:knot-periodic-table",
      blocks: [
        "knot-periodic-table",
        "recursive-atom-knot-atlas",
        "recursive-atom-knot-atlas-registry",
        "recursive-atom-knot-atlas-sdp-uniqueness-wiring",
        "recursive-atom-knot-atlas-open-problems",
      ],
    }),
    section({
      title: "Knot-centric periodic table",
      label: "sec:knot-centric-table",
      blocks: [
        "knot-centric-table-intro",
        "knot-centric-table",
        "knot-centric-table-visualization-spec",

        "knot-centric-table-table1-data",
        "knot-centric-table-table2-data",
        "knot-centric-table-table3-data",
        "knot-periodic-table-sim",
      ],
    }),
  ],
});
