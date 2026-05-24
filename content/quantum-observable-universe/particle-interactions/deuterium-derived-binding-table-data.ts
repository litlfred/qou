import { table } from "../../schema/builders";
export default table({
  label: "tbl:deuterium-derived-binding-table-data",
  title: "Data table from prop:deuterium-derived-binding",
  uses: ["prop:deuterium-derived-binding"],
  tags: ["extracted-table"],
});
