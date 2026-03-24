import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-flatness",
  title: "Quantum flatness",
  tags: ["flatness", "2-group", "instanton"],
  uses: [
    "def:categorical-connection",
    "def:categorical-instanton",
    "def:quantum-gauge-group",
  ],
});
