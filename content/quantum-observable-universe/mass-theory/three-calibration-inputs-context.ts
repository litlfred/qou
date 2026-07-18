import { remark } from "../../schema/builders";

export default remark({
  label: "rem:three-calibration-inputs-context",
  title:
    "Calibration observables, allowed/forbidden substitutions, and cohomological alignment",
  interprets: "prop:three-calibration-inputs",
  tags: [
    "calibration",
    "mass",
    "prediction",
    "falsifiability",
    "wedderburn",
    "substrate-parameter",
  ],
  uses: [
    "prop:three-calibration-inputs",
    "prop:three-parameters-wedderburn",
  ],
});
