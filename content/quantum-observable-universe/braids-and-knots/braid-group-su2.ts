import { example } from "../../schema/builders";

export default example({
  label: "ex:braid-group-su2",
  title: "Braid group action on $\\mathbb{C}^2 \\otimes \\mathbb{C}^2$",
  interprets: "def:braid-group",
  uses: ["ex:quantum-universe-su2", "def:braid-group"],
  tags: ["braid-group", "su2", "example"],
});
