import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-characteristic-classes",
  lean: { decl: "QOU.QuantumCharacteristicClass" },
  status: "stated",
  title: "Quantum Characteristic Classes (Yekutieli obstruction)",
  tags: ["yekutieli", "obstruction", "cohomology", "brane-tower"],
  examples: ["ex:quantum-characteristic-classes-su2"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-lifting-condition",
    "prop:jet-prolongation",
  ],
});
