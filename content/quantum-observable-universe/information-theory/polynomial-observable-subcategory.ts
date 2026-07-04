import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:polynomial-observable-subcategory",
  title: "Polynomial observable subcategory of a resolution tree",
  tags: [
    "P-vs-NP",
    "resolution-tree",
    "observable-subcategory",
    "markov-trace",
    "complexity",
    "computational-horizon",
  ],
  lean: {
    ref: "qou:QOU.PvsNPBoundary.polynomialObservableSubcategory",
    validation: "not_checked",
  },
  uses: [
    "rem:skein-turing-machine",
    "def:observable-subcategory",
  ],
});
