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
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/qbeta/gram_convention_d_singularity_structural_probe.py",
    witness: [
      "computations/qbeta/gram-convention-d-singularity-structural.witness.json",
      "computations/spectral-decomposition-qvalue-d.witness.json",
    ],
    status: "verified",
  },
});
