import { table } from "../../schema/builders";
export default table({
  label: "tbl:regularity-breakdown-table-data",
  title: "Data table from conj:regularity-breakdown",
  uses: ["conj:regularity-breakdown"],
  tags: ["extracted-table"],
});
