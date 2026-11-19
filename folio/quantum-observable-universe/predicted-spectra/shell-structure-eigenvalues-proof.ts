import { proof } from "../../schema/builders";

export default proof({
  label: "prf:shell-structure-eigenvalues",
  title: "Proof of shell structure eigenvalues",
  uses: ["prop:shell-structure-eigenvalues"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json"],
    status: "verified",
  },
});
