import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descent-eigenspaces",
  title: "Eigenspaces of the descent involution",
  tags: ["descent", "eigenspace", "bosonic", "fermionic"],
  // Was `qou:QOU.Torsion.idempotent_direct_sum_decomposition`. No declaration
  // of that name exists anywhere in the tree and the canonical resolver returns
  // unresolved for it. `QOU.Torsion.EigenspaceDecomposition`
  // (`lean/QOU/Torsion/Descent.lean:66`) carries this block's own
  // `\label{prop:descent-eigenspaces}` — the label is the evidence, the ref's
  // name was not. Third repair of this shape, after `thm:su2-emergence`
  // (PR #5222) and `def:ns-regular-qou` (bean `qou-2u26`).
  //
  // Masked the same way as `def:ns-regular-qou`: the block has a co-located
  // sibling `descent-eigenspaces.lean`, and `walkBlocks` resolves the sibling
  // FIRST, so every checker audited the stub and passed while the library ref
  // sat dead. Found by the label test in `qou-szd6`, not by any gate.
  lean: { ref: "qou:QOU.Torsion.EigenspaceDecomposition",
    validation: "not_checked",
  },
  uses: [
    "def:descent-involution",
    "rem:algebraic-filter",
  ],
  proofs: ["prf:descent-eigenspaces"],
});
