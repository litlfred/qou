import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:weinberg-angle-categorical",
  title:
    "Weinberg angle $\\theta_W$ as Hecke-eigenvalue ratio on the EW Hoefsmit projectors",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WeinbergAngleCategorical",
    validation: "not_checked",
  },
  uses: [
    "prop:hoefsmit-ew-cell-content",
    "prop:categorical-linking-operation",
    "prop:categorical-higgs-mechanism",
    "prop:weak-spectral-completeness",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "weinberg-angle",
    "electroweak-mixing",
    "hoefsmit-projector",
    "hecke-eigenvalue",
    "frobenius-trace",
    "categorical-physics",
    "open-problem",
    "tier-a",
  ],
});
