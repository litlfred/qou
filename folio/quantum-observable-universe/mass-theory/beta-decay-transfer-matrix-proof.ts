import { proof } from "../../schema/builders";

export default proof({
  label: "prf:beta-decay-transfer-matrix",
  title: "Proof of beta decay transfer matrix",
  uses: ["prop:beta-decay-transfer-matrix"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/confinement-operator-selection.witness.json",
    status: "verified",
  },
});
