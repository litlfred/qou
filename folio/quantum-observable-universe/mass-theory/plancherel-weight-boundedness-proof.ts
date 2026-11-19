import { proof } from "../../schema/builders";

export default proof({
  label: "prf:plancherel-weight-boundedness",
  title: "Proof of plancherel weight boundedness",
  uses: ["prop:plancherel-weight-boundedness"],
  computation: {
    engine: "python",
    script: "computations/probes/two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.py",
    witness: "computations/probes/two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.witness.json",
    status: "verified",
  },
});
