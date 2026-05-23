import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:electroweak-mass-eigenstate-count",
  title:
    "Exactly three distinct EW/Higgs mass eigenstates from broken $\\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$",
  uses: [
    "def:rigid-monoidal-category",
    "def:frobenius-hopf-substrate",
    "rem:hecke-algebra-from-braiding",
    "prop:wedderburn-mass-formula",
  ],
  tags: [
    "electroweak",
    "higgs-mechanism",
    "mass-eigenstate",
    "wedderburn-decomposition",
    "representation-theory",
    "structural-premise",
    "open-problem",
  ],
});
