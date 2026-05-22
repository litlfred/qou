import { table } from "../../schema/builders";

export default table({
  label: "tbl:amc-natural-elements-table-data",
  title: "Mass predictions: natural elements ($Z = 1$ to $92$)",
  caption:
    "QOU mass formula predictions $M_q$ versus observed atomic masses " +
    "$M_o$ (CODATA 2022 + AME2020) for all 92 naturally occurring " +
    "elements. Sub-keV agreement across the range confirms the " +
    "formula's arithmetic bookkeeping.",
  uses: ["prose:amc-natural-elements-table"],
  tags: ["atomic-mass", "natural-elements", "amc-table", "appendix"],
});
