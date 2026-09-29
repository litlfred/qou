import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-gauge-group",
  label: "rem:j1e-local-states",
  title: "J^1E as the space of local states",
  tags: ["jet-bundle", "gauge-theory"],
  uses: [
    "ex:irreducible-connection",
    "def:quantum-gauge-group",
  ],
});
