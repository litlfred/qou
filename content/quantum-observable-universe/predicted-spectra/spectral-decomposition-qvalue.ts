import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:spectral-decomposition-qvalue",
  proofs: ["prf:spectral-decomposition-qvalue"],
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
});
