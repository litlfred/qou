import { table } from "../../schema/builders";

export default table({
  label: "tbl:alpha-em-categorical-trace-ratio-table-data",
  title:
    "Numerical verification of $\\alpha_{EM} = h^{2} / [q \\cdot \\delta^{\\mathrm{top}}_q(T_{2,9}) \\cdot \\delta^{\\mathrm{top}}_q(T_{3,5})]$ at $q_0 \\approx 1.1099786$",
  caption:
    "Six-row witness check: $h$, $\\delta^{\\mathrm{top}}_q(T_{2,9})$, " +
    "$\\delta^{\\mathrm{top}}_q(T_{3,5})$, the computed ratio, the CODATA " +
    "$\\alpha_{EM}$ definition, and the exact-match verdict " +
    "($10^{-12}$ agreement).",
  uses: ["prop:alpha-em-categorical-trace-ratio"],
  tags: [
    "alpha-em",
    "categorical-trace-ratio",
    "numerical-verification",
    "torus-knot",
  ],
});
