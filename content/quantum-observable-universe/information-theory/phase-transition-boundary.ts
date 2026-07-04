import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:phase-transition-boundary",
  title: "Phase transitions as $S^3$ boundary actions",
  tags: [
    "phase-transition",
    "s3-boundary",
    "statistical-mechanics",
    "sublimation",
    "hecke-algebra",
    "braid-representation",
  ],
  lean: { ref: "qou:QOU.Information.gasLiquidCriticalTemp",
    validation: "not_checked",
  },
  uses: ["prop:quantum-ideal-gas-law"],
});
