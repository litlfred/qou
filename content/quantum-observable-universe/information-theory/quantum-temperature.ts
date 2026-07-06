import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:quantum-temperature",
  title: "Quantum temperature",
  tags: [
    "temperature",
    "statistical-mechanics",
    "reeb-flow",
    "planck-time",
    "non-abelian-stokes",
    "surface-integral",
  ],
  lean: { ref: "qou:QOU.Information.quantumTemperature",
    validation: "not_checked",
  },
  uses: ["rem:kashaev-volume-density", "def:quantum-entropy", "def:planck-time"],
});
