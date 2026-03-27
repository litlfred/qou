import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crossing-energy-decomposition",
  title: "Crossing energy decomposes into strong and Coulomb channels",
  uses: [
    "def:crossing-energy",
    "def:substrate-parameter",
  ],
  tags: [
    "crossing-energy", "strong-force", "coulomb", "decomposition",
    "hyperbolic",
  ],
});
