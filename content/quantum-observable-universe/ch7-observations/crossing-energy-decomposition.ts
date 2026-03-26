import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crossing-energy-decomposition",
  title: "Crossing energy decomposes into strong and Coulomb channels",
  uses: [
    "def:crossing-energy",
    "def:substrate-parameter",
    "rem:pair-creation-energy",
    "rem:chirality-trefoil-electron-positron",
    "rem:mass-comparison-table",
  ],
  tags: [
    "crossing-energy", "strong-force", "coulomb", "decomposition",
    "hyperbolic", "pair-creation", "electromagnetism",
  ],
});
