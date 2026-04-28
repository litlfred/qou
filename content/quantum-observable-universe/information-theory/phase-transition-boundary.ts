import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phase-transition-boundary",
  title: "Phase transitions as $S^3$ boundary actions",
  tags: [
    "phase-transition",
    "s3-boundary",
    "statistical-mechanics",
    "sublimation",
    "hecke-algebra",
    "braid-representation",
  ],
  lean: { ref: "qou:QOU.Information.gasLiquidCriticalTemp",
    validation: "not_checked",
  },
  uses: ["prop:quantum-ideal-gas-law"],
});
