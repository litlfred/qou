import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-su2-classical-limit",
  title: "Classical limit of $\\mathcal{U}_q(\\mathfrak{su}(2))$",
  interprets: "def:quantum-su2",
  tags: ["quantum-group", "su2", "classical-limit"],
  uses: [
    "def:quantum-su2",
    "def:su2-basis",
  ],
});
