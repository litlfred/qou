import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-pressure",
  title: "Quantum pressure",
  tags: [
    "pressure",
    "statistical-mechanics",
    "frobenius",
    "boundary",
    "q-anomaly",
  ],
  lean: {
    decl: "QOU.Information.quantumPressure",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-temperature",
    "def:categorical-action",
    "def:frobenius-pairing",
  ],
});
