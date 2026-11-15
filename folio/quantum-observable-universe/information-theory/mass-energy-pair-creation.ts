import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:mass-energy-equivalence",
  label: "rem:mass-energy-pair-creation",
  title: "Pair creation reinterpreted via crossing energy",
  tags: [
    "mass-energy",
    "pair-creation",
    "crossing-energy",
    "threshold",
    "information-theory",
  ],
  uses: [
    "thm:mass-energy-equivalence",
    "rem:pair-creation-energy",
  ],
});
