import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-observable-universe",
  title: "Quantum Observable Universe",
  tags: ["quantum", "observable", "category-theory"],
  lean: {
    decl: "QOU.QuantumObservableUniverse",
    file: "QOU/QuantumObservableUniverse.lean",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:quantum-universe"],
  examples: ["ex:qou-su2"],
});
