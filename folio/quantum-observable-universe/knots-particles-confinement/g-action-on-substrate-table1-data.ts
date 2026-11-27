import { table } from "../../schema/builders";
export default table({
  label: "tbl:g-action-on-aether-table1-data",
  renamedFrom: ["tbl:g-action-on-substrate-table1-data"],
  title: "Data table 1 from conj:g-action-on-aether",
  uses: ["conj:g-action-on-aether"],
  tags: ["extracted-table"],
});
