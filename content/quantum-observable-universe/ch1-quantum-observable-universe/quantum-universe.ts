import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-universe",
  title: "Quantum Universe",
  tags: ["category-theory", "quantum"],
  lean: {
    decl: "QOU.QuantumUniverse",
    file: "QOU/QuantumUniverse.lean",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:rigid-monoidal-category"],
  examples: ["ex:quantum-universe-su2"],
});
