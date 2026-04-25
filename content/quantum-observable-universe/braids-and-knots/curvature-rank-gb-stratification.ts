import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:curvature-rank-gb-stratification",
  title: "Curvature-rank stratification of the GB spectral sequence",
  lean: {
    ref: "qou:QOU.WedderburnMass.curvature_rank_gb_stratification",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "thm:knot-mass-formula-unified",
    "prop:categorical-mass-markov",
    "prop:frobenius-s-classification",
  ],
});
