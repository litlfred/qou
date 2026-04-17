import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-reeb-unique",
  title: "Uniqueness of the categorical Reeb derivation",
  lean: {
    decl: "QOU.CategoricalReeb.unique",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-reeb",
    "thm:categorical-reeb-exists",
    "def:weight-decomposition",
  ],
  proofs: ["prf:categorical-reeb-unique"],
  tags: ["uniqueness", "reeb", "derivation"],
});
