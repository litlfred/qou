import { definition } from "../../schema/builders";

export default definition({
  label: "def:maximal-torus",
  title: "Maximal torus and weight subcategory",
  lean: {
    decl: "QOU.MaximalTorus",
    validation: "not_checked",
  },
  status: "stated",
  uses: ["def:quantum-observable-universe", "def:spin-labels", "thm:su2-emergence"],
  examples: ["ex:maximal-torus-su2"],
  tags: ["torus", "weight"],
});
