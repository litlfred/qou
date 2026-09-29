import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:quantum-volume",
  title: "Quantum volume",
  tags: [
    "volume",
    "statistical-mechanics",
    "categorical-volume",
    "s3-fibre",
    "reeb-bundle",
  ],
  lean: { ref: "qou:QOU.Information.quantumVolume",
    validation: "not_checked",
  },
  uses: ["def:reeb-bundle"],
});
