import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-shell-binding",
  title:
    "Shell binding from the torus knot hierarchy: $T_{2,3} \\to T_{2,5} \\to T_{2,7} \\to T_{2,9}$",
  tags: [
    "torus-knot",
    "shell-binding",
    "magic-numbers",
    "chebyshev",
    "hecke-algebra",
    "transfer-matrix",
    "nuclear-structure",
    "inductive-construction",
  ],
  lean: { ref: "qou:QOU.Archimedean.torus_knot_shell_binding",
    validation: "not_checked",
  },
  uses: ["def:inter-shell-operator", "def:chebyshev-torus-coefficients"],
  examples: [
    "rem:shell-construction-rules",
  ],
});
