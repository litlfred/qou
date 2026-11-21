import { remark } from "../../schema/builders";

export default remark({
  label: "rem:pair-creation-energy",
  title: "Energy cost of electron--positron conversion",
  interprets: "def:crossing-energy",
  uses: [
    "rem:trefoil-vortex-chirality-flip",
    "rem:mass-comparison-table",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [topologically stable](#rem:trefoil-vortex-chirality-flip)" },
  ],
  tags: [
    "pair-creation", "crossing-energy", "electron", "positron",
    "energy-budget", "exceptional-divisor", "chirality",
  ],
});
