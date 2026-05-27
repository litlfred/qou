import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vertex-is-exceptional-divisor",
  lean: { ref: "qou:QOU.vertex_is_exceptional_divisor",
    validation: "not_checked",
  },
  title: "Vertex operators factor through the exceptional divisor",
  tags: [
    "vertex-operator", "exceptional-divisor", "reeb-bundle",
    "blow-up", "braiding",
  ],
  uses: [
    "def:reeb-bundle",
    "prop:braid-action-tensor",
  ],
  proofs: ["prf:vertex-is-exceptional-divisor"],
});
