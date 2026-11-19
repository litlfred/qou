import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-16", body: "The two components of $T(2,6)$ are read here as the delocalised $\\pi$ electrons, but benzene has six $\\pi$ electrons, and [ex:benzene-symmetric-projector](#ex:benzene-symmetric-projector) projects six $\\pi$ electrons onto the symmetric block $\\mu = (6)$. The two accounts are not yet reconciled." },
  ],
  label: "def:threading-link",
  title: "Threading link $T(2,N)$",
  tags: [
    "threading",
    "torus-link",
    "T26",
    "alexander-polynomial",
    "molecular",
    "ring",
    "non-local",
    "correlated",
  ],
  lean: { ref: "qou:QOU.Organic.ThreadingLink",
    validation: "not_checked",
  },
  uses: ["def:molecular-hopf-chain"],
});
