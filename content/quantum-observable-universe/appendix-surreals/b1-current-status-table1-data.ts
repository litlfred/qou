import { table } from "../../schema/builders";
export default table({
  label: "tbl:b1-current-status-table1-data",
  title: "Data table 1 from rem:b1-current-status",
  uses: ["rem:b1-current-status"],
  tags: ["extracted-table"],
});
