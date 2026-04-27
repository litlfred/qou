import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-exponential-unique",
  title: "Uniqueness of the $q$-exponential grouplike",
  lean: { ref: "qou:QOU.QExponential.unique",
    validation: "not_checked",
  },
  uses: ["prop:q-exponential-exists"],
  proofs: ["prf:q-exponential-unique"],
  tags: ["uniqueness", "q-exponential", "grouplike", "hopf-algebra"],
});
