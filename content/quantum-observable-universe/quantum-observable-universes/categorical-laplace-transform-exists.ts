import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-laplace-exists",
  title: "Existence of the categorical Laplace transform",
  lean: { ref: "qou:QOU.CategoricalLaplace.exists",
    validation: "not_checked",
  },
  uses: ["prop:q-exponential-exists"],
  proofs: ["prf:categorical-laplace-exists"],
  tags: ["existence", "laplace", "monoidal-functor"],
});
