import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:skein-coulomb-enhancement",
  title:
    "Coulomb enhancement from electron-proton Skein crossings",
  tags: [
    "coulomb",
    "fermi-function",
    "sommerfeld",
    "skein",
    "beta-decay",
    "half-life",
    "electron",
    "crossing",
  ],
  lean: { ref: "qou:QOU.Archimedean.skein_coulomb_enhancement",
    validation: "not_checked",
  },
});
