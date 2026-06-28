import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:beta-decay-transfer-matrix",
  label: "rem:beta-decay-tritium-example",
  title: "Beta decay worked example: tritium ${}^3\\mathrm{H} \\to {}^3\\mathrm{He}$",
  tags: ["beta-decay", "tritium", "transfer-matrix", "worked-example"],
  uses: ["def:Q-value-transition"],
});
