import { proposition } from "../../schema/builders";

export default proposition({
  label: "audit:delta-max-numerical-scale",
  title: "Numerical scale of the uniform bound",
  tags: ["binding-energy", "numerical-scale", "probe"],
  lean: {
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
