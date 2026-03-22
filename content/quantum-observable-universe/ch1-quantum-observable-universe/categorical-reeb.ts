import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-reeb",
  title: "Categorical Reeb derivation",
  lean: {
    decl: "QOU.CategoricalReeb",
    validation: "not_checked",
  },
  status: "stated",
  uses: ["def:maximal-torus", "def:weight-decomposition"],
  examples: ["ex:reeb-su2"],
  tags: ["reeb", "derivation"],
});
