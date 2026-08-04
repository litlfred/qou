import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:compound-beta-shell-calibration",
  title:
    "Compound β-decay calibration across magic shells",
  lean: { ref: "qou:QOU.BraidKnot.CompoundBetaShellCalibration",
    validation: "not_checked",
  },
  uses: [
    "def:unstable-atom",
    "prop:shell-schur-weyl-self-duality",
  ],
  cites: [],
  tags: [
    "beta-decay",
    "compound-decay",
    "shell-closure",
    "calibration",
    "knot-operator-transition",
  ],
});
