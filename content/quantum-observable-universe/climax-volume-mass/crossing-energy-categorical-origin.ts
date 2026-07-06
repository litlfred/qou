import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crossing-energy-categorical-origin",
  title: "Crossing weights are Hecke eigenvalues, not postulates",
  interprets: "def:crossing-energy",
  uses: [
    "def:crossing-energy",
    "def:quantum-observable-universe",
    "prop:braiding-eigenvalue-extraction",
    "prop:nuclear-groebner-reduction",
    "rem:r-matrix-braiding",
  ],
  tags: ["crossing", "energy", "hecke", "eigenvalue", "r-matrix"],
});
