import { remark } from "../../schema/builders";

export default remark({
  label: "rem:building-block-knots",
  title:
    "Building block knots: classification, polynomials, and volumes",
  tags: [
    "knot",
    "torus-knot",
    "jones-polynomial",
    "hyperbolic-volume",
    "particle",
    "classification",
    "building-block",
    "amphichiral",
    "mirror",
    "appendix",
  ],
  uses: [
    "prop:torus-knot-generators",
    "def:electron-knot",
    "def:neutrino-knot",
    "def:positron-knot",
    "def:antineutrino-knot",
    "def:up-quark",
    "def:down-quark",
    "def:crossing-energy",
    "prop:topological-mass-formula",
    "def:substrate-parameter",
    "prop:local-substrate-q",
  ],
});
