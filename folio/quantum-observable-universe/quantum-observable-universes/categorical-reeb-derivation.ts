import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-reeb-derivation",
  title: "Categorical Reeb derivation",
  lean: { ref: "qou:QOU.Core.AlgebraicSubstrate.CategoricalReebDerivation",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-aether", "def:categorical-reeb"],
  tags: ["reeb", "derivation", "observer-drift", "contact-geometry"],
});
