import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-functor-uniqueness-context",
  title:
    "Pre-archimedean separation, corollaries, and open problems for the archimedean functor uniqueness",
  interprets: "prop:archimedean-functor-uniqueness",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "archimedean",
    "realization-functor",
    "bloch-wigner",
    "pentagon-identity",
    "pre-archimedean",
    "alpha-em",
  ],
  uses: ["prop:archimedean-functor-uniqueness"],
  cites: ["suslin1991", "bloch2000"],
  authorNotes: [
    {
      kind: "deprecated",
      body: "The multiplicative gluon-octet PSLQ form was a legacy conjecture, removed from the corpus and superseded by prop:em-coupling-bring-zero-mode.",
    },
  ],
});
