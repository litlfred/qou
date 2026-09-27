import { table } from "../../schema/builders";
export default table({
  label: "tbl:shell-filling-rule-table-data",
  title: "Data table from prop:shell-filling-rule",
  uses: ["prop:shell-filling-rule"],
  tags: ["extracted-table"],
});
