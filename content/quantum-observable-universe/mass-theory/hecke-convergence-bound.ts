import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:hecke-convergence-bound",
  title: "Hecke convergence bound: $\\mathrm{MAE}(H_k) \\leq C \\cdot r^{-(k-3)}$",
  lean: { ref: "qou:QOU.BraidKnot.hecke_convergence_bound", validation: "not_checked" },
  uses: [],
  tags: ["convergence", "hecke-level", "plancherel", "mass-formula"],
});
