import { table } from "../../schema/builders";
export default table({
  label: "tbl:tm-knot-pairs-table1-data",
  title: "Data table 1 from tm-knot-pairs",
  uses: ["tm-knot-pairs"],
  tags: ["extracted-table"],
});
