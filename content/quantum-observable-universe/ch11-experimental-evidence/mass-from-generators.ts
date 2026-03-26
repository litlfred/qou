import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-from-generators",
  title: "Mass spectrum from $T_{m,n}$ generators and linking operations",
  tags: [
    "mass",
    "generator",
    "torus-knot",
    "hopf-link",
    "color-tube",
    "skein",
    "CODATA",
    "atomic-chart",
  ],
  uses: [
    "def:knot-particle-generation",
    "prop:torus-knot-generators",
    "prop:topological-mass-formula",
    "rem:skein-mass-relation",
    "prop:terminal-resolution",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "def:color-tube-coordinates",
    "rem:knot-particle-dictionary",
  ],
});
