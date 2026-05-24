import { table } from "../../schema/builders";

export default table({
  label: "tbl:atom-mass-full-hecke-table-data",
  title: "Three-channel $H_3(q)$ decomposition for atomic mass",
  caption:
    "Irreducible channels of $H_3(q)$: symmetric (dim 1, eigenvalue $q$), " +
    "standard (dim 2, $2{\\times}2$ matrix), alternating (dim 1, eigenvalue " +
    "$-q^{-1}$). Weights $w_\\lambda = \\dim(\\lambda)/6$ by Plancherel.",
  uses: ["rem:atom-mass-full-hecke"],
  tags: ["hecke-algebra", "three-channel", "mass-formula"],
});
