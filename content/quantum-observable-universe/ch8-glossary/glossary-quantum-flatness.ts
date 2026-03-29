import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-quantum-flatness",
  lean: { decl: "QOU.QuantumFlatness" },
  title: "Quantum flatness",
  tags: ["glossary", "flatness", "2-group", "instanton"],
  uses: [
    "def:categorical-instanton",
    "def:quantum-gauge-group",
  ],
});
