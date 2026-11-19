import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-degeneracy-blocks-connes",
  title: "A Lipschitz seminorm with nonzero kernel has no finite Connes sup",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.lip_kernel_forces_unbounded",
    validation: "not_checked",
  },
  uses: ["prop:markov-gram-star-positive"],
  tags: [
    "connes-distance",
    "spectral-triple",
    "radical",
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
    engine: "python+mpmath",
    script: "computations/probes/frobenius_gram_matrix_probe.py",
    witness: "computations/probes/frobenius-gram-matrix-probe.witness.json",
    status: "verified",
  },
});
