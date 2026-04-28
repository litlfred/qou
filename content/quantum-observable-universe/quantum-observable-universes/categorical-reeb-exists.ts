import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:categorical-reeb-exists",
  title: "Existence of the categorical Reeb derivation",
  lean: { ref: "qou:QOU.CategoricalReeb.ofWeightDecomposition",
    validation: "not_checked",
  },
  uses: ["def:categorical-reeb"],
  proofs: ["prf:categorical-reeb-exists"],
  tags: ["existence", "reeb", "derivation"],
});
