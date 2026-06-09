import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:substrate-consistency-window",
  lean: { ref: "qou:QOU.Observations.substrate_consistency_window", validation: "not_checked" },
  title: "Overdetermination of the substrate parameter",
  tags: [
    "substrate-parameter",
    "testable-prediction",
    "consistency",
    "fine-structure",
    "mass-ratio",
    "half-life",
    "speed-of-light",
  ],
  uses: [
    "rem:fine-structure-observation",
    "prop:crossing-energy-decomposition",
  ],
});
