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
  uses: ["conj:baryon-period-ratio"],
  lean: { ref: "qou:QOU.Descartes.HyperbolicVolumeTranscendence",
    validation: "not_checked",
  },
});
