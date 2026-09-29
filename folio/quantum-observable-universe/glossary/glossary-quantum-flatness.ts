import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-quantum-flatness",
  lean: { ref: "qou:QOU.QuantumFlatness", validation: "not_checked" },
  title: "Quantum flatness",
  tags: ["glossary", "flatness", "2-group", "instanton"],
  uses: [
    "def:categorical-instanton",
    "def:quantum-gauge-group",
  ],
});
