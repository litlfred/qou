import { remark } from "../../schema/builders";

export default remark({
  label: "rem:pair-creation-energy",
  title: "Energy cost of electron--positron conversion",
  interprets: "def:crossing-energy",
  uses: [
    "def:crossing-energy",
    "rem:chirality-trefoil-electron-positron",
    "rem:trefoil-vortex-chirality-flip",
    "def:substrate-parameter",
    "rem:complex-substrate-interpretation",
    "conj:complex-chirality-rotation",
    "def:exceptional-divisor",
    "rem:mass-comparison-table",
  ],
  tags: [
    "pair-creation", "crossing-energy", "electron", "positron",
    "energy-budget", "exceptional-divisor", "chirality",
  ],
});
