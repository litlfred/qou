import { table } from "../../schema/builders";
export default table({
  label: "tbl:topology-geometry-boundary-table-data",
  title: "Data table from rem:topology-geometry-boundary",
  uses: ["rem:topology-geometry-boundary"],
  tags: ["extracted-table"],
});
