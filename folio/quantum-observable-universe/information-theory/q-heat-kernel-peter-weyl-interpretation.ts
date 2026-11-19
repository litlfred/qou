import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-heat-kernel-peter-weyl",
  label: "rem:q-heat-kernel-peter-weyl-interpretation",
  title:
    "Convergence, the $q$-Gaussian equilibrium mode, and the place in the $q$-heat story",
  uses: [
    "prop:q-heat-kernel-peter-weyl",
    "prop:q-gaussian-solves-q-heat",
    "def:categorical-laplace",
    "def:q-dilogarithm",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json"],
    status: "verified",
  },
});
