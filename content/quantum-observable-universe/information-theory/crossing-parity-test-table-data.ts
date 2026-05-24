import { table } from "../../schema/builders";
export default table({
  label: "tbl:crossing-parity-test-table-data",
  title: "Data table from rem:crossing-parity-test",
  uses: ["rem:crossing-parity-test"],
  tags: ["extracted-table"],
});
