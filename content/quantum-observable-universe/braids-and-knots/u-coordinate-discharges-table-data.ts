import { table } from "../../schema/builders";
export default table({
  label: "tbl:u-coordinate-discharges-table-data",
  title: "Data table from rem:u-coordinate-discharges",
  uses: ["rem:u-coordinate-discharges"],
  tags: ["extracted-table"],
});
