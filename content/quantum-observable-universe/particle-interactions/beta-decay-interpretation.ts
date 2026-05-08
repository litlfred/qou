import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:beta-decay-transfer-matrix",
  label: "rem:beta-decay-interpretation",
  title: "Beta decay universality, tritium example, and double beta decay",
  tags: [
    "beta-decay",
    "universality",
    "tritium",
    "double-beta",
    "transfer-matrix",
    "worked-example",
  ],
  uses: [
    "prop:beta-decay-transfer-matrix",
    "def:Q-value-transition",
  ],
});
