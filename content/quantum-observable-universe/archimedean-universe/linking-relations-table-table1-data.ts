import { table } from "../../schema/builders";
export default table({
  label: "tbl:linking-relations-table-table1-data",
  title: "Data table 1 from rem:linking-relations-table",
  uses: ["rem:linking-relations-table"],
  tags: ["extracted-table"],
});
