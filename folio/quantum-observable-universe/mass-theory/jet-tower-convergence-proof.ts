import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jet-tower-convergence",
  title: "Proof of jet tower convergence",
  uses: ["prop:jet-tower-convergence"],
  computation: {
    engine: "python",
    script: "computations/jet_tower_delta_max.py",
    witness: "computations/jet-tower-delta-max.witness.json",
    status: "verified",
  },
});
