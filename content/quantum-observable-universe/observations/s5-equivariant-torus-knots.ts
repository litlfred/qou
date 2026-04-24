import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:s5-equivariant-torus-knots",
  lean: { decl: "QOU.TorusKnot.s5_equivariant_classification", validation: "not_checked" },
  title: "$S_5$-equivariant torus-knot embeddings: only $T_{2,3}$ and $T_{2,5}$",
  tags: ["torus-knot", "symmetry", "s5", "equivariant", "leptons"],
  uses: [
    "def:brings-surface",
  ],
});
