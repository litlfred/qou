import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:knot-particle-generation",
  label: "rem:knot-particle-generation-consequences",
  title: "Boson links, zero hyperbolic volume, and the Skein-module presentation",
  tags: [
    "knot",
    "particle",
    "torus-knot",
    "fermion-boson",
    "skein",
    "hyperbolic-volume",
  ],
  uses: [
    "def:knot-particle-generation",
    "prop:fermion-boson-knot-link",
    "prop:skein-generation",
    "rem:knot-particle-dictionary",
  ],
});
