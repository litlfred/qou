import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-fourier",
  title: "Categorical Fourier transform",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "fourier", "peter-weyl", "tannakian"],
  lean: {
    decl: "QOU.CategoricalFourier",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-laplace",
    "prop:tannaka-krein-reconstruction",
    "rem:adjoint-trace",
    "rem:lagrange-resolvents",
    "def:briggs-klein-chart",
    "rem:brings-smoothness",
  ],
});
