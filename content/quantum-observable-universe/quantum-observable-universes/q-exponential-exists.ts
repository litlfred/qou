import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-exponential-exists",
  title: "Existence of the $q$-exponential grouplike",
  lean: { ref: "qou:QOU.QExponential.exists_in_shuffle_hopf",
    validation: "not_checked",
  },
  uses: ["def:q-exponential"],
  proofs: ["prf:q-exponential-exists"],
  tags: ["existence", "q-exponential", "grouplike", "hopf-algebra"],
});
