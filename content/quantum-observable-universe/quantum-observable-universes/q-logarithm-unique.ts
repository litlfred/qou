import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-logarithm-unique",
  title: "Uniqueness of the $q$-logarithm primitive",
  lean: { ref: "qou:QOU.QLogarithm.unique",
    validation: "not_checked",
  },
  uses: ["prop:q-logarithm-exists"],
  proofs: ["prf:q-logarithm-unique"],
  tags: ["uniqueness", "q-logarithm", "primitive", "hopf-algebra"],
});
