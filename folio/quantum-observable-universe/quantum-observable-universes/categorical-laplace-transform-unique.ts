import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-laplace-unique",
  title: "Uniqueness of the categorical Laplace transform",
  lean: { ref: "qou:QOU.CategoricalLaplace.unique",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-laplace-exists",
    "prop:q-exponential-unique",
  ],
  proofs: ["prf:categorical-laplace-unique"],
  tags: ["uniqueness", "laplace"],
});
