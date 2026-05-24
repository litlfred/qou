import { table } from "../../schema/builders";
export default table({
  label: "tbl:collatz-hausdorff-comparison-table-data",
  title: "Data table from rem:collatz-hausdorff-comparison",
  uses: ["rem:collatz-hausdorff-comparison"],
  tags: ["extracted-table"],
});
