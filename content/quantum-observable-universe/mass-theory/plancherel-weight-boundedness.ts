import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:plancherel-weight-boundedness",
  title:
    "Plancherel weights define a probability distribution: $\\sum_\\lambda w_\\lambda = 1$, $0 \\leq w_\\lambda \\leq 1$",
  lean: {
    ref: "qou:QOU.BraidKnot.plancherel_weight_boundedness",
    validation: "not_checked",
  },
  uses: ["prop:unified-curvature-rank-mass-formula"],
  tags: [
    "plancherel",
    "boundedness",
    "probability-distribution",
    "wedderburn",
    "convergence",
    "mass-tower",
  ],
  computation: {
    engine: "python",
    script: "computations/probes/plancherel_weight_boundedness_probe.py",
    witness: "computations/probes/plancherel-weight-boundedness-probe.witness.json",
    status: "verified",
  },
});
