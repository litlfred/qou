import { table } from "../../schema/builders";
export default table({
  label: "tbl:feynman-qou-dictionary-table-data",
  title: "Data table from rem:feynman-qou-dictionary",
  uses: ["rem:feynman-qou-dictionary"],
  tags: ["extracted-table"],
});
