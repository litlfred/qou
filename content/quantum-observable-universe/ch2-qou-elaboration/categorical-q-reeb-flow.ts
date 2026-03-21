import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-reeb-flow",
  title: "Categorical q-Reeb flow",
  tags: ["q-deformed", "reeb", "categorical"],
  lean: {
    decl: "QOU.CategoricalQReebFlow",
    validation: "not_checked",
  },
  status: "not_started",
  uses: [
    "def:categorical-reeb",
    "def:categorical-q-lie-bracket",
  ],
});
