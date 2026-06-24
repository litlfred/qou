import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:y-lambda-closed-form-wenzl-bridge",
  proofs: ["prf:y-lambda-closed-form-wenzl-bridge"],
  title:
    "Closed form for Jones-Markov $y_\\lambda$ via Wenzl Schur-element bridge ($Q = q^2$, $z_{\\mathrm{GL}} = q z$)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_closed_form_wenzl_bridge",
    validation: "not_checked",
  },
  uses: [
    "prop:explicit-alpha-k-h3",
    "prop:alpha-k-derivation-procedure",
  ],
  cites: ["wenzl1988", "orellana1998", "chlouveraki2016"],
  tags: [
    "y-lambda",
    "schur-element",
    "wenzl",
    "orellana",
    "convention-bridge",
    "closed-form",
    "q-rational",
    "principal-specialization",
  ],
});
