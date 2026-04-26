import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:y-lambda-cyclotomic-factorization",
  title:
    "Cyclotomic factorisation of $y_\\lambda$ at $H_n(R, q)$ for small $n$ via Wenzl-bridge",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_cyclotomic_factorization",
    validation: "not_checked",
  },
  uses: [
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:explicit-alpha-k-h3",
    "prop:alpha-k-derivation-procedure",
    "thm:jones-markov-trace",
  ],
  cites: ["wenzl1988", "macdonald1995"],
  tags: [
    "y-lambda",
    "cyclotomic-polynomial",
    "schur-element",
    "closed-form",
    "wenzl-bridge",
    "q-rational",
    "principal-specialization",
  ],
});
