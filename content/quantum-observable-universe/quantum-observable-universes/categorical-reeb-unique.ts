import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-reeb-unique",
  title: "Uniqueness of the categorical Reeb derivation",
  lean: { ref: "qou:QOU.CategoricalReeb.unique",
    validation: "not_checked",
  },
  uses: ["thm:categorical-reeb-exists"],
  proofs: ["prf:categorical-reeb-unique"],
  tags: ["uniqueness", "reeb", "derivation"],
});
