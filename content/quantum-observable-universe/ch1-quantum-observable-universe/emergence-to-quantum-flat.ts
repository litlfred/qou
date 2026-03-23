import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:emergence-to-quantum-flat",
  title: "From Tannakian emergence to 2-group quantum flatness",
  tags: ["tannaka-krein", "2-group", "instanton"],
  uses: [
    "def:categorical-volume-constraint",
    "thm:su2-emergence",
    "rem:self-dual-2group",
    "def:instanton",
  ],
  proofs: ["prf:emergence-to-quantum-flat"],
});
