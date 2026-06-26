import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-26",
      body: "While the Galois properties of $\\mathbb{Q}(\\sqrt{5})$ and the golden ratio are entirely standard, introducing the joint group $G = \\mathrm{Gal} \\times \\langle \\iota \\rangle$ acting on the specific quartet $Q$ provides a novel structural refactoring for QOU models. Rather than relying on standard cyclotomic $\\zeta_5$ bookkeeping which carries complex phase ambiguities, this formulation allows physical observables to be strictly bounded within the maximal real subfield. This geometric substitution of the cyclotomic Galois tracking with a pure real orbit $Q$ is conceptually novel in the context of Bring's curve reductions.",
    },
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
  uses: ["prop:golden-skew-dual-node"],
});
