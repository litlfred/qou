import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-linking-operation",
  title:
    "Categorical linking operation $\\mathrm{Lk}_R$: ribbon-category dual of topological linking number",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.categorical_linking_operation",
    validation: "not_checked",
  },
  uses: [
    "conj:force-carrier-knot-vs-link-dichotomy",
    "conj:categorical-higgs-mechanism",
    "def:rigid-monoidal-category",
    "def:frobenius-hopf-substrate",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "ribbon-category",
    "linking-number",
    "categorical-physics",
    "braided-monoidal",
    "trace-cut",
    "knot-vs-link",
    "open-problem",
    "tier-a",
  ],
});
