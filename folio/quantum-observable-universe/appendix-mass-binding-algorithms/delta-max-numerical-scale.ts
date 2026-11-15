import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:delta-max-numerical-scale",
  title: "Numerical scale of the uniform bound",
  tags: ["binding-energy", "numerical-scale", "probe"],
  lean: {
    ref: "qou:QOU.Appendix.DeltaMaxNumericalScale.delta_max_numerical_scale",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
