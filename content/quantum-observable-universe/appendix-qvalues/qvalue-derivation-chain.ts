import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qvalue-derivation-chain",
  title:
    "Q-value derivation chain: from $q$ to $\\beta$-decay predictions",
  tags: [
    "q-value",
    "beta-decay",
    "transfer-matrix",
    "derivation-chain",
    "zero-parameters",
  ],
  interprets: "prop:beta-decay-transfer-matrix",
  uses: [
    "def:stable-nucleus",
    "prop:rj-canonical-inner-product",
    "prop:skein-polynomial-transfer-matrix",
    "prop:shell-closure-normal-form",
  ],
});
