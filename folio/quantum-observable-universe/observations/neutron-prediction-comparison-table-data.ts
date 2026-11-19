import { table } from "../../schema/builders";
export default table({
  label: "tbl:neutron-prediction-comparison-table-data",
  title: "Distribution of neutron-number discrepancies $\\lvert\\Delta n\\rvert$ along the beta-stability curve ($p \\leq 103$)",
  uses: ["prop:neutron-prediction-comparison"],
  tags: ["extracted-table"],
});
