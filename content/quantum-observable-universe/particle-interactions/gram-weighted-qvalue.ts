import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:gram-weighted-qvalue",
  title:
    "Gram-weighted $\\mathcal{Q}_q$-value from Frobenius norm of conversion channels",
  tags: [
    "q-value",
    "gram-matrix",
    "frobenius-norm",
    "beta-decay",
    "garside-element",
    "hecke-algebra",
    "adjoint-character",
  ],
  lean: { ref: "qou:QOU.Archimedean.gram_weighted_qvalue",
    validation: "not_checked",
  },
  uses: ["def:typed-garside-element"],
});
