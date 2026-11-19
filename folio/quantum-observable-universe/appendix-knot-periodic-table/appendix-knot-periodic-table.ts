import { chapter, section } from "../../schema/builders";

/**
 * Appendix A: Knot-Periodic Table of the Elements.
 *
 * Composite knot diagrams of light atoms ($Z \leq 4$), followed by the
 * complete parameter-free knot-periodic table of all 118 known elements
 * ($Z = 1\text{--}118$, hydrogen through oganesson), the recursive
 * particle-to-nuclide knot atlas across all 3,558 AME2020 nuclides,
 * and the Mayer--Jensen knot-centric periodic reorganization.
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
      title: "Knot formulas and derived masses for all 118 elements",
      label: "sec:knot-periodic-table",
      blocks: [
        "knot-periodic-table",
        "recursive-atom-knot-atlas",
        "recursive-atom-knot-atlas-registry",
        "recursive-atom-knot-atlas-interpretation",
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
