import { table } from "../../schema/builders";
export default table({
  label: "tbl:neutron-prediction-comparison-table-data",
  title: "Data table from prop:neutron-prediction-comparison",
  uses: ["prop:neutron-prediction-comparison"],
  tags: ["extracted-table"],
});
