import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unified-curvature-rank-mass-formula",
  proofs: ["prf:unified-curvature-rank-mass-formula"],
  title: "Unified curvature-rank mass formula (clarifies six terms + Term 7)",
  lean: {
    ref: "qou:QOU.WedderburnMass.unified_curvature_rank_mass",
    validation: "not_checked",
  },
  uses: ["prop:plancherel-term-7-formulation"],
});
