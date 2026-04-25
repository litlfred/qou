import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-planck-constant",
  title: "Quantum Planck Constant",
  tags: ["planck", "deformation"],
  lean: { ref: "qou:QOU.quantumPlanckConstant",
    validation: "leanok",
  },
  uses: ["def:substrate-parameter"],
});
