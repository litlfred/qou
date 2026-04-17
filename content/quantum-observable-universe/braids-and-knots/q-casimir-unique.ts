import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-casimir-unique",
  title: "Uniqueness of the $q$-Casimir element up to scalar",
  lean: {
    decl: "QOU.QCasimir.unique_up_to_scalar",
    validation: "not_checked",
  },
  uses: [
    "def:q-casimir",
    "prop:q-casimir-exists",
  ],
  proofs: ["prf:q-casimir-unique"],
  tags: ["uniqueness", "casimir", "central-element"],
});
