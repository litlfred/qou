import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-brings",
  title: "Observations on the Bring's surface",
  tags: ["descartes-universe", "observation", "brings-surface"],
  uses: [
    "def:observation",
    "def:substrate-parameter",
    "rem:two-observer-parallelogram",
  ],
});
