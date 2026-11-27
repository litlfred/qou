import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-twist-flip-relations",
  title: "Relations satisfied by twist, flip and rotation",
  interprets: "def:braid-twist-flip",
  tags: ["braid-group", "dihedral"],
  uses: [
    "def:braid-twist-flip",
    "def:su2-generators",
    "rem:braid-group-action",
  ],
});
