import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:boltzmann-constant",
  title: "Boltzmann constant is unity in QOU natural units",
  tags: [
    "boltzmann-constant",
    "statistical-mechanics",
    "planck-constant",
  ],
  lean: { ref: "qou:QOU.Information.thermalEnergy",
    validation: "not_checked",
  },
  uses: ["def:quantum-temperature"],
});
