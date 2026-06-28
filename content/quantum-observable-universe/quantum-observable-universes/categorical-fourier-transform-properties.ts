import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-fourier-transform-properties",
  interprets: "def:categorical-fourier",
  title: "Realisations of the categorical Fourier transform: Peter--Weyl, Wick rotation, and base rings",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "fourier", "peter-weyl", "tannakian"],
  uses: [
    "def:categorical-fourier",
    "def:categorical-laplace",
    "prop:tannaka-krein-reconstruction",
    "rem:lagrange-resolvents",
    "def:briggs-klein-chart",
    "rem:brings-smoothness",
  ],
});
