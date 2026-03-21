import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-gauge-group",
  title: "Quantum Gauge Group",
  tags: ["gauge-group", "quantum-group"],
  lean: {
    decl: "QOU.QuantumGaugeGroup",
    validation: "leanok",
  },
  status: "not_started",
  uses: ["def:quantum-observable-universe", "def:substrate-parameter", "thm:su2-emergence"],
});
