import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-proton-unique",
  title: "Uniqueness of the categorical proton up to braid isotopy",
  lean: { ref: "qou:QOU.CategoricalProton.unique_up_to_isotopy",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-proton-exists",
    "prop:hadron-unique",
  ],
  proofs: ["prf:categorical-proton-unique"],
  tags: ["uniqueness", "proton"],
});
