import { table } from "../../schema/builders";
export default table({
  label: "tbl:stat-mech-computational-horizon-table-data",
  title: "Data table from rem:stat-mech-computational-horizon",
  uses: ["rem:stat-mech-computational-horizon"],
  tags: ["extracted-table"],
});
