import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
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
