import { remark } from "../../schema/builders";

export default remark({
  label: "rem:calibration-inputs",
  title: "Calibration inputs and predictive content",
  interprets: "def:mass-identity",
  uses: [
    "def:mass-identity",
    "prop:categorical-mass-markov",
    "conj:mass-endomorphism",
    "prop:knot-operator-selection",
    "rem:skein-mass-relation",
  ],
  tags: [
    "calibration",
    "mass",
    "prediction",
    "endomorphism",
    "substrate-parameter",
    "falsifiability",
  ],
});
