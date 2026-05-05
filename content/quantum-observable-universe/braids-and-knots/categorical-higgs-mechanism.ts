import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-higgs-mechanism",
  title:
    "Categorical Higgs mechanism: Goldstone-eating as topological linking",
  uses: [
    "conj:force-carrier-knot-vs-link-dichotomy",
    "conj:hoefsmit-ew-cell-content",
    "conj:categorical-linking-operation",
    "conj:weinberg-angle-categorical",
    "conj:electroweak-mass-eigenstate-count",
    "def:rigid-monoidal-category",
    "def:frobenius-hopf-substrate",
  ],
  tags: [
    "higgs-mechanism",
    "goldstone-eating",
    "linking-number",
    "categorical-physics",
    "broken-symmetry",
    "ew-symmetry-breaking",
    "open-problem",
    "skeleton",
  ],
});
