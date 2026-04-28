import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-hodge-star-unique",
  title: "Uniqueness of the categorical Hodge star",
  lean: { ref: "qou:QOU.CategoricalHodgeStar.unique",
    validation: "not_checked",
  },
  uses: ["prop:categorical-hodge-star-exists"],
  proofs: ["prf:categorical-hodge-star-unique"],
  tags: ["uniqueness", "hodge-star"],
});
