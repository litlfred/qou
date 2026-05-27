import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:single-volume-irrationality",
  title: "Irrationality of a single hyperbolic knot volume",
  lean: { ref: "qou:QOU.Archimedean.SingleVolumeIrrationality", validation: "stub" },
  tags: [
    "irrationality",
    "hyperbolic-volume",
    "bloch-wigner",
    "clausen-function",
    "open-problem",
  ],
  uses: [
    "prop:hyperbolic-volume-transcendence",
  ],
});
