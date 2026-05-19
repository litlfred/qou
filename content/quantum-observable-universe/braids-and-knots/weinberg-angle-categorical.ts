import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weinberg-angle-categorical",
  title:
    "Weinberg angle $\\theta_W$ as Hecke-eigenvalue ratio on the EW Hoefsmit projectors",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WeinbergAngleCategorical",
    validation: "not_checked",
  },
  uses: [
    "conj:hoefsmit-ew-cell-content",
    "conj:categorical-linking-operation",
    "conj:categorical-higgs-mechanism",
    "conj:weak-spectral-completeness",
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
