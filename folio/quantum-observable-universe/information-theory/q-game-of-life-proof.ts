import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-game-of-life",
  title: "Proof of q game of life",
  uses: ["prop:q-game-of-life"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/toffoli-lp-stability.witness.json",
      "computations/probes/toffoli-qand-convention-d-derivation.witness.json",
    ],
    status: "verified",
  },
});
