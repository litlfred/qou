import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qvalue-observation",
  title:
    "Q-value predictions vs experiment: $q$-weighted channel separation",
  interprets: "cor:spectral-decomposition-qvalue",
  tags: [
    "q-value",
    "beta-decay",
    "observation",
    "channel-separation",
    "q-weighted",
    "nndc",
    "error-propagation",
  ],
  uses: [
    "cor:spectral-decomposition-qvalue",
    "rem:mass-comparison-table",
  ],
});
