import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-linking-operation",
  title:
    "Categorical linking operation $\\mathrm{Lk}_R$: ribbon-category dual of topological linking number",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.CategoricalLinkingOperation",
    validation: "not_checked",
  },
  uses: ["prop:categorical-higgs-mechanism"],
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
