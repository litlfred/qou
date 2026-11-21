import { corollary } from "../../schema/builders";

export default corollary({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): relabelled the electron from the trefoil T_{2,3} to the word sigma_0 sigma_1 sigma_0 in B_3 (closure: Hopf link). Wording only; no number moved. The factor m_e/3 is unchanged: sigma_0 sigma_1 sigma_0 has 3 letters, as the backup trefoil has 3 crossings." },
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
    ],
  },
});
