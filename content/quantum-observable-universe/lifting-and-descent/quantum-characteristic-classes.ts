import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-characteristic-classes",
  lean: { ref: "qou:QOU.QuantumCharacteristicClass", validation: "not_checked" },
  title: "Quantum Characteristic Classes",
  tags: ["yekutieli", "obstruction", "cohomology", "brane-tower"],
  examples: ["ex:quantum-characteristic-classes-su2"],
  uses: [
    "def:recursive-brane-tower",
    "def:yekutieli-lifting-condition",
  ],
});
