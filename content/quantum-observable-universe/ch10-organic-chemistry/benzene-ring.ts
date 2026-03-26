import { example } from "../../schema/builders";

export default example({
  label: "ex:benzene-ring",
  title: "Benzene as a molecular Hopf ring $\\mathrm{C}_6$",
  tags: [
    "benzene",
    "c6",
    "ring",
    "aromatic",
    "hexagon",
    "circulant",
    "rigid",
    "delocalized",
  ],
  uses: [
    "def:molecular-hopf-ring",
    "def:threading-link",
    "ex:carbon-chain-c6",
    "rem:carbon-valence",
    "def:covalent-bond-types",
    "prop:ring-closure-barrier",
    "def:substrate-parameter",
  ],
});
