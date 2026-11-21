import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-bloch-group",
  title: "Quantum Bloch group and the pentagon identity",
  cites: ["baseilhac-benedetti2007", "arxiv-2304.12545v1", "neumann2004"],
  uses: ["def:habiro-ring"],
  lean: { ref: "qou:QOU.QuantumBlochGroup" },
});
