import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wenzl-bridge-y-lambda",
  title:
    "Closed-form Jones--Markov $y_\\lambda$ via fractional principal Schur specialisation",
  lean: {
    ref: "qou:QOU.BraidKnot.wenzl_bridge_y_lambda",
    validation: "not_checked",
  },
  uses: [
    "prop:alpha-k-derivation-procedure",
    "prop:plancherel-weight-boundedness",
    "thm:jones-markov-trace",
    "rem:y-lambda-sign-pattern",
    "prop:hoefsmit-seminormal-form",
  ],
  tags: [
    "wenzl-bridge",
    "y-lambda",
    "schur-element",
    "fractional-specialisation",
    "principal-specialisation",
    "macdonald",
    "closed-form",
    "q-rational",
    "jones-markov",
  ],
});
