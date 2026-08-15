import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:five-two-saddle-sum-rule",
  title:
    "The $5_2$ saddle sum rule: $\\mathrm{Li}_2(a) + \\mathrm{Li}_2(\\bar a) + \\mathrm{Li}_2(t)$ in closed form",
  tags: [
    "dilogarithm",
    "five-term-identity",
    "saddle-point",
    "5_2",
    "shape-field",
  ],
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule",
    validation: "leanok",
  },
  uses: ["prop:hyperbolic-knot-shape-fields"],
  cites: ["zagier1986"],
});
