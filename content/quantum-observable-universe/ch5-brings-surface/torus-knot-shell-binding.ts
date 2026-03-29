import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:torus-knot-shell-binding",
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
  lean: {
    decl: "QOU.Descartes.torus_knot_shell_binding",
    validation: "not_checked",
  },
  uses: [
    "prop:shell-closure-normal-form",
    "prop:skein-finiteness-bound",
    "rem:force-knot-identification",
    "prop:beta-decay-transfer-matrix",
    "prop:nuclear-groebner-reduction",
    "rem:fivefold-symmetry",
    "prop:cohomological-embedding",
  ],
});
