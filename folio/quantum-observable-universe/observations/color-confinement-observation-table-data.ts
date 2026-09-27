import { table } from "../../schema/builders";
export default table({
  label: "tbl:color-confinement-observation-table-data",
  title: "Data table from rem:color-confinement-observation",
  uses: ["rem:color-confinement-observation"],
  tags: ["extracted-table"],
});
