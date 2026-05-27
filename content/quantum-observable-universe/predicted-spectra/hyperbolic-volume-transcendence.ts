import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:hyperbolic-volume-transcendence",
  title: "Algebraic independence of QOU hyperbolic volumes",
  tags: [
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
});
