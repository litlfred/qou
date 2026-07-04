import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:crossing-energy-decomposition",
  lean: { ref: "qou:QOU.Braiding.q_decomposition" },
  title: "Crossing energy decomposes into strong and Coulomb channels",
  uses: ["def:crossing-energy"],
  examples: ["rem:pair-creation-energy", "rem:virtual-particles-exceptional-divisor", "rem:electron-immortality", "rem:crossing-energy-decomposition"],
  tags: [
    "crossing-energy", "strong-force", "coulomb", "decomposition",
    "hyperbolic",
  ],
});
