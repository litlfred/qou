import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qvalue-method-distinction",
  title:
    "Categorical Q-value (zero fitting) vs fitted approaches",
  interprets: "prop:beta-decay-transfer-matrix",
  tags: [
    "q-value",
    "beta-decay",
    "methodology",
    "categorical",
    "zero-parameters",
    "channel-separation",
  ],
  uses: [
    "rem:qvalue-derivation-chain",
    "ex:qvalue-benchmark-table",
    "cor:spectral-decomposition-qvalue",
    "prop:beta-decay-transfer-matrix",
  ],
});
