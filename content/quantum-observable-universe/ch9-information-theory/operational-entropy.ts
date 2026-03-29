import { definition } from "../../schema/builders";

export default definition({
  label: "def:operational-entropy",
  title: "Operational entropy of the Reeb dynamics",
  tags: [
    "information-theory",
    "metric-entropy",
    "julia-set",
    "reeb-flow",
    "hausdorff-dimension",
  ],
  lean: {
    decl: "QOU.Information.operationalEntropy",
    validation: "not_checked",
  },
  uses: [
    "rem:julia-set-reeb",
    "def:planck-time",
    "prop:reeb-operations-per-planck",
  ],
});
