import { table } from "../../schema/builders";
export default table({
  label: "tbl:crossing-graded-mass-expansion-table-data",
  title: "Crossing-graded mass expansion: first three orders",
  caption: "Leading terms of the crossing-graded expansion: standard GB NF ($n=0$), linear crossing-lift ($n=1$), and pair-correction ($n=2$).",
  uses: ["conj:crossing-graded-mass-expansion"],
  tags: ["crossing-graded", "mass-expansion", "groebner"],
});
