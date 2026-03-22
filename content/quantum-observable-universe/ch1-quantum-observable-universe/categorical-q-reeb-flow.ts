import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-reeb-flow",
  lean: { decl: "QOU.CategoricalQReebFlow" },
  status: "not_started",
  title: "Categorical q-Reeb flow",
  tags: ["reeb-flow", "q-deformation", "category-theory"],
  uses: [
    "def:categorical-reeb",
    "def:categorical-q-lie-bracket",
  ],
});
