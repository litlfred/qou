import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:chebyshev-torus-coefficients",
  title: "Chebyshev crossing coefficients of $T_{2,n}$",
  tags: [
    "torus-knot",
    "chebyshev",
    "transfer-matrix",
    "hecke-algebra",
    "recurrence",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.ChebyshevTorusCoefficients",
    validation: "not_checked",
  },
});
