import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "refined-framing", date: "2026-11-15", body: "Filed as a definition by owner ruling (2026-11-15): setting $k_B = 1$ is a choice of units, not a theorem. The former proof is now [rem:boltzmann-constant-motivation](#rem:boltzmann-constant-motivation)." },
  ],
  label: "def:boltzmann-constant",
  title: "Boltzmann constant in QOU natural units",
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
