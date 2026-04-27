import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-lagrangian-unique",
  title: "Uniqueness of the categorical Lagrangian",
  lean: { ref: "qou:QOU.CategoricalLagrangian.unique",
    validation: "not_checked",
  },
  uses: ["prop:categorical-lagrangian-exists"],
  proofs: ["prf:categorical-lagrangian-unique"],
  tags: ["uniqueness", "lagrangian"],
});
