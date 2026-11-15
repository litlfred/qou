import { table } from "../../schema/builders";
export default table({
  label: "tbl:particle-nf-table-table-data",
  title: "Data table from rem:particle-nf-table",
  uses: ["rem:particle-nf-table"],
  tags: ["extracted-table"],
});
