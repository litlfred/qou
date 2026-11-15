import { table } from "../../schema/builders";
export default table({
  label: "tbl:embeddability-closure-table-data",
  title: "Data table from thm:embeddability-closure",
  uses: ["thm:embeddability-closure"],
  tags: ["extracted-table"],
});
