import { proof } from "../../schema/builders";

export default proof({
  label: "prf:flavor-split-substrate",
  title: "Proof of the aether-pure flavor split formula",
  uses: ["prop:flavor-split-substrate"],
  computation: {
    engine: "snappea",
    script: "computations/substrate/knot_volumes.py",
    witness: [
      "computations/substrate/knot-volumes.witness.json",
      "computations/b-over-m-order-probe.witness.json",
      "computations/probes/flavor-split-3strand-derivation-probe.witness.json",
      "computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
  },
});
