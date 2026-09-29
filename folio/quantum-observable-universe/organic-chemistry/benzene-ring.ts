import { example } from "../../schema/builders";

export default example({
  interprets: "def:molecular-hopf-ring",
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
    "ex:carbon-chain-c6",
    "prop:ring-closure-barrier",
  ],
});
