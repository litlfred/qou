import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:two-observer-parallelogram",
  title: "Two-observer parallelogram",
  tags: ["observation", "uncertainty"],
  uses: [
    "def:observation",
    "def:fermion-boson-decomposition",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/two-observer-parallelogram-0.svg", blockIndex: 0, hash: "3a231587a84b" },
  ],

});
