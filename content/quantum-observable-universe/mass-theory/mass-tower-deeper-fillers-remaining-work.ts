import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:crystal-basis-resolves-mass-tower-open-problems",
  label: "rem:mass-tower-deeper-fillers-remaining-work",
  title: "Remaining upstream Mathlib work after the deeper mass-tower fillers",
  uses: [
    "prop:type-b-folded-crystal-combinatorics",
    "rem:bloch-wigner-mathlib-filler",
  ],
  cites: ["borel1974", "suslin1991", "zagier1986"],
  tags: [
    "remaining-work",
    "bloch-group",
    "pentagon-identity",
    "faddeev-kashaev",
    "lean-infrastructure",
  ],
});
