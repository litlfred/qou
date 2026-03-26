import { chapter, section } from "../../schema/builders";

/**
 * Appendix A: Knot-Periodic Table.
 *
 * Complete table of all 92 naturally occurring elements expressed as
 * knot-particle generation formulas p𝔭 ⋈ n𝔫 ⋈ pT_{2,3}, with QOU
 * predicted masses and AME2020 binding energies.
 */
export default chapter({
  number: 9,
  tabLabel: "A",
  title: "Knot-Periodic Table of the Elements",
  label: "app:knot-periodic-table",
  sections: [
    section({
      title: "Knot formulas for all elements",
      label: "sec:knot-periodic-table",
      blocks: [
        "knot-atom-diagrams",
        "knot-periodic-table",
      ],
    }),
  ],
});
