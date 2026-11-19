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
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean formalisation (`QOU.Archimedean.HyperbolicVolumeIndependence`): the structural half (tower decomposition, Chern-Simons faithfulness, and downstream implications algebraic independence => Borel-Zagier => irrationality) is proved unconditionally; the transcendence core is axiomatised as the class `HyperbolicVolumeIndependence`.",
    },
  ],
  computation: {
    engine: "snappea",
    script: "computations/substrate/knot_volumes.py",
    witness: "computations/substrate/knot-volumes.witness.json",
    status: "verified",
  },
});
