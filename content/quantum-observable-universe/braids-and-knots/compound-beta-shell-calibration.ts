import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:compound-beta-shell-calibration",
  title:
    "Compound β-decay calibration across magic shells",
  lean: { ref: "qou:QOU.BraidKnot.CompoundBetaShellCalibration",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:stable-atom",
    "def:unstable-atom",
    "prop:bw-coefficient-shadow-price",
    "prop:shell-schur-weyl-self-duality",
    "def:hecke-normal-form",
    "def:knot-operator-energy",
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
