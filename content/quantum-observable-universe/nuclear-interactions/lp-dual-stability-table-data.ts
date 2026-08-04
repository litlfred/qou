import { table } from "../../schema/builders";
export default table({
  label: "tbl:lp-dual-stability-table-data",
  title: "Data table from prop:lp-dual-stability",
  uses: ["prop:lp-dual-stability"],
  tags: ["extracted-table"],
});
