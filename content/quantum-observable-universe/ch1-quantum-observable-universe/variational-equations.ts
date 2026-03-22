import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:variational-equations",
  title: "Variational equations of the categorical action",
  tags: ["variational", "yang-mills", "einstein"],
  uses: ["def:categorical-action"],
  proofs: ["prf:variational-equations"],
});
