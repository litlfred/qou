import { table } from "../../schema/builders";
export default table({
  label: "tbl:magic-shell-coupling-kappa-table-data",
  title: "Data table from conj:magic-shell-coupling-kappa",
  uses: ["conj:magic-shell-coupling-kappa"],
  tags: ["extracted-table"],
});
