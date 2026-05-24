import { table } from "../../schema/builders";
export default table({
  label: "tbl:molecular-crossing-table-table-data",
  title: "Data table from rem:molecular-crossing-table",
  uses: ["rem:molecular-crossing-table"],
  tags: ["extracted-table"],
});
