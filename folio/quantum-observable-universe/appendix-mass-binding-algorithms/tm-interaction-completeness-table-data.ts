import { table } from "../../schema/builders";
export default table({
  label: "tbl:tm-interaction-completeness-table-data",
  title: "Data table from tm-interaction-completeness",
  uses: ["tm-interaction-completeness"],
  tags: ["extracted-table"],
});
