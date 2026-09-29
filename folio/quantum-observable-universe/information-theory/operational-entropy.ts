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
  lean: { ref: "qou:QOU.Information.operationalEntropy",
    validation: "not_checked",
  },
  uses: ["prop:reeb-operations-per-planck"],
});
