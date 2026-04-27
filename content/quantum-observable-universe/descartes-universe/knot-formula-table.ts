import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:knot-particle-generation",
  label: "rem:knot-formula-table",
  title: "Topological knot formulas for fundamental and composite particles",
  tags: [
    "knot",
    "formula",
    "notation",
    "particle",
    "hadron",
    "nucleus",
    "generation",
    "fermion",
    "boson",
    "torus-link",
  ],
  uses: [
    "thm:embeddability-closure",
    "conj:higgs-t28",
  ],
});
