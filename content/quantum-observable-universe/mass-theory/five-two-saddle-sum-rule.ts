import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:five-two-saddle-sum-rule",
  title:
    "The $5_2$ saddle sum rule: the dilogarithm over the Galois orbit of " +
    "$X^3 - 2X^2 + 3X - 1$",
  tags: [
    "dilogarithm",
    "pentagon",
    "five-term-relation",
    "galois-orbit",
    "saddle",
  ],
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule",
    validation: "leanok",
  },
  uses: ["thm:kummer-identity-radial-reduction"],
  cites: ["neumann2004", "zagier1986", "neumann-zagier1985"],
});
