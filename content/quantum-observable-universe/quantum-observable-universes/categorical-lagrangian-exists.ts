import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-lagrangian-exists",
  title: "Existence of the categorical Lagrangian",
  lean: { ref: "qou:QOU.CategoricalLagrangian.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-lagrangian",
    "prop:categorical-dirac-operator-exists",
  ],
  proofs: ["prf:categorical-lagrangian-exists"],
  tags: ["existence", "lagrangian"],
});
