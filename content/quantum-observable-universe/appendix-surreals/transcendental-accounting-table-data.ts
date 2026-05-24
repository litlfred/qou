import { table } from "../../schema/builders";
export default table({
  label: "tbl:transcendental-accounting-table-data",
  title: "Data table from rem:transcendental-accounting",
  uses: ["rem:transcendental-accounting"],
  tags: ["extracted-table"],
});
