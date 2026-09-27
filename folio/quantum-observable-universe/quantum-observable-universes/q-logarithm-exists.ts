import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-logarithm-exists",
  title: "Existence of the $q$-logarithm primitive",
  lean: { ref: "qou:QOU.QLogarithm.exists_in_shuffle_hopf",
    validation: "not_checked",
  },
  uses: [
    "def:q-logarithm",
    "prop:q-exponential-exists",
  ],
  proofs: ["prf:q-logarithm-exists"],
  tags: ["existence", "q-logarithm", "primitive", "hopf-algebra"],
});
