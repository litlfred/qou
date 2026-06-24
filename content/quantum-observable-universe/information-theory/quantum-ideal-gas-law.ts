import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-ideal-gas-law",
  proofs: ["prf:quantum-ideal-gas-law"],
  title: "Quantum ideal gas law",
  tags: [
    "ideal-gas",
    "statistical-mechanics",
    "equation-of-state",
    "q-anomaly",
    "noether",
    "hydrogen",
  ],
  lean: { ref: "qou:QOU.Information.IdealKnotGas",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-pressure",
    "def:quantum-volume",
    "rem:noether-theorem-callout",
  ],
});
