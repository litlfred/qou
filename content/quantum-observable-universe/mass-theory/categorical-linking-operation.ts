import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-linking-operation",
  title:
    "Categorical linking operation $\\mathrm{Lk}_R$: ribbon-category dual of topological linking number",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.CategoricalLinkingOperation",
    validation: "not_checked",
  },
  uses: [
    // broken-ref removed (Phase 7): conj:force-carrier-knot-vs-link-dichotomy
    "prop:categorical-higgs-mechanism",
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
