import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crossing-energy-interpretation",
  title: "Physical interpretation: strong binding and Coulomb repulsion",
  interprets: "prop:crossing-energy-decomposition",
  uses: [
    "prop:crossing-energy-decomposition",
    "rem:mass-comparison-table",
  ],
  tags: [
    "crossing-energy", "strong-force", "coulomb",
    "pair-creation", "electromagnetism", "interpretation",
  ],
});
