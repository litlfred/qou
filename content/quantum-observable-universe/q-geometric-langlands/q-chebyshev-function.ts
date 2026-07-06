import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-chebyshev-function",
  title: "The $q$-Chebyshev function",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.QChebyshevFunction",
    validation: "not_checked",
  },
  uses: ["def:q-von-mangoldt-function"],
  defines: ["q-chebyshev-function"],
  tags: [
    "chebyshev",
    "q-deformation",
    "counting-function",
    "spectral-geometry",
  ],
});
