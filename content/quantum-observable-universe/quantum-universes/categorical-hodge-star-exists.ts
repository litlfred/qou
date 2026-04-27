import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-hodge-star-exists",
  title: "Existence of the categorical Hodge star",
  lean: { ref: "qou:QOU.CategoricalHodgeStar.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-hodge-star",
    "def:frobenius-pairing",
  ],
  proofs: ["prf:categorical-hodge-star-exists"],
  tags: ["existence", "hodge-star"],
});
