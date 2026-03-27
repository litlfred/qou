import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:antiparticle-crossing-reversal",
  title: "Antiparticles from crossing reversal",
  uses: [
    "def:crossing-energy",
    "def:knot-particle-generation",
    "def:hadron",
  ],
  tags: [
    "trefoil", "chirality", "electron", "positron",
    "antiparticle", "crossing-energy",
  ],
});
