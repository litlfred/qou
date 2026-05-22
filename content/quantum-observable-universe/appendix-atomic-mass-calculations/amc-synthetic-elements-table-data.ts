import { table } from "../../schema/builders";

export default table({
  label: "tbl:amc-synthetic-elements-table-data",
  title: "Mass predictions: synthetic elements ($Z = 93$ to $118$)",
  caption:
    "QOU mass formula bookkeeping $M_q$ versus observed atomic " +
    "masses $M_o$ (AME2020) for the 26 synthetic elements. " +
    "$\\dagger$ marks reactor- or accelerator-produced isotopes.",
  uses: ["prose:amc-synthetic-elements-table"],
  tags: ["atomic-mass", "synthetic-elements", "amc-table", "appendix"],
});
