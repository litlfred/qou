import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:g-action-on-substrate",
  title:
    "Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate",
  uses: [
    "def:frobenius-hopf-substrate",
    "def:rigid-monoidal-category",
    "def:fibre-functor",
    "def:categorical-action",
    "rem:hecke-algebra-from-braiding",
    "conj:electroweak-higgs-torus-link-triplet",
    "conj:weak-spectral-completeness",
    "conj:categorical-higgs-idempotent",
  ],
  tags: [
    "g-action",
    "electroweak",
    "frobenius-hopf-substrate",
    "g-equivariance",
    "categorical-higgs",
    "n-sym",
    "open-problem",
  ],
});
