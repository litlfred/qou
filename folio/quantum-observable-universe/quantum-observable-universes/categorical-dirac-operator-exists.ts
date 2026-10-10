import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-dirac-operator-exists",
  title: "Existence of the categorical Dirac operator",
  lean: { ref: "qou:QOU.CategoricalDirac.exists",
    validation: "not_checked",
  },
  uses: ["def:categorical-dirac-operator"],
  proofs: ["prf:categorical-dirac-operator-exists"],
  tags: ["existence", "dirac-operator"],
});
