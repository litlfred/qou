import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-action-unique",
  title: "Uniqueness of the categorical action (given $\\Phi$)",
  lean: {
    decl: "QOU.CategoricalAction.unique",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-action",
    "prop:categorical-action-exists",
  ],
  proofs: ["prf:categorical-action-unique"],
  tags: ["uniqueness", "categorical-action"],
});
