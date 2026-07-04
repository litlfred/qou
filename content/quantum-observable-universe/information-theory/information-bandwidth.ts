import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:information-bandwidth",
  title: "Information bandwidth per Planck time",
  tags: [
    "information-bandwidth",
    "information-theory",
    "bremermann",
    "speed-of-light",
    "operational-entropy",
  ],
  lean: { ref: "qou:QOU.Information.informationBandwidth",
    validation: "not_checked",
  },
  uses: [
    "def:information-speed-of-light",
    "def:operational-entropy",
  ],
});
