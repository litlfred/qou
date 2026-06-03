import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:t-beta-markov-frobenius-collapse-general",
  title:
    "Min-Frobenius-norm collapse: T_β = S · 1 — general unital R-algebra lift of [prop:t-beta-markov-frobenius-collapse]",
  lean: {
    ref: "qou:QOU.QBeta.MarkovFrobeniusCollapse.General.markov_frobenius_min_norm_lift",
    validation: "not_checked",
  },
  uses: [
    "prop:t-beta-markov-frobenius-collapse",
    "prop:markov-trace-frobenius-selection",
  ],
  cites: ["jones1987", "wenzl1988"],
  tags: [
    "markov-trace",
    "frobenius",
    "q-beta",
    "min-norm",
    "categorical-collapse",
    "general-lift",
    "typeclass",
  ],
});
