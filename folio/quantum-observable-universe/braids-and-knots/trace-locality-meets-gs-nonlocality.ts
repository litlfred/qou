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
  authorNotes: [
    {
      kind: "status",
      body:
        "**provable from existing infrastructure.** The proof in `prf:trace-locality-meets-gs-non-locality` assembles three already-established QOU components: `thm:jones-markov-trace`, the Gröbner–Shirshov reduction algorithm (as instrumented in QOU's Hecke / Descartes Lean modules), and Wenzl's 1988 vertex-volume factorisation [`wenzl1988`]. No new mathematics is introduced.",
    },
    {
      kind: "note",
      body:
        "**Summary.** The proposition resolves the apparent tension between Markov locality and Gröbner–Shirshov non-locality as sequential operations bridged by Wenzl's product factorisation, with the proof a straightforward assembly of cited existing components.",
    },
  ],
});
