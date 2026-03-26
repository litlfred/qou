import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-torsion-leaf",
  lean: { decl: "QOU.CategoricalQTorsionLeaf" },
  title: "Categorical q-torsion leaf",
  tags: ["torsion", "q-deformation", "category-theory"],
  uses: ["def:weight-decomposition", "def:categorical-q-reeb-flow"],
});
