import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-generation",
  title: "Skein generation of hadrons from mass-zero fundamentals",
  uses: [
    "def:hadron",
    "rem:hadron-operations",
    "def:hadron-fibre-embedding",
  ],
  tags: ["skein", "generation", "mass", "hadron", "torus-knot"],
});
