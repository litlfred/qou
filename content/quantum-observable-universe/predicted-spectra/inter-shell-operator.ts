import { definition } from "../../schema/builders";

export default definition({
  label: "def:inter-shell-operator",
  title: "Inter-shell torus-knot operator $\\Phi_{\\mathrm{shell}}^{(\\ell)}$",
  tags: [
    "torus-knot",
    "shell-binding",
    "transfer-matrix",
    "hecke-algebra",
    "groebner-basis",
    "nuclear-structure",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.InterShellOperator",
    validation: "not_checked",
  },
  uses: ["def:chebyshev-torus-coefficients"],
});
