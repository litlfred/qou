import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-canonical-markov-weights-explicit-instance",
  title:
    "Explicit $\\sqrt q$-bearing instance of $\\mathbf{CanonicalMarkovWeightsH3}$ (class is inhabitable)",
  uses: [
    "prop:qbeta-per-block-chi-closed-forms",
    "prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  tags: [
    "qbeta",
    "canonical",
    "instance",
    "markov-weights",
    "sqrt-q-bearing",
    "3b-cond",
  ],
  lean: {
    ref:
      "qou:QOU.BraidKnot.CanonicalMarkovWeightsH3.explicitInstance",
  },
  authorNotes: [
    {
      kind: "note",
      body:
        "Provenance: the `markov_parameter` $z(q) = \\sqrt q/(1+q)$ and §Extension #4 landed in PR #1764. Kept in metadata (not scholarly prose) per AGENTS.md §4d.",
    },
  ],
});
