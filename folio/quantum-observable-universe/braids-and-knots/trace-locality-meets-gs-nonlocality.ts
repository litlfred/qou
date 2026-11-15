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
  tags: [
    "locality",
    "markov-property",
    "grobner-shirshov",
    "issue-649",
    "established",
  ],
  proofs: ["prf:trace-locality-meets-gs-non-locality"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Part (3), the product factorisation of the Markov trace over the Gröbner–Shirshov normal form, was removed from the statement on owner ruling (2026-11-15) and moved to `rem:trace-locality-product-factorisation-check`. Its proof left the vertex volumes undefined and relied on multiplicativity of the trace, which does not hold; what survives is a finite check of the Wedderburn block weights for n ≤ 5. The Lean class `HasReconciliation` still carries a `productFactorisation` field, so it now assumes more than this statement says; that is for the Lean-foundations work to rescope.",
    },
  ],
});
