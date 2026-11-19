import { corollary } from "../../schema/builders";

export default corollary({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "cor:spectral-decomposition-qvalue",
  title:
    "Spectral decomposition of the $\\mathcal{Q}_q$-value over the torus knot basis of $\\Sigma_4$",
  tags: [
    "shell-binding",
    "torus-knot",
    "transfer-matrix",
    "q-value",
    "beta-decay",
    "spectral-decomposition",
    "jet-bundle",
    "exceptional-divisor",
    "representation-theory",
    "young-symmetrizer",
    "pauli-exclusion",
    "self-duality",
    "hilbert-space-completeness",
  ],
  lean: { ref: "qou:QOU.Archimedean.spectral_decomposition_qvalue",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/spectral_decomposition_qvalue_d.py",
    witness: [
      "computations/spectral-decomposition-qvalue-d.witness.json",
      "computations/h2s-chiral-residue-bar-antisymmetric.witness.json",
    ],
  },
});
