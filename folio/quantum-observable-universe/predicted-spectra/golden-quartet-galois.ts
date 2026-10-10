import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:golden-quartet-galois",
  title:
    "Golden quartet $\\{1/\\varphi, -\\varphi, \\varphi, -1/\\varphi\\}$ as $\\mathrm{Gal}(\\mathbb{Q}(\\sqrt{5})/\\mathbb{Q}) \\times \\langle \\iota \\rangle$-orbit",
  tags: [
    "golden-ratio",
    "galois-theory",
    "bar-involution",
    "skew-symmetry",
    "minimal-polynomial",
    "splitting-field",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.GoldenQuartetGalois.golden_quartet_galois",
    validation: "not_checked",
  },
  uses: [
    "prop:golden-skew-dual-node",
  ],
});
