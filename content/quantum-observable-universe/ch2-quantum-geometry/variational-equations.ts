import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:variational-equations",
  lean: {
    decl: "QOU.variational_equations",
    validation: "not_checked",
  },
  title: "Variational equations of the categorical action",
  tags: ["variational", "yang-mills", "einstein"],
  uses: ["def:categorical-action"],
  proofs: ["prf:variational-equations"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/variational-equations-0.svg", blockIndex: 0, hash: "27882e5050a7" },
  ],

});
