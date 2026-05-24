import { table } from "../../schema/builders";
export default table({
  label: "tbl:schur-weyl-vanishing-table-data",
  title: "Data table from prop:schur-weyl-vanishing",
  uses: ["prop:schur-weyl-vanishing"],
  tags: ["extracted-table"],
});
