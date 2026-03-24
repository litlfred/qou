import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:emergence-to-quantum-flat",
  lean: {
    decl: "QOU.emergence_to_quantum_flat",
    validation: "not_checked",
  },
  title: "From Tannakian emergence to 2-group quantum flatness",
  tags: ["tannaka-krein", "2-group", "instanton"],
  uses: [
    "def:quantum-observable-universe",
    "thm:su2-emergence",
    "rem:self-dual-2group",
    "ex:instanton",
  ],
  proofs: ["prf:emergence-to-quantum-flat"],
});
