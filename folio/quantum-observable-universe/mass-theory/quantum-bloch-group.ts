import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-bloch-group",
  title: "Quantum Bloch group and the pentagon identity",
  cites: ["baseilhac-benedetti2007", "kirillov1995"],
  uses: ["def:habiro-ring"],
  lean: { ref: "qou:QOU.QuantumBlochGroup" },
});
