import { table } from "../../schema/builders";
export default table({
  label: "tbl:yang-mills-mass-gap-table-data",
  title: "Data table from conj:yang-mills-mass-gap",
  uses: ["conj:yang-mills-mass-gap"],
  tags: ["extracted-table"],
});
