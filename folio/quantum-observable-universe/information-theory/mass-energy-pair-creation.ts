import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:mass-energy",
  label: "rem:mass-energy-pair-creation",
  title: "Pair-creation threshold in terms of energy",
  tags: [
    "mass-energy",
    "pair-creation",
    "crossing-energy",
    "threshold",
    "information-theory",
  ],
  uses: [
    "prop:mass-energy",
    "rem:pair-creation-energy",
  ],
});
