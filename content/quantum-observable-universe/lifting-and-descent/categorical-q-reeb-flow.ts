import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-reeb-flow",
  lean: { ref: "qou:QOU.CategoricalQReebFlow", validation: "not_checked" },
  title: "Categorical q-Reeb flow",
  tags: ["reeb-flow", "q-deformation", "category-theory"],
  uses: ["def:categorical-q-lie-bracket"],
});
