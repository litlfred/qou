import { proof } from "../../schema/builders";

export default proof({
  label: "prf:degree-one-braid-trivial-volume",
  title: "Proof of degree one braid trivial volume",
  uses: ["lem:degree-one-braid-trivial-volume"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
