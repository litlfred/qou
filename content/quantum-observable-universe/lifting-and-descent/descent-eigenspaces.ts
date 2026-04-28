import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descent-eigenspaces",
  title: "Eigenspaces of the descent involution",
  tags: ["descent", "eigenspace", "bosonic", "fermionic"],
  lean: { ref: "qou:QOU.Torsion.idempotent_direct_sum_decomposition",
    validation: "not_checked",
  },
  uses: [
    "def:descent-involution",
    "rem:algebraic-filter",
  ],
  proofs: ["prf:descent-eigenspaces"],
});
