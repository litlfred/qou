import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-asymmetry-prediction",
  title: "Particle--antiparticle mass asymmetry at Skein scale",
  tags: [
    "mass-asymmetry",
    "testable-prediction",
    "crossing-energy",
    "cpt",
    "speed-of-light",
    "electron",
    "positron",
  ],
  uses: [
    "thm:mass-energy-equivalence",
    "def:information-speed-of-light",
    "def:crossing-energy",
    "prop:crossing-energy-decomposition",
    "def:mass-identity",
  ],
});
