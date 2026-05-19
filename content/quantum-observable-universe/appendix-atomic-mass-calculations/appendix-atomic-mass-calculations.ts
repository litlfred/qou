import { chapter, section } from "../../schema/builders";

/**
 * Appendix C: Atomic Mass Calculations.
 *
 * Self-contained, fully worked calculations of the atomic mass for
 * every known element (Z = 1 to 118) from the QOU
 * topological mass formula.  Each step is shown explicitly so
 * that any reader can verify the arithmetic independently.
 *
 * Accompanied by a Lean 4 formalization that states the QOU
 * predicted mass, the AME2020 observed mass, and the percentage
 * deviation for each atom.
 */
export default chapter({
  tabLabel: "C",
  title: "Atomic Mass Calculations",
  label: "app:atomic-mass-calculations",
  sections: [
    section({
      title: "Method and input parameters",
      label: "sec:amc-method",
      blocks: [
        "amc-method",
        "amc-wedderburn-method",
      ],
    }),
    section({
      title: "Worked calculations for all elements ($Z = 1$ to $118$)",
      label: "sec:amc-calculations",
      blocks: [
        "amc-calculations",
      ],
    }),
    section({
      title: "Summary and percentage deviations",
      label: "sec:amc-summary",
      blocks: [
        "amc-summary",
        "amc-natural-elements-table",
        "amc-synthetic-elements-table",
      ],
    }),
    section({
      title: "$q$-integer mass table (zero fitted parameters)",
      label: "sec:amc-q-integer",
      blocks: [
        "amc-q-integer-table",
      ],
    }),
  ],
});
