import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-gauge-group",
  title: "Quantum Gauge Group",
  tags: ["gauge-group", "quantum-group"],
  lean: { ref: "qou:QOU.QuantumGaugeGroup",
    validation: "leanok",
  },
  uses: ["def:substrate-parameter"],
});
