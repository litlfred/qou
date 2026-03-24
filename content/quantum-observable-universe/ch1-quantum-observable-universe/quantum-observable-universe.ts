import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-observable-universe",
  title: "Quantum Observable Universe",
  tags: ["quantum", "observable", "category-theory"],
  lean: {
    decl: "QOU.QuantumObservableUniverse",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe"],
  examples: ["ex:qou-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-observable-universe-0.svg", blockIndex: 0, hash: "5a4a07b8bf1e" },
    { mime: "image/svg+xml", url: "rendered/quantum-observable-universe-1.svg", blockIndex: 1, hash: "11598a0a0ca3" },
  ],

});
