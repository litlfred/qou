import { example } from "../../schema/builders";

export default example({
  interprets: "def:rigid-monoidal-category",
  label: "ex:rigid-monoidal-vect",
  title: "$\\mathbb{C}[z]$ and $\\mathcal{O}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2RigidData", validation: "not_checked" },
  tags: ["complex", "su2", "representation-theory"],
  uses: ["def:rigid-monoidal-category"],
});
