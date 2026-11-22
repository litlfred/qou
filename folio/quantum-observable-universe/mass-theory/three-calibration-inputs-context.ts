import { remark } from "../../schema/builders";

export default remark({
  label: "rem:three-calibration-inputs-context",
  title:
    "Calibration observables, allowed/forbidden substitutions, and cohomological alignment",
  interprets: "conj:three-calibration-inputs",
  tags: [
    "calibration",
    "mass",
    "prediction",
    "falsifiability",
    "wedderburn",
    "substrate-parameter",
  ],
  uses: [
    "conj:three-calibration-inputs",
    "prop:three-parameters-wedderburn",
  ],
});
