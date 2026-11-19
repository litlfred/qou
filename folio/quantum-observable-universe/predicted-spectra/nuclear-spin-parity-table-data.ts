import { table } from "../../schema/builders";
export default table({
  label: "tbl:nuclear-spin-parity-table-data",
  title: "Mass-number parity $A \\bmod 2$ and observed ground-state nuclear spins $J$",
  uses: ["prop:nuclear-spin-parity"],
  tags: ["extracted-table"],
});
