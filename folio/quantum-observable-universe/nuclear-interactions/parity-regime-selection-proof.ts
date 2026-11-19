import { proof } from "../../schema/builders";

export default proof({
  label: "prf:parity-regime-selection",
  title: "Proof of parity regime selection",
  uses: ["thm:parity-regime-selection"],
  computation: {
    engine: "python",
    script: "computations/branching-qvalue-chain.py",
    witness: "computations/branching-qvalue-chain.witness.json",
    status: "verified",
  },
});
