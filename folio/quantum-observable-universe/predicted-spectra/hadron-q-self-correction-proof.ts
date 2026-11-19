import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hadron-q-self-correction",
  title: "Net signed crossing and magnitude of the self-deformation",
  uses: ["prop:hadron-q-self-correction", "prop:qou-canonical-action"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
