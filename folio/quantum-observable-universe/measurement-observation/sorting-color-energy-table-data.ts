import { table } from "../../schema/builders";
export default table({
  label: "tbl:sorting-color-energy-table-data",
  title: "Data table from prop:sorting-color-energy",
  uses: ["prop:sorting-color-energy"],
  tags: ["extracted-table"],
});
