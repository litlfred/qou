import { remark } from "../../schema/builders";

export default remark({
  label: "rem:frobenius-gram-matrix-context",
  title: "NF Markov-trace computation, operator identification via the dual, and the annihilation identity",
  interprets: "prop:frobenius-gram-matrix",
  tags: ["frobenius", "gram-matrix", "markov-trace", "operator-selection"],
  uses: ["prop:frobenius-gram-matrix"],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/frobenius_gram_matrix_probe.py",
    witness: [
      "computations/probes/frobenius-gram-matrix-probe.witness.json",
      "computations/alpha-k-jones-markov-h3.witness.json",
      "computations/probes/trm5-zcubed-live-producer-audit.witness.json",
    ],
    status: "verified",
  },
});
