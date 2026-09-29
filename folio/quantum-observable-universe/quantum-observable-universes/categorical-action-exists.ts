import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-action-exists",
  title: "Existence of the categorical action",
  lean: { ref: "qou:QOU.CategoricalAction.exists",
    validation: "not_checked",
  },
  uses: ["def:categorical-action"],
  proofs: ["prf:categorical-action-exists"],
  tags: ["existence", "categorical-action"],
});
