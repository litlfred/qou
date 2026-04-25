import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-generation",
  lean: { ref: "qou:QOU.Torsion.skein_generation",
    validation: "not_checked",
  },
  title: "Skein generation of hadrons from mass-zero fundamentals",
  uses: [
    "rem:hadron-operations",
    "def:hadron-fibre-embedding",
  ],
  proofs: ["prf:skein-generation"],
  tags: ["skein", "generation", "mass", "hadron", "torus-knot"],
});
