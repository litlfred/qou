import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:symmetric-crystal-pair-production",
  label: "rem:two-photon-pair-production",
  title:
    "Two photons hitting a heavy nucleus: $\\gamma\\gamma \\to e^- e^+$ as a forced symmetric-crystal step",
  uses: ["prop:symmetric-crystal-pair-production"],
  tags: [
    "pair-production",
    "two-photon",
    "concrete-example",
    "qed",
    "symmetric-crystal",
    "cpt",
  ],
});
