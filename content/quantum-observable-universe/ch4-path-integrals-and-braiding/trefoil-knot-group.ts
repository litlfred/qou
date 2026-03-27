import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:braid-group",
  label: "rem:trefoil-knot-group",
  title: "Trefoil knot group",
  tags: ["trefoil", "knot-group", "braid-group"],
  uses: ["def:braid-group"],
});
