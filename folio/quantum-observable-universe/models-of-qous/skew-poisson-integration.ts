import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:skew-poisson-integration",
  lean: { ref: "qou:QOU.Archimedean.skew_poisson_integration",
    validation: "not_checked",
  },
  title: "Integration of skewed-Poisson structures",
  uses: ["def:witt-vector-lift"],
  proofs: ["prf:skew-poisson-integration"],
});
