import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:composite-crossing-parity",
  title: "Sublimation from shell-filling representation theory",
  tags: [
    "sublimation",
    "shell-structure",
    "young-diagram",
    "hecke-representation",
    "phase-transition",
    "magic-numbers",
  ],
  lean: { ref: "qou:QOU.Information.crossing_parity_eq_Z",
    validation: "not_checked",
  },
  uses: [
    "prop:shell-structure-eigenvalues",
    "prop:noble-gas-characterization",
  ],
});
