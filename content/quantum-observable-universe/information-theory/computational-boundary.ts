import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:computational-boundary",
  title: "Computational boundary of a resolution tree",
  tags: [
    "P-vs-NP",
    "computational-horizon",
    "jet-horizon",
    "resolution-tree",
    "complexity",
    "information-barrier",
  ],
  lean: {
    ref: "qou:QOU.PvsNPBoundary.computationalBoundary",
    validation: "not_checked",
  },
  uses: [
    "def:polynomial-observable-subcategory",
    "def:jet-horizon",
  ],
});
