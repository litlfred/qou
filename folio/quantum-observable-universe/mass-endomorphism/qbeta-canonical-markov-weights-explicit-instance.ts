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
    ref: "qou:QOU.BraidKnot.CanonicalMarkovWeightsH3.explicitInstance",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean class `CanonicalMarkovWeightsH3` (declared in [Per-block character closed forms for $\\chi_\\lambda(\\Delta_{T_\\beta})(q)$ over $H_3(q)$](qbeta-per-block-chi-closed-forms.md) §Extension #4) is inhabited. We construct an explicit $\\sqrt q$-bearing instance:" },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**Convention C is excised by owner ruling; this instance is " +
        "deliberately left on it.** The block exists to witness that " +
        "`CanonicalMarkovWeightsH3` is inhabitable, and the witness it " +
        "carries was built on $z(q) = 1/(q^{1/2}+q^{-1/2})$. Rebuilding it " +
        "on the production $z = q^3/(q^2+1)$ would be a different " +
        "construction, not a correction, and nothing downstream reads this " +
        "instance's $z$ as the paper's. The prose states that scope; the " +
        "ruling's date sits here per \u00a74d.",
    },
    {
      kind: "note",
      body:
        "Provenance: the `markov_parameter` $z(q) = \\sqrt q/(1+q)$ and §Extension #4 landed in PR #1764. Kept in metadata (not scholarly prose) per AGENTS.md §4d.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). The forcing construct is the **square root**: " +
        "this instance is built from `markov_parameter q = Real.sqrt q / " +
        "(1 + q)` (`QBetaPerBlockChiClosedForms`, itself flagged there as " +
        "*\"pure archimedean construction — depends on `Real.sqrt`\"*), and " +
        "`Real.sqrt` has no `CommRing` analogue: $\\sqrt q \\notin " +
        "\\mathbb{Z}[q^{\\pm 1}]$, and even over $\\mathbb{Z}[q^{\\pm 1/2}]$ " +
        "a branch must be chosen, which is precisely what the real square " +
        "root supplies. The specialisation is therefore *inherited*, not " +
        "introduced here — the class `CanonicalMarkovWeightsH3` already " +
        "types its weights `ℝ → ℝ` and quantifies its normalisation axiom " +
        "$\\forall q > 0$, and " +
        "`delta_tau_M_canonical_explicit_has_q2_minus_1_factor` carries the " +
        "same `0 < q` hypothesis. What stays generic is the other half of " +
        "the product: the per-block characters `chi_block_3/21/111` are " +
        "rational in $q$ and their $(q^2-1)$ factorisation is discharged by " +
        "`ring`, so the $(q^2-1)$ theorem is pre-archimedean in its " +
        "character input and archimedean only through the $\\sqrt q$ weight " +
        "it multiplies by.",
    },
  ],
});
