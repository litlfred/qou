import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-torsion-leaf",
  title: "Categorical q-torsion leaf",
  tags: ["q-deformed", "torsion", "categorical"],
  lean: {
    decl: "QOU.CategoricalQTorsionLeaf",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:categorical-q-reeb-flow"],
});
