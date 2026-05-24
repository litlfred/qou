import { table } from "../../schema/builders";
export default table({
  label: "tbl:phi-q-resums-trace-series-table-data",
  title: "Data table from rem:phi-q-resums-trace-series",
  uses: ["rem:phi-q-resums-trace-series"],
  tags: ["extracted-table"],
});
