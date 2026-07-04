import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-flatness",
  title: "Quantum flatness ($F_\\nabla = B$)",
  tags: ["2-group", "gauge-theory", "instanton", "quantum-flatness"],
  defines: ["quantum-flatness"],
  uses: ["def:categorical-connection", "def:quantum-gauge-group"],
  lean: {
    ref: "qou:QOU.QuantumObservableUniverse.IsQuantumFlat",
    validation: "not_checked",
  },
});
