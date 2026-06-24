import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-tower-coefficient-stratification",
  proofs: ["prf:mass-tower-coefficient-stratification"],
  title:
    "Mass-tower coefficients $(\\lambda_V, \\lambda_S, \\lambda_{\\mathrm{pair}}, \\alpha_k)$ as Wedderburn-block projections",
  lean: {
    ref: "qou:QOU.BraidKnot.mass_tower_coefficient_stratification",
    validation: "not_checked",
  },
  uses: [
    "prop:knot-factor-spectral-form",
  ],
  tags: [
    "mass-tower",
    "bethe-weizsacker",
    "lambda-V",
    "lambda-S",
    "lambda-pair",
    "alpha-k",
    "wedderburn",
    "stratification",
    "coordination",
  ],
});
