import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:variational-equations",
  lean: { ref: "qou:QOU.variational_equations",
    validation: "not_checked",
  },
  title: "Variational equations of the categorical action",
  tags: ["variational", "yang-mills", "einstein"],
  uses: ["def:categorical-action"],
  proofs: ["prf:variational-equations"],
});
