import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:emergence-to-quantum-flat",
  lean: { ref: "qou:QOU.emergence_to_quantum_flat",
    validation: "not_checked",
  },
  title: "From Tannakian emergence to 2-group quantum flatness",
  tags: ["tannaka-krein", "2-group", "instanton"],
  uses: ["rem:self-dual-2group"],
  proofs: ["prf:emergence-to-quantum-flat"],
  defines: ["quantum-flatness"],
});
