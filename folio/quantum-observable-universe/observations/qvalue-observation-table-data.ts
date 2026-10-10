import { table } from "../../schema/builders";
export default table({
  label: "tbl:qvalue-observation-table-data",
  title: "Data table from rem:qvalue-observation",
  uses: ["rem:qvalue-observation"],
  tags: ["extracted-table"],
});
