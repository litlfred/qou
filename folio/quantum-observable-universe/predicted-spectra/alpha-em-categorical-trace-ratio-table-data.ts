import { table } from "../../schema/builders";

export default table({
  label: "tbl:alpha-em-categorical-trace-ratio-table-data",
  title:
    "Numerical verification of $\\alpha_{EM} = h^{2} / [q \\cdot \\delta^{\\mathrm{top}}_q(T_{2,9}) \\cdot \\delta^{\\mathrm{top}}_q(T_{3,5})]$ at the proton and muon $q_0$ anchors",
  caption:
    "Evaluation of $h$, $\\delta^{\\mathrm{top}}_q(T_{2,9})$, " +
    "$\\delta^{\\mathrm{top}}_q(T_{3,5})$, the trace-ratio expression, and " +
    "$1/(q\\,[9]_q\\,[10]_q)$ at the primary proton-pinned $q_0$ (matching " +
    "prop:em-coupling-projection) alongside the muon-pinned comparison anchor.",
  uses: ["prop:alpha-em-categorical-trace-ratio", "prop:em-coupling-projection"],
  tags: [
    "alpha-em",
    "categorical-trace-ratio",
    "numerical-verification",
    "torus-knot",
  ],
});
