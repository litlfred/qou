import { table } from "../../schema/builders";

export default table({
  label: "tbl:amc-wedderburn-method-table-data",
  title:
    "Input parameters for the three-invariant computation method (no fitted parameters)",
  caption:
    "Seven input parameters used by the three-invariant atomic-mass " +
    "computation: substrate $q_0$, CODATA $m_e$, derived $m_{\\mathfrak{p}}$ " +
    "and $m_{\\mathfrak{n}}$, derived coefficients $\\alpha$, $\\beta_2$, " +
    "$\\beta_3$. Fitted parameters: none.",
  uses: ["prose:amc-wedderburn-method"],
  tags: ["amc", "wedderburn", "input-parameters", "zero-fitting"],
});
