import { table } from "../../schema/builders";
export default table({
  label: "tbl:categorical-neutron-table-data",
  title: "Data table from def:categorical-neutron",
  uses: ["def:categorical-neutron"],
  tags: ["extracted-table"],
});
