import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-dirac-operator-unique",
  title: "Uniqueness of the categorical Dirac operator",
  lean: { ref: "qou:QOU.CategoricalDirac.unique",
    validation: "not_checked",
  },
  uses: ["prop:categorical-dirac-operator-exists"],
  proofs: ["prf:categorical-dirac-operator-unique"],
  tags: ["uniqueness", "dirac-operator"],
});
