import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phase-boundary-variety",
  title: "Phase-boundary variety $\\mathcal{B}$ is Zariski-closed and measure-zero",
  lean: { ref: "qou:QOU.BraidKnot.PhaseBoundaryVariety",
    validation: "not_checked",
  },
  uses: ["def:local-shadow-ordering"],
  tags: [
    "phase-boundary",
    "zariski-closed",
    "measure-zero",
    "shadow-price",
  ],
});
