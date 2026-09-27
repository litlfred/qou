import { table } from "../../schema/builders";
export default table({
  label: "tbl:half-life-shell-worked-table-data",
  title: "Data table from ex:half-life-shell-worked",
  uses: ["ex:half-life-shell-worked"],
  tags: ["extracted-table"],
});
