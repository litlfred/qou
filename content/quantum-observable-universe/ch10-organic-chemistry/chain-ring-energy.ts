import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chain-ring-energy",
  title: "Why the C$_6$ chain resists hexagonalisation",
  tags: [
    "energy-barrier",
    "chain",
    "ring",
    "carbon",
    "stability",
    "kinetic",
    "thermodynamic",
  ],
  uses: [
    "ex:carbon-chain-c6",
    "ex:benzene-ring",
    "def:threading-link",
    "prop:ring-closure-barrier",
    "def:crossing-energy",
    "rem:chain-spring-modes",
  ],
});
