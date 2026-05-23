import { table } from "../../schema/builders";

export default table({
  label: "tbl:amc-q-integer-table-data",
  title:
    "Atomic masses from the seven-term $q$-integer BW formula " +
    "(He through U, 32 isotopes, MAE 0.020\\%)",
  caption:
    "Predicted versus observed atomic masses, with seven $q$-integer " +
    "coefficients and shell width $\\sigma = [2]_q$ at $q_0 \\approx 1.110$. " +
    "Observed masses from AME2020. Error column shows the relative " +
    "deviation $(M_{\\mathrm{pred}} - M_{\\mathrm{obs}}) / M_{\\mathrm{obs}}$.",
  uses: ["rem:q-integer-mass-table"],
  tags: ["mass-table", "q-integer", "zero-parameters", "AME2020", "appendix"],
});
