import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-reeb",
  title: "Categorical Reeb derivation",
  lean: { ref: "qou:QOU.CategoricalReeb",
    validation: "not_checked",
  },
  uses: ["def:weight-decomposition"],
  examples: ["ex:reeb-su2", "ex:connection-su2"],
  tags: ["reeb", "derivation"],
});
