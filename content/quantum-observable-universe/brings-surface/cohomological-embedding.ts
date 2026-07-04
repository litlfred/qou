import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:cohomological-embedding",
  title:
    "Cohomological embedding: torus knot representations exhaust $H^1(\\Sigma_g)$",
  tags: [
    "cohomological-embedding",
    "torus-knot",
    "representation",
    "jones-polynomial",
    "genus",
    "completeness",
    "magic-numbers",
    "shell-model",
  ],
  lean: { ref: "qou:QOU.Archimedean.cohomological_embedding",
    validation: "not_checked",
  },
  uses: ["rem:fivefold-symmetry"],
  examples: ["rem:fivefold-symmetry"],
});
