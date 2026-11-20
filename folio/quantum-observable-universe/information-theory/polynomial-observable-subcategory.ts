import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The poset $\\mathcal{R}^{\\circ}(L, q)$ forms the computational analog of the physical observable subcategory $\\mathrm{Bun}^{\\circ}(\\mathbb{P}(V))$ ([observable subcategory](#def:observable-subcategory))." },
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
