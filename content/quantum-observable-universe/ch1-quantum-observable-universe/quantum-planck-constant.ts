import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-planck-constant",
  title: "Quantum Planck Constant",
  tags: ["planck", "deformation"],
  lean: {
    decl: "QOU.quantumPlanckConstant",
    validation: "leanok",
  },
  status: "proved",
  uses: ["def:quantum-observable-universe", "def:substrate-parameter"],
});
