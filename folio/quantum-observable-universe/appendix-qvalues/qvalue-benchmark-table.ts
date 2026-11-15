import { example } from "../../schema/builders";

export default example({
  label: "ex:qvalue-benchmark-table",
  title:
    "Benchmark Q-values: $\\mathcal{Q}_q$ predictions vs NNDC data ($2 \\times 2 = 6 \\times 6$, MAE $\\approx 4.4\\%$, zero fitting)",
  tags: [
    "q-value",
    "beta-decay",
    "benchmark",
    "error-bounds",
    "nndc",
    "codata",
    "q-weighted",
    "channel-separation",
    "shell-correction",
  ],
  uses: [
    "rem:qvalue-derivation-chain",
    "cor:spectral-decomposition-qvalue",
  ],
});
