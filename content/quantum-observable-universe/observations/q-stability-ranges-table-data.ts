import { table } from "../../schema/builders";
export default table({
  label: "tbl:q-stability-ranges-table-data",
  title: "Data table from rem:q-stability-ranges",
  uses: ["rem:q-stability-ranges"],
  tags: ["extracted-table"],
});
