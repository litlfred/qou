import { table } from "../../schema/builders";
export default table({
  label: "tbl:statistical-mechanical-time-table-data",
  title: "Data table from rem:statistical-mechanical-time",
  uses: ["rem:statistical-mechanical-time"],
  tags: ["extracted-table"],
});
