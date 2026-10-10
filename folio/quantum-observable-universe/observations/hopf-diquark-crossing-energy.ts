import { example } from "../../schema/builders";

export default example({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c): the crossing-energy sum and the binding inequality $\\mathfrak{E}_{\\mathrm{cross}} < 0$ are evaluated at the substrate $q$. The underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "ex:hopf-diquark-crossing-energy",
  title: "Hopf crossing energy of a diquark",
  interprets: "def:hopf-diquark",
  tags: ["diquark", "hopf", "crossing-energy", "cooper-pair"],
  uses: ["def:hopf-diquark"],
});
