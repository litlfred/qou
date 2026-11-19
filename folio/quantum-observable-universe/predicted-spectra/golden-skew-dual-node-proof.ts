import { proof } from "../../schema/builders";

export default proof({
  label: "prf:golden-skew-dual-node",
  title: "Proof of golden skew dual node",
  uses: ["prop:golden-skew-dual-node"],
  computation: {
    engine: "python",
    script: "computations/probes/two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.py",
    witness: "computations/probes/two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.witness.json",
    status: "verified",
  },
});
