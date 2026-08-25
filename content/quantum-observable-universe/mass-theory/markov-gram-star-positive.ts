import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-gram-star-positive",
  title:
    "The Markov--Gram star form is positive semidefinite; positivity reduces to $y_\\lambda \\ge 0$",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.markov_star_nonneg",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-gram-matrix",
    "prop:h3-markov-wenzl-weights",
  ],
  tags: [
    "markov-trace",
    "gram-matrix",
    "star-pairing",
    "hecke-algebra",
    "convention-d",
    "trace-convention",
  ],
});
