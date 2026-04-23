import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-lagrangian",
  title: "Categorical Lagrangian",
  tags: ["lagrangian", "dirac", "endomorphism"],
  lean: { ref: "qou:QOU.CategoricalLagrangian",
    validation: "not_checked",
  },
  uses: ["def:categorical-dirac-operator"],
});
