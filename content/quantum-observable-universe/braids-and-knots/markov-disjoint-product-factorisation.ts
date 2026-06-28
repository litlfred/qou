import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-disjoint-product-factorisation",
  interprets: "prop:markov-trace-frobenius-selection",
  title:
    "Disjoint-product factorisation from M3 alone; discharges the `MarkovDisjointStabilisation` class for `prop:categorical-chain-convergence-mechanisms`",
  uses: ["prop:categorical-chain-convergence-mechanisms"],
  cites: ["jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "disjoint-factorisation",
    "class-discharge",
    "convergence-mechanism",
  ],
});
