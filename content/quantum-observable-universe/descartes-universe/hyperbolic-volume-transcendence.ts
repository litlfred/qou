import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hyperbolic-volume-transcendence",
  title: "Algebraic independence of QOU hyperbolic volumes",
  tags: [
    "hyperbolic-volume",
    "transcendence",
    "algebraic-independence",
    "bloch-wigner",
    "open-problem",
  ],
  uses: [
    "prop:topological-mass-formula",
    "conj:baryon-period-ratio",
    "def:substrate-parameter",
  ],
  lean: {
    decl: "QOU.Descartes.HyperbolicVolumeIndependence",
    file: "QOU/Descartes/HyperbolicVolumeTranscendence.lean",
    validation: "not_checked",
  },
});
