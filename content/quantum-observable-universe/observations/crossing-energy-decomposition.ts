import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crossing-energy-decomposition",
  proofs: ["prf:crossing-energy-decomposition"],
  lean: { ref: "qou:QOU.Braiding.q_decomposition" },
  title: "Crossing energy decomposes into strong and Coulomb channels",
  uses: ["def:crossing-energy"],
  examples: ["rem:pair-creation-energy", "rem:virtual-particles-exceptional-divisor", "rem:electron-immortality", "rem:crossing-energy-decomposition"],
  tags: [
    "crossing-energy", "strong-force", "coulomb", "decomposition",
    "hyperbolic",
  ],
});
