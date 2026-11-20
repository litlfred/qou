import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hyperbolic-volume-transcendence",
  title: "Algebraic independence of QOU hyperbolic volumes",
  tags: [
    "tier:famous",
    "hyperbolic-volume",
    "transcendence",
    "algebraic-independence",
    "bloch-wigner",
    "open-problem",
  ],
  uses: [],
  lean: { ref: "qou:QOU.Archimedean.HyperbolicVolumeIndependence",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean\nformalisation proves the structural half: the tower\ndecomposition, Chern--Simons faithfulness, and the downstream\nimplications (algebraic independence $\\Rightarrow$ Borel--Zagier\n$\\Rightarrow$ irrationality). The transcendence core is\naxiomatised as the Lean class `HyperbolicVolumeIndependence`. Following\nthe conditional-class convention, the downstream results remain conditionally rigorous." },
  ],
});
