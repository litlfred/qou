import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-shell-binding",
  title:
    "Shell binding from the torus knot hierarchy: $T_{2,3} \\to T_{2,5} \\to T_{2,7} \\to T_{2,9}$",
  tags: [
    "shell-binding",
    "torus-knot",
    "transfer-matrix",
    "strong-force",
    "q-value",
    "beta-decay",
    "groebner-normal-form",
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
  ],
});
