import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-tower-coefficient-stratification",
  title:
    "Mass-tower coefficients $(\\lambda_V, \\lambda_S, \\lambda_{\\mathrm{pair}}, \\alpha_k)$ as Wedderburn-block projections",
  lean: {
    ref: "qou:QOU.BraidKnot.mass_tower_coefficient_stratification",
    validation: "not_checked",
  },
  uses: [
    "prop:unified-curvature-rank-mass-formula",
    "prop:plancherel-term-7-formulation",
    "prop:plancherel-weight-boundedness",
    "rem:mass-formula-wedderburn-enumeration",
    "prop:gravity-spectral-prefactor",
    "prop:knot-factor-spectral-form",
    "prop:pauli-factor-wedderburn",
    "prop:confinement-categorical",
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
