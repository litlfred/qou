import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weinberg-angle-categorical",
  title:
    "Weinberg angle $\\theta_W$ as Hecke-eigenvalue ratio on the EW Hoefsmit projectors",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WeinbergAngleCategorical",
    validation: "not_checked",
  },
  tags: [
    "tier:E",
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
