import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-categorical",
  title: "Confinement = spectral-sequence collapse (only Wedderburn-central observables survive)",
  lean: {
    ref: "qou:QOU.WedderburnMass.confinement_categorical",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
    "prop:curvature-rank-gb-stratification",
    "prop:categorical-mass-markov",
    "prop:plancherel-term-7-formulation",
    "prop:unified-curvature-rank-mass-formula",
  ],
});
