import { table } from "../../schema/builders";
export default table({
  label: "tbl:eos-borromean-cfl-table-data",
  title: "Data table from prop:eos-borromean-cfl",
  uses: ["prop:eos-borromean-cfl"],
  tags: ["extracted-table"],
});
