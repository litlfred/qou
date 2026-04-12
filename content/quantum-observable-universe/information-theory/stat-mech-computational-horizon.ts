import { remark } from "../../schema/builders";

export default remark({
  label: "rem:stat-mech-computational-horizon",
  title:
    "Statistical mechanics as the polynomial observable subcategory",
  interprets: "prop:quantum-ideal-gas-law",
  tags: [
    "statistical-mechanics",
    "computational-horizon",
    "ideal-gas-law",
    "phase-transition",
    "polynomial-observable",
    "degree-0-opacity",
    "incompleteness",
  ],
  uses: [
    "prop:quantum-ideal-gas-law",
    "prop:incompleteness-implies-horizon",
    "def:computational-horizon",
    "prop:phase-transition-boundary",
    "rem:incompleteness-horizon",
    "def:jet-horizon",
    "rem:hawking-radiation",
  ],
});
