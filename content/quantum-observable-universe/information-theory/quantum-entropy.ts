import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-entropy",
  title: "Quantum entropy as a non-abelian surface integral",
  tags: [
    "entropy",
    "statistical-mechanics",
    "non-abelian-stokes",
    "surface-integral",
    "operational-entropy",
    "yekutieli",
  ],
  lean: { ref: "qou:QOU.Information.quantumEntropy",
    validation: "not_checked",
  },
  uses: [
    "def:operational-entropy",
    "def:quantum-observable-universe",
    "def:yekutieli-triple",
  ],
  cites: ["yekutieli2015"],
});
