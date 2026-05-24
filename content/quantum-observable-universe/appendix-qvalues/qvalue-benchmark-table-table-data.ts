import { table } from "../../schema/builders";
export default table({
  label: "tbl:qvalue-benchmark-table-table-data",
  title: "Data table from ex:qvalue-benchmark-table",
  uses: ["ex:qvalue-benchmark-table"],
  tags: ["extracted-table"],
});
