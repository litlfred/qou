import { remark } from "../../schema/builders";

export default remark({
  label: "rem:per-nucleon-channel-decomposition-remark",
  title: "Branching origin and channels of the per-nucleon decomposition",
  interprets: "def:per-nucleon-channel-decomposition",
  uses: [
    "def:per-nucleon-channel-decomposition",
    "def:typed-crossing-operator",
  ],
});
