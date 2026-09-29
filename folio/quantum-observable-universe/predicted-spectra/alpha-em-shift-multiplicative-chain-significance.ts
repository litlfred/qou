import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-shift-multiplicative-chain-significance",
  title:
    "Significance: the $\\alpha_{EM}$ shift chain and the atomic-braid shift framework share one combinatorial primitive",
  interprets: "prop:alpha-em-shift-multiplicative-chain",
  uses: ["prop:alpha-shift-torus-knot"],
  tags: [
    "alpha-em",
    "alpha-shift",
    "torus-knot",
    "seminormal-trace",
    "atomic-shift",
  ],
});
