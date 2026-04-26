import { remark } from "../../schema/builders";

export default remark({
  label: "rem:y-lambda-sign-pattern",
  title:
    "Jones–Markov block weights $y_\\lambda$ are not individually non-negative for $n \\geq 4$",
  interprets: "prop:alpha-k-derivation-procedure",
  uses: [
    "prop:alpha-k-derivation-procedure",
    "prop:plancherel-weight-boundedness",
    "thm:jones-markov-trace",
    "prop:explicit-alpha-k-h3",
    "prop:bw-coefficient-shadow-price",
  ],
  tags: [
    "jones-markov",
    "y-lambda",
    "positivity",
    "sign-pattern",
    "lp-feasibility",
    "structural-observation",
    "alternating-block",
  ],
});
