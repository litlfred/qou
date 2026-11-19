import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gluon-model-comparison",
  title: "Gluon models: $B_3$ encodes Hopf links",
  tags: ["gluon", "hopf-link", "borromean", "nucleon-nf", "appendix"],
  uses: ["rem:hecke-operations"],
  interprets: "conj:borromean-quark",
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/nf-qvalues.witness.json",
      "computations/probes/h4-fulltwist-alpha-and-carbon12-groebner.witness.json",
      "computations/probes/h2_weak_vertex_electron/h2-weak-vertex-electron.witness.json",
    ],
    status: "verified",
  },
});
