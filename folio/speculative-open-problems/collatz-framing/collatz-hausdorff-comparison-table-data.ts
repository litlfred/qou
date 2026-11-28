import { table } from "../../schema/builders";

export default table({
  label: "tbl:collatz-hausdorff-comparison-table-data",
  title: "Formal comparison of the smooth Hausdorff recurrence and real-$q$ step multipliers",
  uses: ["rem:collatz-hausdorff-comparison"],
  tags: ["extracted-table", "collatz", "heuristic"],
});
