import { remark } from "../../schema/builders";

export default remark({
  label: "rem:two-observer-parallelogram",
  title: "Two-observer parallelogram",
  tags: ["observation", "uncertainty"],
  uses: [
    "def:observation",
    "def:categorical-point",
    "def:fermion-boson-decomposition",
  ],
});
