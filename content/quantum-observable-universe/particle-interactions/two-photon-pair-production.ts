import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:symmetric-crystal-pair-production",
  label: "rem:two-photon-pair-production",
  title:
    "Two photons hitting a heavy nucleus: $\\gamma\\gamma \\to e^- e^+$ as a forced symmetric-crystal step",
  uses: [
    "conj:symmetric-crystal-pair-production",
    "conj:crystal-graph-realization",
  ],
  tags: [
    "pair-production",
    "two-photon",
    "concrete-example",
    "qed",
    "symmetric-crystal",
    "cpt",
  ],
});
