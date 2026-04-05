import { example } from "../../schema/builders";

export default example({
  label: "ex:qvalue-benchmark-table",
  title:
    "Benchmark Q-values: predictions vs NNDC data with error bounds",
  tags: [
    "q-value",
    "beta-decay",
    "benchmark",
    "error-bounds",
    "nndc",
    "codata",
  ],
  uses: [
    "rem:qvalue-derivation-chain",
    "prop:beta-decay-transfer-matrix",
  ],
});
