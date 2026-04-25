import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:plancherel-term-7-formulation",
  title: "Term 7 as Plancherel-weighted log functional at curvature-rank ≥ 4",
  lean: {
    ref: "qou:QOU.WedderburnMass.plancherel_term_7",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
    "prop:curvature-rank-gb-stratification",
    "thm:wedderburn-mass-formula",
    "prop:categorical-mass-markov",
    "conj:shell-correction-term-seven",
  ],
});
