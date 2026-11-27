import { table } from "../../schema/builders";
export default table({
  label: "tbl:g-action-on-aether-table2-data",
  renamedFrom: ["tbl:g-action-on-substrate-table2-data"],
  title: "Data table 2 from conj:g-action-on-aether",
  uses: ["conj:g-action-on-aether"],
  tags: ["extracted-table"],
});
