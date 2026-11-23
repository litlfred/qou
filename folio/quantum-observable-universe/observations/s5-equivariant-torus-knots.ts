import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:s5-equivariant-torus-knots",
  lean: { ref: "qou:QOU.TorusKnot.s5_equivariant_classification", validation: "not_checked" },
  title: "$S_5$-equivariant torus-knot embeddings: the $\\mathbb{Z}_s$ and monodromy tests",
  tags: ["torus-knot", "symmetry", "s5", "equivariant", "leptons"],
  uses: [
    "def:brings-surface",
  ],
});
