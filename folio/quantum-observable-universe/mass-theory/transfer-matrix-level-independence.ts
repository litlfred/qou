import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:transfer-matrix-level-independence",
  lean: { ref: "qou:QOU.transfer_matrix_level_independence_of_derived",
    validation: "not_checked",
  },
  title: "Transfer matrix level independence",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "markov-trace", "level-independence",
  ],
  uses: [
    "conj:crystal-graph-realization",
    "def:categorical-transfer-matrix",
    "def:bundle-isotopy-equivalence",
  ],
  proofs: ["prf:transfer-matrix-level-independence"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([isotopy equivalence](#def:bundle-isotopy-equivalence))" },
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**Part 1 was backed by a false axiom.** " +
        "`transfer_matrix_level_independence_axiom` asserted that the " +
        "constituent product equals `HadronConfig.compositePolynomial` -- " +
        "but the composite is a free field of that structure, tied to the " +
        "constituents by nothing, so the empty configuration has product " +
        "1 and composite 0. Refuted in the sibling `.lean` by " +
        "`not_transfer_matrix_level_independence`. A SECOND axiom of the " +
        "same name, over `CategoricalTransferMatrix`, was found false and " +
        "repaired separately in `categorical-transfer-matrix.lean`; the " +
        "shared name is what let this one survive that fix. The live " +
        "statement derives the composite from the constituents and " +
        "concludes that configurations sharing constituents share it. " +
        "Parts 2 and 3 remain unformalised.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
