import { proof } from "../../schema/builders";

export default proof({
  label: "prf:exterior-square-borromean",
  title: "Proof of exterior square borromean",
  uses: ["prop:exterior-square-borromean"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
