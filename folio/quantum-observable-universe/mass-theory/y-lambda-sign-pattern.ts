import { remark } from "../../schema/builders";

export default remark({
  label: "rem:y-lambda-sign-pattern",
  title:
    "Jones–Markov block weights $y_\\lambda$ are not individually non-negative for $n \\geq 4$",
  interprets: "prop:alpha-k-derivation-procedure",
  uses: [
    "prop:alpha-k-derivation-procedure",
    "prop:explicit-alpha-k-h3",
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
  computation: {
    engine: "python+mpmath",
    script: "computations/alpha/alpha_k_jones_markov_h4.py",
    witness: "computations/alpha-k-jones-markov-h4.witness.json",
    status: "verified",
  },
});
