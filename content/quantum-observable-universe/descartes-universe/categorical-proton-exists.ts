import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-proton-exists",
  title: "Existence of the categorical proton",
  lean: {
    decl: "QOU.CategoricalProton.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-proton",
    "conj:borromean-quark",
  ],
  proofs: ["prf:categorical-proton-exists"],
  tags: ["existence", "proton", "baryon"],
});
