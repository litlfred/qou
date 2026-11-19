import { table } from "../../schema/builders";
export default table({
  label: "tbl:centered-hecke-variance-positive-table-data",
  title: "Centred Hecke variance numerical verification at $q_0$",
  caption: "Step-by-step evaluation of $\\mathrm{Var}(\\sigma_i) = (q-q^{-1})z + 1 - z^2 \\approx 0.855$ at the aether $q_0 \\approx 1.110$.",
  uses: ["prop:centered-hecke-variance-positive"],
  tags: ["hecke-variance", "numerical-verification"],
});
