import { table } from "../../schema/builders";
export default table({
  label: "tbl:collatz-hausdorff-comparison-table-data",
  title: "Dynamical comparison of the $q$-Hausdorff recurrence and Skein--Collatz Lyapunov iteration",
  uses: ["rem:collatz-hausdorff-comparison"],
  tags: ["extracted-table"],
});
