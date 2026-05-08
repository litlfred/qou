import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-instanton-exists",
  title: "Existence of categorical instantons",
  lean: { ref: "qou:QOU.CategoricalInstanton.exists",
    validation: "not_checked",
  },
  uses: ["def:categorical-instanton"],
  proofs: ["prf:categorical-instanton-exists"],
  tags: ["existence", "instanton", "self-duality"],
});
