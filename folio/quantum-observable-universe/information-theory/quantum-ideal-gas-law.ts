import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:quantum-ideal-gas-law",
  title: "Quantum ideal gas law",
  tags: [
    "ideal-gas",
    "statistical-mechanics",
    "equation-of-state",
    "q-anomaly",
    "noether",
    "hydrogen",
  ],
  lean: { ref: "qou:QOU.Information.IdealKnotGas",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-pressure",
    "def:quantum-volume",
    "rem:noether-theorem-callout",
  ],
});
