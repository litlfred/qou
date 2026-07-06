import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:jet-prefix-transport",
  title: "Jet-prefix transport in the $q \\to 1$ limit",
  uses: [
    "prop:jet-prefix-gb-filtration",
    "prop:gb-spectral-sequence",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/gb_filtration_jet_order_reader.py",
    witness: "computations/gb-filtration-jet-order-reader.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-8",
    "jet-order",
    "q-limit",
    "canonical-chain",
  ],
});
