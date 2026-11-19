import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-gram-bilinear-vs-star",
  title:
    "Two pairings, two signatures: $\\mathrm{tr}_M(b_ib_j)$ versus $\\mathrm{tr}_M(b_ib_j^{*})$",
  interprets: "prop:markov-gram-star-positive",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.traceform_M2",
    validation: "not_checked",
  },
  uses: ["prop:markov-gram-star-positive"],
  tags: [
    "star-pairing",
    "signature",
    "retraction",
    "gram-matrix",
    "trace-convention",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "Retraction carrier. Commit 748ba9b1 withdrew the 'Lorentzian / indefinite " +
        "Markov-Gram form' reading and with it the claim that the framework's natural " +
        "object is a causal structure rather than a metric space. The (3,1) split on the " +
        "(2,1) block is a property of the BILINEAR pairing tr_M(b_i b_j) alone; under the " +
        "Hecke star pairing tr_M(b_i b_j*) the same block contributes (4,0) and the whole " +
        "form is positive — (6,0,0) under convention C, (5,0,1) under convention D. " +
        "No block in this corpus may write 'indefinite' or 'Lorentzian' of the Markov-Gram " +
        "form without naming which of the two pairings it means.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/qbeta/gram_convention_d_singularity_structural_probe.py",
    witness: "computations/qbeta/gram-convention-d-singularity-structural.witness.json",
    status: "verified",
  },
});
