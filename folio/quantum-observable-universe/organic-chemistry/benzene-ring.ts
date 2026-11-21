import { example } from "../../schema/builders";

export default example({
  authorNotes: [
    { kind: "caveat", date: "2026-11-16", body: "The two components of $T(2,6)$ are read here as the delocalised $\\pi$ electrons, but benzene has six $\\pi$ electrons, and [ex:benzene-symmetric-projector](#ex:benzene-symmetric-projector) projects six $\\pi$ electrons onto the symmetric block $\\mu = (6)$. The two accounts are not yet reconciled." },
  ],
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
    "conj:ring-closure-barrier",
  ],
});
