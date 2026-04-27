import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-proton-exists",
  title: "Existence of the categorical proton",
  lean: { ref: "qou:QOU.CategoricalProton.exists",
    validation: "not_checked",
  },
  proofs: ["prf:categorical-proton-exists"],
  tags: ["existence", "proton", "baryon"],
});
