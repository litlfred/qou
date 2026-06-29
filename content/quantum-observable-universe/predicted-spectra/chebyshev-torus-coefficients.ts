import { definition } from "../../schema/builders";

export default definition({
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
