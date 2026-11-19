import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-bloch-group",
  title: "Quantum Bloch group and the pentagon identity",
  uses: ["def:habiro-ring"],
  lean: { ref: "qou:QOU.QuantumBlochGroup" },
});
