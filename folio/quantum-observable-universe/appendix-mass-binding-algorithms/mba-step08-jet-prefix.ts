import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:jet-prefix-transport",
  title: "Jet-prefix transport in the $q \\to 1$ classical neighbourhood",
  uses: [
    "prop:jet-prefix-gb-filtration",
    "prop:gb-spectral-sequence",
    "alg:gb-filtration",
  ],
  tags: [
    "mba",
    "step-8",
    "jet-order",
    "q-limit",
    "canonical-chain",
  ],
});
