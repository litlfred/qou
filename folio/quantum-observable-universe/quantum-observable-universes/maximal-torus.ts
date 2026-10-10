import { definition } from "../../schema/builders";

export default definition({
  label: "def:maximal-torus",
  title: "Maximal torus and weight subcategory",
  lean: { ref: "qou:QOU.MaximalTorus",
    validation: "not_checked",
  },
  uses: ["prop:spin-labels"],
  examples: ["ex:maximal-torus-su2"],
  tags: ["torus", "weight"],
});
