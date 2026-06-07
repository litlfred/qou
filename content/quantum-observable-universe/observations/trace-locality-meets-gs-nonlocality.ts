import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trace-locality-meets-gs-non-locality",
  title:
    "Reconciliation: Markov locality of single generators vs. Gröbner-Shirshov non-locality of composite braids",
  lean: {
    ref: "qou:QOU.Observations.TraceLocalityMeetsGsNonLocality.HasReconciliation",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "rem:non-commutative-probability-dictionary",
  ],
  cites: ["wenzl1988"],
  tags: [
    "locality",
    "markov-property",
    "grobner-shirshov",
    "product-factorization",
    "vertex-volume",
    "issue-649",
    "established",
  ],
  proofs: ["prf:trace-locality-meets-gs-non-locality"],
});
