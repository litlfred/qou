import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vertex-is-exceptional-divisor",
  lean: {
    decl: "QOU.Descartes.vertex_is_exceptional_divisor",
    validation: "not_checked",
  },
  title: "Vertex operators factor through the exceptional divisor",
  tags: [
    "vertex-operator", "exceptional-divisor", "reeb-bundle",
    "blow-up", "braiding",
  ],
  uses: [
    "def:exceptional-divisor",
    "def:reeb-bundle",
    "cor:descartes-braid-structure",
  ],
  proofs: ["prf:vertex-is-exceptional-divisor"],
});
