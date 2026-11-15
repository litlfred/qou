import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mirror-3d-3d-correspondence",
  title:
    "3d–3d correspondence — Hecke partition functions on hyperbolic 3-manifolds ↔ 3d $\\mathcal{N}{=}2$ gauge theories",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.Mirror3d3dCorrespondence",
    validation: "not_checked",
  },
  uses: ["conj:borromean-bloch-group-element"],
  cites: [
    "dimofte-gaiotto-gukov2014",
    "terashima-yamazaki2011",
    "neumann-zagier1985",
  ],
  tags: [
    "tier:S",
    "mirror-symmetry",
    "3d-3d",
    "duality-d18",
    "n2-gauge-theory",
    "partition-function",
    "research-grade",
    "long-horizon",
    "axiom-class",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "The middle row of the dictionary previously read $m_p \\leftrightarrow Z_{T[\\mathcal{B}_3]}(q_0)$; it was retired under the absolute-mass excision ruling of 2026-08-11.",
    },
  ],
});
