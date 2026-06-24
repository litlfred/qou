import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:antiparticle-crossing-reversal",
  proofs: ["prf:antiparticle-crossing-reversal"],
  lean: { ref: "qou:QOU.Torsion.antiparticle_crossing_reversal" },
  title: "Antiparticles from crossing reversal",
  uses: ["def:knot-particle-generation"],
  tags: [
    "trefoil", "chirality", "electron", "positron",
    "antiparticle", "crossing-energy",
  ],
});
