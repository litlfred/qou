import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-intent-energy",
  title: "Intent and the energetic cost of observation",
  tags: [
    "observation",
    "intent",
    "energy",
    "crossing",
    "entropy",
  ],
  uses: [
    "def:observation",
    "def:crossing-energy",
  ],
});
