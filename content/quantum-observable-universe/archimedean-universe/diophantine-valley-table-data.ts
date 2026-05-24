import { table } from "../../schema/builders";
export default table({
  label: "tbl:diophantine-valley-table-data",
  title: "Data table from rem:diophantine-valley",
  uses: ["rem:diophantine-valley"],
  tags: ["extracted-table"],
});
