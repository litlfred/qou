import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-higgs-mechanism",
  lean: { ref: "qou:QOU.BraidsAndKnots.CategoricalHiggsMechanism" },
  title:
    "Categorical Higgs mechanism: Goldstone-eating as topological linking",
  uses: [
    // broken-ref removed (Phase 7): conj:force-carrier-knot-vs-link-dichotomy
    "prop:hoefsmit-ew-cell-content",
    "prop:categorical-linking-operation",
    "prop:weinberg-angle-categorical",
    // broken-ref removed (Phase 7): conj:electroweak-mass-eigenstate-count
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
