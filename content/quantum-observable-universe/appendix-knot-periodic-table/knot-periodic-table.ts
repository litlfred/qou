import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-periodic-table",
  title: "Knot-periodic table of the elements",
  tags: [
    "knot",
    "periodic-table",
    "mass",
    "generation",
    "torus-knot",
    "proton",
    "neutron",
    "appendix",
  ],
  uses: [
    "def:knot-particle-generation",
    "prop:torus-knot-generators",
    "thm:embeddability-closure",
    "rem:knot-formula-table",
    "rem:mass-comparison-table",
    "prop:terminal-resolution",
    "def:substrate-parameter",
  ],
});
