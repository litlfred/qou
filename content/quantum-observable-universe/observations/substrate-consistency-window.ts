import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:substrate-consistency-window",
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
    "thm:mass-energy-equivalence",
    "prop:crossing-energy-decomposition",
  ],
});
