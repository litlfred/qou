import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-gauge-group-remark",
  title: "The quantum gauge group as a local field",
  interprets: "def:quantum-gauge-group",
  uses: ["def:quantum-gauge-group"],
  tags: ["gauge-group", "quantum-group"],
});
